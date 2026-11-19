# Bài 6 - Sử dụng bộ Testing Skills do Anh Tester xây dựng

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/332](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/332)

✅ Cài đặt bộ Testing Skills do Anh Tester xây dựng vào project cụ thể  
✅ Phân tích và sử dụng bộ Testing Skills  
✅ Cách xây dựng bộ Skills cho AI hiểu trong một project bất kỳ

## 1. Bộ Testing Skills của Anh Tester là gì?

Ở bài trước bạn đã tự tay tạo RULE, SKILL và COMMAND cho AI Agent: viết `CLAUDE.md`, tách quy tắc ra `.claude/rules/`, dựng Skill `skills-requirements-analyzer`, Skill `skills-generate-testcases` và Command `/generate_testcases_from_requirements`. Đó là bài học về **cơ chế** — mỗi Skill chỉ dài vài chục dòng, đủ để hiểu nguyên lý.

Bài này bạn nhận **bản đầy đủ** của đúng những thứ đó: một bộ Rule/Skill/Command đã được Anh Tester xây dựng và tinh chỉnh theo quy trình kiểm thử thực tế, đóng gói sẵn trong một repo GitHub:

🔗 **Repo bộ Testing Skills**

<https://github.com/anhtester/claude-testing-skills> và <https://github.com/anhtester/codex-testing-skills>

Repo dành riêng cho học viên chính thức của Anh Tester. Nếu bạn chưa truy cập được, liên hệ để được cấp quyền trước khi làm tiếp bài này.

Bộ này **không chỉ dành cho Automation**. Nó phủ cả vòng đời kiểm thử cho Manual Tester: khảo sát hệ thống → sinh Requirements → sinh Test Case → review → chạy tay → viết Bug Report → retest → ma trận truy vết → báo cáo release. Khoá học này sẽ đi hết nhánh Manual đó.

### 1.1. Quy mô bộ Skills

<table class="rt-table">
<thead>
<tr>
<th>Thành phần</th>
<th>Số lượng</th>
<th>Tương ứng với khái niệm nào ở bài trước</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Rules</strong><br/><code>.claude/rules/</code></td>
<td>6 file</td>
<td>Chính là cơ chế tách RULE nhiều file bạn học ở mục 2.3 bài trước — tự động nạp, không cần khai báo.</td>
</tr>
<tr>
<td><strong>Skills</strong><br/><code>.claude/skills/</code></td>
<td>19 skill</td>
<td>Mỗi skill là một thư mục chứa <code>SKILL.md</code> với frontmatter <code>name</code> + <code>description</code> — đúng cấu trúc mục 3.3 bài trước.</td>
</tr>
<tr>
<td><strong>Commands</strong><br/><code>.claude/commands/</code></td>
<td>34 lệnh</td>
<td>File Markdown gọi bằng <code>/tên_file</code>, đóng vai trò điều phối gọi nhiều Skill theo thứ tự — đúng mục 5 bài trước.</td>
</tr>
<tr>
<td><strong>Prompts mẫu</strong><br/><code>prompts/</code></td>
<td>31 file <code>.txt</code></td>
<td>Bản copy-paste của từng tác vụ, dùng cho AI Agent không có slash command (Codex, Cursor, Antigravity...).</td>
</tr>
<tr>
<td><strong>Plans</strong><br/><code>plans/</code></td>
<td>3 quy trình</td>
<td>Quy trình 6 bước chuyên sâu (Manual AI-RBT, Automation, Cross-module) — chạy tuần tự trong cùng một cuộc hội thoại.</td>
</tr>
</tbody>
</table>

Điểm đáng chú ý: Skill `skills-requirements-analyzer` mà bạn tự viết ở bài trước **có tên trùng đúng với Skill thật trong bộ này**, và Command `/generate_testcases_from_requirements` cũng vậy. Đó không phải tình cờ — bài trước cố tình dùng đúng quy ước đặt tên của bộ Skills để hôm nay bạn nhìn vào là thấy quen ngay. Khác biệt duy nhất là độ sâu: bản trong repo có thêm quy tắc đánh mã REQ, quy tắc chụp evidence, Quality Gate tự chấm điểm...

### 1.2. Vì sao nên dùng bộ dựng sẵn thay vì tự viết hết?

