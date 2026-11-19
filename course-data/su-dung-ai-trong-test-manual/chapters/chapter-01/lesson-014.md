# Bài 14 - Tạo Checklist Test tạo Report Truy Vết tạo Summary Report tổng thể

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/366](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/366)

✅ Tạo Checklist Test (preview nhanh, customer tuỳ biến status test)  
✅ Tạo Report Truy Vết (Requirement <-> Test Cases <-> Bugs)  
✅ Tạo Summary Report tổng thể (gửi sang Slack, Teams, Telegram,...)

## 1. Ba câu hỏi người khác sẽ hỏi bạn

Ở bài trước bạn đã dựng bộ nhớ `memories/` để AI không quên những sự thật riêng của dự án. Tính tới đây, bạn đã có đủ mọi mảnh ghép của một đợt kiểm thử: Requirements có mã truy vết, Master Test Plan, bộ Test Case đã review, lượt chạy kèm evidence, bug report, vòng delta khi requirement đổi.

Nhưng để ý: toàn bộ chỗ tài liệu đó là viết **cho bạn** đọc. Đến cuối mỗi đợt, sẽ có ba người khác gõ cửa với ba câu hỏi rất ngắn:

<table class="rt-table">
<thead>
<tr>
<th>Ai hỏi</th>
<th>Câu hỏi</th>
<th>Tài liệu trả lời</th>
<th>Lệnh của bộ kit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dev vừa đẩy build mới, tester được nhờ rà giúp</td>
<td><strong>"Rà nhanh bản này thế nào cho đủ?"</strong></td>
<td><strong>Checklist Test</strong> — danh sách tick tay</td>
<td><code>/generate-checklist-test</code></td>
</tr>
<tr>
<td>QA Lead, người nghiệm thu, auditor</td>
<td><strong>"Đã test đủ chưa? Lấy gì chứng minh?"</strong></td>
<td><strong>Ma trận truy vết (RTM)</strong></td>
<td><code>/generate-traceability-matrix</code></td>
</tr>
<tr>
<td>PM, PO, khách hàng</td>
<td><strong>"Release được không?"</strong></td>
<td><strong>Báo cáo tổng hợp</strong> (Test Summary Report)</td>
<td><code>/generate-test-summary-report</code></td>
</tr>
</tbody>
</table>

Ba câu hỏi nghe đơn giản, nhưng trả lời sai thì hậu quả không nhỏ: checklist mơ hồ thì người tick tay tick bừa; RTM tính sai mẫu số thì báo "phủ 100%" trong khi cả module chưa ai chạm tới; báo cáo tổng hợp thiếu căn cứ thì release xong có sự cố, không ai biết QA đã cảnh báo hay chưa.

Trong toàn cảnh 8 chặng của bộ kit, ba lệnh này nằm ở ba chỗ khác nhau:

```none
Chặng 2   /generate-testcases-manual-rbt   → TC chi tiết có steps
   2'     /generate-checklist-test         → checklist tick tay (mode CHECKLIST)
   ...
Chặng 4–5 chạy tay · bug · retest           ← bài Review → Execute → Log Bug, bài Update → Retest
          /execute-test-cases chạy được cả bộ TC lẫn checklist
Chặng 6   /generate-traceability-matrix    → RTM — chứng minh độ phủ
Chặng 7   /generate-test-summary-report    → báo cáo tổng hợp + khuyến nghị GO / NO-GO
```

