# Bài 5 - Cách thiết lập SKILL, RULE cho AI Agent trên Claude + Codex

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/331](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/331)

✅ Thiết lập SKILLS, RULES, COMMANDS trên Claude Desktop  
✅ Thiết lập SKILL, RULES trên Codex

## 1. SKILL, RULE, COMMAND là gì và vì sao Tester cần tự thiết lập?

<table class="rt-table">
<thead>
<tr>
<th>Khái niệm</th>
<th>Bản chất</th>
<th>Khi nào nạp vào AI</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>RULE</strong><br/>(<code>CLAUDE.md</code> / <code>AGENTS.md</code>)</td>
<td>Một file text mô tả bối cảnh dự án và các quy tắc bắt buộc phải theo. Trên Claude Code, có thể tách thành nhiều file nhỏ trong <code>.claude/rules/</code> — xem mục 2.3.</td>
<td><strong>Luôn luôn</strong> được nạp ngay từ đầu mỗi phiên làm việc, dù bạn có nhắc tới hay không (riêng Rule trong <code>.claude/rules/</code> có khai báo <code>paths</code> thì chỉ nạp khi đụng tới file khớp).</td>
</tr>
<tr>
<td><strong>SKILL</strong></td>
<td>Một quy trình hoặc Một chuỗi kiến thức làm việc nhất định, được đóng gói sẵn (hướng dẫn nhiều bước, có thể kèm script/file phụ trợ), gọi ra bằng dấu <code>/</code>.</td>
<td>Chỉ nạp <strong>khi cần</strong>: hoặc bạn gõ tay <code>/ten-skill</code>, hoặc AI tự nhận thấy phù hợp và tự gọi.</td>
</tr>
<tr>
<td><strong>COMMAND</strong></td>
<td>
<p>Một file Markdown đơn giản trong <code>.claude/commands/</code>, nội dung file chính là prompt.</p>
<p>Nhưng cách dùng do mình quyết định, Commands để trình bày quy trình thực thi tổng quan cho một việc gồm nhiều khâu, Skill thì trình bày Kiến thức cho một việc nhất định.</p>
<p>Trong một Commands có thể gọi nhiều Skills.</p>
</td>
<td>
<p>Giống Skill: gọi bằng <code>/ten-file</code>. <strong>Trên Claude Code hiện nay, Command đã được gộp chung cơ chế với Skill</strong> — xem mục 3.6.</p>
</td>
</tr>
</tbody>
</table>

Vì sao Tester nên tự thiết lập thay vì chỉ dùng RULE/SKILL có sẵn?

- Mỗi công ty/dự án có **chuẩn Test Case, chuẩn Bug Report riêng** — RULE giúp AI nhớ chuẩn đó xuyên suốt, không phải nhắc lại mỗi prompt.
- Những việc bạn lặp đi lặp lại (sinh Test Case, review Test Case, viết Bug Report...) nên đóng gói thành **Skill** — gõ một lệnh ngắn thay vì paste lại cả đoạn prompt dài mỗi lần.
- Ở bài kế tiếp (bài 6), Anh Tester sẽ cung cấp cho bạn **một bộ Skill dựng sẵn cho Manual Testing**. Để dùng tốt bộ đó, bạn cần hiểu cơ chế Skill hoạt động thế nào — đó chính là nội dung bài này.

> **Lưu ý về tính cập nhật:** Cơ chế Skill là tính năng được các công cụ AI Agent cập nhật khá thường xuyên. Nội dung dưới đây tổng hợp theo tài liệu chính thức của Claude Code và Codex tính đến 8/2026. Nếu sau này có khác biệt, hãy ưu tiên gõ dấu `/` trong ứng dụng bạn đang dùng hoặc đọc tài liệu chính thức để đối chiếu lại.

## 2. Thiết lập RULE

### 2.1. Thiết lập file RULE toàn cục cho một repo source

#### 🔆 CLAUDE.md và AGENTS.md ở gốc dự án

#### 🟢 CLAUDE.md — dành cho Claude Code

Đây là file markdown chứa hướng dẫn được Claude Code đọc vào đầu mỗi phiên làm việc, giúp Claude "nhớ" ngữ cảnh dự án xuyên suốt các lần chạy khác nhau (vì mỗi phiên vốn bắt đầu từ bộ nhớ trống).

**Các cấp độ (từ rộng đến hẹp):**

- **Chính sách tổ chức** — file quản lý tập trung, áp dụng cho mọi máy trong công ty
- **Cá nhân, mọi dự án** — `~/.claude/CLAUDE.md` (Toàn cục)
- **Cá nhân, dự án riêng** — `./CLAUDE.md` hoặc `./.claude/CLAUDE.md`

Claude Code đọc ngược từ thư mục làm việc lên tới thư mục gốc; các file `CLAUDE.md` nằm trong thư mục con chỉ được nạp khi Claude thực sự đọc file trong thư mục đó. Nên giữ mỗi file dưới khoảng 200 dòng, viết ngắn gọn cụ thể (ví dụ "dùng thụt lề 2 khoảng trắng" thay vì "định dạng code cho gọn"), vì file càng dài thì độ tuân thủ càng giảm. Có thể chạy `/init` để tự sinh file này, và `/memory` để xem/sửa.

Cấu trúc thư mục — CLAUDE.md + rule rẽ nhánh

