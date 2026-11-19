#!/usr/bin/env python3
"""Resume a course export from the existing headed Playwright CLI session.

Run: uv run --with beautifulsoup4 --with markdownify --with markdown-it-py \
    python scripts/export-course.py --limit 8
No credential, cookie, storage-state, or profile files are read or exported.
"""
import argparse
import hashlib
import json
import mimetypes
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'output/playwright'
CLI = ['npx', '--yes', '--package', '@playwright/cli', 'playwright-cli', '--session=anhtester-export']


class LoginRequired(RuntimeError):
    pass


class MissingLessonBody(RuntimeError):
    def __init__(self, metadata):
        self.metadata = metadata
        super().__init__('No lesson body in source DOM; title and short description only')


def now():
    return datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def browser(command, argument=None, log_name=None):
    cmd = CLI + [command] + ([argument] if argument is not None else [])
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=100)
    if log_name:
        (WORK / log_name).write_text(result.stdout)
    if result.returncode or '### Error' in result.stdout:
        (WORK / 'last-playwright-error.txt').write_text(result.stdout + '\n' + result.stderr)
        raise RuntimeError(f'Playwright {command} failed; inspect local browser logs')
    if command == 'goto':
        check_authentication()
    if '### Result\n' in result.stdout:
        payload = result.stdout.split('### Result\n', 1)[1].split('\n### ', 1)[0].strip()
        return json.loads(payload)
    return None


def check_authentication():
    state = browser('eval', '() => ({login:/^\\/(login|signin|sign-in)(\\/|$)/i.test(location.pathname)||!!document.querySelector("input[type=password]"),path:location.pathname})')
    if state and state['login']:
        raise LoginRequired('Manual login required; browser session kept open')


class Converter(MarkdownConverter):
    def convert_iframe(self, el, text, parent_tags):
        url = el.get('src', '')
        return f'\n\n[Video nhúng]({url})\n\n' if url else ''

    def convert_video(self, el, text, parent_tags):
        child = el.find('source')
        url = el.get('src') or (child.get('src', '') if child else '')
        return f'\n\n[Video]({url})\n\n' if url else text

    def convert_pre(self, el, text, parent_tags):
        code = el.get_text()
        child = el.find('code')
        classes = ' '.join((child or el).get('class', [])) + ' ' + ' '.join(el.get('class', []))
        match = re.search(r'language-([\w+-]+)', classes)
        language = match.group(1) if match else ''
        width = max([3] + [len(m.group()) + 1 for m in re.finditer(r'`+', code)])
        fence = '`' * width
        trailing = '' if code.endswith('\n') else '\n'
        return f'\n\n{fence}{language}\n{code}{trailing}{fence}\n\n'

    def convert_table(self, el, text, parent_tags):
        # HTML tables preserve cell formatting, spans, multiline content and code.
        return '\n\n' + str(el) + '\n\n'


CONVERTER = Converter(heading_style='ATX', bullets='-', strip_pre=None, wrap=False)


def semantic(node):
    if isinstance(node, NavigableString):
        return {'type': 'text', 'text': str(node)}
    if not isinstance(node, Tag):
        return None
    tag = node.name
    kinds = {'p': 'paragraph', 'pre': 'code_block', 'blockquote': 'blockquote',
             'ul': 'list', 'ol': 'list', 'li': 'list_item', 'table': 'table',
             'img': 'image', 'a': 'link', 'br': 'line_break', 'hr': 'divider',
             'iframe': 'embed', 'video': 'video', 'audio': 'audio',
             'figure': 'figure', 'figcaption': 'caption'}
    data = {'type': 'heading' if re.fullmatch(r'h[1-6]', tag) else kinds.get(tag, 'element'), 'tag': tag}
    if node.attrs:
        data['attributes'] = dict(node.attrs)
    if tag == 'pre':
        code = node.find('code')
        classes = ' '.join((code or node).get('class', []))
        language = re.search(r'language-([\w+-]+)', classes)
        data.update(code=node.get_text(), language=language.group(1) if language else '')
        return data
    if data['type'] == 'heading':
        data['level'] = int(tag[1:])
    if tag in ['ul', 'ol']:
        data['ordered'] = tag == 'ol'
    if tag == 'table':
        data['html'] = str(node)
    if tag == 'img':
        data.update(url=node.get('src', ''), alt=node.get('alt', ''))
    data['children'] = [s for c in node.children if (s := semantic(c)) is not None]
    return data


def blocks(soup):
    result = []
    for node in soup.contents:
        if isinstance(node, NavigableString) and not str(node).strip():
            continue
        block = semantic(node)
        if block:
            block['order'] = len(result) + 1
            result.append(block)
    return result