> 📌 Nguồn gốc của bài: [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md) chặng 6 và chặng 7, cùng ba file lệnh trong [.claude/commands](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/commands). Mọi ví dụ trong bài dựng trên tài liệu **có thật** của CRM demo trong bộ kit (`docs/`), không dùng số liệu tưởng tượng.
>
> 💡 Trên **Codex**, cả ba đều là skill cùng tên, gọi bằng dấu `$`: `$generate-checklist-test`, `$generate-traceability-matrix`, `$generate-test-summary-report` — repo [codex-testing-skills](https://github.com/anhtester/codex-testing-skills).

## 2. Checklist Test — lớp rà nhanh nằm trên bộ Test Case

### 2.1. Checklist khác Test Case ở đâu

Lỗi phổ biến nhất là coi checklist như "Test Case viết tắt". Lệnh của kit tách bạch hai thứ bằng đúng một câu: **checklist trả lời "đã rà hết chưa?", Test Case trả lời "rà bằng cách nào?"**.

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Test Case</th>
<th>Checklist</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Hình dạng</strong></td>
<td>Pre-Condition · Test Steps đánh số · Test Data · Expected Result</td>
<td>Mỗi mục <strong>1 dòng, ≤ 20 từ</strong>, mở đầu bằng động từ, kèm kết quả kỳ vọng quan sát được</td>
</tr>
<tr>
<td><strong>Ai chạy</strong></td>
<td>Tester đã đọc Requirements, hoặc giao cho automation</td>
<td>Bất kỳ ai — kể cả người <strong>chưa đọc</strong> Requirements, mỗi mục verify trong ≤ 2 phút</td>
</tr>
<tr>
<td><strong>Sống bao lâu</strong></td>
<td>Tài liệu sống — sửa tại chỗ khi requirement đổi</td>
<td><strong>Ảnh chụp tại một thời điểm</strong> — lần rà mới sinh file mới, không sửa đè</td>
</tr>
<tr>
<td><strong>Dùng khi</strong></td>
<td>Lưu trữ, import Jira/TestRail, chạy regression đầy đủ</td>
<td>Smoke build mới, rà sau hotfix, rà trước release</td>
</tr>
<tr>
<td><strong>Xem bằng</strong></td>
<td><code>scripts/testcases-viewer</code></td>
<td>Trình xem Markdown bất kỳ, hoặc <strong>in ra giấy tick tay</strong> — <strong>không</strong> nạp vào testcases-viewer</td>
</tr>
<tr>
<td><strong>Kết quả chạy nằm ở</strong></td>
<td>Execution report của <code>/execute-test-cases</code></td>
<td><strong>Cũng là execution report</strong> nếu chạy bằng <code>/execute-test-cases</code> — file checklist giữ nguyên, không tick vào. Tick trên giấy thì kết quả dừng ở tờ giấy đó</td>
</tr>
</tbody>
</table>

> ⚠️ **Checklist không thay bộ Test Case.** Nó là lớp rà nhanh nằm *trên* bộ TC. Đội nào bỏ bộ TC chỉ giữ checklist thì đến lúc cần chứng minh "đã test REQ này bằng cách nào", không còn gì để đưa ra.

### 2.2. Bốn loại checklist và ngưỡng quy mô

Kit chia checklist thành bốn loại, mỗi loại có **trần số mục và trần thời gian** — đây là điểm khiến checklist của kit khác hẳn kiểu "liệt kê càng nhiều càng tốt":

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Mục đích</th>
<th>Số mục</th>
<th>Chạy tay</th>
<th>Lấy mục từ vòng nào</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Smoke</strong></td>
<td>Build chạy được, luồng sống còn không vỡ</td>
<td>10–20</td>
<td>≤ 15 phút</td>
<td>Chỉ Vòng 1</td>
</tr>
<tr>
<td><strong>Post-hotfix</strong></td>
<td>Vùng ảnh hưởng của bản vá + vùng lân cận</td>
<td>5–15</td>
<td>≤ 10 phút</td>
<td>Vòng 1 của vùng vá + nhánh Vòng 2 bản vá chạm tới</td>
</tr>
<tr>
<td><strong>Regression (module)</strong></td>
<td>Rà trọn một module trước khi bàn giao</td>
<td>20–40</td>
<td>≤ 45 phút</td>
<td>Vòng 1 + 2 + Vòng 3 <code>Permission</code></td>
</tr>
<tr>
<td><strong>Release-readiness</strong></td>
<td>Rà toàn hệ thống trước khi lên production</td>
<td>30–60</td>
<td>≤ 60 phút</td>
<td>Vòng 1 + nhánh sống còn Vòng 2 + Vòng 3 <code>Permission</code>/<code>Security</code> + Vòng 4 <code>E2E</code></td>
</tr>
</tbody>
</table>

"Vòng" ở đây chính là **Bản Đồ Loại Kiểm Thử 4 Vòng** bạn đã gặp ở bài sinh Test Case. Checklist không chấm bảng 4 vòng, nhưng dùng nó để biết *dừng ở đâu*: smoke mà kéo cả kiểm thử biên và bảo mật vào thì không còn là smoke nữa.

> 💡 Vượt ngưỡng thì kit **bắt buộc** tách theo module hoặc hạ scope, và ghi rõ phần đã cắt. Checklist 80 mục không ai tick hết trong một buổi — người tick sẽ lướt, và lướt thì checklist mất tác dụng.

### 2.3. Hai nguồn đầu vào — vì sao ưu tiên TC-based

<table class="rt-table">
<thead>
<tr>
<th>Nguồn</th>
<th>Khi nào</th>
<th>Cách AI làm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>TC-based</strong> (ưu tiên)</td>
<td>Module đã có bộ Test Case</td>
<td><strong>Rút gọn</strong> từ bộ TC — gom TC cùng chủ đề thành một mục, điền cột <code>TC ID liên quan</code> để truy ngược. Bỏ qua TC <code>@Deprecated</code></td>
</tr>
<tr>
<td><strong>REQ-based</strong></td>
<td>Chưa có TC, mới có Requirements hoặc UI</td>
<td>Rút mục thẳng từ Requirements + ba bảng checklist chuẩn trong skill (Field-Level · Component-Level · Non-Functional)</td>
</tr>
</tbody>
</table>

Vì sao đã có TC thì phải đi đường TC-based? Vì sinh mới từ đầu thì checklist **lệch** với bộ TC gốc: cùng một chức năng, checklist ghi kỳ vọng một kiểu, Test Case ghi kiểu khác, và người tick không biết tin bên nào. Rút từ bộ TC thì mọi mục đều đã đi qua review và đối chiếu evidence — checklist thừa hưởng toàn bộ chất lượng đó.

## 3. Thực hành: checklist Smoke module Đăng nhập

Tình huống thật trong Master Test Plan Release 1.0 của CRM demo: tiêu chí vào số 10 yêu cầu *"Smoke `LOGIN` chạy PASS trên môi trường mới"* trước khi bắt đầu thực thi. Người chạy smoke có thể không phải bạn — một checklist tick tay là đúng thứ cần giao.

### 3.1. Prompt

Dựa trên mẫu [prompt\_15\_generate\_checklist.txt](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/prompt_15_generate_checklist.txt):

```none
/generate-checklist-test

# CONTEXT
- Module/Tính năng cần rà: Đăng nhập (LOGIN)
- Loại checklist: Smoke
- Môi trường: môi trường test riêng của Release 1.0 — build v1.0.0

# NGUỒN INPUT
## Cách 1: TC-based
- File TC: docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md

# TÙY CHỌN
- Role cần rà: Admin
- Trọng tâm: xác nhận requirements khảo sát trên bản demo vẫn đúng trên môi trường mới
```

Ba chỗ đáng chú ý trong prompt:

- **Trỏ vào file index** `TEST_CASES_LOGIN_SUMMARY.md`, không trỏ thẳng file nền tảng — AI đọc mục `Bản đồ tài liệu` rồi tự đi tới `web/test_cases_login_web.md`. Index không chứa dòng TC nào; nó là bản đồ.
- **Ghi rõ loại checklist.** Không ghi thì lệnh sẽ hỏi lại, hoặc tự suy rồi ghi loại đã chọn ở đầu file — bạn phải đọc lại để chắc nó không chọn nhầm Regression.
- **Ghi build.** Checklist không gắn build thì bảng ký nhận ở cuối không có nghĩa.

### 3.2. Kết quả và cách đọc

Module Đăng nhập có sẵn bộ chạy `@Smoke` gồm 9 TC (~12 phút) trong file index. AI rút từ đó, mỗi TC thành một mục. Đầu file có ba dòng nhận diện:

```none
## Đăng nhập — Checklist Smoke (10 mục · ~12 phút)

**Nguồn:** TC-based (docs/testcases/login/web/test_cases_login_web.md)
**Scope:** LOGIN · web · role Admin
**Mã checklist:** CL-smoke_20261009
```

Dòng **Mã checklist** nhỏ nhưng quan trọng nhất — mục 3.4 sẽ giải thích vì sao. Còn đây là một phần bảng mục:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>✅</th>
<th>Hạng mục kiểm tra</th>
<th>Kết quả kỳ vọng</th>
<th>Priority</th>
<th>REQ ID</th>
<th>TC ID liên quan</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>☐</td>
<td>Mở <code>/admin/authentication</code> khi chưa đăng nhập</td>
<td>Dừng đúng URL đó, thấy biểu mẫu đăng nhập, không trang lỗi</td>
<td>P1</td>
<td>REQ-LOGIN-01</td>
<td>CRM_LOGIN_TC_001</td>
</tr>
<tr>
<td>2</td>
<td>☐</td>
<td>Đăng nhập Admin hợp lệ, mật khẩu lấy từ <code>.env</code></td>
<td>Vào <code>/admin/</code>, tab có chữ <code>Dashboard</code>, thấy menu trái</td>
<td>P1</td>
<td>REQ-LOGIN-06</td>
<td>CRM_LOGIN_TC_005</td>
</tr>
<tr>
<td>3</td>
<td>☐</td>
<td>Bấm <code>Login</code> khi để trống cả hai ô</td>
<td>Đúng 2 dải đỏ: <code>The Password field is required.</code> rồi <code>The Email Address field is required.</code></td>
<td>P1</td>
<td>REQ-LOGIN-10</td>
<td>CRM_LOGIN_TC_011-a</td>
</tr>
<tr>
<td>4</td>
<td>☐</td>
<td>Gõ thẳng <code>/admin/clients</code> khi chưa đăng nhập</td>
<td>Bị đưa về <code>/admin/authentication</code>, không thấy dữ liệu khách hàng</td>
<td>P1</td>
<td>REQ-LOGIN-17</td>
<td>CRM_LOGIN_TC_021-a</td>
</tr>
<tr>
<td>5</td>
<td>☐</td>
<td>Đăng xuất rồi bấm Back của trình duyệt</td>
<td>Không hiện lại dữ liệu cũ, bị đưa về <code>/admin/authentication</code></td>
<td>P1</td>
<td>REQ-LOGIN-32, 33</td>
<td>CRM_LOGIN_TC_036-a</td>
</tr>
</tbody>
</table>

Đọc kỹ cột `TC ID liên quan`: mục 3 ghi `TC_011-a` chứ không ghi `TC_011`. Bộ TC Đăng nhập viết ở độ hạt GỘP — `TC_011` có 4 biến thể, smoke chỉ lấy biến thể `a`. Ghi thiếu hậu tố thì khi mục này FAIL, không ai biết case nào hỏng.

Cuối file luôn có hai phần mà người mới hay bỏ qua:

```none
### Không áp dụng cho module này
- Data Table/List · CRUD Lifecycle · Status Flow — màn đăng nhập không có bảng dữ liệu,
  không tạo/sửa/xoá bản ghi, không có luồng trạng thái
- Modal/Dialog — chỉ xuất hiện khi còn bộ đếm giờ đang chạy (TC_034), ngoài phạm vi smoke

### Ký nhận
| Môi trường | Build / Version | Người thực hiện | Ngày | Kết quả (Pass/Fail/Blocked) |
|---|---|---|---|---|
|  |  |  |  |  |
```

Phần **Không áp dụng** trả lời câu hỏi mà người duyệt chắc chắn sẽ hỏi: "sao không thấy mục phân trang?". Không ghi ra thì không phân biệt được *cố ý bỏ* với *quên*. Phần **Ký nhận** biến checklist thành bằng chứng: ai chạy, trên build nào, ngày nào — đây chính là thứ bạn đưa ra để chứng minh tiêu chí vào số 10 đã đạt.

File được ghi theo quy ước đường dẫn của kit, AI chỉ báo số mục và đường dẫn trong chat (Write-first), không in cả bảng ra:

```none
docs/checklists/login/web/checklist_smoke_20261009.md
```

### 3.3. Cổng chất lượng 5 tiêu chí — và lần nó bắt lỗi thật

Trước khi ghi file, lệnh phải tự chạy **Checklist Quality Gate**:

<table class="rt-table">
<thead>
<tr>
<th>Tiêu chí</th>
<th>Kiểm gì</th>
<th>Với checklist Smoke Đăng nhập</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Verify được</strong></td>
<td>100% mục có kết quả quan sát được, không còn "hoạt động đúng / bình thường / OK"</td>
<td>✅ Mọi kỳ vọng là URL, nội dung dải báo lỗi, số dải, chữ trên tab</td>
</tr>
<tr>
<td><strong>2. Critical path đủ</strong></td>
<td>Đăng nhập, CRUD bản ghi chính, phân quyền… đều có ≥ 1 mục P1</td>
<td>✅ Đăng nhập · chặn URL nội bộ · đăng xuất đều có P1</td>
</tr>
<tr>
<td><strong>3. Component đủ</strong></td>
<td>Component có mặt thì có mục; không có thì ghi vào "Không áp dụng"</td>
<td>✅ Có phần Không áp dụng</td>
</tr>
<tr>
<td><strong>4. Đúng quy mô</strong></td>
<td>Số mục nằm trong ngưỡng của loại đã chọn</td>
<td>❌ <strong>9 mục</strong> — Smoke cần <strong>10–20</strong></td>
</tr>
<tr>
<td><strong>5. Truy vết được</strong></td>
<td>Header có <code>Mã checklist</code> khớp tên file · mục có REQ thì điền <code>REQ ID</code> · TC-based thì điền <code>TC ID liên quan</code> · Release-readiness có cột <code>Module</code> ở mọi mục</td>
<td>✅ <code>CL-smoke_20261009</code> khớp <code>checklist_smoke_20261009.md</code>, mọi mục có cả REQ ID lẫn TC ID</td>
</tr>
</tbody>
</table>

Tiêu chí 4 trượt ngay ở ví dụ thật: bộ `@Smoke` của module có đúng 9 TC, rút một-đổi-một ra 9 mục. Lệnh không được xuất file khi cổng chưa đạt, nên AI phải bổ sung một mục Vòng 1 có sẵn TC — ví dụ `TC_027`, nằm ở nhánh *Vòng 1 · Open form* trong bảng 4 vòng của module:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>✅</th>
<th>Hạng mục kiểm tra</th>
<th>Kết quả kỳ vọng</th>
<th>Priority</th>
<th>REQ ID</th>
<th>TC ID liên quan</th>
</tr>
</thead>
<tbody>
<tr>
<td>10</td>
<td>☐</td>
<td>Bấm liên kết <code>Forgot Password?</code></td>
<td>Dừng ở <code>/admin/authentication/forgot_password</code>, có ô <code>Email Address</code> và nút <code>Confirm</code></td>
<td>P2</td>
<td>REQ-LOGIN-23</td>
<td>CRM_LOGIN_TC_027</td>
</tr>
</tbody>
</table>

> 💡 **Bài học từ chỗ này:** đừng nghĩ cổng chất lượng chỉ để chặn checklist quá dài. Nó chặn cả hai chiều. Và khi đọc kết quả, hãy kiểm xem mục được thêm vào có **TC ID thật** không — mục bổ sung mà cột `TC ID liên quan` ghi `—` trong khi bộ TC có sẵn case tương ứng nghĩa là AI đã tự nghĩ ra thay vì rút từ bộ TC.

### 3.4. Chạy checklist — từ ô tick tới execution report

Checklist in ra tick tay vẫn dùng được. Nhưng kết quả trên giấy **dừng lại ở tờ giấy**: RTM không đọc được, báo cáo tổng hợp không đọc được, bug sinh ra không trỏ về đâu. Muốn kết quả đi tiếp xuống các chặng sau, bạn chạy checklist bằng chính lệnh chạy Test Case:

```none
/execute-test-cases

- File TC hoặc checklist: docs/checklists/login/web/checklist_smoke_20261009.md
- Phạm vi chạy: toàn bộ file
- Môi trường dùng chung: Không — môi trường test riêng Release 1.0, build v1.0.0
```

Lệnh coi mỗi mục là một đơn vị chạy và ghi kết quả vào `execution_report.md` như một lượt chạy bình thường — **không** tick vào file checklist. Bảng Ký nhận ở cuối checklist vẫn do người chịu trách nhiệm tự điền.

Chỗ khác biệt nằm ở **mã**. Cột `#` trong checklist chỉ là số thứ tự trong một file — mục `#3` của checklist smoke và mục `#3` của checklist regression là hai việc khác nhau. Vì vậy khi kết quả ra khỏi file checklist, mỗi mục mang mã riêng:

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Quy tắc</th>
<th>Ví dụ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Mã checklist</strong></td>
<td><code>CL-</code> + phần tên file <strong>sau</strong> <code>checklist_</code>, bỏ <code>.md</code></td>
<td><code>checklist_smoke_20261009.md</code> → <code>CL-smoke_20261009</code></td>
</tr>
<tr>
<td><strong>Mã mục</strong></td>
<td><code>&lt;Mã checklist&gt;-&lt;số mục 2 chữ số&gt;</code> — lệnh tự ghép khi ghi report, không ghi vào bảng checklist</td>
<td>mục 3 → <code>CL-smoke_20261009-03</code></td>
</tr>
</tbody>
</table>

Bốn luật lệnh `/execute-test-cases` tuân theo khi chạy checklist — đọc report AI trả về, bạn kiểm đúng bốn điều này:

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Sai thì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cột <code>TC ID</code> của report ghi <strong>mã mục</strong> <code>CL-smoke_20261009-03</code>, cấm ghi <code>#3</code> trần</td>
<td><code>#3</code> trùng giữa mọi checklist — viewer, RTM và báo cáo tổng hợp nối nhầm mục của hai checklist khác nhau mà không ai biết</td>
</tr>
<tr>
<td>Header report có ô <strong><code>Loại nguồn</code></strong> = <code>Checklist smoke · CL-smoke_20261009</code>; bảng kết quả chép thêm <code>Priority</code> · <code>REQ ID</code> · <code>TC ID liên quan</code></td>
<td>Thiếu ô này, lượt chạy 10 mục smoke bị coi là lượt chạy bộ TC và <strong>thay số</strong> của cả module 51 TC</td>
</tr>
<tr>
<td>Checklist Release-readiness chạy ra <code>docs/executions/_release/&lt;nền-tảng&gt;/</code>, bảng kết quả có cột <code>Module</code></td>
<td>Một lượt chạy trải nhiều module — không có cột <code>Module</code> thì không biết mục FAIL thuộc module nào</td>
</tr>
<tr>
<td>Mục FAIL → bug đặt ở <code>docs/bugs/&lt;module của mục&gt;/&lt;nền-tảng&gt;/</code>, trỏ về <code>TC ID liên quan</code> <strong>và</strong> mã mục</td>
<td>Mục REQ-based không có TC thì mã mục + REQ ID là neo duy nhất — mất nó là bug mồ côi</td>
</tr>
</tbody>
</table>

> 📌 Tên file bug từ mục checklist vẫn theo quy ước `BUG_<module>_<timestamp>_<hậu tố>`: hậu tố là `TC ID liên quan` rút gọn (mục 2 của checklist trên FAIL → hậu tố `TC005`). Mục REQ-based không có TC thì hậu tố là `CL` + số mục, ví dụ `CL03`.

### 3.5. Checklist sau hotfix

Module Đăng nhập đang có một bug Critical mở: `BUG_login_1785678750_TC039` — trang đăng nhập phục vụ được qua HTTP thuần, không ép sang HTTPS. Giả sử Dev báo đã vá cấu hình máy chủ và cần bạn rà gấp vùng lân cận. Loại checklist là **Post-hotfix**, và prompt **bắt buộc** có phần vùng ảnh hưởng:

```none
/generate-checklist-test

# CONTEXT
- Module/Tính năng cần rà: Đăng nhập (LOGIN)
- Loại checklist: Post-hotfix
- Môi trường: môi trường test riêng — build v1.0.1

# NGUỒN INPUT
## Cách 1: TC-based
- File TC: docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md

# VÙNG ẢNH HƯỞNG
Bản vá cấu hình máy chủ cho BUG_login_1785678750_TC039: mọi request http:// chuyển hướng
vĩnh viễn sang https:// và trả header HSTS. Ticket: <TICKET-ID>.
Không sửa mã nguồn biểu mẫu đăng nhập.
```

File ra sẽ mang mã ticket thay vì ngày: `docs/checklists/login/web/checklist_post-hotfix_<TICKET-ID>.md`, mã checklist là `CL-post-hotfix_<TICKET-ID>` — hai hotfix cùng ngày không đè nhau. Bản vá đổi hành vi ở tầng giao thức, nên vùng lân cận AI cần khoanh là những chỗ đi qua chuyển hướng: đăng nhập thành công, đăng xuất, trang Quên mật khẩu, chặn URL nội bộ khi chưa đăng nhập.

> ⚠️ **Checklist post-hotfix không thay `/retest-fixed-bugs`.** Bug đã có mã trong `docs/bugs/` thì việc chấm FIXED/NOT\_FIXED và ghi Lịch sử retest vẫn là của lệnh retest bạn đã học ở bài Update → Retest — bug Critical còn phải chạy mode FULL kèm regression. Checklist là để *người khác* tick tay vùng lân cận trong 10 phút khi bản vá đi gấp.
>
> 📌 Riêng `TC_039` có một bẫy đã ghi trong bộ TC: Chrome tự nâng `http://` lên `https://`, nên nhìn thanh địa chỉ có thể PASS giả. Mục checklist cho bug này phải giữ nguyên điều kiện "tắt HTTPS-Upgrades của Chrome" từ TC gốc — rút gọn mà làm mất điều kiện đó là checklist nói dối.

### 3.6. Năm lỗi khi dùng checklist

<table class="rt-table">
<thead>
<tr>
<th>Lỗi</th>
<th>Hậu quả</th>
<th>Làm đúng</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Để AI tự tick ô ☐</strong></td>
<td>Checklist trông như đã chạy xong trong khi chưa ai mở trình duyệt</td>
<td>Kit cấm agent tự tick. Người chạy tay thì tự tick và ký; agent chạy thì kết quả vào execution report, file checklist giữ nguyên</td>
</tr>
<tr>
<td><strong>Ghi <code>#3</code> thay cho mã mục, bỏ trống <code>Loại nguồn</code></strong></td>
<td>Kết quả checklist bị nối nhầm sang checklist khác, hoặc bị cộng lẫn vào số của bộ TC</td>
<td>Kiểm cột <code>TC ID</code> của report là <code>CL-…-&lt;nn&gt;</code> và header có <code>Loại nguồn</code></td>
</tr>
<tr>
<td><strong>Sửa đè checklist của lần rà trước</strong></td>
<td>Mất bằng chứng của build cũ — có thể đã có người tick và ký</td>
<td>Lần rà mới → file mới theo ngày / ticket / mốc. Chỉ ghi đè khi cùng ngày, cùng loại</td>
</tr>
<tr>
<td><strong>Nạp checklist vào testcases-viewer</strong></td>
<td>Ra bảng rỗng — checklist cố tình không có cột <code>Test Steps</code>, <code>Test Data</code></td>
<td>Mở bằng trình xem Markdown bất kỳ, hoặc in ra</td>
</tr>
<tr>
<td><strong>Đòi checklist có steps chi tiết</strong></td>
<td>Thành Test Case dở dang: không đủ để lưu trữ, quá dài để tick nhanh</td>
<td>Cần steps → quay lại <code>/generate-testcases-from-requirements</code> hoặc <code>/generate-testcases-manual-rbt</code></td>
</tr>
</tbody>
</table>

## 4. Truy vết — sợi chỉ nối Requirement tới bug

### 4.1. Chuỗi bốn mắt xích

Danh mục bug của kit mở đầu bằng một câu đáng chép lại: bug là **mắt xích thứ tư** của chuỗi truy vết.

```none
requirements  →  testcases  →  executions  →  bugs
 REQ-LOGIN-44    CRM_LOGIN_TC_039   run_1787215085   BUG_login_1785678750_TC039
                 (cột REQ ID)       (TC FAIL)        (trỏ về TC ID + REQ ID)
```

Mắt xích giữ cả chuỗi là `REQ ID`. Bài phân tích Requirements sinh ra nó, bài sinh Test Case ghi nó vào cột `REQ ID` của từng TC, và chặng 6 dùng nó để tính độ phủ. Đứt ở đâu thì từ chỗ đó trở đi không chứng minh được "đã test đủ".

### 4.2. Câu chuyện TC\_039: khi truy vết nhầm còn tệ hơn không truy vết

Ví dụ ở trên không phải sơ đồ minh hoạ — nó là lịch sử thật của bộ kit:

1. Bug Critical về HTTPS được mở từ 02-08-2026. Sau lần rà lại ngày 20-08-2026, nó trỏ vào `CRM_LOGIN_TC_039`, và TC đó trỏ vào `REQ-LOGIN-01` — "Truy cập trang đăng nhập".
2. Nhưng `REQ-LOGIN-01` **không nói gì về HTTPS**. Tài liệu chỉ ghi "toàn bộ qua HTTPS" ở mục môi trường, không REQ nào ràng buộc việc ép chuyển hướng.
3. Hệ quả: một bug Critical đứng trên một requirement không đòi hỏi điều nó tố cáo. Dev hoàn toàn có thể trả lời "không phải lỗi, requirement đâu có yêu cầu".
4. Câu hỏi được đẩy lên PO thành `AMB-LOGIN-20`. Ngày 19-09-2026 PO chốt: bắt buộc ép HTTPS kèm HSTS → sinh `REQ-LOGIN-44`, TC\_039 chuyển sang trỏ vào REQ mới.

> 📌 Danh mục bug của kit ghi thẳng: bug phải trỏ về TC ID và REQ ID **đang có hiệu lực** — trỏ vào mã đã đổi nghĩa còn tệ hơn không trỏ. Không trỏ thì ai cũng biết là thiếu; trỏ sai thì mọi người tin nó đúng.

### 4.3. Đã có Bảng Đối Soát Coverage — vì sao vẫn cần RTM

Nếu bạn mở `TEST_CASES_LOGIN_SUMMARY.md`, bạn sẽ thấy một bảng **Đối Soát Coverage** kết luận "40/40 REQ trong phạm vi có ≥ 1 TC". Câu hỏi tự nhiên: vậy còn cần RTM làm gì?

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Bảng Đối Soát Coverage trong file TC</th>
<th>RTM</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Phạm vi</strong></td>
<td>Một module</td>
<td><strong>Toàn hệ thống</strong> — mọi module, mọi nền tảng</td>
</tr>
<tr>
<td><strong>Lập lúc nào</strong></td>
<td>Lúc sinh / sửa bộ TC</td>
<td>Trước release, và chạy lại sau mỗi đợt delta</td>
</tr>
<tr>
<td><strong>Thấy module chưa khảo sát?</strong></td>
<td>Không — nó chỉ biết module của mình</td>
<td><strong>Có</strong> — mục ⬛ đọc từ <code>docs/requirements/README.md</code></td>
</tr>
<tr>
<td><strong>Tầng automation</strong></td>
<td>Không</td>
<td>Có — quét script thật nếu bạn đưa thư mục test</td>
</tr>
<tr>
<td><strong>Test mồ côi</strong></td>
<td>Không tìm</td>
<td>Có — TC/script không map về REQ nào</td>
</tr>
</tbody>
</table>

Nói ngắn: bảng trong file TC là *lời tự khai* của một module lúc nó được viết. RTM là *kiểm toán* cắt ngang toàn hệ thống tại một thời điểm.

## 5. Ma trận truy vết với `/generate-traceability-matrix`

### 5.1. Năm chỉ số, năm ký hiệu

<table class="rt-table">
<thead>
<tr>
<th>Chỉ số</th>
<th>Công thức</th>
<th>Trả lời câu hỏi</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Requirement Coverage</strong></td>
<td>REQ có ≥ 1 TC / tổng REQ</td>
<td>Requirement nào chưa được test</td>
</tr>
<tr>
<td><strong>Platform Coverage</strong></td>
<td>Cặp (REQ × nền tảng REQ khai) có TC trên đúng nền tảng đó / tổng cặp</td>
<td>REQ khai Web · Android mà chỉ có TC web thì Android <strong>chưa phủ</strong></td>
</tr>
<tr>
<td><strong>Automation Coverage</strong></td>
<td>TC có ≥ 1 script / tổng TC</td>
<td>TC nào còn chạy tay</td>
</tr>
<tr>
<td><strong>REQ chỉ có checklist</strong></td>
<td>Số REQ có mục checklist nhưng 0 TC</td>
<td>Vùng đã rà nhanh nhưng chưa có TC để chạy lại, chưa automate được</td>
</tr>
<tr>
<td><strong>Orphan Tests</strong></td>
<td>Số test không map về REQ nào</td>
<td>Test thừa, hoặc requirement chưa được ghi nhận</td>
</tr>
</tbody>
</table>

Kết quả được phân nhóm bằng năm ký hiệu, cộng một mục cần người xác nhận:

<table class="rt-table">
<thead>
<tr>
<th>Ký hiệu</th>
<th>Nghĩa</th>
<th>Việc tiếp theo</th>
</tr>
</thead>
<tbody>
<tr>
<td>⬛</td>
<td><strong>Module chưa có tài liệu</strong> — nằm ngoài phạm vi RTM</td>
<td>Khảo sát bằng <code>/generate-requirements-from-website</code>. Đọc mục này <strong>trước</strong> mọi con số phần trăm</td>
</tr>
<tr>
<td>🔴</td>
<td>REQ chưa có TC nào phủ</td>
<td>Gap nghiêm trọng nhất — sinh TC lấp gap</td>
</tr>
<tr>
<td>🟠</td>
<td>REQ <strong>chỉ có mục checklist</strong>, chưa có TC — <strong>không</strong> tính là đã cover</td>
<td>Đã có người rà, nhưng chưa có cách rà lặp lại được — sinh TC</td>
</tr>
<tr>
<td>🟡</td>
<td>TC chưa được automate</td>
<td>Xếp thứ tự automate theo priority</td>
</tr>
<tr>
<td>⚪</td>
<td>Test mồ côi</td>
<td>Bổ sung requirement, gắn ID, hoặc bỏ nếu thừa</td>
</tr>
<tr>
<td>⚠️</td>
<td>Mapping suy luận theo tên/mô tả, không có ID</td>
<td>Người xác nhận — <strong>không</strong> được trộn với mapping có ID</td>
</tr>
</tbody>
</table>

Vì sao 🟠 không được tính là đã phủ, dù đã có người rà? Vì mục checklist không có steps, không có test data — không chạy lại theo đúng cách cũ được, càng không automate được. Nó chứng minh *đã có người nhìn qua*, không chứng minh *REQ đó được kiểm theo cách lặp lại được*. Ngược lại, checklist TC-based như ví dụ ở mục 3 thì mục nào cũng có `TC ID liên quan` — REQ đã được phủ qua TC, cột `Checklist` của ma trận chỉ để tra.

### 5.2. Prompt cho CRM demo — RTM hai chiều của Tester Manual

Lệnh cần **ít nhất 2 trong 3 nguồn**: Requirements, Test Case, Automation script. Tester Manual thường chỉ có hai nguồn đầu — và như thế là hợp lệ: RTM hai chiều REQ ↔ TC, có ghi chú rõ phần thiếu. Chỉ có một nguồn thì lệnh dừng và hỏi bổ sung. Checklist là **nguồn phụ**: lệnh tự quét `docs/checklists/`, nhưng checklist không được tính vào "2 trong 3".

```none
/generate-traceability-matrix

# CONTEXT
- Phạm vi: Toàn dự án (Perfex CRM demo)
- Mục đích: Báo cáo coverage trước Release 1.0

# NGUỒN DỮ LIỆU
## 1. Requirements
- File path: docs/requirements/README.md (danh mục) → index REQUIREMENTS_*_SUMMARY.md từng module
## 2. Manual Test Cases
- File TC: docs/testcases/README.md (danh mục) → index TEST_CASES_*_SUMMARY.md từng module
## 3. Automation Scripts
- Không có — đội Manual, chưa có project automation

# ĐỊNH DẠNG ID
- Requirement ID: REQ-<MODULE>-<số>
- Test Case ID: CRM_<MODULE>_TC_<3 số> (có hậu tố biến thể -a, -b...)

# TÙY CHỌN
- Xuất thêm file CSV để import Excel: Có
```

Prompt không cần nói ghi file ở đâu — RTM có **vị trí cố định**:

<table class="rt-table">
<thead>
<tr>
<th>Phạm vi</th>
<th>Đường dẫn</th>
</tr>
</thead>
<tbody>
<tr>
<td>Toàn hệ thống (mặc định)</td>
<td><code>docs/traceability/traceability_matrix.md</code> — tên file bất biến</td>
</tr>
<tr>
<td>Một module</td>
<td><code>docs/traceability/&lt;module&gt;/traceability_matrix_&lt;module&gt;.md</code> — <strong>không</strong> ghi đè file toàn hệ thống</td>
</tr>
</tbody>
</table>

Ba điều đi kèm vị trí cố định:

- **Ghi đè tại chỗ**, không thêm ngày vào tên file. Bản cũ tra bằng lịch sử git — cùng luật với file index requirements và testcases.
- **Header có Ngày sinh · Phạm vi · Mốc git** (hash commit lúc sinh RTM). TC sửa sau mốc đó là RTM đã cũ — và báo cáo tổng hợp sẽ đọc dòng này để ghi rõ *"RTM đã cũ, sinh ngày …"*.
- **RTM cũ nằm chỗ khác** (ở gốc repo, rải trong `docs/`) vẫn đọc được; lần sinh mới ghi về vị trí chuẩn và **nhắc bạn gỡ file cũ** — lệnh không tự xoá.

> ⚠️ Vì sao kit chốt cứng chỗ này? Vì RTM không chỉ để người đọc: năm lệnh khác đọc nó — `/generate-test-summary-report`, `/generate-test-progress-report`, `/generate-master-test-plan`, `/update-testcases-from-impact`, `/update-automation-from-impact`. Mỗi lần RTM nằm một chỗ thì có lệnh tìm không ra, và có lệnh đọc nhầm bản RTM một module tưởng là toàn hệ thống.

Vì sao trỏ vào **danh mục và file index** chứ không trỏ thẳng file TC? Skill `skills-coverage-traceability` ghi rõ: index Test Case **không chứa dòng TC** — chỉ đọc index là báo độ phủ 0% sai. AI phải theo mục `Bản đồ tài liệu` đọc tiếp *mọi* file nền tảng và mọi `parts/`. Module Khách hàng chẳng hạn chia 129 TC ra 5 part — sót một part là sót cả nhóm REQ.

### 5.3. Đọc kết quả: 100%, 54,4% hay 3/23?

Đây là bức tranh mà một RTM đúng phải vẽ ra từ tài liệu hiện có trong kit (Anh Tester đối chiếu tay từ các file index để bạn có số so với kết quả AI):

<table class="rt-table">
<thead>
<tr>
<th>Module</th>
<th>Tổng REQ</th>
<th>Trong phạm vi kiểm thử</th>
<th>Có ≥ 1 TC</th>
<th>Nhóm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Đăng nhập <code>LOGIN</code></td>
<td>44</td>
<td>40</td>
<td>40</td>
<td>✅ — 4 REQ ngoài phạm vi theo quyết định PO, <strong>không</strong> phải 🔴</td>
</tr>
<tr>
<td>Khách hàng <code>CUST</code></td>
<td>84</td>
<td>84</td>
<td>84</td>
<td>✅ — 129 TC</td>
</tr>
<tr>
<td>Dự án <code>PRJ</code></td>
<td>104</td>
<td>104</td>
<td><strong>0</strong></td>
<td>🔴 104 REQ chưa có TC</td>
</tr>
<tr>
<td>20 module còn lại</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>⬛ Chưa khảo sát — không có REQ nào để tính</td>
</tr>
</tbody>
</table>

Cùng một bộ dữ liệu, có ba cách kể chuyện:

<table class="rt-table">
<thead>
<tr>
<th>Con số</th>
<th>Cách tính</th>
<th>Vấn đề</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>100%</strong></td>
<td>124/124 — chỉ tính module đã có TC</td>
<td>Lặng lẽ bỏ <code>PRJ</code> ra khỏi mẫu số. Đây là con số <strong>sai</strong></td>
</tr>
<tr>
<td><strong>54,4%</strong></td>
<td>124/228 — mọi REQ trong phạm vi của 3 module đã có tài liệu</td>
<td>Đúng công thức, nhưng một mình nó vẫn gây hiểu nhầm</td>
</tr>
<tr>
<td><strong>3/23 module</strong></td>
<td>Module đã có tài liệu / tổng module trong danh mục</td>
<td>Câu phải đứng <strong>trước</strong> mọi phần trăm: 54,4% chỉ tính trên 3 module</td>
</tr>
</tbody>
</table>

> ⚠️ Kit gọi mục ⬛ là **điểm mù của RTM**: module chưa khảo sát thì không có REQ nào "chưa cover", nên tỷ lệ tính đúng công thức vẫn có thể rất đẹp trong khi cả vùng chưa ai chạm tới. RTM nào đặt phần trăm lên trên mà không có danh sách ⬛ phía trên nó là RTM chưa đạt — trả lại cho AI làm lại.

Thêm ba điểm khi đọc kết quả của CRM demo:

- **4 REQ ngoài phạm vi của `LOGIN`** (`REQ-LOGIN-27`, `34`, `35`, `40`) phải nằm trong một danh sách riêng kèm lý do và mã AMB — không bị đếm thành 🔴, cũng không bị lờ đi. File index đã ghi sẵn bảng "REQ cố ý KHÔNG có TC", AI chỉ cần dẫn lại.
- **104 dòng 🔴 của `PRJ`** không phải lỗi của RTM — RTM làm đúng việc là phơi chúng ra. Master Test Plan Release 1.0 đã hẹn hạn sinh và review TC `PRJ` là 02-10-2026; RTM là nơi cho thấy hạn đó đã giữ được chưa.
- **🟠 bằng 0, cột `Checklist` trống** — kit chưa có checklist nào trong `docs/checklists/`. Sau khi bạn sinh checklist smoke ở mục 3 và chạy lại RTM, cột `Checklist` của các REQ đăng nhập sẽ có mã mục, nhưng trạng thái **không đổi**: mục nào cũng TC-based, REQ đã được phủ qua TC từ trước.

### 5.4. Sáu việc không được để AI làm với RTM

<table class="rt-table">
<thead>
<tr>
<th>Không được</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bịa mapping</strong> cho đẹp bảng</td>
<td>Không chắc thì để trống và đưa vào mục "cần xác nhận". Một ô sai tự tin còn nguy hiểm hơn mười ô trống</td>
</tr>
<tr>
<td><strong>Tự sửa file TC</strong> để thêm REQ ID còn thiếu</td>
<td>Lệnh chỉ được <em>đề xuất</em>. Sửa bộ TC là việc của <code>/review-testcases</code> mode FIX hoặc vòng delta, có người duyệt</td>
</tr>
<tr>
<td><strong>Lấy cột <code>Automation = Yes</code></strong> trong file TC làm độ phủ automation</td>
<td>README của execution-viewer cảnh báo thẳng: cột đó là <strong>dự định</strong> lúc viết TC, không phải <strong>thực tế</strong> đã có script. Không có thư mục script → Automation Coverage là "không có dữ liệu", không phải 80%</td>
</tr>
<tr>
<td><strong>Tính REQ ngoài phạm vi là 🔴</strong></td>
<td>Làm sai lệch gap thật và khiến người đọc đòi sinh TC cho thứ PO đã loại</td>
</tr>
<tr>
<td><strong>Tính REQ chỉ có checklist (🟠)</strong> là đã cover</td>
<td>Requirement Coverage tăng mà không có TC nào để chạy lại — con số đẹp lên đúng ở chỗ yếu nhất</td>
</tr>
<tr>
<td><strong>Tính TC <code>@Deprecated</code></strong> là đang phủ REQ</td>
<td>Chức năng đã gỡ thì TC đó không chứng minh được gì. Skill loại chúng khỏi cả độ phủ REQ lẫn mẫu số automation</td>
</tr>
</tbody>
</table>

> 💡 Muốn xem trực quan và xuất Excel nhiều sheet: mở [scripts/execution-viewer/bundle.html](https://github.com/anhtester/claude-testing-skills/blob/main/scripts/execution-viewer/README.md), kéo thả `docs/traceability/traceability_matrix.md` vào → tab **Độ phủ automation**. Trang này tự tính lại từ bảng "Ma trận chi tiết" chứ không đọc bảng Tổng quan — nên nếu AI chép số tổng quan sai, viewer sẽ ra số khác và bạn bắt được ngay. Trạng thái 🟠 *Chỉ có checklist* cũng được viewer tách riêng.

## 6. Báo cáo tổng hợp — trả lời "release được không"

### 6.1. QA khuyến nghị, PM quyết định

Đây là luật đầu tiên của skill `skills-test-summary-reporter`, và được đặt lên trước cả phần số liệu. Báo cáo đưa ra **khuyến nghị kèm căn cứ**; quyết định release là của PM/PO — họ cân thêm áp lực thị trường, hợp đồng, chi phí trễ hạn mà QA không nắm.

<table class="rt-table">
<thead>
<tr>
<th>✅ Viết thế này</th>
<th>❌ Không viết thế này</th>
</tr>
</thead>
<tbody>
<tr>
<td>"Khuyến nghị <strong>NO-GO</strong>: còn 1 bug Critical mở (<code>BUG_login_1785678750_TC039</code>). Nếu vẫn release, mật khẩu người dùng có thể bị gửi qua kết nối không mã hoá."</td>
<td>"Cấm release."</td>
</tr>
<tr>
<td>"Khuyến nghị <strong>GO có điều kiện</strong>: đạt tiêu chí, trừ module X chưa test. Chấp nhận được nếu module đó chưa mở cho người dùng."</td>
<td>"OK, release thoải mái."</td>
</tr>
</tbody>
</table>

Ba mức khuyến nghị, và thứ **bắt buộc** đi kèm từng mức:

<table class="rt-table">
<thead>
<tr>
<th>Khuyến nghị</th>
<th>Khi nào</th>
<th>Bắt buộc kèm</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 <strong>GO</strong></td>
<td>Đạt toàn bộ tiêu chí exit</td>
<td><strong>Vẫn phải</strong> liệt kê rủi ro tồn đọng</td>
</tr>
<tr>
<td>🟡 <strong>GO có điều kiện</strong></td>
<td>Đạt phần lớn; phần thiếu có workaround hoặc ngoài tầm người dùng</td>
<td>Điều kiện đánh số + rủi ro nếu vẫn release</td>
</tr>
<tr>
<td>🔴 <strong>NO-GO</strong></td>
<td>Còn bug Critical mở, hoặc luồng nghiệp vụ chính chưa chạy được</td>
<td>Nêu <strong>đích danh</strong> bug/vùng chặn và việc cần làm để gỡ</td>
</tr>
</tbody>
</table>

Và một câu phải có trong **mọi** báo cáo, nguyên văn:

> ⚠️ Quyết định release thuộc về PM/PO. Báo cáo này cung cấp căn cứ, không thay thế quyết định đó.

Vì sao GO cũng phải kèm rủi ro? Vì GO trơn tru không nêu tồn đọng là báo cáo vô trách nhiệm — release xong có sự cố, không ai biết QA đã cảnh báo hay chưa. Rủi ro được ghi ra giấy là thứ bảo vệ cả người viết báo cáo lẫn người ra quyết định.

### 6.2. Tiêu chí exit chốt trước — plan công bố, báo cáo chấm lại

Nhìn kết quả rồi mới đặt ngưỡng là **hợp thức hoá kết quả**, không phải đánh giá. Vì vậy lệnh lấy tiêu chí exit theo thứ tự cố định:

1. **Master Test Plan của mốc** — `docs/test-plans/test_plan_<mốc>.md` mục 4.2. Có plan thì lấy đúng bộ đã công bố, **không hỏi lại**. Đây là lý do bài Chuẩn hoá Requirements và Test Plan dặn bạn chốt tiêu chí từ đầu đợt.
2. Không có plan → hỏi bạn tiêu chí của dự án.
3. Không có cả hai → dùng bộ mặc định, và báo cáo **ghi rõ là bộ mặc định của agent, cần PM xác nhận**.

Plan Release 1.0 của CRM demo chọn bộ mặc định — 7 tiêu chí, Anh Tester chọn ngày 17-09-2026:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Tiêu chí</th>
<th>Ngưỡng</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Bug <strong>Critical</strong> đang mở</td>
<td><strong>0</strong></td>
</tr>
<tr>
<td>2</td>
<td>Bug <strong>Major</strong> đang mở</td>
<td>0, hoặc có workaround PM chấp nhận bằng văn bản</td>
</tr>
<tr>
<td>3</td>
<td>Pass rate TC <strong>Priority High</strong></td>
<td>≥ 95%</td>
</tr>
<tr>
<td>4</td>
<td>Pass rate toàn bộ TC đã chạy</td>
<td>≥ 90%</td>
</tr>
<tr>
<td>5</td>
<td>Tỷ lệ <strong>BLOCKED</strong></td>
<td>≤ 5%</td>
</tr>
<tr>
<td>6</td>
<td>REQ mức Critical có ít nhất 1 TC <strong>PASS</strong></td>
<td>100%</td>
</tr>
<tr>
<td>7</td>
<td>Module trong phạm vi đã có TC và đã chạy — tính trên <strong>từng cặp module × nền tảng</strong></td>
<td>100%</td>
</tr>
</tbody>
</table>

Mỗi tiêu chí chỉ có bốn cách chấm: **✅ Đạt · ❌ Không đạt · 🟡 Ngoại lệ chờ duyệt · ➖ Không áp dụng**. Không có "gần đạt". 94,8% với ngưỡng 95% là **không đạt** — PM có thể chấp nhận, nhưng phải ghi là ngoại lệ và ghi ai duyệt.

### 6.3. Đừng nhầm với ba loại báo cáo khác

<table class="rt-table">
<thead>
<tr>
<th>Lệnh</th>
<th>Phạm vi</th>
<th>Trả lời</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/analyze-test-report</code></td>
<td><strong>Một</strong> lượt chạy</td>
<td>"Lượt vừa rồi fail vì sao?" — gom nhóm root cause</td>
</tr>
<tr>
<td><code>/generate-test-progress-report</code></td>
<td>Một kỳ <strong>trong</strong> đợt — thường hằng tuần</td>
<td>"Có kịp mốc không, đang vướng gì?" — <strong>không</strong> khuyến nghị release</td>
</tr>
<tr>
<td><code>/generate-traceability-matrix</code></td>
<td>Toàn hệ thống tại một thời điểm</td>
<td>"Requirement nào chưa có test?"</td>
</tr>
<tr>
<td><code>/generate-test-summary-report</code></td>
<td><strong>Toàn dự án tại một mốc</strong></td>
<td>"Đã test gì, còn lỗi gì, có release được không?"</td>
</tr>
</tbody>
</table>

Báo cáo tổng hợp *tiêu thụ* những thứ còn lại: đọc plan để lấy phạm vi và tiêu chí, đọc các báo cáo tiến độ để lấy trở ngại và sai lệch lịch, đọc RTM cho mục độ phủ. Bài Schedule sắp tới sẽ hẹn giờ cho báo cáo tiến độ thứ Sáu; còn báo cáo tổng hợp thì chạy theo mốc, không theo lịch tuần.

### 6.4. Chín mục, đúng thứ tự

Báo cáo của kit biên soạn theo cấu trúc **ISO/IEC/IEEE 29119-3 — Test Completion Report**, đủ 9 mục. Thứ tự không phải ngẫu nhiên:

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Vì sao ở vị trí đó</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Khuyến nghị</td>
<td>Người đọc bận — kết luận phải nằm ở dòng đầu</td>
</tr>
<tr>
<td><strong>2. Vùng chưa kiểm thử</strong></td>
<td><strong>Trước mọi tỷ lệ</strong> — nếu không, con số đẹp che mất vùng trắng. Cùng luật với mục ⬛ của RTM</td>
</tr>
<tr>
<td>3. Đối chiếu tiêu chí exit</td>
<td>Cho thấy khuyến nghị dựa trên chuẩn, không phải cảm tính</td>
</tr>
<tr>
<td>4. Kết quả theo module</td>
<td>Mỗi dòng một cặp module × nền tảng. <strong>Ba bảng riêng, không cộng gộp:</strong> bộ TC manual · kết quả rà checklist (bảng 4b) · automation</td>
</tr>
<tr>
<td>5. Tình hình lỗi</td>
<td>Bug đang mở theo Severity + regression phát sinh trong kỳ</td>
</tr>
<tr>
<td>6. Độ phủ yêu cầu</td>
<td>Lấy từ RTM, nếu có</td>
</tr>
<tr>
<td>7. Đề xuất hành động</td>
<td>Việc cụ thể, ai làm, lệnh nào</td>
</tr>
<tr>
<td>8. Yếu tố cản trở &amp; Bài học</td>
<td>Đọc xong kết quả mới hiểu vì sao số ra như vậy</td>
</tr>
<tr>
<td>9. Phụ lục — Ánh xạ chuẩn</td>
<td>Cho người nghiệm thu/audit, không phải người đọc thường</td>
</tr>
</tbody>
</table>

> ⚠️ Hai câu kit cấm AI viết vào báo cáo: **số điều khoản** của chuẩn (số đổi giữa các bản phát hành, agent không có bản chuẩn để tra — ghi số là bịa), và câu **"tuân thủ ISO/IEC/IEEE 29119"** (tuân thủ là kết luận của đánh giá viên). Câu đúng: *"biên soạn theo cấu trúc ISO/IEC/IEEE 29119-3 — Test Completion Report"*.

## 7. Diễn tập: chấm Release 1.0 bằng số liệu thật trong kit

Báo cáo tổng hợp chính thức của Release 1.0 hẹn ngày 10-12-2026 trong plan. Nhưng bạn không cần đợi tới đó mới chạy lệnh: chạy **diễn tập** ngay bây giờ cho bạn thấy đợt đang cách GO bao xa, và — quan trọng hơn — cho bạn tập soát số liệu AI đưa ra. Bản diễn tập là để bạn đọc, **không gửi PM**; giữa đợt thì thứ gửi PM là báo cáo tiến độ.

### 7.1. Prompt

```none
/generate-test-summary-report

# CONTEXT
- Mốc báo cáo: Release 1.0 — bản DIỄN TẬP giữa đợt, không gửi ra ngoài
- Build / Version: v1.0.0
- Môi trường: môi trường test riêng của Release 1.0
- Người nhận báo cáo: PM nội bộ

# PHẠM VI RELEASE
- Lấy theo docs/test-plans/test_plan_release_1.0.md mục 2.1 · 2.2

# TIÊU CHÍ EXIT
- Lấy theo plan mục 4.2 — không đặt lại

# NGUỒN DỮ LIỆU
- Execution report: để trống — tự glob docs/executions/
- Bug: docs/bugs/
- RTM: docs/traceability/traceability_matrix.md
- Report automation: để trống — đợt này không chạy automation
```

Vì plan đã có, Bước 0 (checkpoint duy nhất bắt buộc hỏi) của lệnh chỉ còn hỏi bạn đúng phần plan không biết — **build thực tế**, và prompt trên đã trả lời sẵn. Phạm vi, tiêu chí exit, người nhận đã được plan công bố.

### 7.2. Sáu cái bẫy số liệu AI phải tránh

Dữ liệu thật hiếm khi sạch. Module Đăng nhập trong kit có **hai** lượt chạy, và chỉ riêng chuyện ghép hai lượt đó đã đủ để ra ba con số pass rate khác nhau. Skill `skills-test-summary-reporter` nay ghi thẳng hai nguyên tắc số liệu cho đúng chỗ này: *số của một module × nền tảng là kết quả mới nhất của **từng TC**, không phải lần chạy mới nhất*, và *không gộp kết quả checklist với kết quả bộ TC*. Lệnh đã làm đúng mặc định — nhưng bạn vẫn phải biết bẫy nằm đâu để soát:

<table class="rt-table">
<thead>
<tr>
<th>Bẫy</th>
<th>Con số sai</th>
<th>Cách làm đúng</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Lấy run mới nhất làm số của module</strong></td>
<td><code>run_1789759574</code>: 13/13 PASS = <strong>100%</strong> — nhưng lượt này chỉ chạy 13 TC bổ sung</td>
<td>Gộp <strong>theo từng TC</strong>: TC nào lấy kết quả lần chạy mới nhất của TC đó. Ra <strong>51 TC: 45 PASS · 6 FAIL · 0 BLOCKED · 0 SKIPPED</strong></td>
</tr>
<tr>
<td><strong>2. Chỉ nhìn run cũ</strong></td>
<td><code>run_1787215085</code>: 32/40 = <strong>80,0%</strong>, BLOCKED 4,9%</td>
<td><code>TC_014</code>, <code>TC_034</code> (BLOCKED) và <code>TC_026</code> (SKIPPED) đã được chạy bổ sung PASS ở run sau</td>
</tr>
<tr>
<td><strong>3. TC đã sửa sau lượt chạy</strong></td>
<td><code>TC_018</code> FAIL ở run cũ vì biến thể <code>a</code> — nhưng biến thể đó <strong>đã bị bỏ</strong> ngày 19-09-2026 (Expected sai, trùng <code>TC_046-c</code>); biến thể còn lại PASS</td>
<td>Báo <strong>cả hai</strong>: 45/51 = <strong>88,2%</strong> theo kết quả đã ghi · 46/51 = <strong>90,2%</strong> nếu chấm lại <code>TC_018</code>. Đề xuất chạy lại <code>TC_018</code> bản hiện hành — không tự chọn số đẹp</td>
</tr>
<tr>
<td><strong>4. Kết quả trên môi trường khác build</strong></td>
<td>Cả hai lượt chạy trên <strong>bản demo dùng chung</strong>, không phải build <code>v1.0.0</code> trên môi trường riêng</td>
<td>Ghi rõ đây là số <strong>điểm xuất phát</strong>, không phải bằng chứng cho build release. Báo cáo tiến độ 17-09 của kit cũng đã ghi đúng câu này</td>
</tr>
<tr>
<td><strong>5. Số trong plan khác hiện trạng</strong></td>
<td>Plan v1.3 ghi <code>LOGIN</code> 43 REQ · 50 TC, <code>CUST</code> <strong>0 TC</strong></td>
<td>Hiện trạng: <code>LOGIN</code> 44 REQ · 51 TC, <code>CUST</code> <strong>129 TC</strong>. Nêu cả hai: plan là cam kết lúc lập, file index là hiện trạng</td>
</tr>
<tr>
<td><strong>6. Cộng lượt chạy checklist vào bộ TC</strong></td>
<td>Chạy checklist smoke 10 mục trên môi trường mới rồi cộng vào: 51 + 10 = 61 "TC" — cả tổng lẫn pass rate đều vô nghĩa</td>
<td>Lượt chạy có <code>Loại nguồn</code> = <code>Checklist …</code> báo ở <strong>bảng 4b riêng</strong>. 10 mục smoke không phải 10 TC</td>
</tr>
</tbody>
</table>

> 📌 Bẫy 3 là ví dụ đẹp nhất của luật *"số liệu mâu thuẫn → nêu cả hai, không tự chọn số đẹp hơn"*: ngưỡng tiêu chí 4 là 90%. Chọn 88,2% thì **không đạt**, chọn 90,2% thì **đạt**. Một TC duy nhất, xử lý thế nào là đổi kết luận. Đó là lý do lệnh không được tự quyết — và bạn cũng không.

### 7.3. Đối chiếu 7 tiêu chí exit

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Tiêu chí</th>
<th>Ngưỡng</th>
<th>Thực tế</th>
<th>Kết quả</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Bug Critical đang mở</td>
<td>0</td>
<td><strong>1</strong> — <code>BUG_login_1785678750_TC039</code>, retest gần nhất <code>NOT_FIXED</code></td>
<td>❌ Không đạt</td>
</tr>
<tr>
<td>2</td>
<td>Bug Major đang mở</td>
<td>0</td>
<td>0 — 5 bug đang mở gồm 1 Critical · 3 Minor · 1 Trivial</td>
<td>✅ Đạt</td>
</tr>
<tr>
<td>3</td>
<td>Pass rate TC Priority High</td>
<td>≥ 95%</td>
<td>14/18 = <strong>77,8%</strong> — FAIL: <code>TC_016</code>, <code>TC_028</code>, <code>TC_029</code>, <code>TC_039</code></td>
<td>❌ Không đạt</td>
</tr>
<tr>
<td>4</td>
<td>Pass rate toàn bộ TC đã chạy</td>
<td>≥ 90%</td>
<td>45/51 = <strong>88,2%</strong> (90,2% nếu chấm lại <code>TC_018</code> — chờ lượt chạy)</td>
<td>❌ Không đạt</td>
</tr>
<tr>
<td>5</td>
<td>Tỷ lệ BLOCKED</td>
<td>≤ 5%</td>
<td>0/51 sau khi gộp</td>
<td>✅ Đạt</td>
</tr>
<tr>
<td>6</td>
<td>REQ mức Critical có TC PASS</td>
<td>100%</td>
<td>Tài liệu REQ <strong>không có cột mức độ</strong> — không chấm thẳng được</td>
<td>⚠️ Không có dữ liệu — AI phải nêu cách suy (nếu dùng) và để PM xác nhận</td>
</tr>
<tr>
<td>7</td>
<td>Cặp module × nền tảng đã có TC và đã chạy</td>
<td>100%</td>
<td><strong>1/3</strong> — <code>LOGIN</code> web ✅ · <code>CUST</code> web có 129 TC, chưa chạy · <code>PRJ</code> web chưa có TC</td>
<td>❌ Không đạt</td>
</tr>
</tbody>
</table>

Ba chỗ trong bảng đáng dừng lại:

- **Tiêu chí 3 — "Priority High" nghĩa là gì?** Thang Priority của bộ TC có 4 mức: Critical 10 TC · High 18 · Medium 19 · Low 4. Hiểu "High" là đúng mức High thì 77,8%; gộp cả Critical thì 24/28 = 85,7%. Lần này cả hai cách đều không đạt nên kết luận không đổi — nhưng báo cáo vẫn phải ghi đang hiểu theo cách nào, và bạn nên đề nghị ghi rõ vào mục 4.2 của plan cho đợt sau.
- **Tiêu chí 6 — thiếu dữ liệu thì nói thiếu.** Skill cấm bịa số: "thiếu dữ liệu thì ghi không có dữ liệu, không ước lượng". AI có thể đề xuất cách suy (ví dụ REQ có TC Priority Critical — cả 10 TC Critical đều PASS), nhưng phải đánh dấu đó là suy luận, không được tự chấm ✅.
- **Checklist không cứu được tiêu chí 3, 4, 5, 7.** Giả sử tuần tới bạn kịp chạy checklist smoke cho `CUST` — tiêu chí 7 vẫn ❌, mục 2 ghi *"Khách hàng: chỉ rà checklist smoke"*. Ba tiêu chí pass rate và BLOCKED chỉ đo bộ TC. Kết quả checklist chỉ được tính cho tiêu chí 6, và **chỉ** với REQ chưa có TC nào. Đợt nào muốn dùng checklist làm điều kiện ra thì phải thêm tiêu chí riêng vào plan từ đầu, ví dụ *"Checklist release-readiness: 100% mục P1 PASS"*.

### 7.4. Khuyến nghị và vùng chưa kiểm thử

Với 4 tiêu chí không đạt, trong đó có bug Critical đang mở, khuyến nghị chỉ có thể là:

```none
## 1. Khuyến nghị

> ## 🔴 NO-GO
>
> Đạt 2/7 tiêu chí exit · 1 tiêu chí không có dữ liệu.

**Vùng chặn:**
1. BUG_login_1785678750_TC039 (🔴 Critical) — trang đăng nhập phục vụ qua HTTP, không ép HTTPS,
   không HSTS. Retest gần nhất NOT_FIXED. Gỡ: vá cấu hình máy chủ → /retest-fixed-bugs mode FULL
2. 2/3 cặp module × nền tảng trong phạm vi chưa chạy: Khách hàng (129 TC chưa chạy lần nào),
   Dự án (104 REQ chưa có TC)

> ⚠️ Quyết định release thuộc về PM/PO. Báo cáo này cung cấp căn cứ, không thay thế quyết định đó.
```

Ngay sau đó, **trước mọi tỷ lệ**, là mục 2 — vùng chưa kiểm thử. Với Release 1.0 nó phải nêu đủ hai loại:

<table class="rt-table">
<thead>
<tr>
<th>Vùng</th>
<th>Loại</th>
<th>Ghi chú</th>
</tr>
</thead>
<tbody>
<tr>
<td>Khách hàng · Dự án</td>
<td><strong>Trong phạm vi</strong>, chưa chạy</td>
<td>Tính vào tiêu chí 7 — đây là vùng chặn</td>
</tr>
<tr>
<td>20 module CRM còn lại</td>
<td>Ngoài phạm vi theo plan 2.2</td>
<td>Không tính vào tiêu chí 7, nhưng <strong>vẫn liệt kê</strong> — người đọc phải biết hệ thống còn 20/23 module chưa ai khảo sát</td>
</tr>
<tr>
<td>Cổng khách hàng · khu Quản trị hệ thống · Activity Log</td>
<td>Ngoài phạm vi / thiếu quyền</td>
<td>Activity Log cần Super Admin — plan ghi được cấp trước 06-10-2026 thì đưa vào</td>
</tr>
</tbody>
</table>

> 💡 Đọc lại bảng này và bạn sẽ thấy vì sao kit bắt "vùng chưa test đứng trước tỷ lệ". Nếu mục 4 đứng đầu, PM đọc thấy *"Đăng nhập 88,2%"* và nghĩ đợt test gần xong — trong khi hai phần ba phạm vi release chưa chạy một TC nào.

### 7.5. Checklist mới FAIL, bộ TC cũ PASS — tin checklist

Quay lại checklist smoke ở mục 3. Giả sử bạn chạy nó bằng `/execute-test-cases` trên môi trường riêng, build `v1.0.0`, và mục 2 — *đăng nhập Admin hợp lệ* — FAIL. Trong khi đó `CRM_LOGIN_TC_005`, TC liên quan của chính mục này, vẫn đang PASS ở `run_1787215085` trên bản demo.

Hai nguồn nói hai điều ngược nhau, và kit chốt rõ tin bên nào: **checklist mới hơn mà FAIL, bộ TC cũ hơn mà PASS → tin checklist**. Mục FAIL trên build mới có TC liên quan từng PASS trên build cũ nghĩa là **build mới đã vỡ** — đó là regression. Báo cáo tổng hợp phải:

- Báo mục `CL-smoke_20261009-02` FAIL ở bảng 4b — **không** sửa số của bảng bộ TC.
- Nêu lại ở mục 5 (Tình hình lỗi) như một regression, ghi **cả hai nguồn**: lượt chạy checklist và lượt chạy bộ TC.
- Không để con số *"`TC_005` PASS"* của build cũ che đi tín hiệu của build mới.

> 💡 Đây là lý do checklist smoke trên môi trường mới quan trọng hơn vẻ ngoài "chỉ có 10 mục" của nó. Bộ TC của module Đăng nhập chạy trên bản demo — chưa ai biết nó còn đúng trên build release hay không. Checklist chạy trên build mới là **tín hiệu mới nhất** về build đó.

### 7.6. Mục 8 — thứ hay bị bỏ nhất

Skill gọi mục 8 (Yếu tố cản trở & Bài học) là **mục hay bị bỏ nhất và mất mát nhiều nhất**: không ghi lại vì sao đợt này chậm thì đợt sau lặp lại nguyên xi. Kit có sẵn nguyên liệu thật cho mục này trong hai execution report:

<table class="rt-table">
<thead>
<tr>
<th>Yếu tố</th>
<th>Mất bao lâu</th>
<th>Bài học → áp dụng vào đâu</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TC_014</code> BLOCKED — mật khẩu demo toàn chữ số, không thử được sai kiểu chữ hoa/thường</td>
<td>20-08 → 19-09-2026 (~1 tháng)</td>
<td>Tài khoản test riêng cho TC đặc thù phải là <strong>tiêu chí vào</strong> — mục 4.1 của plan đợt sau</td>
</tr>
<tr>
<td><code>TC_034</code> BLOCKED — cần một task có bộ đếm giờ đang chạy, thuộc module khác</td>
<td>20-08 → 19-09-2026</td>
<td>TC phụ thuộc dữ liệu module khác phải có bước dựng và dọn dữ liệu ngay trong TC (đã sửa ở lượt review 19-09)</td>
</tr>
<tr>
<td>Môi trường test riêng trễ lịch</td>
<td>27-09 → 05-10-2026 (8 ngày)</td>
<td>Bắt đầu thực thi lùi theo; báo cáo tiến độ lập theo lịch cũ phải được cập nhật — mục 7.1 của plan</td>
</tr>
</tbody>
</table>

> ⚠️ Hai điều kit bắt buộc ở mục này: ghi **thời lượng thực tế** chứ không chỉ tên sự việc (không có con số thì đợt sau vẫn ước lượng sai y như đợt này), và mỗi bài học phải chỉ **đích danh mục nào của plan đợt sau** sẽ đổi. Bài học không có nơi áp dụng chỉ là câu nói suông.

## 8. Ba tài liệu nối với nhau thế nào

```none
/generate-checklist-test        → checklist · Mã checklist CL-<loại>_<ngày>        ← mỗi build · mỗi hotfix
        ↓
/execute-test-cases             → execution_report.md · Loại nguồn: Checklist <loại>
        ↓                         mỗi mục mang mã CL-…-<nn> (bộ TC chạy cùng lệnh này)
/create-bug-report              → docs/bugs/<module của mục>/<nền-tảng>/
/retest-fixed-bugs              → như bug của bộ TC
        ↓
/generate-traceability-matrix   → cột Checklist · 🟠 không tính là đã cover → mục 6 "Độ phủ yêu cầu"
        ↓
/generate-test-progress-report ─┤  (trở ngại, sai lệch lịch → mục 8)
/generate-master-test-plan ─────┤  (phạm vi + tiêu chí exit → mục 2, 3)
        ↓
/generate-test-summary-report   → bảng bộ TC · bảng 4b checklist · bảng automation → PM / PO / khách hàng
```

Nhịp chạy của từng tài liệu và nơi file nằm:

<table class="rt-table">
<thead>
<tr>
<th>Tài liệu</th>
<th>Khi nào chạy</th>
<th>File</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Checklist</strong></td>
<td>Mỗi build mới · mỗi hotfix · trước release</td>
<td><code>docs/checklists/&lt;module&gt;/&lt;nền-tảng&gt;/checklist_&lt;loại&gt;_&lt;YYYYMMDD&gt;.md</code><br/>post-hotfix: <code>checklist_post-hotfix_&lt;TICKET-ID&gt;.md</code><br/>release: <code>docs/checklists/_release/&lt;nền-tảng&gt;/checklist_release_&lt;mốc&gt;.md</code><br/>kết quả chạy: <code>docs/executions/&lt;module&gt;/&lt;nền-tảng&gt;/run_*/</code> — release thì <code>docs/executions/_release/&lt;nền-tảng&gt;/run_*/</code></td>
</tr>
<tr>
<td><strong>RTM</strong></td>
<td>Trước release · <strong>sau mỗi vòng delta</strong> khi requirement đổi</td>
<td><code>docs/traceability/traceability_matrix.md</code> (+ <code>.csv</code> cùng tên) — ghi đè tại chỗ, bản cũ tra git<br/>một module: <code>docs/traceability/&lt;module&gt;/traceability_matrix_&lt;module&gt;.md</code></td>
</tr>
<tr>
<td><strong>Báo cáo tổng hợp</strong></td>
<td>Mỗi mốc release / sprint / UAT</td>
<td><code>docs/executions/test_summary_&lt;mốc&gt;_&lt;timestamp&gt;.md</code> — ở <strong>gốc</strong> <code>executions/</code> vì cắt ngang mọi module</td>
</tr>
</tbody>
</table>

Với checklist Release-readiness, `<mốc>` dùng **cùng slug** với file plan. Plan tên `test_plan_release_1.0.md` thì slug là `release_1.0` và checklist thành `docs/checklists/_release/web/checklist_release_release_1.0.md`, mã checklist `CL-release_release_1.0` — chữ "release" lặp hai lần trông lạ nhưng đúng quy ước. Đừng để AI "sửa cho gọn" thành tên khác: cùng slug là cách các lệnh tự tìm thấy tài liệu của nhau mà không phải hỏi.

Hai điểm riêng của checklist Release-readiness: nó có **một file cho mỗi nền tảng** (đợt release có cả web lẫn mobile thì hai file), và bảng mục có thêm cột **`Module`**. Thư mục `_release` đóng vai *module giả* — dấu `_` đầu báo cho các lệnh quét module bỏ qua nó. Cột `Module` là thứ quy từng mục về đúng module thật khi sinh bug, khi tính RTM và khi lập báo cáo tổng hợp.

> 📌 Bài Update → Retest đã nhắc: sau mỗi đợt delta, chạy lại `/generate-traceability-matrix` để ma trận khớp với REQ và TC mới. RTM cũ sau một vòng delta là RTM nói dối — nó vẫn chấm phủ cho REQ đã đổi nghĩa. Giờ thì lời nói dối đó có dấu vết: dòng **Mốc git** ở header RTM cho báo cáo tổng hợp biết RTM sinh trước lần sửa TC cuối, và báo cáo sẽ ghi rõ *"RTM đã cũ"* thay vì lặng lẽ dùng số cũ.

## 9. Gửi báo cáo ra ngoài an toàn

Báo cáo tổng hợp là tài liệu **duy nhất** trong ba thứ thường được gửi ra khỏi đội — tới PM, tới khách hàng. Skill dặn rõ: không đưa credentials, không đưa dữ liệu khách hàng thật vào báo cáo. Nghe hiển nhiên, nhưng chỗ rò rỉ thường nằm ở những nơi bạn không để ý:

<table class="rt-table">
<thead>
<tr>
<th>Chỗ dễ lọt</th>
<th>Ví dụ thật trong kit</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bảng thông tin đầu execution report</strong></td>
<td>Execution report ghi cả email ba tài khoản dùng để chạy. AI chép phần đầu sang báo cáo là email tài khoản theo ra ngoài</td>
</tr>
<tr>
<td><strong>Ảnh evidence đính kèm</strong></td>
<td>Danh mục bug cảnh báo: screenshot hệ thống thật thường <strong>chứa dữ liệu khách hàng</strong> — cùng mức nhạy cảm với <code>docs/executions/</code></td>
</tr>
<tr>
<td><strong>URL môi trường nội bộ</strong></td>
<td>Báo cáo cho khách hàng chỉ cần tên môi trường (Staging, môi trường test riêng), không cần URL</td>
</tr>
</tbody>
</table>

Với người ngoài đội không quen đọc Markdown, xuất Excel từ `scripts/execution-viewer/bundle.html`: nạp các `execution_report.md` thì Excel có sheet **Tổng hợp** (kết quả mới nhất — đúng tinh thần gộp ở bẫy 1) cộng mỗi lần chạy một sheet giữ nguyên bản; nạp `docs/traceability/traceability_matrix.md` thì có tab độ phủ. Chạy offline, double-click là mở. Lượt chạy checklist hiện nhãn **CHECKLIST** riêng ở sidebar; nạp lẫn với lượt chạy bộ TC thì viewer cảnh báo *trộn bộ TC với checklist* — chọn từng lượt chạy để xem số đúng trước khi xuất Excel gửi đi.

## 10. Nghiệm thu và lỗi hay gặp

### 10.1. Checklist nghiệm thu

<table class="rt-table">
<thead>
<tr>
<th>Tài liệu</th>
<th>Kiểm trước khi dùng</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Checklist</strong></td>
<td>Đã ghi loại + nguồn + <code>Mã checklist</code> khớp tên file ở đầu file · mọi mục ≤ 20 từ, mở bằng động từ, kỳ vọng quan sát được · cột <code>TC ID liên quan</code> có hậu tố biến thể · có phần Không áp dụng · có bảng Ký nhận · ô ☐ còn trống · số mục trong ngưỡng · chạy bằng <code>/execute-test-cases</code> thì report có <code>Loại nguồn</code> và mã mục <code>CL-…-&lt;nn&gt;</code></td>
</tr>
<tr>
<td><strong>RTM</strong></td>
<td>File nằm ở <code>docs/traceability/</code>, header có Ngày sinh · Phạm vi · Mốc git · danh sách ⬛ đứng trên mọi phần trăm · mẫu số gồm cả module có REQ mà chưa có TC · REQ 🟠 chỉ có checklist không tính là đã phủ · REQ ngoài phạm vi tách riêng kèm lý do · mapping ⚠️ tách khỏi mapping có ID · Automation Coverage lấy từ script thật hoặc ghi "không có dữ liệu" · file TC gốc không bị sửa</td>
</tr>
<tr>
<td><strong>Báo cáo tổng hợp</strong></td>
<td>Khuyến nghị ở dòng đầu, có căn cứ đích danh · câu chốt "quyết định thuộc PM/PO" · vùng chưa test đứng trước tỷ lệ · tiêu chí lấy từ plan (hoặc ghi rõ bộ mặc định) · số gộp theo từng TC · checklist ở bảng 4b, không cộng vào bộ TC · số mâu thuẫn nêu cả hai · gắn build · manual và automation không cộng gộp · RTM cũ thì ghi rõ đã cũ · mục 8 có thời lượng · không có số điều khoản chuẩn, không tuyên bố tuân thủ · không có tài khoản, URL nội bộ</td>
</tr>
</tbody>
</table>

### 10.2. Bốn lỗi hay gặp nhất

**Lỗi 1 — Tin con số đầu tiên AI đưa ra.**  
Ba con số pass rate 100% · 80,0% · 88,2% đều "đúng" theo một cách đọc nào đó. Bạn chỉ phát hiện được khi biết hỏi lại: *"số này gộp từ những lượt chạy nào, mỗi TC lấy kết quả lần nào?"*

**Lỗi 2 — Đặt lại tiêu chí sau khi thấy kết quả.**  
"Pass rate 88% thôi, hay hạ ngưỡng xuống 85% cho đợt này?" — đó chính là hợp thức hoá kết quả. Muốn chấp nhận rủi ro thì đi đường chính thức: PM chấp nhận bằng văn bản, báo cáo vẫn ghi ❌ kèm tên người duyệt.

**Lỗi 3 — Sinh RTM một lần rồi để đó.**  
RTM là ảnh chụp tại một thời điểm. Sau một vòng delta mà không chạy lại, nó vẫn chấm phủ cho REQ đã đổi nghĩa. Báo cáo tổng hợp sẽ nhìn dòng Mốc git và ghi *"RTM đã cũ"* — nhưng một báo cáo mang dòng đó gửi lên PM là bạn đã chậm một bước.

**Lỗi 4 — Biến checklist thành Test Case.**  
Thêm steps, thêm test data, thêm pre-condition cho "đầy đủ" — rồi checklist 15 phút thành tài liệu 2 tiếng mà vẫn không đủ chuẩn để lưu trữ. Cần steps thì quay về lệnh sinh TC.

## 11. Bài tập thực hành

**Bài tập 1 — Checklist Smoke và cổng quy mô.** Chạy `/generate-checklist-test` loại Smoke cho module Đăng nhập theo prompt ở mục 3.1. Kiểm: kết quả có đủ 10–20 mục không, và nếu AI bổ sung mục ngoài bộ `@Smoke` thì mục đó có TC ID thật không. Kiểm header có `Mã checklist` khớp tên file. Sau đó chạy checklist bằng `/execute-test-cases` trên `crm.anhtester.com` và mở report: ô `Loại nguồn` có ghi `Checklist smoke` không, cột `TC ID` có phải mã mục `CL-smoke_<ngày>-01`… chứ không phải `#1` không.

**Bài tập 2 — Checklist sau hotfix.** Viết prompt Post-hotfix cho `BUG_login_1787226514_TC016` (ô Email không giữ giá trị sau khi đăng nhập thất bại), với vùng ảnh hưởng do bạn tự mô tả. Đối chiếu: vùng lân cận AI khoanh có hợp lý không, và số mục có nằm trong 5–15 không.

**Bài tập 3 — RTM và ba con số.** Chạy `/generate-traceability-matrix` cho toàn dự án CRM demo. Tìm trong kết quả: danh sách ⬛ có đứng trên phần trăm không, mẫu số có gồm 104 REQ của `PRJ` không, 4 REQ ngoài phạm vi của `LOGIN` có bị đếm thành 🔴 không. Kiểm file nằm đúng `docs/traceability/traceability_matrix.md`, header có Mốc git, và nếu đã làm bài tập 1 thì cột `Checklist` có mã mục smoke.

**Bài tập 4 — Diễn tập báo cáo tổng hợp.** Chạy `/generate-test-summary-report` theo prompt mục 7.1. So kết quả với bảng 7 tiêu chí ở mục 7.3: AI có gộp theo từng TC không, có nêu cả 88,2% lẫn 90,2% không, có chấm tiêu chí 6 là ✅ một cách tự tin không. Nếu đã chạy checklist ở bài tập 1: kết quả có nằm ở bảng 4b riêng, hay bị cộng vào 51 TC? Chỗ nào lệch, viết lại prompt cho tới khi khớp.

**Bài tập 5 — Soát báo cáo trước khi gửi.** Giả sử báo cáo ở bài tập 4 sẽ gửi khách hàng. Tìm và gỡ mọi email tài khoản, URL môi trường và đường dẫn ảnh evidence. Sau đó xuất Excel từ execution-viewer và so sheet Tổng hợp với bảng mục 4 của báo cáo.

## 12. Tổng kết

- **Ba câu hỏi, ba tài liệu:** "rà nhanh thế nào" → Checklist · "đã test đủ chưa" → RTM · "release được không" → Báo cáo tổng hợp. Cả ba viết cho người khác đọc, nên sai một con số là sai ở chỗ người khác dựa vào để quyết định.
- **Checklist trả lời "đã rà hết chưa", Test Case trả lời "rà bằng cách nào".** Mục 1 dòng ≤ 20 từ, kỳ vọng quan sát được, đúng ngưỡng của loại. Đã có bộ TC thì rút từ bộ TC, giữ hậu tố biến thể, ghi phần Không áp dụng, để trống ô tick, mỗi lần rà một file mới.
- **Muốn kết quả checklist đi tiếp thì chạy bằng `/execute-test-cases`.** Mỗi checklist có `Mã checklist` `CL-<loại>_<ngày>`, mỗi mục có mã `CL-…-<nn>` — không bao giờ `#3` trần. Report ghi `Loại nguồn` để không ai cộng nhầm vào bộ TC.
- **Cổng chất lượng 5 tiêu chí chặn cả hai chiều:** bộ Smoke 9 TC của module Đăng nhập rút ra 9 mục là chưa đủ ngưỡng 10–20; checklist không có mã khớp tên file là chưa truy vết được.
- **`REQ ID` là sợi chỉ của chuỗi requirements → testcases → executions → bugs.** Truy vết nhầm còn tệ hơn không truy vết — bug Critical TC\_039 từng đứng trên một REQ không nói gì về HTTPS.
- **RTM: đọc ⬛ trước mọi phần trăm.** CRM demo có 100% hay 54,4% tuỳ mẫu số, và cả hai chỉ tính trên 3/23 module. Không bịa mapping, không sửa file TC, không lấy cột `Automation` làm độ phủ automation, không tính REQ 🟠 chỉ có checklist là đã phủ. File cố định ở `docs/traceability/`, header có Mốc git, chạy lại sau mỗi vòng delta.
- **Báo cáo tổng hợp: QA khuyến nghị, PM quyết định.** Tiêu chí chốt trước trong plan, chấm sau không có "gần đạt". GO vẫn kèm rủi ro, NO-GO nêu đích danh vùng chặn, vùng chưa test đứng trước tỷ lệ. Ba bảng riêng: bộ TC · checklist (4b) · automation. Checklist không cứu được tiêu chí 3, 4, 5, 7 — nhưng checklist mới FAIL trên build mới thì tin checklist, báo regression.
- **Soát số liệu là việc của bạn:** gộp theo từng TC chứ không lấy run mới nhất, TC đã sửa sau lượt chạy thì nêu cả hai con số, ghi build, thiếu dữ liệu thì nói thiếu. Ghi thời lượng cản trở ở mục 8, và gỡ tài khoản, URL, ảnh evidence trước khi gửi ra ngoài.
- Bài kế tiếp: **Sử dụng MCP Server trên các nền tảng ứng dụng trong công việc** — đến giờ AI chỉ đọc và ghi file trong repo của bạn. MCP Server giúp nó với tay sang được Jira, Slack, trình duyệt — nơi checklist được giao, bug được đẩy lên và báo cáo được gửi đi.