```text
manual-test-project/
├── CLAUDE.md                           # Nạp mỗi phiên — hướng dẫn chung toàn dự án
├── .claude/
│   ├── rules/
│   │   ├── testcase_rules.md           # Quy ước viết test case (paths: test-cases/**)
│   │   ├── bugreport_rules.md          # Quy ước báo cáo lỗi (paths: bug-reports/**)
│   │   ├── checklist_rules.md          # Quy ước checklist (paths: checklists/**)
│   │   └── module_thanh_toan.md        # Rule riêng, nhạy cảm hơn (paths: test-cases/module-thanh-toan/**)
│   └── skills/
│       ├── skills-rbt-manual-testing/
│       │   └── SKILL.md                # Sinh manual test case từ requirements
│       ├── skills-testcase-reviewer/
│       │   └── SKILL.md                # Review test case: TC mơ hồ, thiếu assertion, trùng lặp
│       └── skills-bug-reporter/
│           └── SKILL.md                # Sinh bug report chuẩn kèm evidence từ test FAIL
├── docs/
│   ├── test-strategy.md
│   └── environment-setup.md
├── test-plans/
│   └── release-1.0-test-plan.md
├── test-cases/
│   ├── module-dang-nhap/
│   ├── module-thanh-toan/
│   └── module-quan-ly-don-hang/
├── checklists/
│   ├── smoke-test-checklist.md
│   └── regression-checklist.md
├── bug-reports/
└── test-data/
    └── accounts.csv
```

