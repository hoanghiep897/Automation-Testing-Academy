() => {
  const assignmentId = /^#assignment-\d+$/.test(location.hash) ? location.hash : null;
  const assignmentCard = assignmentId ? document.querySelector(assignmentId) : null;
  const root = document.querySelector('.col-lg-8 .course-description') || assignmentCard?.querySelector('.assignment-instructions');
  const title = document.querySelector('[data-testid="watch-lesson-title"]') || assignmentCard?.querySelector('.assignment-title .fw-semibold, .assignment-title');
  if (!title) throw new Error('Lesson DOM unavailable; authentication/access may be required');
  const redactions = [];
  function safeUrl(value) {
    if (!value) return value;
    try {
      const u = new URL(value, location.href);
      if (!['http:', 'https:', 'data:'].includes(u.protocol)) return '';
      u.username = ''; u.password = '';
      for (const key of [...u.searchParams.keys()]) {
        if (/token|secret|password|cookie|authorization|signature|credential|^sig$|^jwt$|^key$|^expires$|^policy$|^x-amz-|^x-goog-/i.test(key)) {
          u.searchParams.delete(key);
          redactions.push(key);
        }
      }
      return u.href;
    } catch { return ''; }
  }
  function codeText(pre) {
    const c = (pre.querySelector('code') || pre).cloneNode(true);
    c.querySelectorAll('.line-numbers-rows, [aria-hidden="true"], .toolbar, button').forEach(e => e.remove());
    return c.textContent;
  }
  function clean(element) {
    if (!element) return '';
    const clone = element.cloneNode(true);
    clone.querySelectorAll('script, style, form, input, textarea, select, button, .toolbar, .line-numbers-rows, [aria-hidden="true"]').forEach(e => e.remove());
    clone.querySelectorAll('pre').forEach(pre => {
      const source = pre.querySelector('code') || pre;
      const match = (source.className + ' ' + pre.className).match(/language-([\w+-]+)/);
      const text = source.textContent;
      pre.replaceChildren();
      const code = document.createElement('code');
      if (match) code.className = 'language-' + match[1];
      code.textContent = text;
      pre.append(code);
    });
    for (const e of [clone, ...clone.querySelectorAll('*')]) {
      for (const attr of [...e.attributes]) {
        if (!['href','src','alt','title','width','height','colspan','rowspan','start','reversed','type','class','id','open','controls','poster','download','allowfullscreen','frameborder','loading','allow','sandbox','referrerpolicy'].includes(attr.name)) e.removeAttribute(attr.name);
      }
      for (const attr of ['href','src','poster']) {
        if (e.hasAttribute(attr)) e.setAttribute(attr, safeUrl(e.getAttribute(attr)));
      }
      if (e.tagName === 'IMG') {
        const sourceImg = Array.from(element.querySelectorAll('img'))[Array.from(clone.querySelectorAll('img')).indexOf(e)];
        const src = sourceImg?.getAttribute('data-src') || sourceImg?.getAttribute('src');
        if (src) e.setAttribute('src', safeUrl(src));
      }
    }
    // Unwrap UI-only wrappers; preserve the author's semantic content.
    clone.querySelectorAll('.code-toolbar, .rt-code-block, .rt-table-wrap').forEach(e => e.replaceWith(...e.childNodes));
    return clone.innerHTML;
  }
  const desc = document.querySelector('.col-lg-8 .lesson-short-desc');
  const main = document.querySelector('.col-lg-8');
  const intro = title.closest('.card')?.cloneNode(true);
  intro?.querySelector('[data-testid="watch-lesson-title"]')?.remove();
  intro?.querySelector('[data-testid="lesson-assignment-link"]')?.remove();
  const introHtml = clean(intro);
  function videoLink(a) {
    try {
      const u = new URL(a.href);
      return (/^(www\.)?(youtube\.com|youtube-nocookie\.com)$/.test(u.hostname) && (u.pathname === '/watch' && u.searchParams.has('v') || /^\/(embed|shorts)\/[\w-]{11}$/.test(u.pathname))) || (u.hostname === 'youtu.be' && /^\/[\w-]{11}$/.test(u.pathname)) || /\.(mp4|webm|mov|m4v|ogv)$/i.test(u.pathname);
    } catch { return false; }
  }
  const mediaElements = Array.from(main?.querySelectorAll('iframe,video,audio,source,a[href]') || []).filter(e => e.tagName !== 'A' || videoLink(e));
  const allMedia = mediaElements.map((e,i) => ({
    order:i+1,type:e.tagName.toLowerCase(),url:safeUrl(e.tagName === 'A' ? e.href : e.getAttribute('src') || e.getAttribute('data-src') || ''),
    title:e.getAttribute('title') || (e.tagName === 'A' ? e.textContent.trim() : ''),poster:safeUrl(e.getAttribute('poster') || ''),
    position:root?.contains(e) ? 'lesson_content' : (root && e.compareDocumentPosition(root) & Node.DOCUMENT_POSITION_FOLLOWING ? 'before_lesson_content' : 'after_lesson_content'),
    download_offered:e.tagName === 'A' ? e.hasAttribute('download') : e.tagName === 'VIDEO' && e.hasAttribute('controls') && !e.controlsList?.contains('nodownload')
  }));
  if (!root) {
    const main = document.querySelector('.col-lg-8');
    const extra = Array.from(main?.children || []).filter(e => !e.matches('.watch-nav') && !e.contains(title));
    // A different content layout must be inspected, never silently counted as empty.
    if (!main || extra.some(e => e.textContent.trim() || e.querySelector('img,iframe,video,audio,source'))) throw new Error('Unknown lesson content layout');
    return {
      title:title.textContent.trim(), url:safeUrl(location.href), source_content_missing:true,intro_html:introHtml,media:allMedia,
      short_description_html:clean(desc),
      dom_evidence:{lesson_body_count:0,extra_content_container_count:extra.length,
        main_code_count:main.querySelectorAll('pre').length,
        main_image_count:main.querySelectorAll('img').length,
        main_media_count:main.querySelectorAll('iframe,video,audio,source').length}
    };
  }
  const contentHtml = clean(root);
  const cleanDom = document.createElement('div');
  cleanDom.innerHTML = contentHtml;
  const figures = Array.from(cleanDom.querySelectorAll('img')).map((e,i) => ({order:i+1,url:e.src,alt:e.getAttribute('alt') || '',title:e.getAttribute('title') || ''}));
  const media = allMedia;
  const links = Array.from(cleanDom.querySelectorAll('a[href]')).map((e,i) => ({order:i+1,text:e.textContent,url:e.href,download:e.hasAttribute('download')}));
  const assignmentLink = document.querySelector('[data-testid="lesson-assignment-link"]');
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const sourceText = [];
  while (walker.nextNode()) {
    if (!walker.currentNode.parentElement.closest('script, style, form, input, textarea, select, button, .toolbar, .line-numbers-rows, [aria-hidden="true"]')) sourceText.push(walker.currentNode.textContent);
  }
  return {
    title:title.textContent.trim(), url:safeUrl(location.href),
    short_description_html:clean(desc),intro_html:introHtml, content_html:contentHtml,
    images:figures, media, links,
    assignment_link:assignmentLink ? {title:assignmentLink.getAttribute('title') || assignmentLink.textContent.trim(),url:safeUrl(assignmentLink.href)} : null,
    source_audit:{
      code_blocks:Array.from(root.querySelectorAll('pre')).map((e,i) => ({order:i+1,code:codeText(e)})),
      headings:Array.from(root.querySelectorAll('h1,h2,h3,h4,h5,h6')).map(e=>({level:Number(e.tagName.slice(1)),text:e.textContent})),
      table_count:root.querySelectorAll('table').length,
      image_count:root.querySelectorAll('img').length,
      paragraph_count:root.querySelectorAll('p').length,
      list_count:root.querySelectorAll('ul,ol').length,
      blockquote_count:root.querySelectorAll('blockquote').length,
      sanitized_text:sourceText.join(''),
      collapsed_code_count:root.querySelectorAll('.rt-code-block.is-collapsed').length
    },
    media_audit:{declared_media_references:allMedia.length,declared_urls:allMedia.map(e=>e.url),intro_iframe_count:intro?.querySelectorAll('iframe').length || 0},
    redacted_url_parameter_count:redactions.length
  };
}