- **Những thứ khó nhất đã được viết sẵn.** Ví dụ quy tắc "mở toàn bộ ảnh evidence trước khi viết Test Case, ảnh thắng tài liệu khi hai bên mâu thuẫn" — không tự nghĩ ra được nếu chưa từng bị AI bịa test case.
- **Các Skill nối được với nhau.** Đầu ra của Skill này là đầu vào của Skill kia, nhờ một quy ước chung về mã `REQ ID`, `TC ID` và cấu trúc thư mục `docs/`. Tự viết rời rạc thì mỗi Skill ra một định dạng, ghép lại không được.
- **Sửa được, không phải hộp đen.** Toàn bộ là file Markdown — bạn đọc hiểu, sửa theo chuẩn công ty mình. Bài "Thực hành chỉnh lại bộ Skills cho phù hợp dự án thực tế" ở phía sau sẽ làm đúng việc này.

## 2. Bên trong bộ Skills có gì?

Repo chia làm 2 phần rất rõ: **khung** (dùng lại cho mọi dự án) và **đầu ra** (dữ liệu của dự án bạn đang làm).

```none
claude-testing-skills/
│
│ ═══════════ KHUNG — dùng lại cho mọi dự án ═══════════
├── CLAUDE.md                 # RULE gốc: ngôn ngữ, quy trình, cấu trúc docs/ bắt buộc
├── .claude/
│   ├── commands/             # 34 slash command
│   ├── rules/                # 6 rule bắt buộc (browser, locator, reporting...)
│   ├── skills/               # 19 skill chuyên biệt
│   ├── settings.json         # cấu hình quyền hạn cho Claude Code
│   └── settings.local.json   # cấu hình riêng từng máy — đã gitignore
├── plans/                    # quy trình 6 bước: manual / automation / cross-module
├── prompts/                  # 31 prompt mẫu copy-paste
├── scripts/                  # 3 web viewer offline xem kết quả
│
│ ═══════════ ĐẦU RA — dữ liệu dự án của bạn ═══════════
└── docs/
    ├── requirements/         # tài liệu yêu cầu + evidence
    ├── testcases/            # bộ test case
    ├── executions/           # kết quả chạy + báo cáo
    └── bugs/                 # bug report
```

### 2.1. Các Skill dành cho Manual Tester

Trong 19 Skill, đây là nhóm bạn sẽ dùng nhiều nhất ở khoá này:

<table class="rt-table">
<thead>
<tr>
<th>Skill</th>
<th>Làm gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>skills-requirements-analyzer</code></td>
<td>Khảo sát hệ thống/tài liệu, sinh tài liệu Requirements có mã <code>REQ-&lt;MODULE&gt;-NN</code>, ghi nhận điểm mờ cần hỏi lại PO.</td>
</tr>
<tr>
<td><code>skills-rbt-manual-testing</code></td>
<td>Skill chủ lực sinh Manual Test Case theo Risk-Based Testing, có 4 chế độ: QUICK, FULL RBT, CHECKLIST, DELTA.</td>
</tr>
<tr>
<td><code>skills-testcase-reviewer</code></td>
<td>Review chất lượng bộ Test Case đã có: TC mơ hồ, trùng lặp, thiếu case biên/negative, chấm điểm theo rubric.</td>
</tr>
<tr>
<td><code>skills-manual-test-executor</code></td>
<td>Mở browser thật, chạy từng bước theo Test Case, chấm PASS/FAIL/BLOCKED/SKIPPED và thu ảnh evidence.</td>
</tr>
<tr>
<td><code>skills-bug-reporter</code></td>
<td>Sinh Bug Report chuẩn từ TC FAIL, tự lấy evidence của lần chạy vừa rồi, tuỳ chọn đẩy lên Jira.</td>
</tr>
<tr>
<td><code>skills-test-report-analyzer</code></td>
<td>Gom nhóm các TC FAIL theo nguyên nhân gốc — 12 TC FAIL thường chỉ do 2 bug.</td>
</tr>
<tr>
<td><code>skills-coverage-traceability</code></td>
<td>Sinh ma trận truy vết RTM: REQ nào chưa có TC, TC nào mồ côi không map về REQ nào.</td>
</tr>
<tr>
<td><code>skills-test-summary-reporter</code></td>
<td>Báo cáo tổng hợp tại mốc release, kết luận GO / GO có điều kiện / NO-GO kèm căn cứ.</td>
</tr>
</tbody>
</table>

Danh sách đầy đủ 19 Skill: [.claude/skills/](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/skills) · 34 Command: [.claude/commands/](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/commands) · 6 Rule: [.claude/rules/](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/rules)