Trong cây trên, **RULE là thứ bạn tự viết** — mỗi công ty một chuẩn test case/bug report khác nhau, không dùng chung được. Ngược lại **SKILL thì dùng lại được**: ba Skill trong ví dụ (`skills-rbt-manual-testing`, `skills-testcase-reviewer`, `skills-bug-reporter`) là Skill có thật trong bộ Testing Skills của Anh Tester tại [github.com/anhtester/claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bài 6 sẽ hướng dẫn cài cả bộ — ở đây bạn chỉ cần nhớ chúng nằm ở đâu trong dự án.

Ví dụ nội dung trình bày trong CLAUDE.md

```none
# Ngữ cảnh dự án
Dự án: Hệ thống CRM
Vai trò của bạn: Senior Manual Tester

# Quy tắc viết Test Case
- Mã Test Case theo định dạng: TC_<MODULE>_<số thứ tự 3 chữ số>.
- Mỗi Test Case bắt buộc có: Mã Test Case, Tiền điều kiện, Các bước, Dữ liệu test, Kết quả mong đợi, Độ ưu tiên.
```

File này được AI đọc **tự động**, ngay cả khi bạn không nhắc gì tới nó. Đây là lý do RULE phù hợp cho những thứ mang tính *quy tắc/bối cảnh cố định*, còn quy trình nhiều bước nên tách ra thành Skill (mục 3, 4) để không làm RULE phình to.

```markdown
# CLAUDE.md — Dự án Manual Test [Tên sản phẩm]

## Tổng quan
Repo này chứa toàn bộ tài liệu kiểm thử thủ công cho [tên sản phẩm]:
test case, checklist, báo cáo lỗi, kế hoạch kiểm thử. Đây không phải
repo chứa code nguồn ứng dụng.

## Quy ước đặt tên
- Test case: `TC_<MODULE>_<SỐ THỨ TỰ>.md`, ví dụ `TC_LOGIN_003.md`
- Báo cáo lỗi: `BUG_<SỐ THỨ TỰ>_<mô-tả-ngắn-không-dấu>.md`
- Mỗi module có một thư mục riêng trong `test-cases/`

## Định dạng một test case
Mỗi file test case phải có đủ các mục sau, theo đúng thứ tự:1. Mã test case
2. Mục tiêu kiểm thử
3. Điều kiện tiên quyết
4. Các bước thực hiện (đánh số)
5. Kết quả mong đợi
6. Mã ticket Jira liên quan (nếu có), định dạng `PROJ-1234`7. Mức độ8. Làm Automation (Yes/No)

## Định dạng báo cáo lỗi
- Luôn ghi rõ: môi trường (Windows/macOS, trình duyệt/phiên bản),
  bước tái hiện, kết quả thực tế vs kết quả mong đợi, mức độ nghiêm trọng
- Gắn link Jira ticket tương ứng nếu lỗi đã được tạo ticket
- Không đánh dấu bug là "Đã sửa" nếu chưa có xác nhận retest

## Khi hỗ trợ viết test case
- Ưu tiên bám sát acceptance criteria trong ticket Jira được cung cấp
- Luôn bao gồm cả trường hợp âm tính (negative case) và trường hợp biên (edge case)
- Không tự suy đoán kết quả mong đợi nếu tài liệu chưa nêu rõ — hỏi lại
  thay vì đoán

## Khi hỗ trợ tổng hợp báo cáo test
- Trình bày theo bảng: Module | Số test case | Pass | Fail | Blocked
- Không tự ý đánh giá "sẵn sàng release" — chỉ tổng hợp số liệu thực tế

## Ngôn ngữ
Toàn bộ tài liệu viết bằng tiếng Việt, thuật ngữ kỹ thuật giữ nguyên
tiếng Anh khi chưa có từ tương đương phổ biến (ví dụ: bug, ticket).
```

#### 🔵 AGENTS.md — dành cho Codex

#### Phạm vi toàn cục

Đặt tại `~/.codex/AGENTS.md` (thư mục cấu hình Codex, mặc định `~/.codex`). Đây là nơi ghi các quy ước áp dụng cho mọi dự án bạn làm việc. Theo từng máy tính khi cài Codex.

#### Phạm vi cục bộ (trong repo)

Bắt đầu từ gốc dự án, Codex đi dần xuống đến thư mục làm việc hiện tại, kiểm tra từng thư mục trên đường đi xem có `AGENTS.md` không. Mỗi thư mục chỉ lấy một file. Nhờ vậy, trong một kho mã nguồn dùng chung nhiều gói, mỗi gói con có thể có `AGENTS.md` riêng, chứa quy ước chỉ áp dụng cho gói đó — ví dụ gốc dự án ghi quy tắc chung, còn `services/payments/AGENTS.md` ghi thêm lệnh kiểm thử riêng của dịch vụ đó.

#### Trong dự án cụ thể:

```text
manual-test-project/                     # Gốc dự án (Git root)
├── AGENTS.md                            # Quy ước chung toàn dự án
├── .agents/
│   └── skills/                          # Bản Codex bỏ tiền tố "skills-" ở tên thư mục
│       ├── rbt-manual-testing/
│       │   └── SKILL.md
│       ├── testcase-reviewer/
│       │   └── SKILL.md
│       └── bug-reporter/
│           └── SKILL.md
├── docs/
├── test-plans/
├── test-cases/
│   ├── module-dang-nhap/
│   ├── module-thanh-toan/
│   │   └── AGENTS.md                    # Quy tắc riêng — đây là cách "rẽ nhánh" của Codex
│   └── module-quan-ly-don-hang/
├── checklists/
├── bug-reports/
│   └── AGENTS.md                        # Quy ước riêng cho báo cáo lỗi
└── test-data/
```

#### Cách gộp và thứ tự ưu tiên

Codex nối các file lại theo thứ tự: **toàn cục trước, rồi đến các file cục bộ theo hướng từ gốc dự án xuống thư mục hiện tại**, mỗi file cách nhau một dòng trống. File càng gần thư mục làm việc hiện tại thì càng nằm ở cuối văn bản gộp — nên nếu có mâu thuẫn, hướng dẫn cục bộ (cụ thể hơn) được coi trọng hơn hướng dẫn toàn cục.

### 2.2. Một vài mẹo khi viết RULE

- **Giữ RULE ngắn gọn.** RULE được nạp vào *mọi* phiên, kể cả khi không dùng tới — RULE càng dài, càng tốn ngữ cảnh (token) một cách vô ích. Quy trình dài, ít dùng → đưa vào Skill thay vì RULE.
- **Viết dạng gạch đầu dòng, tránh văn xuôi dài dòng.** AI đọc danh sách quy tắc rõ ràng hiệu quả hơn một đoạn văn giải thích.
- **Nêu rõ điều KHÔNG được làm**, không chỉ điều nên làm — ví dụ "Không tự ý xoá file trong thư mục /docs" giúp tránh AI làm quá tay.
- **Với Codex:** ngoài `AGENTS.md` ở thư mục dự án, Codex còn đọc `AGENTS.md` ở thư mục Codex Home (mặc định `~/.codex`) cho các quy tắc áp dụng chung cho mọi dự án của bạn — tương tự Skill cá nhân của Claude ở mục 3.2. Nếu có cả hai, Codex ghép nội dung lại, phần ở thư mục dự án được ưu tiên hơn khi có xung đột.

Việc tổ chức RULE cho dự án lớn, nhiều sub-project... sẽ được nói kỹ hơn ở bài **"Xây dựng bộ nhớ Local dành riêng cho từng dự án chuyên biệt"** phía sau. Ở đây bạn chỉ cần nắm nguyên tắc: RULE = quy tắc cố định, ngắn gọn, luôn nạp.

### 2.3. Tách RULE thành nhiều file với .claude/rules/

Khi `CLAUDE.md` phình to vì gộp nhiều chủ đề khác nhau (chuẩn Test Case, chuẩn Bug Report, quy tắc bảo mật...), Claude Code cho tách các quy tắc đó ra thành nhiều file nhỏ trong thư mục `.claude/rules/`, đặt ở thư mục gốc dự án — bên cạnh `CLAUDE.md` đã tạo ở mục 2.1:

```none
ten-du-an/
├── CLAUDE.md
└── .claude/
    └── rules/
        ├── testcase-style.md
        ├── bugreport-style.md
        └── automation/
            └── selenium-convention.md
```

Toàn bộ file `.md` trong `.claude/rules/` (kể cả thư mục con) được Claude Code **tự động tìm và nạp** — không cần khai báo hay trỏ đường dẫn gì thêm trong `CLAUDE.md`. Nếu file không có phần khai báo `paths`, nó được nạp ngay từ đầu phiên, cùng mức ưu tiên với `CLAUDE.md`.

Điểm mạnh riêng của `.claude/rules/` so với việc viết thẳng vào `CLAUDE.md`: có thể giới hạn một Rule chỉ nạp khi Claude đang làm việc với đúng loại file liên quan, bằng cách thêm phần khai báo `paths` (dùng glob pattern) ở đầu file:

```none
---
paths:
  - "tests/**/*.md"
---

# Quy tắc đặt tên file Test Case
- Tên file: testcases_<module>.md
- Mỗi file chỉ chứa Test Case của đúng 1 module.
```

Với khai báo trên, Rule này **chỉ nạp vào ngữ cảnh khi Claude đang đọc/sửa file trong thư mục `tests/`**, không tốn token ở những phiên không đụng tới thư mục đó — khác với `CLAUDE.md` hoặc Rule không có `paths`, vốn luôn nạp bất kể đang làm gì. Đây chính là cách áp dụng thực tế nguyên tắc "giữ RULE ngắn gọn" đã nói ở mục 2.2, cho những quy tắc dài nhưng chỉ liên quan đến một phần cụ thể của dự án.

Cũng có Rule cá nhân áp dụng cho mọi dự án, tương tự Skill cá nhân ở mục 3.2: đặt file vào `~/.claude/rules/`.

> **Với Codex:** hiện Codex chưa có cơ chế tách nhiều file Rule kèm nạp theo `paths` tương đương `.claude/rules/` — chỉ có `AGENTS.md` ở thư mục dự án và thư mục Codex Home như đã nói ở mục 2.2.

## 3. Thiết lập SKILL & COMMAND trên Claude Desktop

### 3.1. Nên tạo Skill khi nào?

Tạo Skill khi bạn thấy mình **liên tục copy-paste cùng một đoạn prompt**, hoặc một phần trong `CLAUDE.md` đã phình to thành cả một quy trình nhiều bước thay vì một quy tắc đơn giản. Khác với RULE, nội dung Skill chỉ tốn ngữ cảnh khi thật sự được gọi tới.

### 3.2. Skill lưu ở đâu?

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Đường dẫn</th>
<th>Áp dụng cho</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cá nhân</td>
<td><code>~/.claude/skills/&lt;ten-skill&gt;/SKILL.md</code></td>
<td>Mọi dự án bạn mở trên máy này.</td>
</tr>
<tr>
<td>Theo dự án</td>
<td><code>.claude/skills/&lt;ten-skill&gt;/SKILL.md</code> (đặt ở thư mục gốc dự án)</td>
<td>Chỉ dự án đó. Có thể commit vào Git để chia sẻ cho cả team.</td>
</tr>
</tbody>
</table>

Với Tester mới bắt đầu: nên để Skill cá nhân trước (áp dụng được ngay cho mọi dự án đang test), khi nào làm việc nhóm và cần chuẩn chung cho cả team thì chuyển sang Skill theo dự án và đưa vào Git.

### 3.3. Cấu trúc file SKILL.md

Một Skill tối thiểu chỉ cần một file `SKILL.md` gồm 2 phần: phần khai báo (frontmatter, nằm giữa hai dòng `---`) và phần nội dung hướng dẫn.

```none
---
name: my-skill
description: Mô tả ngắn gọn skill làm gì và dùng khi nào. Đây là phần AI dùng để tự quyết định có nên gọi skill này hay không.
---

Nội dung hướng dẫn Claude thực hiện khi Skill được gọi.
```

Một số trường (field) hay dùng nhất trong phần khai báo:

<table class="rt-table">
<thead>
<tr>
<th>Trường</th>
<th>Ý nghĩa</th>
<th>Có bắt buộc?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>Tên định danh của skill. Theo chuẩn Agent Skills (chuẩn chung mà cả Claude và Codex dùng), đây là trường <strong>bắt buộc</strong>. Với skill cá nhân/dự án trên Claude Code, lệnh gọi thực tế vẫn luôn lấy theo <em>tên thư mục</em> chứa <code>SKILL.md</code> chứ không lấy theo giá trị <code>name</code> — nên đặt <code>name</code> trùng với tên thư mục cho nhất quán. Ví dụ thư mục <code>skills-testcases-generate/</code> nên có <code>name: skills-testcases-generate</code>, và luôn tạo ra lệnh <code>/skills-testcases-generate</code>.</td>
<td>Có</td>
</tr>
<tr>
<td><code>description</code></td>
<td>Mô tả skill làm gì và <strong>dùng khi nào</strong>. Đây là "chìa khoá" để AI tự nhận biết lúc nào nên gọi skill này — mô tả càng cụ thể, AI càng gọi đúng lúc.</td>
<td>Có</td>
</tr>
<tr>
<td><code>disable-model-invocation</code></td>
<td>Đặt <code>true</code> để <strong>chỉ bạn</strong> mới gọi được skill bằng tay (AI không tự ý gọi). Phù hợp cho các skill có hành động nhạy cảm (ví dụ gửi báo cáo, tạo file quan trọng). Chi tiết cơ chế: <a href="https://code.claude.com/docs/en/skills">tài liệu chính thức Claude Code — mục "Control who invokes a skill"</a>.</td>
<td>Không</td>
</tr>
<tr>
<td><code>allowed-tools</code></td>
<td>Danh sách công cụ được phép dùng mà không cần hỏi xin quyền lại mỗi lần, trong lượt gọi skill đó.</td>
<td>Không</td>
</tr>
<tr>
<td><code>argument-hint</code></td>
<td>Gợi ý tham số hiển thị khi gõ tự động hoàn thành, ví dụ <code>[ten-chuc-nang]</code>.</td>
<td>Không</td>
</tr>
</tbody>
</table>

Trong nội dung hướng dẫn, có thể dùng `$ARGUMENTS` để nhận phần bạn gõ thêm sau tên skill. Ví dụ gõ `/skills-testcases-generate Đăng nhập bằng Email` thì `$ARGUMENTS` sẽ được thay bằng `Đăng nhập bằng Email`.

### 3.4. Thực hành: tạo bộ 2 Skill liên kết nhau

Một Skill không nhất thiết phải đứng riêng lẻ. Phần này dựng **2 Skill phối hợp với nhau**: Skill thứ nhất phân tích yêu cầu, Skill thứ hai dùng lại kết quả đó để sinh Test Case — cả hai đều tuân theo quy tắc đã đặt trong `CLAUDE.md` ở mục 2.

#### Skill 1 — "skills-requirements-analyzer"

**Bước 1** — Tạo thư mục:

```none
mkdir -p ~/.claude/skills/skills-requirements-analyzer
```

**Bước 2** — Tạo file `SKILL.md`:

```none
---
name: skills-requirements-analyzer
description: Phân tích một yêu cầu/chức năng thành Happy Path, Alternate Path, Exception Path và liệt kê các điểm còn mơ hồ cần hỏi lại. Dùng trước khi sinh Test Case cho một chức năng phức tạp, nhiều luồng xử lý.
argument-hint: [mô tả chức năng cần phân tích]
---

Đóng vai Senior QA Engineer chuyên phân tích Requirement. Phân tích chức năng sau: $ARGUMENTS

Yêu cầu:
- Bóc tách thành 3 luồng: Happy Path (luồng chính), Alternate Path (luồng thay thế), Exception Path (luồng lỗi/bị từ chối).
- Liệt kê các điểm còn mơ hồ, thiếu sót hoặc mâu thuẫn trong mô tả (nếu có), đặt thành câu hỏi cần người dùng làm rõ.
- Trình bày dạng danh sách rõ ràng theo từng luồng, viết bằng tiếng Việt.
```

#### Skill 2 — "skills-testcases-generate" (dùng lại kết quả của Skill 1)

**Bước 1** — Tạo thư mục:

```none
mkdir -p ~/.claude/skills/skills-testcases-generate
```

**Bước 2** — Tạo file `SKILL.md`:

```none
---
name: skills-testcases-generate
description: Sinh bộ Test Case Manual đầy đủ (Happy path, Negative case, Edge case) từ mô tả một chức năng. Dùng khi cần viết Test Case nhanh cho một chức năng cụ thể, có thể dùng ngay sau Skill skills-requirements-analyzer.
argument-hint: [mô tả chức năng cần test]
---

Đóng vai Senior Manual QA Engineer. Sinh bộ Test Case Manual cho chức năng sau: $ARGUMENTS

Nếu trong hội thoại đã có kết quả phân tích luồng (Happy/Alternate/Exception Path) từ Skill skills-requirements-analyzer, hãy dùng chính kết quả đó làm nền — không phân tích lại từ đầu.

Yêu cầu:
- Bao gồm Happy path, Negative case, Edge case (tối thiểu 30% là Negative/Edge case).
- Mỗi Test Case có: Tiền điều kiện, Các bước thực hiện, Dữ liệu test, Kết quả mong đợi, Độ ưu tiên (High/Medium/Low).
- Mã Test Case theo định dạng: TC_<MODULE>_<số thứ tự 3 chữ số>.
- Trình bày dạng bảng Markdown.
- Viết toàn bộ bằng tiếng Việt.
```

**Bước 3** — Mở Claude Code, gọi lần lượt hai Skill trong cùng một đoạn hội thoại:

```none
/skills-requirements-analyzer Quên mật khẩu qua Email

/skills-testcases-generate Quên mật khẩu qua Email
```

Ở lệnh gọi thứ nhất, Claude trả về 3 luồng (Happy/Alternate/Exception) kèm câu hỏi cần làm rõ. Ở lệnh gọi thứ hai, Claude tận dụng luôn kết quả vừa có ở trên (vì vẫn trong cùng phiên chat) để sinh Test Case, thay vì phân tích lại từ đầu — đây chính là cách một Skill "dùng lại" kết quả của Skill khác.

> **Để ý:** quy tắc `TC_<MODULE>_<số>` trong Skill `skills-testcases-generate` chính là quy tắc đã đặt trong `CLAUDE.md` ở bài trước. Bạn có thể để quy tắc đó nằm trong `CLAUDE.md` (áp dụng chung, luôn nạp) và/hoặc nhắc lại trong Skill (để chắc chắn được áp dụng ngay cả khi ai đó dùng chung dự án nhưng không đọc kỹ `CLAUDE.md`). Không có gì sai khi lặp lại một quy tắc quan trọng ở cả hai nơi.

### 3.5. Gọi Skill: để AI tự gọi hay gọi tay?

- **Mặc định**: cả hai đều được. Bạn gõ `/skills-testcases-generate ...` để gọi trực tiếp; hoặc chỉ cần hỏi bằng lời tự nhiên kiểu "Viết test case cho chức năng đăng nhập giúp tôi", Claude thấy khớp với `description` của skill thì sẽ tự nạp và áp dụng.
- **Muốn bắt buộc gọi tay** (ví dụ skill có hành động nhạy cảm như ghi đè file, gửi báo cáo): thêm `disable-model-invocation: true` vào phần khai báo.
- **Kiểm tra skill đã có những gì:** gõ dấu `/` trong ô nhập, danh sách hiện ra sẽ có cả skill bạn vừa tạo.

### 3.6. Command kiểu cũ (`.claude/commands/`) — vẫn dùng được không?

Trước khi có Skill, Claude Code chỉ có **Custom Command**: một file Markdown đặt trong `.claude/commands/`, nội dung file chính là prompt, gọi bằng tên file (không có phần đuôi `.md`).

```none
# .claude/commands/report-bug.md
Viết Bug Report cho lỗi vừa phát hiện, theo mẫu:
[Module] Mô tả ngắn gọn lỗi
- Steps to Reproduce (đánh số)
- Actual Result
- Expected Result
- Severity
```

File trên tạo ra lệnh `/report-bug`, hoạt động giống hệt một Skill đơn giản. Hiện tại, **Command đã được gộp chung cơ chế với Skill**: file ở `.claude/commands/deploy.md` và một Skill ở `.claude/skills/deploy/SKILL.md` đều tạo ra cùng lệnh `/deploy` và hoạt động như nhau.

Command cũng có thể dùng để **gọi nối tiếp nhiều Skill theo đúng thứ tự**, thay vì chỉ chứa một đoạn prompt đơn lẻ. Ví dụ file sau gộp lại đúng 2 bước đã làm ở mục 3.4 thành một lệnh duy nhất:

```none
# .claude/commands/generate_testcases_from_requirements.md
Thực hiện lần lượt các bước sau cho chức năng: $ARGUMENTS

1. Dùng Skill `skills-requirements-analyzer` để bóc tách Happy Path, Alternate Path, Exception Path và liệt kê điểm còn mơ hồ. Nếu có điểm mơ hồ quan trọng, dừng lại hỏi người dùng trước khi làm bước 2.
2. Dùng Skill `skills-testcases-generate` để sinh Test Case đầy đủ dựa trên kết quả bước 1, tuân thủ đúng quy tắc TC_<MODULE>_<số> đã đặt trong CLAUDE.md.
```

File trên tạo ra lệnh `/generate_testcases_from_requirements`: gõ `/generate_testcases_from_requirements Quên mật khẩu qua Email` là chạy đúng 2 bước theo thứ tự đã định sẵn, thay vì phải tự tay gõ lần lượt `/skills-requirements-analyzer` rồi `/skills-testcases-generate`. Đây cũng chính là ví dụ cụ thể cho phần **mapping giữa RULE, SKILL và COMMAND** ở mục 5.

Vì vậy:

- Các file `.claude/commands/` cũ vẫn chạy bình thường, không cần chuyển đổi gấp.
- Với skill/command **tạo mới**, nên dùng thư mục `.claude/skills/` vì có thêm các tính năng Command không có: thư mục con chứa file/script phụ trợ, kiểm soát ai được gọi (`disable-model-invocation`), và để AI tự động nạp khi phù hợp.
- Nếu cả Skill và Command trùng tên, Skill được ưu tiên chạy.

## 4. Thiết lập SKILL trên Codex

### 4.1. Vị trí lưu Skill trên Codex

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Đường dẫn</th>
<th>Áp dụng cho</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cá nhân</td>
<td><code>~/.agents/skills/&lt;ten-skill&gt;/SKILL.md</code></td>
<td>Mọi dự án bạn mở trên máy này.</td>
</tr>
<tr>
<td>Theo dự án</td>
<td><code>.agents/skills/&lt;ten-skill&gt;/SKILL.md</code> (đặt ở thư mục gốc dự án)</td>
<td>Chỉ dự án đó. Có thể commit vào Git để chia sẻ cho cả team.</td>
</tr>
</tbody>
</table>

Đúng vậy — thư mục là `.agents` (không phải `.codex`) vì Skill đi theo chuẩn mở **Agent Skills**, dùng chung được giữa nhiều công cụ AI khác nhau chứ không riêng gì Codex.

### 4.2. Cấu trúc SKILL.md trên Codex

Về cơ bản giống Claude: file `SKILL.md` gồm phần khai báo (`name`, `description`) và phần nội dung hướng dẫn.

```none
---
name: skills-testcases-generate
description: Sinh bộ Test Case Manual đầy đủ (Happy path, Negative case, Edge case) từ mô tả một chức năng.
---

Đóng vai Senior Manual QA Engineer. Sinh bộ Test Case Manual cho chức năng được mô tả.

Yêu cầu:
- Bao gồm Happy path, Negative case, Edge case.
- Mỗi Test Case có: Tiền điều kiện, Các bước thực hiện, Dữ liệu test, Kết quả mong đợi, Độ ưu tiên.
- Mã Test Case theo định dạng: TC_<MODULE>_<số thứ tự 3 chữ số>.
- Trình bày dạng bảng Markdown, viết bằng tiếng Việt.
```

### 4.3. Thực hành: tạo Skill tương tự cho Codex

**Bước 1** — Tạo thư mục:

```none
mkdir -p ~/.agents/skills/skills-testcases-generate
```

**Bước 2** — Lưu nội dung ở mục 4.2 vào file `~/.agents/skills/skills-testcases-generate/SKILL.md`.

**Bước 3** — Mở Codex, gõ dấu `/` để kiểm tra skill đã xuất hiện trong danh sách, hoặc gõ thẳng yêu cầu bằng lời tự nhiên khớp với mô tả để Codex tự nhận diện và áp dụng.

Bộ 2 Skill liên kết nhau ở mục 3.4 (`skills-requirements-analyzer` + `skills-testcases-generate`) áp dụng y hệt trên Codex, chỉ đổi đường dẫn thành `~/.agents/skills/skills-requirements-analyzer/SKILL.md` và `~/.agents/skills/skills-testcases-generate/SKILL.md`. Điểm khác biệt: vì Codex không có Command riêng (mục 4.4), muốn gộp 2 bước thành một lệnh gọi tắt như `/generate_testcases_from_requirements` ở mục 3.6, cách làm là viết thêm một Skill thứ ba mà nội dung chỉ đơn giản là chỉ dẫn gọi lần lượt 2 Skill kia — không có cơ chế Command tách biệt để làm việc này.

### 4.4. Lưu ý: Custom Prompts trên Codex đã bị thay thế

> Trước đây Codex có **Custom Prompts** (file đặt trong `~/.codex/prompts`) làm cùng vai trò với Command của Claude. Tính năng này hiện đã **deprecated (không còn khuyến khích dùng)** — Codex khuyến nghị dùng **Skill** thay thế cho mọi nhu cầu tạo lệnh/quy trình tuỳ chỉnh, vì Skill vừa gọi tay được bằng `/`, vừa để Codex tự nhận diện và gọi khi phù hợp, lại chia sẻ được qua Git nếu đặt ở thư mục dự án.

## 5. Mapping giữa RULE, SKILL và COMMAND

Ở bài Antigravity trước, 3 khái niệm RULE — SKILL — WORKFLOW nằm tách biệt thành 3 thư mục riêng (`.agent/rules/`, `.agent/skills/`, `.agent/workflows/`), trong đó WORKFLOW đóng vai trò điều phối gọi đến RULE và SKILL theo đúng trình tự. **Trên Claude Code và Codex không có tầng WORKFLOW riêng** — đừng nhầm hai cơ chế này với nhau. Vai trò "điều phối nhiều Skill theo trình tự" được gộp thẳng vào chính nội dung của một SKILL hoặc COMMAND, như ví dụ `/generate_testcases_from_requirements` ở mục 3.6.

Ráp lại đúng những gì đã tạo ở các mục trước, sơ đồ gọi thực tế trên Claude Code như sau:

```none
/generate_testcases_from_requirements Quên mật khẩu qua Email          (COMMAND — người dùng gõ)
  │
  ├─ 1. gọi Skill "skills-requirements-analyzer"             (SKILL — năng lực phân tích)
  │
  └─ 2. gọi Skill "skills-testcases-generate"                  (SKILL — năng lực sinh Test Case)
        └─ áp dụng quy tắc TC_<MODULE>_<số>   (RULE — CLAUDE.md, luôn được nạp sẵn)
```

> **Lưu ý về cơ chế:** dòng "Dùng Skill `skills-requirements-analyzer`" trong nội dung Command **không phải một lệnh gọi hàm được đảm bảo** — đó vẫn là một câu hướng dẫn bằng ngôn ngữ tự nhiên. Claude Code nạp sẵn `description` của mọi Skill vào ngữ cảnh; khi đọc thấy hướng dẫn này khớp với một Skill đang có, Claude **tự quyết định** gọi Skill đó — trên thực tế rất đáng tin cậy nếu hướng dẫn rõ ràng, nhưng về bản chất vẫn là Claude "làm theo lời dặn" (giống cơ chế tự nhận diện đã nói ở mục 3.5), không phải một cơ chế lập trình cứng. Việc "dừng lại hỏi khi có điểm mờ" giữa 2 bước cũng vậy: không có cơ chế pause riêng của Claude Code, mà là Claude tự áp dụng đúng yêu cầu đã viết trong Command.

Từ sơ đồ trên, có thể thấy vai trò của từng thành phần:

<table class="rt-table">
<thead>
<tr>
<th>Thành phần</th>
<th>Vai trò</th>
<th>Trong ví dụ trên</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>RULE</strong></td>
<td>Quy tắc/bối cảnh cố định, <strong>luôn được nạp</strong> dù có ai gọi tới hay không.</td>
<td>Quy tắc <code>TC_&lt;MODULE&gt;_&lt;số&gt;</code> trong <code>CLAUDE.md</code>.</td>
</tr>
<tr>
<td><strong>SKILL</strong></td>
<td>Một năng lực cụ thể, <strong>chỉ nạp khi được gọi</strong> (tự động hoặc gõ tay), có thể được một Skill/Command khác gọi tới.</td>
<td><code>skills-requirements-analyzer</code> và <code>skills-testcases-generate</code>.</td>
</tr>
<tr>
<td><strong>COMMAND</strong></td>
<td>Lệnh gọi tắt, cơ chế trùng với Skill. Có thể chỉ chứa một đoạn prompt đơn giản (như <code>/report-bug</code>), hoặc đóng vai trò "chất kết dính" gọi nối tiếp nhiều Skill theo thứ tự cố định.</td>
<td><code>/generate_testcases_from_requirements</code> gọi lần lượt 2 Skill ở trên.</td>
</tr>
</tbody>
</table>

Vài nguyên tắc rút ra khi tổ chức RULE/SKILL/COMMAND cho một dự án thật:

- Quy tắc nào **áp dụng cho mọi tác vụ, không phân biệt Skill nào đang chạy** (chuẩn đặt tên, format Test Case...) → đưa vào RULE.
- Năng lực nào **đứng độc lập, có thể tái dùng ở nhiều ngữ cảnh khác nhau** (phân tích yêu cầu, sinh Test Case, review code...) → tách thành SKILL riêng, đừng gộp hết vào một Skill khổng lồ.
- Trình tự nào **cố định, lặp lại nhiều lần** (luôn phân tích trước rồi mới sinh Test Case) → gói vào một COMMAND gọi nối tiếp các Skill, thay vì bắt người dùng nhớ gọi đúng thứ tự bằng tay mỗi lần.

## 6. So sánh nhanh Skill trên Claude và Codex

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Claude Code</th>
<th>Codex</th>
</tr>
</thead>
<tbody>
<tr>
<td>File RULE</td>
<td><code>CLAUDE.md</code></td>
<td><code>AGENTS.md</code></td>
</tr>
<tr>
<td>Rule dạng module, nạp theo path</td>
<td><code>.claude/rules/*.md</code> (khai báo <code>paths</code> để nạp có điều kiện, mục 2.3)</td>
<td>Chưa có — chỉ có <code>AGENTS.md</code> ở project + Codex Home</td>
</tr>
<tr>
<td>Skill cá nhân</td>
<td><code>~/.claude/skills/&lt;ten&gt;/SKILL.md</code></td>
<td><code>~/.agents/skills/&lt;ten&gt;/SKILL.md</code></td>
</tr>
<tr>
<td>Skill theo dự án</td>
<td><code>.claude/skills/&lt;ten&gt;/SKILL.md</code></td>
<td><code>.agents/skills/&lt;ten&gt;/SKILL.md</code></td>
</tr>
<tr>
<td>Cách gọi</td>
<td><code>/ten-skill</code>, hoặc để Claude tự nhận diện</td>
<td><code>/ten-skill</code>, hoặc để Codex tự nhận diện</td>
</tr>
<tr>
<td>Command tuỳ chỉnh riêng biệt</td>
<td>Có (<code>.claude/commands/</code>), nhưng đã gộp chung cơ chế với Skill</td>
<td>Custom Prompts đã deprecated, dùng Skill thay thế</td>
</tr>
<tr>
<td>Gọi nhiều Skill theo trình tự</td>
<td>COMMAND gọi nối tiếp nhiều Skill (mục 3.6)</td>
<td>Không có Command; gộp vào 1 Skill tự chỉ dẫn gọi Skill khác (mục 4.3)</td>
</tr>
</tbody>
</table>

## 7. Bài tập thực hành

**Bài tập 1** — Tạo Skill `skills-testcases-generate` theo hướng dẫn ở mục 3.4 (hoặc 4.3 nếu bạn dùng Codex), thử gọi với ít nhất 2 chức năng khác nhau (ví dụ: Đăng nhập, Quên mật khẩu).

**Bài tập 2** — Tạo thêm một Skill thứ hai tên `review-testcase`: nhận vào một file Test Case, trả về danh sách các case còn thiếu (đặc biệt case biên, case bảo mật) và các case bị trùng/mô tả chưa rõ ràng. Gợi ý: có thể tham khảo cấu trúc prompt review đã dùng ở bài trước.

**Bài tập 3** — Thử đặt `disable-model-invocation: true` cho một trong hai Skill trên, quan sát sự khác biệt: hỏi AI bằng lời tự nhiên xem AI có tự gọi skill đó không, so với khi gọi tay bằng `/`.

> **Cơ chế thật đằng sau flag này** (theo [tài liệu chính thức Claude Code](https://code.claude.com/docs/en/skills)): khi đặt `disable-model-invocation: true`, `description` của Skill bị **loại khỏi ngữ cảnh hoàn toàn** — Claude thậm chí không "biết" Skill này tồn tại để cân nhắc gọi, chứ không đơn thuần là "Claude tự nguyện không gọi". Nếu Claude vẫn cố gọi qua đường khác, Claude Code sẽ **chặn cứng** lệnh gọi đó ở tầng hệ thống. Đây là điểm khác với cơ chế "mềm" đã nói ở mục 5 (dòng "Dùng Skill X" trong nội dung Command chỉ là hướng dẫn ngôn ngữ tự nhiên, không được đảm bảo) — `disable-model-invocation` là một cơ chế enforce thật, không phải lời dặn.

## 8. Tổng kết

- **RULE** (`CLAUDE.md`/`AGENTS.md`) dùng cho quy tắc/bối cảnh cố định, luôn được nạp — nên giữ ngắn gọn.
- **SKILL** dùng cho quy trình nhiều bước, hay lặp lại — chỉ nạp khi cần, gọi bằng `/ten-skill` hoặc để AI tự nhận diện qua `description`. Một Skill có thể dùng lại kết quả của Skill khác trong cùng phiên chat (mục 3.4).
- Trên Claude Code, **Command đã gộp chung cơ chế với Skill** và có thể gọi nối tiếp nhiều Skill theo thứ tự cố định; trên Codex, **Custom Prompts đã deprecated**, không có Command riêng nên việc điều phối nhiều Skill được gộp vào chính một Skill — xem mapping cụ thể ở mục 5.
- Vị trí lưu quyết định phạm vi áp dụng: cá nhân (mọi dự án) hay theo dự án (chia sẻ qua Git cho cả team).
- Bài kế tiếp sẽ giới thiệu **bộ Skill dựng sẵn cho Manual Testing do Anh Tester xây dựng** — dựa đúng trên cơ chế bạn vừa học ở bài này.