def content_kind(html):
    soup = BeautifulSoup(html, 'html.parser')
    if not soup.find('a') or soup.select('pre,table,img,iframe,video,ul,ol'):
        return 'lesson_article'
    for element in soup.select('h1,h2,h3,h4,h5,h6,a'):
        element.decompose()
    return 'resource_links_only' if not soup.get_text().strip() else 'lesson_article'


def walk(items):
    for item in items:
        yield item
        yield from walk(item.get('children', []))


def fetch_asset(url, category):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in ['http', 'https']:
        return {'status': 'not_downloaded', 'reason': 'unsupported_url_scheme', 'url': url}
    asset_id = hashlib.sha256(url.encode()).hexdigest()[:20]
    suffix = Path(parsed.path).suffix.lower()
    if not re.fullmatch(r'\.[a-z0-9]{1,8}', suffix):
        suffix = '.bin'
    relative = Path('assets') / (asset_id + suffix)
    path = ROOT / relative
    record = {'url': url, 'category': category, 'path': str(relative)}
    try:
        if not path.exists():
            # Public GET only: never forward browser cookies, tokens or headers.
            req = urllib.request.Request(url, headers={'User-Agent': 'AnhTesterOwnerExport/1.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                content_type = response.headers.get_content_type()
                if response.status != 200:
                    raise ValueError(f'http_status_{response.status}')
                if content_type == 'text/html':
                    raise ValueError('html_instead_of_asset')
                raw = response.read(30 * 1024 * 1024 + 1)
                if len(raw) > 30 * 1024 * 1024:
                    raise ValueError('asset_exceeds_30MiB_limit')
                if not raw:
                    raise ValueError('empty_asset')
            temp = path.with_suffix(path.suffix + '.tmp')
            temp.write_bytes(raw)
            temp.replace(path)
        raw = path.read_bytes()
        record.update(status='downloaded', bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
                      content_type=mimetypes.guess_type(path)[0] or 'application/octet-stream')
    except urllib.error.HTTPError as e:
        record.update(status='failed', reason=f'http_{e.code}')
    except Exception as e:
        record.update(status='failed', reason=str(e) if isinstance(e, ValueError) else type(e).__name__)
    return record


def audit(soup, source, md, content_blocks):
    original_codes = [x['code'] for x in source['code_blocks']]
    exported_codes = [x.get_text() for x in soup.find_all('pre')]
    json_codes = [x['code'] for x in walk(content_blocks) if x['type'] == 'code_block']
    md_tokens = MarkdownIt('commonmark', {'html': True}).parse(md)
    md_codes = [t.content for t in md_tokens if t.type == 'fence']
    # The sample uses no pre blocks nested inside tables. Preserve those as HTML
    # and include their contents in the comparison if future lessons contain any.
    md_html_codes = []
    for t in md_tokens:
        if t.type == 'html_block':
            md_html_codes.extend(x.get_text() for x in BeautifulSoup(t.content, 'html.parser').find_all('pre'))
    expected_md = [c if c.endswith('\n') else c + '\n' for c in original_codes]
    heading_values = [{'level': int(x.name[1:]), 'text': x.get_text()} for x in soup.select('h1,h2,h3,h4,h5,h6')]
    checks = {
        'code_exact_html': exported_codes == original_codes,
        'code_exact_json': json_codes == original_codes,
        'code_markdown_whitespace': md_codes == expected_md if not md_html_codes else sorted(md_codes + [c if c.endswith('\n') else c + '\n' for c in md_html_codes]) == sorted(expected_md),
        'headings_exact': heading_values == source['headings'],
        'table_count_matches': len(soup.find_all('table')) == source['table_count'],
        'image_count_matches': len(soup.find_all('img')) == source['image_count'],
        'paragraph_count_matches': len(soup.find_all('p')) == source['paragraph_count'],
        'list_count_matches': len(soup.select('ul,ol')) == source['list_count'],
        'blockquote_count_matches': len(soup.find_all('blockquote')) == source['blockquote_count'],
        'all_cleaned_text_preserved': soup.get_text() == source['sanitized_text'],
        'content_nonempty': bool(soup.get_text().strip()),
        'no_form_or_script': not bool(soup.select('form,input,textarea,script')),
    }
    return {'checked_at': now(), 'passed': all(checks.values()), 'checks': checks,
            'heading_count': len(heading_values), 'code_block_count': len(original_codes),
            'table_count': source['table_count'], 'image_count': source['image_count'],
            'code_sha256': [digest(x) for x in original_codes],
            'content_text_sha256': digest(source['sanitized_text']),
            'note': 'JSON/HTML preserve code exactly. Markdown adds the required final line ending before a closing fence when absent in the source.'}


def direct_video(url):
    """Download only an explicitly offered ordinary video file; no player extraction."""
    parts = urllib.parse.urlsplit(url)
    suffix = Path(parts.path).suffix.lower()
    relative = Path('assets/videos') / (hashlib.sha256(url.encode()).hexdigest()[:20] + suffix)
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    record = {'url':url, 'category':'video', 'path':str(relative)}
    try:
        if not target.exists():
            request = urllib.request.Request(url, headers={'User-Agent':'CourseOwnerExport/1.0'})
            with urllib.request.urlopen(request, timeout=30) as response:
                if response.status != 200 or response.headers.get_content_type() not in ['video/mp4','video/webm','video/quicktime','video/x-m4v','video/ogg','application/octet-stream']:
                    raise ValueError('not_an_ordinary_video_file')
                length = int(response.headers.get('Content-Length') or 0)
                if length and length > shutil.disk_usage(ROOT).free * 0.8:
                    raise ValueError('insufficient_free_disk_space')
                temp = target.with_suffix(target.suffix + '.tmp')
                with temp.open('wb') as output:
                    while chunk := response.read(1024 * 1024):
                        output.write(chunk)
                temp.replace(target)
        checksum = hashlib.sha256()
        with target.open('rb') as source:
            while chunk := source.read(1024 * 1024):
                checksum.update(chunk)
        record.update(status='downloaded', bytes=target.stat().st_size, sha256=checksum.hexdigest())
    except Exception as error:
        record.update(status='failed', reason=str(error) if isinstance(error, ValueError) else type(error).__name__)
    return record


def collect_videos(raw):
    videos = []
    seen = {}
    assets = []
    for medium in raw.get('media', []):
        url = medium.get('url', '')
        if not url:
            continue
        parts = urllib.parse.urlsplit(url)
        video_id = None
        if parts.hostname in ['youtube.com','www.youtube.com','youtube-nocookie.com','www.youtube-nocookie.com']:
            if parts.path.startswith(('/embed/','/shorts/')):
                video_id = parts.path.split('/')[2]
            elif parts.path == '/watch':
                video_id = urllib.parse.parse_qs(parts.query).get('v', [None])[0]
        elif parts.hostname == 'youtu.be':
            video_id = parts.path.strip('/')
        if video_id and not re.fullmatch(r'[A-Za-z0-9_-]{11}', video_id):
            video_id = None
        key = 'youtube:' + video_id if video_id else url
        if key in seen:
            seen[key]['references'].append(medium)
            continue
        video = {'order':len(videos)+1, 'source_url':url, 'title':medium.get('title',''),
                 'references':[medium], 'download_status':'not_offered_by_source'}
        seen[key] = video
        if video_id:
            watch = 'https://www.youtube.com/watch?v=' + video_id
            video.update(provider='youtube', video_id=video_id, watch_url=watch,
                         download_reason='Trang nguồn cung cấp video nhúng/liên kết YouTube; chưa chạy bước tải video công khai riêng.')
            endpoint = 'https://www.youtube.com/oembed?' + urllib.parse.urlencode({'url':watch,'format':'json'})
            try:
                request = urllib.request.Request(endpoint, headers={'User-Agent':'CourseOwnerExport/1.0'})
                with urllib.request.urlopen(request, timeout=20) as response:
                    metadata = json.load(response)
                video.update(availability_check='official_oembed_ok', remote_title=metadata.get('title',''), thumbnail_url=metadata.get('thumbnail_url',''))
            except urllib.error.HTTPError as error:
                video.update(availability_check='official_oembed_http_' + str(error.code))
            except Exception as error:
                video.update(availability_check='official_oembed_request_failed', availability_reason=type(error).__name__)
            time.sleep(0.6)
        elif re.search(r'\.(mp4|webm|mov|m4v|ogv)$', parts.path, re.I) and medium.get('download_offered'):
            asset = direct_video(url)
            assets.append(asset)
            video.update(provider='direct_file', download_status=asset['status'], asset=asset)
        else:
            video.update(provider='embedded_or_external', download_reason='Không có liên kết tải tệp video thông thường được cung cấp trên trang; chỉ lưu URL.')
        videos.append(video)
    return videos, assets


def video_index(manifest):
    entries = []
    for chapter in manifest['chapters']:
        for lesson in chapter['lessons']:
            for video in lesson.get('videos', []):
                entries.append({'lesson_order':lesson['order'], 'lesson_title':lesson['title'], 'lesson_url':lesson['url'], **video})
    data = {'course':manifest['course'], 'video_count':len(entries),
            'downloaded_files':sum(v['download_status']=='downloaded' for v in entries), 'videos':entries,
            'lessons_without_video':[{'order':l['order'],'title':l['title'],'url':l['url']} for c in manifest['chapters'] for l in c['lessons'] if l.get('content_status') in ['exported','metadata_only'] and not l.get('videos')]}
    write_json(ROOT / 'videos.json', data)
    return data


def export_assignment(link, extractor, source_id):
    browser('goto', link['url'], f'navigation-assignment-{source_id}.txt')
    time.sleep(2)
    target = urllib.parse.urlsplit(link['url'])
    expected_course = urllib.parse.parse_qs(target.query).get('course')
    visited = {urllib.parse.urlunsplit(target._replace(fragment=''))}
    for _ in range(10):
        state = browser('eval', '''() => ({
          found: /^#assignment-\\d+$/.test(location.hash) && !!document.querySelector(location.hash),
          pages: Array.from(document.querySelectorAll('a[href*="student-assignments"][href*="page="]')).map(a => a.href)
        })''')
        if state['found']:
            break
        candidates = []
        for url in state['pages']:
            parts = urllib.parse.urlsplit(url)
            base = urllib.parse.urlunsplit(parts._replace(fragment=''))
            if parts.netloc == target.netloc and parts.path == target.path and urllib.parse.parse_qs(parts.query).get('course') == expected_course and base not in visited:
                candidates.append((base, parts))
        if not candidates:
            raise ValueError('Linked assignment not present on accessible course assignment pages')
        base, parts = candidates[0]
        visited.add(base)
        browser('goto', urllib.parse.urlunsplit(parts._replace(fragment=target.fragment)), f'navigation-assignment-{source_id}-page-{len(visited)}.txt')
        time.sleep(2)
    else:
        raise ValueError('Assignment pagination exceeded ten pages')
    browser('run-code', '''async (page) => {
      const anchor = new URL(page.url()).hash;
      if (!/^#assignment-\\d+$/.test(anchor)) throw new Error('Unexpected assignment anchor');
      const card = page.locator(anchor);
      if (!await card.locator('.assignment-details').isVisible()) await card.locator('button.assignment-toggle').click();
      await card.locator('.assignment-instructions').waitFor({state:'visible'});
      const toggles = card.locator('.assignment-instructions .rt-code-block.is-collapsed > button.rt-code-block__toggle');
      let count = 0;
      while (await toggles.count()) { await toggles.first().click(); if (++count > 100) throw new Error('toggle limit'); }
      return {expanded:count};
    }''')
    raw = browser('eval', extractor, f'assignment-{source_id}-extraction.txt')
    soup = BeautifulSoup(raw['content_html'], 'html.parser')
    rendered = BeautifulSoup(raw['content_html'], 'html.parser')
    records = []
    for img, image in zip(rendered.find_all('img'), raw['images']):
        record = fetch_asset(image['url'], 'assignment_image')
        records.append(record)
        image['asset'] = record
        if record['status'] == 'downloaded':
            img['src'] = '../../' + record['path']
        time.sleep(0.6)
    content_blocks = blocks(soup)
    md = CONVERTER.convert(str(rendered))
    quality = audit(soup, raw['source_audit'], md, content_blocks)
    if not quality['passed']:
        raise ValueError('Assignment quality check failed: ' + ', '.join(k for k,v in quality['checks'].items() if not v))
    return ({'title':raw['title'], 'url':raw['url'], 'status':'exported',
             'content':{'html':raw['content_html'], 'blocks':content_blocks},
             'images':raw['images'], 'media':raw['media'], 'links':raw['links'],
             'assets':records, 'quality':quality}, md)


def write_report(manifest, progress):
    video_data = video_index(manifest)
    all_items = [l for c in manifest['chapters'] for l in c['lessons']]
    exported = [l for l in all_items if l.get('content_status') == 'exported']
    failed = [l for l in all_items if l.get('content_status') == 'failed']
    metadata_only = [l for l in all_items if l.get('content_status') not in ['exported', 'failed']]
    limit = min(manifest.get('sample_limit', 3), len(all_items))
    assignment_expected = [l for l in exported if l.get('assignment_link')]
    assets = [a for l in all_items for a in l.get('assets', []) + (l.get('assignment') or {}).get('assets', [])]
    lines = ['# Báo cáo xuất: ' + manifest['course']['title'], '', f'Cập nhật: {now()}', '',
             f'Chủ sở hữu website xác nhận mục đích xuất dữ liệu để chuyển sang website khác. Phạm vi lần này: {limit} mục.', '',
             '## Kết quả', '', f'- Danh mục: {manifest["chapter_count"]} chương, {manifest["lesson_count"]} mục.',
             f'- Có content_status: exported: {len(exported)}/{len(all_items)} mục; content_status: failed: {len(failed)}.',
             f'- Trong các mục đã xuất: {sum(l.get("content_kind")=="lesson_article" for l in exported)} bài giảng và {sum(l.get("content_kind")=="resource_links_only" for l in exported)} mục chỉ gồm liên kết tài nguyên nguồn.',
             f'- Chỉ có metadata, chưa có nội dung được xuất: {len(metadata_only)} mục. Không tính các mục này là thành công.',
             f'- Assets tải thành công: {sum(a["status"]=="downloaded" for a in assets)}; lỗi: {sum(a["status"]=="failed" for a in assets)}.',
             f'- Bài tập riêng đã xuất: {sum((l.get("assignment") or {}).get("status")=="exported" for l in exported)}/{len(assignment_expected)} mục có liên kết bài tập; thêm {sum((l.get("assignment") or {}).get("quality",{}).get("code_block_count",0) for l in exported)} khối code trong đề bài/hướng dẫn.',
             '- Mỗi bài có JSON cấu trúc, HTML nội dung trong JSON và Markdown. Không viết lại hay tóm tắt bài giảng.', '',
             '## Đối chiếu trang gốc', '',
             '| Bài | Headings | Code block | Bảng | Ảnh | Kiểm tra DOM → JSON/Markdown |',
             '|---|---:|---:|---:|---:|---|']
    for l in exported:
        q = l['quality']
        lines.append(f'| [{l["order"]}]({l["url"]}) | {q["heading_count"]} | {q["code_block_count"]} | {q["table_count"]} | {q["image_count"]} | {"Đạt" if q["passed"] else "Có lỗi"} |')
    lines += ['', 'Đối chiếu toàn bộ các khối code, thứ tự headings, số đoạn văn/danh sách/bảng/ảnh/ghi chú và toàn bộ text sau khi loại bỏ các nút giao diện. Mỗi khối code có SHA-256 để kiểm tra khi chuyển hệ thống.', '',
              f'Đã đối chiếu nội dung {len(exported)} mục với DOM gốc trong quá trình xuất. Yêu cầu tối thiểu 5 bài: {"đạt" if len(exported)>=5 else "chưa đủ"}.', '',
              '## Định dạng và phạm vi', '',
              '- Code lấy bằng textContent của pre/code, bỏ riêng số dòng và nút Copy. Giữ tab, khoảng trắng, xuống dòng và ngôn ngữ code.',
              '- Markdown dùng fence đủ dài để không xung đột với backtick trong code. Nếu code nguồn thiếu newline cuối, Markdown bổ sung newline bắt buộc trước fence đóng; JSON giữ nguyên tuyệt đối.',
              '- Bảng trong Markdown giữ dạng HTML để bảo toàn cấu trúc ô và định dạng; bảng và hình ảnh giữ đúng vị trí trong bài.',
              '- Ảnh dùng đường dẫn assets cục bộ trong Markdown. URL nguồn và SHA-256 được giữ trong JSON.',
              '- Mở các khối code thu gọn bằng nút Expand thông thường. Không thao tác hoàn thành bài, nộp bài, phát video hoặc đổi tài khoản.',
              '- Chỉ xuất vùng nội dung bài và mô tả; không xuất menu, hồ sơ, trạng thái nộp bài, cookies, tokens hay thông tin đăng nhập.',
              '- Bài tập/đáp án có trong bài giảng được giữ nguyên. Đề bài và hướng dẫn của bài tập riêng cũng được xuất vào trường assignment trong JSON và phần cuối Markdown; không lấy form nộp bài hay dữ liệu học viên.', '',
              '## Video, tài liệu và lỗi truy cập', '']
    for l in exported:
        lines.append(f'- Bài {l["order"]}: {len(l.get("media", []))} media nhúng; {len(l.get("links", []))} liên kết nội dung; {len(l.get("images", []))} ảnh.')
        for a in l.get('assets', []):
            if a['status'] != 'downloaded':
                lines.append(f'  - Asset chưa tải: {a["url"]} ({a.get("reason",a["status"])}).')
    lines += ['', '## Bài tập riêng', '', '| Bài | Khối code | Đối chiếu DOM → JSON/Markdown |', '|---|---:|---|']
    for l in exported:
        assignment = l.get('assignment') or {}
        q = assignment.get('quality', {})
        lines.append(f'| {l["order"]} | {q.get("code_block_count",0)} | {"Đạt" if q.get("passed") else ("Không có liên kết bài tập" if not l.get("assignment_link") else "Chưa xuất")} |')
    if not any(l.get('media') for l in exported):
        lines.append('- Không có phần tử iframe/video/audio/source trong các mục đã xuất; không suy đoán hoặc dò tìm video ngoài DOM.')
    lines += ['', 'Các liên kết tài liệu được ghi lại. Ảnh/tài liệu tĩnh được tải khi truy cập công khai được; video công khai của chủ sở hữu được xử lý bằng bước tải riêng, không dùng cookies/đăng nhập hoặc vượt DRM/CAPTCHA.', '',
              '## Tiếp tục và đóng gói', '',
              '`progress.json` ghi ngay sau từng bài, khóa theo URL. Script mặc định bỏ qua bài đã xuất đủ file; dùng --force để đối chiếu/xuất lại. Script mặc định xuất toàn bộ danh mục; có thể đặt --limit để giới hạn.', '',
              f'Chạy tiếp: `uv run --with beautifulsoup4 --with markdownify --with markdown-it-py python scripts/export-course.py --limit {limit}` (không dùng --force).', '',
              'Cần giữ phiên trình duyệt Playwright CLI `anhtester-export` đang đăng nhập. Script không xuất hồ sơ hay lưu storage-state. ZIP chỉ chứa dữ liệu xuất, assets, báo cáo và mã nguồn script; không chứa log/snapshot/profile trình duyệt.']
    if failed:
        lines += ['', '## Bài lỗi', ''] + [f'- {l["order"]}: {l.get("error", "unknown")}' for l in failed]
    if metadata_only:
        lines += ['', '## Mục chỉ có metadata, không tính thành công', '',
                  'Các mục dưới đây chưa có nội dung bài giảng được xuất. Mô tả ngắn được lưu riêng, không được tính là lý thuyết hoặc nội dung đầy đủ.', '',
                  '| Mục | Tên bài | Trạng thái và lý do |', '|---|---|---|']
        for l in metadata_only:
            lines.append(f'| {l["order"]} | [{l["title"]}]({l["url"]}) | {l.get("content_status")}: {l.get("missing_content_reason", "Chưa xử lý")} |')
    lines += ['', '## Video từng bài và từng phần', '',
              f'- URL video riêng biệt theo từng bài: {video_data["video_count"]}. Tệp video đã tải: {video_data["downloaded_files"]}.',
              '- Đã kiểm tra iframe ở vùng trình phát phía trên bài và liên kết video trong nội dung/mô tả, gồm các bài có nhiều phần.',
              '- videos.json và trường videos trong JSON bài ghi đầy đủ URL, vị trí tham chiếu, tình trạng kiểm tra và lý do chưa tải tệp.',
              '- Kiểm tra oEmbed là kiểm tra metadata chính thức của YouTube, không khẳng định đã kiểm tra phát toàn bộ video.',
              '- Bước tải video dùng yt-dlp với nguồn YouTube public/unlisted không DRM, không cookies hoặc tài khoản đăng nhập; không xử lý CAPTCHA hoặc vượt kiểm soát truy cập.', '',
              '| Bài | Phần | Video | Metadata chính thức | Tệp video |', '|---|---|---|---|---|']
    for video in video_data['videos']:
        url = video.get('watch_url') or video['source_url']
        lines.append(f'| {video["lesson_order"]} | {video["order"]} | [Xem video]({url}) | {video.get("availability_check", "Không áp dụng")} | {video["download_status"]} |')
    if video_data['lessons_without_video']:
        lines += ['', 'Bài không có video trong DOM nguồn: ' + ', '.join(str(l['order']) for l in video_data['lessons_without_video']) + '. Không tự tìm hoặc gán video từ khóa học khác.']
    (ROOT / 'export-report.md').write_text('\n'.join(lines) + '\n')


def update_counts(manifest, progress, lessons):
    exported = sum(l.get('content_status') == 'exported' for l in lessons)
    failed = sum(l.get('content_status') == 'failed' for l in lessons)
    metadata = len(lessons) - exported - failed
    progress.update(updated_at=now(), full_content_exported=exported,
                    full_content_failed=failed, full_content_skipped=metadata,
                    metadata_only=metadata)
    manifest.update(exported_at=now(), full_content_exported=exported,
                    full_content_failed=failed, metadata_only=metadata)


def package():
    files = [ROOT / 'manifest.json', ROOT / 'progress.json', ROOT / 'export-report.md']
    if (ROOT / 'videos.json').exists():
        files.append(ROOT / 'videos.json')
    if (ROOT / 'video-download-plan.json').exists():
        files.append(ROOT / 'video-download-plan.json')
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    completed_video_paths = {a['path'] for c in manifest['chapters'] for l in c['lessons'] for a in l.get('assets', []) if a.get('category') == 'video' and a.get('status') == 'downloaded'}
    for folder in ['chapters', 'assets', 'scripts']:
        for p in sorted((ROOT / folder).rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts or p.name.endswith(('.tmp','.part','.ytdl')) or p.name == '.DS_Store':
                continue
            if p.is_relative_to(ROOT / 'assets/videos') and str(p.relative_to(ROOT)) not in completed_video_paths:
                continue
            files.append(p)
    target = ROOT / 'ai-testing-google-antigravity-export.zip'
    temp = target.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in files:
            compression = zipfile.ZIP_STORED if p.suffix.lower() in ['.mp4','.webm','.mov','.m4v'] else zipfile.ZIP_DEFLATED
            z.write(p, Path('ai-testing-google-antigravity-export') / p.relative_to(ROOT), compress_type=compression)
    with zipfile.ZipFile(temp) as z:
        if z.testzip() is not None:
            raise RuntimeError('ZIP integrity check failed')
    temp.replace(target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=None)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    progress = json.loads((ROOT / 'progress.json').read_text())
    if args.limit is None:
        args.limit = manifest['lesson_count']
    full_course = args.limit >= manifest['lesson_count']
    scope = 'full_course_content' if full_course else 'sample_full_content'
    manifest.update(schema_version=2, scope=scope, status='in_progress', owner_confirmed=True, sample_limit=args.limit)
    progress.update(scope=scope, sample_limit=args.limit)
    for c in manifest['chapters']:
        for lesson in c['lessons']:
            if lesson.get('content_status') == 'not_exported_copyright_limit':
                lesson['content_status'] = 'not_in_sample'
                entry = progress['lessons'][lesson['url']]
                entry['content_status'] = 'not_in_sample'
                existing = json.loads((ROOT / lesson['json_path']).read_text())
                existing['content_status'] = 'not_in_sample'
                write_json(ROOT / lesson['json_path'], existing)
    all_lessons = [l for c in manifest['chapters'] for l in c['lessons']]
    extractor = (ROOT / 'scripts/extract-lesson.js').read_text()
    login_required = False
    for lesson in all_lessons[:args.limit]:
        if lesson.get('content_status') == 'exported' and not args.force and all((ROOT / lesson[k]).exists() for k in ['json_path', 'markdown_path']):
            print(f'SKIP lesson {lesson["order"]}: already exported', flush=True)
            continue
        print(f'START lesson {lesson["order"]}: source id {lesson["source_id"]}', flush=True)
        try:
            browser('goto', lesson['url'], f'navigation-{lesson["source_id"]}.txt')
            time.sleep(2)
            layout = browser('eval', '() => ({hasBody:!!document.querySelector(".col-lg-8 .course-description")})')
            if not layout['hasBody']:
                metadata = browser('eval', extractor, f'lesson-{lesson["source_id"]}-extraction.txt')
                if metadata.get('source_content_missing'):
                    if re.sub(r'\s+', ' ', metadata['title']).strip() != re.sub(r'\s+', ' ', lesson['title']).strip() or urllib.parse.urlsplit(metadata['url']).path != urllib.parse.urlsplit(lesson['url']).path:
                        raise ValueError('Lesson identity mismatch')
                    raise MissingLessonBody(metadata)
            browser('run-code', 'async (page) => { await page.locator(".col-lg-8 .course-description").waitFor({state:"visible",timeout:20000}); const toggles=page.locator(".course-description .rt-code-block.is-collapsed > button.rt-code-block__toggle"); let count=0; while(await toggles.count()){await toggles.first().click();if(++count>100)throw new Error("toggle limit");} return {expanded:count}; }')
            raw = browser('eval', extractor, f'lesson-{lesson["source_id"]}-extraction.txt')
            if re.sub(r'\s+', ' ', raw['title']).strip() != re.sub(r'\s+', ' ', lesson['title']).strip() or urllib.parse.urlsplit(raw['url']).path != urllib.parse.urlsplit(lesson['url']).path:
                raise ValueError('Lesson identity mismatch')
            original = BeautifulSoup(raw['content_html'], 'html.parser')
            rendered = BeautifulSoup(raw['content_html'], 'html.parser')
            asset_records = []
            for img, record in zip(rendered.find_all('img'), raw['images']):
                asset = fetch_asset(record['url'], 'image')
                asset_records.append(asset)
                record['asset'] = asset
                if asset['status'] == 'downloaded':
                    img['src'] = '../../' + asset['path']
                time.sleep(0.6)
            for link in raw['links']:
                parts = urllib.parse.urlsplit(link['url'])
                if parts.netloc == 'anhtester.com' and re.search(r'\.(pdf|docx?|xlsx?|csv|txt|md|json|zip|js|ts)$', parts.path, re.I):
                    asset_records.append(fetch_asset(link['url'], 'document'))
                    time.sleep(0.6)
            content_blocks = blocks(original)
            desc_md = CONVERTER.convert(raw.get('intro_html') or raw['short_description_html'])
            body_md = CONVERTER.convert(str(rendered))
            md = f'# {raw["title"]}\n\nChương: {lesson["chapter_title"]}\n\nNguồn: [{raw["url"]}]({raw["url"]})\n\n' + desc_md + '\n\n' + body_md
            quality = audit(original, raw['source_audit'], body_md, content_blocks)
            if not quality['passed']:
                write_json(WORK / f'quality-failure-{lesson["source_id"]}.json', quality)
                raise ValueError('Quality check failed: ' + ', '.join(k for k,v in quality['checks'].items() if not v))
            videos, video_assets = collect_videos(raw)
            asset_records.extend(video_assets)
            assignment = None
            if raw['assignment_link']:
                a = raw['assignment_link']
                assignment, assignment_md = export_assignment(a, extractor, lesson['source_id'])
                md += f'\n\n---\n\n## Bài tập riêng — {assignment["title"]}\n\nNguồn bài tập: [{a["url"]}]({a["url"]})\n\n' + assignment_md
            lesson.update(title=raw['title'], export_scope='full_lesson_content', content_status='exported', exported_at=now(),
                          content_kind=content_kind(raw['content_html']),
                          short_description_html=raw['short_description_html'],
                          intro={'html':raw.get('intro_html',''), 'blocks':blocks(BeautifulSoup(raw.get('intro_html',''),'html.parser'))},
                          content={'html':raw['content_html'], 'blocks':content_blocks},
                          images=raw['images'], media=raw['media'], links=raw['links'],
                          videos=videos, media_audit=raw.get('media_audit',{}),
                          assignment_link=raw['assignment_link'], assets=asset_records, quality=quality,
                          assignment=assignment,
                          redacted_url_parameter_count=raw['redacted_url_parameter_count'])
            lesson.pop('error', None)
            write_json(ROOT / lesson['json_path'], lesson)
            md_path = ROOT / lesson['markdown_path']
            md_tmp = md_path.with_suffix('.md.tmp')
            md_tmp.write_text(md)
            md_tmp.replace(md_path)
            print(f'OK lesson {lesson["order"]}: {quality["code_block_count"]} code blocks, {len(asset_records)} assets', flush=True)
        except MissingLessonBody as e:
            metadata = e.metadata
            videos, video_assets = collect_videos(metadata)
            lesson.update(content_status='metadata_only', export_scope='metadata_only', content=None,
                          short_description_html=metadata['short_description_html'],
                          intro={'html':metadata.get('intro_html',''), 'blocks':blocks(BeautifulSoup(metadata.get('intro_html',''),'html.parser'))},
                          media=metadata.get('media',[]), videos=videos, assets=video_assets,
                          missing_content_reason='Trang nguồn không có vùng nội dung lý thuyết; tiêu đề, mô tả và URL video (nếu có) được lưu riêng.',
                          source_checked_at=now(), dom_evidence=metadata['dom_evidence'])
            lesson.pop('error', None)
            write_json(ROOT / lesson['json_path'], lesson)
            md = (f'# {lesson["title"]}\n\nChương: {lesson["chapter_title"]}\n\n'
                  f'Nguồn: [{lesson["url"]}]({lesson["url"]})\n\n'
                  '> Trạng thái: chỉ có metadata. Trang nguồn không hiển thị nội dung lý thuyết; mục này không được tính là xuất nội dung lý thuyết thành công.\n\n'
                  '## Mô tả và video từ trang nguồn\n\n' + CONVERTER.convert(metadata.get('intro_html') or metadata['short_description_html']))
            (ROOT / lesson['markdown_path']).write_text(md)
            print(f'METADATA_ONLY lesson {lesson["order"]}: no lesson body in source DOM', flush=True)
        except LoginRequired:
            login_required = True
            print('LOGIN_REQUIRED: manual login required; no further lessons will be visited', flush=True)
            break
        except Exception as e:
            try:
                check_authentication()
            except LoginRequired:
                login_required = True
                print('LOGIN_REQUIRED: manual login required; no further lessons will be visited', flush=True)
                break
            lesson.update(content_status='failed', error=str(e))
            write_json(ROOT / lesson['json_path'], lesson)
            print(f'FAIL lesson {lesson["order"]}: {e}', flush=True)
        entry = progress['lessons'][lesson['url']]
        entry.update(status={'exported':'content_exported','failed':'failed','metadata_only':'metadata_only'}[lesson['content_status']], content_status=lesson['content_status'], updated_at=now())
        update_counts(manifest, progress, all_lessons)
        write_json(ROOT / 'manifest.json', manifest)
        write_json(ROOT / 'progress.json', progress)
        write_report(manifest, progress)
        time.sleep(2)
    update_counts(manifest, progress, all_lessons)
    manifest['status'] = 'authentication_required' if login_required else ('exported' if all(l.get('content_status')=='exported' for l in all_lessons[:args.limit]) else ('with_errors' if progress['full_content_failed'] else 'with_missing_content'))
    write_json(ROOT / 'manifest.json', manifest)
    write_json(ROOT / 'progress.json', progress)
    write_report(manifest, progress)
    package()
    print(json.dumps({'status':manifest['status'], 'full_content_exported':progress.get('full_content_exported',0), 'zip':str(ROOT/'ai-testing-google-antigravity-export.zip')}, ensure_ascii=False), flush=True)
    if login_required:
        sys.exit(3)


if __name__ == '__main__':
    main()