> **Skill và Command khác nhau thế nào trong bộ này?**
>
> Command là "cửa vào" — bạn gõ `/generate_testcases_manual_rbt`, file command đó khai báo nó cần dùng Skills nào và điều phối thứ tự. Skills là "phần ruột" — chứa toàn bộ quy tắc chuyên môn. Vì vậy bạn **chỉ cần nhớ tên Command**, không cần nhớ tên Skill.

## 3. Cài đặt bộ Skills vào dự án của bạn

### 3.1. Bước 1 — Lấy repo về máy

Mở terminal tại thư mục bạn muốn chứa repo, chạy:

```none
git clone https://github.com/anhtester/claude-testing-skills.git
```

Nếu bạn đã cấu hình SSH key ở bài "Cài đặt và sử dụng Git GitHub GitLab":

```none
git clone git@github.com:anhtester/claude-testing-skills.git
```

### 3.2. Bước 2 — Chọn cách dùng

<table class="rt-table">
<thead>
<tr>
<th>Cách</th>
<th>Làm gì</th>
<th>Phù hợp khi</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cách A — Dùng thẳng repo</strong></td>
<td>Mở luôn thư mục <code>claude-testing-skills</code> vừa clone bằng Claude Code, làm việc trong đó.</td>
<td>Học theo khoá này, chưa có dự án riêng. <strong>Khuyến nghị cho bài này.</strong></td>
</tr>
<tr>
<td><strong>Cách B — Copy vào dự án có sẵn</strong></td>
<td>Copy thư mục <code>.claude/</code> và file <code>CLAUDE.md</code> sang thư mục gốc dự án của bạn.</td>
<td>Bạn đã có repo tài liệu test của công ty và muốn gắn bộ Skills vào đó.</td>
</tr>
</tbody>
</table>

Với **Cách B**, nên copy thêm `prompts/`, `plans/` và `scripts/` nếu bạn muốn dùng prompt mẫu và web viewer. Riêng `docs/` thì **không copy** — đó là dữ liệu của dự án mẫu, dự án của bạn sẽ tự sinh ra thư mục này.

**Lưu ý về `CLAUDE.md`**

nếu dự án của bạn *đã có* file `CLAUDE.md` riêng, đừng ghi đè. Hãy mở cả hai ra và gộp thủ công, hoặc giữ file của bạn rồi thêm một dòng trỏ tới các rule của bộ kit. Ghi đè là mất hết bối cảnh dự án bạn đã dày công viết ở bài trước.

### 3.3. Bước 3 — Mở bằng Claude Code

Claude Code tự động nhận diện `CLAUDE.md` và thư mục `.claude/` ở thư mục gốc — không cần khai báo hay import gì thêm.

<table class="rt-table">
<thead>
<tr>
<th>Bạn đang dùng</th>
<th>Cách mở</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claude Code CLI</strong></td>
<td>Mở terminal tại thư mục gốc dự án → gõ <code>claude</code></td>
</tr>
<tr>
<td><strong>Claude Code Desktop</strong></td>
<td>Mở app → chọn/thêm thư mục dự án làm working directory</td>
</tr>
<tr>
<td><strong>Claude Code trong VS Code</strong></td>
<td>Mở thư mục dự án trong VS Code → mở panel Claude Code (<code>Ctrl + Shift + P</code> → "Claude Code: Open")</td>
</tr>
</tbody>
</table>

> **Nếu bạn dùng Codex thay vì Claude Code:**
>
> bộ Skills này viết theo chuẩn Claude Code (`.claude/`, slash command). Codex không đọc được cấu trúc này. Thay vào đó hãy dùng thư mục [plans/manual/QUICK\_START.md](https://github.com/anhtester/claude-testing-skills/blob/main/plans/manual/QUICK_START.md) và [prompts/](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/README.md) — đó là bản copy-paste của cùng quy trình, dán thẳng vào Codex là chạy được.

## 4. Bật Playwright MCP — điều kiện để AI mở được browser thật

Copy `.claude/` vào dự án là AI đã có Rule/Skill/Command. Nhưng để AI **mở được trình duyệt thật** — điều kiện bắt buộc của các lệnh khảo sát hệ thống và chạy test tay — bạn cần thêm một công cụ bên ngoài tên **Playwright MCP**.

<table class="rt-table">
<thead>
<tr>
<th>Lệnh</th>
<th>Có cần Playwright MCP không?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/discover_system</code></td>
<td><strong>Bắt buộc</strong> — AI phải tự dạo qua hệ thống để vẽ bản đồ module</td>
</tr>
<tr>
<td><code>/generate_requirements_from_website</code></td>
<td><strong>Bắt buộc</strong> — phải mở từng form, trigger validation, chụp evidence</td>
</tr>
<tr>
<td><code>/execute_test_cases</code></td>
<td><strong>Bắt buộc</strong> — chạy từng bước test trên browser thật</td>
</tr>
<tr>
<td><code>/retest_fixed_bugs</code></td>
<td><strong>Bắt buộc</strong> — cùng lý do trên</td>
</tr>
<tr>
<td><code>/generate_testcases_manual_rbt</code>, <code>/review_testcases</code>, <code>/create_bug_report</code>, <code>/generate_traceability_matrix</code>...</td>
<td>Không cần — chỉ đọc/ghi file Markdown</td>
</tr>
</tbody>
</table>

### 4.1. Cách nhanh nhất — một lệnh cho Claude Code CLI

Chạy tại **thư mục gốc dự án**:

```none
claude mcp add --scope project playwright -- npx -y @playwright/mcp --viewport-size "1600,750" --config ".claude/playwright-mcp-config.json"
```

Lệnh này tạo file `.mcp.json` ở gốc dự án. Vì scope là `project`, file đó commit lên Git được — cả team dùng chung một cấu hình, không ai phải cài lại.

> **Vì sao là `1600×750` mà không phải `1920×1080`?**
>
> Cửa sổ trình duyệt **không nở ra được sau khi đã launch**, nên viewport phải đặt ngay lúc khởi động. Trên màn hình 1920×1080, thanh tab + thanh địa chỉ đã ăn mất chiều cao — đặt viewport bằng đúng kích thước màn là trang bị cắt mất phần bên phải, bạn nhìn không thấy. Màn hình khác thì tính lại: viewport = (rộng − 17) × (cao − 135). Ví dụ màn 1366×768 → `1349,633`.

### 4.2. Dùng Claude Code Desktop

Bản Desktop không có form điền sẵn — vào **Settings → Developer → Local MCP servers → Edit Config**, file `claude_desktop_config.json` sẽ mở ra, thêm khối `playwright` vào trong `mcpServers`:

```none
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Lưu file → **thoát hẳn Claude Desktop từ khay hệ thống** (không phải chỉ đóng cửa sổ) → mở lại → vào Settings → Developer, server `playwright` phải hiện trạng thái **running / connected**.

> ⚠️ **Nếu file đã có sẵn nội dung, đừng ghi đè cả file.** Nó còn chứa cấu hình khác của Claude Desktop. Chỉ thêm key `"playwright"` vào bên trong object `mcpServers`. Sai một dấu phẩy là Claude **im lặng không nạp server nào cả**, không báo lỗi gì.
>
> 🪟 **Windows báo lỗi `spawn npx ENOENT`?** Đổi sang dạng bọc: `"command": "cmd"` và `"args": ["/c", "npx", "-y", "@playwright/mcp@latest"]`.

Hướng dẫn đầy đủ (kèm cách cài Connector Atlassian/Slack/GitHub và bảng lỗi thường gặp): [SETUP\_CLAUDE.md](https://github.com/anhtester/claude-testing-skills/blob/main/SETUP_CLAUDE.md). Tài liệu chính thức về MCP của Claude Code: <https://code.claude.com/docs/en/mcp>.

> 📌 Bài **"Thiết lập MCP Server trên Claude và Codex"** ở phía sau khoá học sẽ đi sâu vào MCP (bao gồm cả Appium MCP cho mobile). Ở bài này bạn chỉ cần cài đúng Playwright MCP để chạy được các lệnh ở bài 7–9.

## 5. Nghiệm thu — kiểm tra bộ Skills đã hoạt động

Đừng vội chạy lệnh thật. Tick đủ 4 mục dưới đây trước, vì lỗi cài đặt thường lộ ra rất muộn và làm bạn tưởng là "AI dở".

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Kiểm tra thế nào</th>
<th>Kết quả đúng phải thấy</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Gõ dấu <code>/</code> trong ô chat</td>
<td>Danh sách gợi ý hiện ra các lệnh của bộ kit: <code>/discover_system</code>, <code>/generate_testcases_manual_rbt</code>, <code>/execute_test_cases</code>...</td>
</tr>
<tr>
<td>2</td>
<td>Hỏi: <em>"Bạn đang đọc được những rule nào của dự án này?"</em></td>
<td>AI liệt kê được <code>CLAUDE.md</code> và các file trong <code>.claude/rules/</code> (locator strategy, playwright rules, reporting rules...)</td>
</tr>
<tr>
<td>3</td>
<td>Hỏi: <em>"Liệt kê các skill bạn đang có"</em></td>
<td>AI kể được các skill <code>skills-*</code> của bộ kit, kèm mô tả ngắn — đúng phần <code>description</code> trong frontmatter.</td>
</tr>
<tr>
<td>4</td>
<td>Chạy thử <code>/discover_system</code> với một URL bất kỳ</td>
<td>Trình duyệt <strong>thật mở lên</strong> và AI bắt đầu dạo qua các trang. Không mở được browser ⟹ Playwright MCP chưa chạy, quay lại mục 4.</td>
</tr>
</tbody>
</table>

> **AI trả lời bằng tiếng Anh?**
>
> Kiểm tra lại xem `CLAUDE.md` đã nằm đúng ở **thư mục gốc** chưa — bộ kit có quy tắc bắt buộc giao tiếp bằng tiếng Việt ngay trong file này. Nếu `CLAUDE.md` nằm sai chỗ (trong thư mục con, hoặc bạn mở Claude Code ở thư mục cha), toàn bộ rule sẽ không được nạp.

## 6. Toàn cảnh quy trình 8 chặng cho Manual Testing

Bộ Skills không phải một đống lệnh rời rạc — nó là **một quy trình khép kín**, áp cho tình huống phổ biến nhất mà Tester gặp: *hệ thống chỉ có UI, không tài liệu, không bộ test case nào cả*.

```none
┌─ CHUẨN BỊ TÀI LIỆU ──────────────────────────────────────────────┐
│  0. /discover_system                     → bản đồ module + prefix│  1 lần / hệ thống
│  1. /generate_requirements_from_website  → REQ ID                │  N lần = số module
└──────────────────────────────────────────────────────────────────┘
                                  ↓
┌─ SINH & KIỂM TEST CASES ─────────────────────────────────────────┐
│  2. /generate_testcases_manual_rbt       → TC có cột REQ ID      │  N lần = số module
│  3. /review_testcases                    → chấm rubric, lấp gap  │
└──────────────────────────────────────────────────────────────────┘
                                  ↓
┌─ THỰC THI & XỬ LÝ LỖI ───────────────────────────────────────────┐
│  4. /execute_test_cases                  → chạy tay, chấm P/F/B/S│  Mỗi đợt kiểm thử
│  5. /analyze_test_report                 → gom nhóm root cause   │
│     /create_bug_report                   → bug report chuẩn      │
│     /retest_fixed_bugs   ←──── dev fix ───┘  → FIXED? regression?│  ↻ lặp tới khi hết bug
└──────────────────────────────────────────────────────────────────┘
                                  ↓
┌─ CHỨNG MINH ĐỘ PHỦ ──────────────────────────────────────────────┐
│  6. /generate_traceability_matrix        → RTM                   │  Trước release
└──────────────────────────────────────────────────────────────────┘
                                  ↓
┌─ BÁO CÁO & QUYẾT ĐỊNH ───────────────────────────────────────────┐
│  7. /generate_test_summary_report        → go / no-go có căn cứ  │  Mỗi mốc release
└──────────────────────────────────────────────────────────────────┘
```

### 6.1. Bảng tra nhanh — chạy lệnh nào, bao nhiêu lần

<table class="rt-table">
<thead>
<tr>
<th>Chặng</th>
<th>Lệnh</th>
<th>Đầu ra</th>
<th>Số lần chạy</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>0</strong></td>
<td><code>/discover_system</code></td>
<td>Bản đồ module + prefix mã</td>
<td><strong>1 lần</strong> cho cả hệ thống</td>
</tr>
<tr>
<td><strong>1</strong></td>
<td><code>/generate_requirements_from_website</code></td>
<td>Tài liệu yêu cầu có <code>REQ ID</code> + evidence</td>
<td><strong>N lần</strong> = số module</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><code>/generate_testcases_manual_rbt</code></td>
<td>Bộ Test Case có cột <code>REQ ID</code></td>
<td><strong>N lần</strong> = số module</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><code>/review_testcases</code></td>
<td>Điểm rubric + danh sách gap cần lấp</td>
<td>1 lần / bộ TC</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><code>/execute_test_cases</code></td>
<td>Execution report + ảnh evidence</td>
<td>Mỗi đợt kiểm thử</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><code>/analyze_test_report</code><br/><code>/create_bug_report</code><br/><code>/retest_fixed_bugs</code></td>
<td>Phân tích root cause · Bug report · Kết quả retest</td>
<td>Lặp tới khi hết bug</td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><code>/generate_traceability_matrix</code></td>
<td>Ma trận truy vết RTM</td>
<td>Trước release</td>
</tr>
<tr>
<td><strong>7</strong></td>
<td><code>/generate_test_summary_report</code></td>
<td>Báo cáo tổng hợp + khuyến nghị GO/NO-GO</td>
<td>Mỗi mốc release / sprint</td>
</tr>
</tbody>
</table>

Sơ đồ và bảng đầy đủ (kèm biến thể cho từng tình huống): [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md).

### 6.2. Mắt xích giữ cả chuỗi: `REQ ID`

Đây là ý quan trọng nhất của cả bài. Cả 8 chặng nối với nhau bằng **một sợi dây duy nhất là mã `REQ ID`**:

```none
Chặng 1 sinh ra REQ-LOGIN-01
        ↓
Chặng 2 ghi REQ-LOGIN-01 vào cột "REQ ID" của từng Test Case
        ↓
Chặng 6 đối chiếu: REQ nào chưa có TC nào cover → đó là lỗ hổng
```

Đứt ở đâu thì từ đó trở đi **bạn không chứng minh được "đã test đủ"**. Đó là lý do đừng nhảy thẳng vào chặng 2 dù rất muốn — sinh Test Case không có `REQ ID` thì sau này phải viết lại toàn bộ.

### 6.3. Ba chế độ sinh Test Case — chọn đúng cái

<table class="rt-table">
<thead>
<tr>
<th>Mode</th>
<th>Lệnh</th>
<th>Dùng khi</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>FULL RBT</strong></td>
<td><code>/generate_testcases_manual_rbt</code></td>
<td>Module lớn, yêu cầu còn mơ hồ, cần đánh giá rủi ro. Đây là <strong>bộ TC gốc</strong> của module.</td>
</tr>
<tr>
<td><strong>QUICK</strong></td>
<td><code>/generate_testcases_from_requirements</code></td>
<td>Yêu cầu đã rõ, phạm vi chỉ 1 form / 1 tính năng, cần nhanh.</td>
</tr>
<tr>
<td><strong>CHECKLIST</strong></td>
<td><code>/generate_checklist_test</code></td>
<td>Rà tay nhanh: smoke test, sau hotfix, trước release. Ra danh sách tick, <strong>không</strong> có steps.</td>
</tr>
</tbody>
</table>

> 💡 **Khuyến nghị:** module đầu tiên của hệ thống nên làm bằng **FULL RBT** — nó ép bạn trả lời những câu hỏi nghiệp vụ mà sau này kiểu gì cũng phải hỏi. Các module tương tự sau đó dùng QUICK cho nhanh.

Ba chặng 1, 2, 3 sẽ được thực hành chi tiết ở ba bài kế tiếp của khoá học, nên ở bài này bạn chỉ cần **thuộc bản đồ**, chưa cần chạy hết.

## 7. Đầu ra của bộ Skills — thư mục `docs/`

Mọi lệnh trong bộ kit đều ghi kết quả vào thư mục `docs/` theo một cấu trúc cố định. Đây không phải sở thích sắp xếp — **các lệnh phía sau đọc file theo đúng đường dẫn này**, đặt sai chỗ là chuỗi quy trình đứt.

```none
docs/
├── requirements/
│   ├── README.md                               ← DANH MỤC: module nào đã có tài liệu
│   ├── _discovery/system_map.md                ← bản đồ hệ thống (chặng 0)
│   └── <module>/
│       ├── requirements_<module>.md            ← TÊN FILE BẤT BIẾN
│       └── evidence/*.png                      ← ảnh chứng minh
├── testcases/
│   ├── README.md
│   └── <module>/test_cases_<module>.md         ← TÊN FILE BẤT BIẾN
├── executions/
│   ├── test_summary_<mốc>_<timestamp>.md       ← báo cáo cắt ngang mọi module
│   └── <module>/run_<timestamp>/
│       ├── execution_report.md
│       └── evidence/<TC_ID>_<mô_tả>.png
└── bugs/
    ├── README.md
    └── <module>/BUG_<module>_<timestamp>_<TC_ID>.md
```

### 7.1. Những quy tắc bất biến cần nhớ

<table class="rt-table">
<thead>
<tr>
<th>Quy tắc</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tên file index <strong>luôn</strong> là <code>requirements_&lt;module&gt;.md</code> / <code>test_cases_&lt;module&gt;.md</code>. Không thêm <code>_v2</code>, <code>_new</code>, <code>_final</code>...</td>
<td>Mọi lệnh phía sau đọc theo đúng mẫu đường dẫn này. Đổi tên là vỡ chuỗi truy vết. Bản cũ chuyển vào <code>archive/</code>.</td>
</tr>
<tr>
<td><strong>Không đánh lại mã REQ từ 01</strong> khi module đã có tài liệu. Mỗi module một prefix duy nhất.</td>
<td>Đụng mã là vỡ toàn bộ traceability — hai REQ khác nhau cùng số thì không ai lần ra được.</td>
</tr>
<tr>
<td><strong>Không xoá dòng REQ / không đổi TC ID.</strong> Tính năng bị gỡ thì đổi trạng thái sang Deprecated.</td>
<td>TC ID là khoá nối sang RTM và các execution report cũ. Đổi là cắt hết mối nối, không có cách nào phát hiện tự động.</td>
</tr>
<tr>
<td>🔒 <strong>Không ghi giá trị bí mật thật vào <code>docs/</code></strong> — mật khẩu, token, cookie, API key. Chỉ ghi <em>hình thái</em>, ví dụ <code>&lt;16 ký tự hex&gt;</code>.</td>
<td><code>docs/</code> được commit lên Git, và <strong>lịch sử Git không xoá được bằng cách sửa file</strong>. Credentials sống ở <code>.env</code> (đã gitignore).</td>
</tr>
<tr>
<td>📸 Evidence chụp <strong>đúng phạm vi cần chứng minh</strong>, không chụp thừa cả trang dữ liệu nghiệp vụ.</td>
<td>Ảnh full-page của màn hình nghiệp vụ kéo theo tên khách hàng, số tiền, nhật ký — không liên quan gì tới REQ mà vẫn bị commit.</td>
</tr>
</tbody>
</table>

### 7.2. Xem kết quả bằng web viewer, không cần đọc file Markdown thô

Trong thư mục `scripts/` có 3 trang web tĩnh, **double-click là mở, chạy offline, không cần cài gì**. Kéo thả file `.md` vào là xem được:

<table class="rt-table">
<thead>
<tr>
<th>Trang</th>
<th>Nạp file gì</th>
<th>Xem được gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>scripts/testcases-viewer/bundle.html</code></td>
<td><code>test_cases_*.md</code><br/><code>checklist_*.md</code></td>
<td>Duyệt, lọc, xuất Excel bộ Test Case</td>
</tr>
<tr>
<td><code>scripts/execution-viewer/bundle.html</code></td>
<td><code>execution_report.md</code><br/><code>retest_report.md</code><br/><code>traceability_matrix.md</code></td>
<td>Thống kê PASS/FAIL/BLOCKED/SKIPPED, <strong>so sánh giữa các lần chạy</strong> (mới fail · fail liên tục · vừa được fix), độ phủ automation</td>
</tr>
<tr>
<td><code>scripts/bugs-viewer/bundle.html</code></td>
<td><code>docs/bugs/README.md</code><br/><code>BUG_*.md</code></td>
<td>Lọc bug theo Severity/Priority/Trạng thái, xem lịch sử retest</td>
</tr>
</tbody>
</table>

Cả ba đều xuất được **CSV / Excel** đúng phần đang hiển thị — tiện khi sếp hoặc khách hàng cần file Excel thay vì Markdown.

## 8. Ba lỗi hay gặp nhất khi mới dùng bộ Skills

**Lỗi 1 — Nhảy thẳng vào chặng 2, bỏ qua chặng 0 và 1.**  
Rất dễ mắc, vì ai cũng muốn có Test Case ngay. Hậu quả: TC sinh ra không có `REQ ID` → chặng 6 không chạy được → không ai chứng minh được "đã test đủ". Sửa sau thì phải viết lại toàn bộ TC.

**Lỗi 2 — Bỏ qua checkpoint, gõ "tiếp tục" cho nhanh.**  
Nhiều lệnh trong bộ kit cố tình **dừng lại hỏi bạn** giữa chừng: ranh giới module ở đâu, phạm vi test tới đâu, còn scenario nào thiếu. Đó chính xác là những chỗ AI *không thể tự quyết đúng* vì nó không nắm nghiệp vụ. Bấm qua cho nhanh là đẩy sai lầm xuống tận chặng 4 mới lộ ra.

**Lỗi 3 — Tin con số coverage % mà không đọc phần "module chưa có tài liệu".**  
Coverage 95% mà còn 3 module chưa ai khảo sát thì con số đó vô nghĩa — nó chỉ tính trên phần *đã có* tài liệu. Luôn đọc mục cảnh báo module chưa khảo sát **trước** mọi tỷ lệ phần trăm.

> **Bonus — đừng để AI tự sửa Test Case trong lúc đang chạy test.**
>
> Nếu một TC FAIL vì viết sai (chứ không phải hệ thống lỗi), hãy **ghi nhận lại** rồi chạy tiếp. Chạy xong mới quay về `/review_testcases` để sửa. Sửa giữa chừng là mất dấu vết của chính lần chạy đó — báo cáo sau này không ai đối chiếu được.

## 9. Bài tập thực hành

**Bài tập 1 — Cài đặt và nghiệm thu.** Clone repo bộ Skills về máy, mở bằng Claude Code, cài Playwright MCP. Sau đó tick đủ 4 mục nghiệm thu ở mục 5. Chụp lại màn hình danh sách slash command hiện ra khi bạn gõ `/`.

**Bài tập 2 — Đọc để hiểu, không chỉ để chạy.** Mở file [.claude/skills/skills-rbt-manual-testing/SKILL.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-rbt-manual-testing/SKILL.md), đọc phần `description` trong frontmatter và liệt kê ra 4 chế độ (mode) mà Skill này hỗ trợ. Đối chiếu với bảng ở mục 6.3 xem mode nào ứng với lệnh nào.

**Bài tập 3 — So sánh với Skill bạn tự viết.** Mở [.claude/skills/skills-requirements-analyzer/SKILL.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-requirements-analyzer/SKILL.md) của bộ kit, đặt cạnh Skill cùng tên mà bạn tự viết ở bài trước. Viết ra **3 điểm** mà bản của bộ kit có thêm mà bản của bạn chưa có. Đây là bài tập quan trọng nhất — nó cho bạn thấy khoảng cách giữa "Skill chạy được" và "Skill dùng được trong dự án thật".

**Bài tập 4 (tuỳ chọn) — Chạy thử chặng 0.** Chọn một website bất kỳ mà bạn có tài khoản test, chạy `/discover_system` và quan sát: AI công bố mode gì ở câu đầu tiên, nó dừng lại hỏi bạn mấy câu, và nó tạo ra những file nào trong `docs/requirements/`. Chưa cần làm tiếp chặng 1 — bài kế tiếp sẽ làm.

## 10. Tổng kết

- Bộ **Testing Skills của Anh Tester** ([github.com/anhtester/claude-testing-skills](https://github.com/anhtester/claude-testing-skills)) là bản đầy đủ của đúng cơ chế RULE/SKILL/COMMAND bạn đã học ở bài trước: 6 Rule, 19 Skill, 34 Command, 31 prompt mẫu.
- Cài đặt gọn trong 2 việc: **copy `.claude/` + `CLAUDE.md`** vào thư mục gốc dự án, và **bật Playwright MCP** để AI mở được browser thật.
- Đừng bỏ bước nghiệm thu ở mục 5 — lỗi cài đặt hay bị nhầm thành "AI dở".
- Bộ kit là **một quy trình 8 chặng khép kín**, không phải một đống lệnh rời. Sợi dây nối cả chuỗi là mã `REQ ID`: chặng 1 sinh ra → chặng 2 gắn vào Test Case → chặng 6 dùng để chứng minh độ phủ.
- Mọi đầu ra nằm trong `docs/` theo cấu trúc cố định. Tên file index và mã REQ/TC là **bất biến** — đổi là vỡ chuỗi truy vết.
- Ba bài kế tiếp sẽ đi vào thực hành từng chặng: **phân tích Requirements**, **sinh Test Case**, rồi **review → thực thi → log bug**. Sau đó có riêng một bài hướng dẫn **chỉnh lại bộ Skills cho khớp chuẩn dự án thực tế** của công ty bạn.