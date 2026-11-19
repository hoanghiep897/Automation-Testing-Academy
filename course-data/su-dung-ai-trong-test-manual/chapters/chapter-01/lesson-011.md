# Bài 11 - Update Requirements -> Update Test Cases -> Execute Test Cases -> Retest

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/363](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/363)

✅ Sử dụng Skills để thực hiện Cập nhật Requirements -> Cập nhật lại bộ Test Cases -> Chạy lại test

## 1. Khi Requirements đổi sau khi đã có Test Case

Ở bài trước bạn đã chạy trọn một vòng: review bộ Test Case, chạy trên browser thật, gom nhóm FAIL rồi viết bug report. Trước ngày 19/09/2026, bộ tài liệu của module Đăng nhập trên CRM demo đã đủ bốn tầng: **43 REQ → 50 TC → 1 execution report → 6 bug đang mở** — và còn đúng một điểm mờ chưa có câu trả lời.

Và đúng lúc đó, PO gửi một câu trả lời, hoặc dev báo một ticket vừa đổi luật. Ở bài **Chuẩn hoá Requirements và tạo Test Plan** bạn đã biết: sửa REQ *khi chưa có TC* thì không TC nào phải sửa theo. Bây giờ thì khác — mỗi REQ đổi kéo theo một chuỗi:

```none
REQ đổi  →  TC nào đang mô tả hành vi CŨ?  →  sửa đúng TC đó
         →  chạy lại phần bị ảnh hưởng     →  bug nào còn đúng, bug nào hết đúng?
```

Chỗ nguy hiểm nhất không nằm ở REQ, mà ở **Test Case stale** — TC mô tả rất đúng một hành vi *đã bị thay*. Nó không sai chính tả, không thiếu bước, không mơ hồ. Nó chỉ kiểm nhầm thứ:

<table class="rt-table">
<thead>
<tr>
<th>TC stale gặp hệ thống mới</th>
<th>Kết quả chạy</th>
<th>Hậu quả</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hệ thống đã làm đúng luật mới</td>
<td>❌ FAIL</td>
<td>Bạn log một bug giả. Dev mất thời gian điều tra, uy tín bảng báo cáo giảm</td>
</tr>
<tr>
<td>Hệ thống vẫn chạy theo luật cũ (dev chưa làm)</td>
<td>✅ PASS</td>
<td><strong>Tệ hơn nhiều</strong>: TC xanh trên một hệ thống chưa đạt yêu cầu mới — bug không bao giờ được mở</td>
</tr>
<tr>
<td>TC dựa trên một giả định tạm mà PO vừa bác bỏ</td>
<td>PASS hoặc FAIL, nhưng <strong>không chứng minh được gì</strong></td>
<td>Kết quả được đưa vào báo cáo go/no-go như thể là bằng chứng thật</td>
</tr>
</tbody>
</table>

Không lệnh review nào bắt được TC stale bằng cách đọc chính TC đó — vì bản thân TC không có lỗi. Muốn bắt nó, phải đi từ **thay đổi của Requirements** xuống. Đó là nội dung của bài này.

> 📌 Bài này **không** dạy lại cách chạy Test Case, cách viết bug report hay bốn trạng thái retest — bạn đã học ở bài trước. Ở đây chỉ nói những gì **khác đi** khi nguyên nhân chạy lại là *Requirements thay đổi*.

## 2. Bốn bước, bốn lệnh — chuỗi delta của Manual Tester

Trong [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md), phần này có tên **"Vòng lặp khi Requirements thay đổi"**, với lời dặn ngắn gọn: *đừng sinh lại từ đầu*. Bộ kit tách vòng lặp thành bốn bước, mỗi bước một lệnh, mỗi lệnh ghi ra một file làm đầu vào cho lệnh sau:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Bước</th>
<th>Lệnh</th>
<th>Đầu ra — và ai đọc nó tiếp</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>Update Requirements</td>
<td><code>/update-requirements-from-ticket</code></td>
<td>Tài liệu REQ sửa tại chỗ + <strong>Impact Report</strong> <code>docs/requirements/&lt;module&gt;/impact/impact_&lt;TICKET-ID&gt;.md</code> → bước 2 đọc</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>Update Test Cases</td>
<td><code>/update-testcases-from-impact</code></td>
<td>TC sửa tại chỗ + <strong>mốc git</strong> của bản cũ ghi vào Nhật ký + <strong>Delta TC List</strong> <code>docs/testcases/&lt;module&gt;/impact/delta_tc_&lt;TICKET-ID&gt;.md</code> → bước 3 biết chạy lại TC nào</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Execute Test Cases</td>
<td><code>/execute-test-cases</code> — phạm vi <strong>theo TC ID</strong></td>
<td>Execution report của một <code>run_id</code> mới → bước 4 biết bug nào cần xét lại</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Retest</td>
<td><code>/retest-fixed-bugs</code> (+ <code>/create-bug-report</code> nếu có lỗi mới)</td>
<td>Retest report + dòng mới trong <code>Lịch sử retest</code> của từng bug</td>
</tr>
</tbody>
</table>

Hai lệnh đầu là **chế độ delta**: chỉ chạm đúng phần đã đổi, giữ nguyên mọi mã. Hai lệnh sau bạn đã dùng ở bài trước — điểm mới là **chọn phạm vi** cho chúng, vì chạy lại cả module mỗi lần có ticket là không ai chịu nổi.

> ⚠️ Bộ kit có thêm lệnh thứ năm cùng chuỗi: `/update-automation-from-impact` — sửa script automation web · mobile · API của module **đã có automation**. Lệnh này **không** đọc Impact Report: đầu vào bắt buộc của nó là file `delta_tc_<TICKET-ID>.md` do bước 2 ghi ra. Chỉ có Impact Report mà chưa có file đó — tức TC chưa được đồng bộ — thì lệnh dừng. Lý do: TC còn mô tả hành vi cũ mà script đã đổi theo ticket thì hai bên lệch nhau, và suite vẫn xanh nên không ai phát hiện. Sửa script là việc của đội Automation; bạn chỉ cần biết **Delta TC List ở bước 2 chính là đầu vào của họ**, nên nó phải ghi đủ TC ID, đúng nền tảng.

### 2.1. Gọi lệnh trên Claude Code, Codex và Antigravity

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Claude Code</th>
<th>Codex</th>
<th>Antigravity <em>(phụ)</em></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Repo bộ kit</strong></td>
<td><a href="https://github.com/anhtester/claude-testing-skills">claude-testing-skills</a></td>
<td><a href="https://github.com/anhtester/codex-testing-skills">codex-testing-skills</a></td>
<td><a href="https://github.com/anhtester/antigravity-testing-skills">antigravity-testing-skills</a></td>
</tr>
<tr>
<td><strong>Bước 1</strong></td>
<td><code>/update-requirements-from-ticket</code></td>
<td><code>$update-requirements-from-ticket</code></td>
<td><code>/update-requirements-from-ticket</code></td>
</tr>
<tr>
<td><strong>Bước 2</strong></td>
<td><code>/update-testcases-from-impact</code></td>
<td><code>$update-testcases-from-impact</code></td>
<td><code>/update-testcases-from-impact</code></td>
</tr>
<tr>
<td><strong>Bước 3</strong></td>
<td><code>/execute-test-cases</code></td>
<td><code>$execute-test-cases</code></td>
<td><code>/execute-test-cases</code></td>
</tr>
<tr>
<td><strong>Bước 4</strong></td>
<td><code>/retest-fixed-bugs</code></td>
<td><code>$retest-fixed-bugs</code></td>
<td><code>/retest-fixed-bugs</code></td>
</tr>
<tr>
<td><strong>Skill nền tảng chính</strong></td>
<td><code>skills-requirements-analyzer</code><br/><code>skills-rbt-manual-testing</code> (mode DELTA)<br/><code>skills-manual-test-executor</code></td>
<td><code>requirements-analyzer</code><br/><code>rbt-manual-testing</code><br/><code>manual-test-executor</code></td>
<td><code>requirements_analyzer</code><br/><code>rbt_manual_testing</code><br/><code>manual_test_executor</code></td>
</tr>
</tbody>
</table>

Toàn bài viết theo cú pháp Claude Code. Dùng Codex thì thay `/` bằng `$`; Antigravity gõ y hệt Claude Code.

> 📌 AI Agent chưa có bộ kit riêng thì dùng prompt mẫu trong [prompts/](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/README.md): `prompt_21_update_requirements_from_ticket.txt` · `prompt_27_update_testcases_from_impact.txt` · `prompt_16_execute_test_cases.txt` · `prompt_23_retest_fixed_bugs.txt`.

## 3. Tình huống của module Đăng nhập

### Trường hợp 1 — SỬA đảo ngược nghĩa: khoá tài khoản (`REQ-LOGIN-41`)

**Bước 1: Cập nhật requirements**

```none
/update-requirements-from-ticket
Module: login
Thư mục test cases: docs/testcases/login/
Ticket: CRM-LOGIN-101 — Khoá tài khoản khi đăng nhập sai nhiều lần
Nội dung ticket (PO chốt ngày 28-09-2026):
- Đăng nhập sai mật khẩu 5 lần liên tiếp với cùng một email thì tài khoản bị khoá 15 phút.
- Khi bị khoá, trang đăng nhập hiển thị: "Your account is locked. Please try again in 15 minutes."
- Trong thời gian bị khoá, nhập đúng mật khẩu cũng không đăng nhập được.
- Đăng nhập thành công trước khi đủ 5 lần thì bộ đếm lần sai được đặt lại về 0.
- Chỉ khoá theo email, không khoá theo IP.
- Môi trường dùng chung: TC phải dùng tài khoản Project Manager, KHÔNG dùng tài khoản Admin.
```

> Kết quả mong đợi: `REQ-LOGIN-41` đổi sang 🟡 Changed và **giữ nguyên mã**, không cấp mã mới. Impact Report chỉ ra `CRM_LOGIN_TC_025` đã lỗi thời.

**Bước 2: Cập nhật test cases.** Chạy PLAN trước để học viên xem kế hoạch, rồi mới APPLY.

```none
/update-testcases-from-impact
Mode: PLAN
Impact Report: docs/requirements/login/impact/impact_CRM-LOGIN-101.md
```

```none
/update-testcases-from-impact
Mode: APPLY
Impact Report: docs/requirements/login/impact/impact_CRM-LOGIN-101.md
Tôi duyệt kế hoạch. Giữ nguyên TC ID CRM_LOGIN_TC_025, sửa tại chỗ.
```

**Bước 3: Thực thi**

```none
/execute-test-cases
File TC: docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md
Phạm vi: chỉ CRM_LOGIN_TC_025
URL và tài khoản: lấy từ .env (EMAIL_PM / PASSWORD_PM)
Môi trường dùng chung: CÓ
Build: demo-2026-09-28
```

> Kết quả mong đợi: ❌ **FAIL**, vì hệ thống hiện chưa khoá tài khoản.

**Bước 4: Mở bug**

```none
/create-bug-report
Từ TC FAIL CRM_LOGIN_TC_025 của lần chạy vừa rồi trong docs/executions/login/web/
Nền tảng: web. Không đẩy Jira.
```

**Bước 5: Retest**

```none
/retest-fixed-bugs
Mode: RETEST
Bug: docs/bugs/login/web/<file BUG_..._TC025 vừa tạo>.md
Build mới: demo-2026-10-05 (dev báo đã fix khoá tài khoản)
Tài khoản: .env (EMAIL_PM / PASSWORD_PM) · Môi trường dùng chung: CÓ
```

> Nếu server chưa được sửa thì kết quả là **NOT\_FIXED**. Nhân tiện có thể dạy chốt chặn của workflow: nếu nhập build **giống** build lúc log bug, workflow sẽ dừng lại.

---

### 

### Trường hợp 2

Trước ngày 19/09/2026, module Đăng nhập của CRM demo đã đóng 18/19 điểm mờ. Còn đúng **một** cái đang treo, và nó là ví dụ đẹp nhất để học chuỗi delta vì nó **đã có TC dựa vào**:

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Hiện trạng trong repo kit</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>REQ-LOGIN-42</code></td>
<td>Phiên đăng nhập hết hạn sau <strong>1 giờ</strong> — quyết định PO đợt <code>PO-2026-08-18-B</code></td>
</tr>
<tr>
<td><code>AMB-LOGIN-19</code> ❓ 🟡</td>
<td>1 giờ tính theo <strong>thời gian không hoạt động</strong> (mỗi thao tác gia hạn lại) hay theo <strong>tổng thời gian từ lúc đăng nhập</strong> (hết giờ là ra, dù đang dùng)?</td>
</tr>
<tr>
<td>Giả định tạm</td>
<td>Không hoạt động — ghi ở mục Giả định của bộ TC là <code>ASM-01</code></td>
</tr>
<tr>
<td><code>CRM_LOGIN_TC_026</code></td>
<td>Đăng nhập, để yên 65 phút, rồi mở <code>/admin/clients</code> → phải bị đưa về trang đăng nhập. Tag <code>@Slow</code>, <code>@AssumptionBased</code>. Chính TC này ghi chú: <em>nếu phiên tính theo tổng thời gian thì TC vẫn PASS nhưng không phân biệt được hai cách — cần TC bổ sung khi <code>AMB-LOGIN-19</code> được trả lời</em></td>
</tr>
<tr>
<td>Lần chạy <code>run_1787215085</code></td>
<td><code>TC_026</code> bị <strong>SKIPPED</strong> — không đủ 65 phút chờ trong phiên đó</td>
</tr>
</tbody>
</table>

Ngày 19/09/2026, PO trả lời qua chat: *"1 giờ tính theo thời gian không hoạt động — mỗi thao tác gia hạn lại"*. Câu trả lời **trùng** giả định tạm. Phản xạ tự nhiên là: *"Trùng rồi thì TC đang đúng, khỏi làm gì"*. Và đây chính là chỗ bài học nằm:

<table class="rt-table">
<thead>
<tr>
<th>Vì sao trùng giả định vẫn phải chạy delta</th>
<th>Chi tiết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>TC còn mang nhãn "dựa trên giả định"</strong></td>
<td><code>TC_026</code> vẫn gắn <code>@AssumptionBased</code> và cảnh báo <code>AMB-LOGIN-19</code> còn treo. Không gỡ thì báo cáo go/no-go vẫn xếp kết quả của nó vào loại "chưa chắc"</td>
</tr>
<tr>
<td><strong>REQ được viết lại thành 2 tiêu chí chấp nhận</strong></td>
<td><code>REQ-LOGIN-42</code> nay có <strong>AC1</strong> (để yên quá 1 giờ thì hết phiên) và <strong>AC2</strong> (đang thao tác thì không bị đăng xuất dù tổng thời gian đã quá 1 giờ). AC2 <strong>chưa có TC nào</strong></td>
</tr>
<tr>
<td><strong>TC cũ không phân biệt được hai cách tính</strong></td>
<td>Để yên 65 phút thì cách nào cũng hết phiên → <code>TC_026</code> PASS dưới cả hai luật. Chỉ một TC <strong>thao tác đều đặn</strong> mới bác bỏ được cách "tính từ lúc đăng nhập"</td>
</tr>
</tbody>
</table>

> 📌 **Toàn bộ đợt thay đổi này có thật trong repo kit**, bạn mở ra đối chiếu từng dòng được: Nhật ký thay đổi ngày 19-09-2026 trong [REQUIREMENTS\_LOGIN\_SUMMARY.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md) · kế hoạch [impact\_plan\_adhoc\_2026-09-19.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/impact/impact_plan_adhoc_2026-09-19.md) · kết quả [delta\_tc\_adhoc\_2026-09-19.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/impact/delta_tc_adhoc_2026-09-19.md) · bộ TC sau khi sửa [test\_cases\_login\_web.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/web/test_cases_login_web.md). Trạng thái **trước** đợt được git giữ ở mốc `05efd17` — bài tập 1 dùng mốc này để bạn tự chạy lại cả chuỗi.

## 4. Bước 1 — Update Requirements khi module đã có Test Case

Lệnh vẫn là `/update-requirements-from-ticket` mà bạn đã dùng để chốt điểm mờ ở bài Chuẩn hoá Requirements. Khác biệt nằm ở đầu vào số 3 — **thư mục Test Case**. Lúc chưa có TC, Impact Report ghi *"Không có TC nào phải sửa"*. Bây giờ, đưa thư mục TC vào là để lệnh tra ngược **chính xác TC nào đã stale**:

```none
/update-requirements-from-ticket
Module: login
Ticket: PO trả lời AMB-LOGIN-19 qua chat — "1 giờ tính theo thời gian không hoạt động, mỗi thao tác gia hạn lại"
Thư mục test cases: docs/testcases/login/
```

> 📌 **Không có mã ticket thì đặt mã gì?** Câu trả lời đến qua chat, không qua Jira. Bộ kit quy định mã `adhoc_<YYYY-MM-DD>` — đợt này là `adhoc_2026-09-19`. Mã này là **hậu tố chung** cho mọi file của đợt ở các tầng sau, nên phải chốt ngay từ bước 1.

### 4.1. Lệnh làm gì — và bạn phải soát chỗ nào

<table class="rt-table">
<thead>
<tr>
<th>Bước của lệnh</th>
<th>Bạn soát gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tóm tắt trạng thái hiện tại</strong> trước khi sửa</td>
<td>Con số phải khớp: <em>43 REQ, 1 ambiguity treo, mã kế tiếp <code>REQ-LOGIN-44</code></em>. Lệch là AI đang đọc nhầm file — dừng ngay</td>
</tr>
<tr>
<td><strong>Phân loại delta</strong> vào 5 nhóm: 🟢 Thêm · 🟡 Sửa · 🔴 Bỏ · ⚪ Chưa build · ⏸️ Trùng</td>
<td>Ca này phải là <strong>🟡 SỬA <code>REQ-LOGIN-42</code></strong> — cùng hành vi (hết phiên), khác tham số (cách tính giờ). Nếu AI xếp vào 🟢 THÊM và cấp <code>REQ-LOGIN-44</code> thì đó là <strong>lỗi nặng nhất</strong> của lệnh này: một hành vi có hai REQ, RTM đếm độ phủ sai từ đó về sau</td>
</tr>
<tr>
<td><strong>Đối chiếu với AMB đang treo</strong></td>
<td><code>AMB-LOGIN-19</code> ❓ → ✅. Dù kết luận <strong>trùng</strong> hay <strong>khác</strong> giả định tạm, mọi TC dựa trên giả định đó vẫn phải vào Impact Report — trùng thì gỡ nhãn giả định, khác thì sửa kỳ vọng. AI ghi <em>"trùng giả định, không TC nào phải sửa"</em> là sai</td>
</tr>
<tr>
<td><strong>Áp vào tài liệu</strong> — sửa tại chỗ</td>
<td>Giữ đúng 4 nơi khớp nhau: Nhật ký thay đổi ↔ trạng thái REQ ↔ dải mã ↔ danh mục <code>docs/requirements/README.md</code> (cột <code>AMB treo</code> về 0)</td>
</tr>
<tr>
<td><strong>Ghi Impact Report ra file</strong></td>
<td>Phải có file, không chỉ nằm trong chat — xem 4.2</td>
</tr>
</tbody>
</table>

### 4.2. Impact Report — tờ giấy bàn giao duy nhất sang tầng Test Case

Với đợt `adhoc_2026-09-19`, phần quan trọng nhất của Impact Report trông như sau:

```none
## Impact Report — adhoc_2026-09-19 · Module LOGIN

### Tóm tắt
| Nhóm       | Số lượng | REQ          |
|------------|----------|--------------|
| 🟡 Sửa     | 1        | REQ-LOGIN-42 |

### Test case cần xử lý
| TC ID            | REQ liên quan | Hành động       | Lý do                                                  |
|------------------|---------------|-----------------|--------------------------------------------------------|
| CRM_LOGIN_TC_026 | REQ-LOGIN-42  | ⚠️ Review & sửa | Gắn @AssumptionBased — giả định nay đã được PO chốt    |
| —                | REQ-LOGIN-42  | ➕ Viết mới      | AC2 "đang thao tác thì được gia hạn" chưa có TC nào    |

### Ambiguity
| Mã            | Chuyển trạng thái | Ghi chú                                        |
|---------------|-------------------|------------------------------------------------|
| AMB-LOGIN-19  | ❓ → ✅            | TRÙNG giả định tạm — thời gian không hoạt động |
```

> 📌 Mã điểm mờ giờ mang tên module: `AMB-LOGIN-19`, không còn là `AMB-19` trần như tài liệu cũ. Hai module tự đánh số `AMB-15` là một mã hai câu hỏi; có prefix thì grep ra đúng một nghĩa.

Lệnh ghi rõ lý do bắt buộc ra file: Impact Report là đầu vào của `/update-testcases-from-impact`, mà lệnh đó **thường chạy ở phiên khác, có khi hôm sau**. Đóng phiên là mất, và không có cách dựng lại ngoài chạy lại cả lệnh.

> 💡 **Vì sao Impact Report tìm được `TC_026` mà không phải đoán?** Vì cột `REQ ID` bạn giữ từ bài phân tích Requirements. Lệnh tra theo thứ tự: cột `REQ ID` trong file TC → RTM → không có nguồn nào thì ghi `⚠️ chưa rà soát` và yêu cầu chạy `/generate-traceability-matrix` trước. Bộ TC thiếu cột `REQ ID` thì tới bước này bạn chỉ còn cách mò bằng tên TC.

## 5. Bước 2 — Update Test Cases theo Impact Report

### 5.1. Cái bẫy đầu tiên: dùng nhầm `/review-testcases`

Phản xạ rất tự nhiên: *"TC cần sửa thì chạy lệnh review mode FIX"*. Bộ kit cấm đúng phản xạ này, và lý do đáng nhớ:

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th><code>/update-testcases-from-impact</code></th>
<th><code>/review-testcases</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Trả lời câu hỏi</strong></td>
<td>TC còn khớp requirement <strong>mới</strong> không?</td>
<td>TC viết có đạt chuẩn không?</td>
</tr>
<tr>
<td><strong>Đầu vào</strong></td>
<td>Impact Report + REQ đã đổi</td>
<td>Bộ TC</td>
</tr>
<tr>
<td><strong>Bỏ sót</strong></td>
<td>Chất lượng câu chữ của TC</td>
<td><strong>TC stale</strong> — <code>TC_026</code> viết rất tốt về hành vi cũ vẫn đạt 12/12 điểm rubric</td>
</tr>
<tr>
<td><strong>Ghi ra đâu</strong></td>
<td>Sửa <strong>tại chỗ</strong>, ghi mốc git của bản cũ</td>
<td>Cũng sửa tại chỗ — nhưng chỉ các TC bạn duyệt sau khi chấm rubric</td>
</tr>
<tr>
<td><strong>Đầu ra cho automation</strong></td>
<td>File <code>delta_tc_&lt;TICKET-ID&gt;.md</code></td>
<td><strong>Không có</strong> — đội Automation không biết script nào phải sửa</td>
</tr>
</tbody>
</table>

Thứ tự đúng: **đồng bộ nội dung bằng delta trước, chấm chất lượng bằng review sau**.

> 📌 **Câu hỏi để chọn đúng lệnh: REQ có đổi không?** Cùng ngày 19/09 trong repo kit có hai TC được sửa, đi hai đường khác nhau:
>
> - `TC_026` — `REQ-LOGIN-42` **vừa đổi** theo quyết định PO → đi **delta** (bài này).
> - `TC_018` biến thể `a` — kỳ vọng sai so với ranh giới 64 ký tự **đã có trong REQ** từ đợt recon 11/09, REQ không đổi gì → đây là **TC viết sai**, sửa bằng `/review-testcases` mode FIX, và bug [BUG\_login\_1787226515\_TC018](https://github.com/anhtester/claude-testing-skills/blob/main/docs/bugs/login/web/BUG_login_1787226515_TC018.md) đóng với trạng thái *không phải lỗi*.
>
> Dùng nhầm theo chiều nào cũng hỏng: review cho TC stale thì không có Delta TC List; delta cho TC viết sai thì bịa ra một "thay đổi requirements" chưa từng xảy ra.

### 5.2. PLAN trước, APPLY sau

Lệnh có hai mode. Mặc định là **PLAN** — chỉ ghi kế hoạch ra `docs/testcases/login/impact/impact_plan_<TICKET-ID>.md` rồi dừng. Nói *"sửa luôn"* thì thành **APPLY**, nhưng lệnh vẫn dừng ở checkpoint xin duyệt trước khi động vào file.

```none
/update-testcases-from-impact
Mode: PLAN
Impact Report: docs/requirements/login/impact/impact_<TICKET-ID>.md
```

Lệnh cũng nhận **danh sách REQ đã đổi** thay cho Impact Report — đợt `adhoc_2026-09-19` trong repo đi đường này: nguồn thay đổi là dòng Nhật ký ngày 19-09-2026 của `REQUIREMENTS_LOGIN_SUMMARY.md`, không có file `impact_` riêng. Làm được, nhưng đổi lại không còn tờ giấy bàn giao ở mục 4.2: người làm bước 2 ở phiên khác phải tự đọc Nhật ký để biết TC nào bị chạm. Ở checkpoint, bạn soát kỹ ba nhóm mà lệnh đánh dấu phải xác nhận: **mapping suy luận** (TC nối với REQ bằng cách so mô tả, không bằng cột `REQ ID`) · **TC chuyển Deprecated** · **danh sách nhánh 4 vòng bị chạm**. Kế hoạch đã được duyệt của đợt này:

<table class="rt-table">
<thead>
<tr>
<th>TC</th>
<th>Hành động</th>
<th>Sửa gì — và vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CRM_LOGIN_TC_026</code></td>
<td>✏️ Sửa</td>
<td>Kỳ vọng <em>"để yên 65 phút thì hết phiên"</em> <strong>vẫn đúng</strong>, nên <strong>không</strong> Deprecated. Chỉ sửa đúng phần giả định: bỏ tag <code>@AssumptionBased</code>, thay đoạn cảnh báo <code>AMB-LOGIN-19</code> trong Expected bằng một câu trỏ sang <code>TC_051</code>. <strong>Steps, Test Data, Pre-Condition giữ nguyên</strong></td>
</tr>
<tr>
<td><code>CRM_LOGIN_TC_051</code></td>
<td>➕ Mới</td>
<td><em>"Đang thao tác thì phiên được gia hạn — không bị đăng xuất dù đã quá 1 giờ kể từ lúc đăng nhập"</em>: đăng nhập lúc T0, bấm menu ở T0+30 và T0+55 phút, kiểm ở T0+70 → vẫn ở trang nội bộ. Đây là TC <strong>duy nhất bác bỏ được</strong> cách "tính từ lúc đăng nhập": nếu hệ thống tính kiểu đó thì bước cuối bị đăng xuất → FAIL. Mã <code>051</code> là mã <strong>kế tiếp dải hiện có</strong>, không chèn vào giữa</td>
</tr>
</tbody>
</table>

> 💡 **Vì sao `TC_051` là TC mới, không phải biến thể `b` của `TC_026`?** Bộ TC viết ở độ hạt GỘP, nhưng hai vế này cho **khác loại phản hồi** (một bên bị đăng xuất, một bên giữ phiên) và **khác chuỗi thao tác** (để yên với thao tác định kỳ) — đúng trường hợp **cấm gộp**. Kế hoạch thật ghi rõ lý do này; bạn soát kế hoạch cũng phải hỏi đúng câu đó.

> ⚠️ `TC_051` được lệnh này sinh vì nó nằm **trong phạm vi một REQ 🟡** (TC negative/boundary bổ sung cho REQ vừa sửa). Còn REQ **🟢 mới hoàn toàn** thì lệnh **không** tự viết TC — nó chuyển sang `/generate-testcases-manual-rbt`. Ranh giới này giữ cho chế độ delta không phình thành "sinh lại cả module".

### 5.3. Năm luật bất biến của chế độ delta

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Vì sao — và vi phạm thì hỏng cái gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Không đổi TC ID, không đánh lại từ 001</strong></td>
<td>TC ID là khoá nối sang execution report, bug report, RTM và script automation. <code>TC_026</code> đổi số là 1 execution report + RTM + nhãn <code>testId</code> của đội Automation cùng gãy</td>
</tr>
<tr>
<td><strong>Không xoá dòng TC</strong></td>
<td>Chức năng bị gỡ thì gắn tag <code>@Deprecated</code> ở cột <code>Tags</code> <strong>và</strong> tiền tố <code>🗑️ Deprecated (&lt;TICKET-ID&gt;, &lt;ngày&gt;) —</code> ở đầu ô <code>Test Scenario</code>. Bảng TC không có cột trạng thái, nên tag là thứ <code>/execute-test-cases</code> và RTM lọc theo. Đối xứng với luật "không xoá dòng REQ" ở tầng trên</td>
</tr>
<tr>
<td><strong>Không sinh <code>_improved</code> / <code>_v2</code> / <code>_new</code>, không có <code>archive/</code></strong></td>
<td>Tên file TC là bất biến. Hai file TC song song — kể cả bản cũ nằm trong <code>archive/</code> — là grep một TC ID ra hai kết quả, không ai biết bản nào có hiệu lực</td>
</tr>
<tr>
<td><strong>Ghi mốc git trước khi sửa</strong></td>
<td>Với từng file sắp sửa: có thay đổi chưa commit → lệnh <strong>dừng</strong>, đề nghị bạn commit trước; sạch thì ghi hash commit gần nhất vào Nhật ký và vào <code>delta_tc_</code>. Đợt này ghi mốc <code>05efd17</code> — xem lại bản cũ bằng <code>git show 05efd17:docs/testcases/login/test_cases_login.md</code> (lúc đó file còn tên cũ)</td>
</tr>
<tr>
<td><strong>Bám đúng độ hạt đang có</strong></td>
<td>Bộ TC Đăng nhập viết ở độ hạt GỘP (trước đợt: 50 TC · 70 biến thể). TC mới cũng theo luật GỘP — và luật đó cũng nói khi nào <strong>cấm</strong> gộp, như <code>TC_051</code>. Đổi độ hạt trong chế độ delta = đánh lại toàn bộ TC ID — bị cấm</td>
</tr>
</tbody>
</table>

### 5.4. Tác động lan toả — một câu trả lời của PO chạm sáu chỗ

Impact Report chỉ liệt kê **TC map trực tiếp** với REQ. Nhưng file TC còn các bảng tổng hợp nhắc tới chính những TC đó. Với `AMB-LOGIN-19`, sửa xong `TC_026` và thêm `TC_051` là **chưa xong** — kế hoạch thật liệt kê thêm năm chỗ nữa trong file TC:

<table class="rt-table">
<thead>
<tr>
<th>Chỗ trong file TC</th>
<th>Hiện đang ghi</th>
<th>Sau khi đồng bộ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bảng TC</td>
<td><code>TC_026</code> gắn giả định</td>
<td><code>TC_026</code> sửa · <code>TC_051</code> mới</td>
</tr>
<tr>
<td>Mục Giả định — <code>ASM-01</code></td>
<td>Tạm hiểu là thời gian không hoạt động</td>
<td>✅ Đã giải quyết 19-09-2026 — giả định trùng quyết định PO. <strong>Giữ dòng</strong>, không xoá, để lần chạy cũ vẫn truy được</td>
</tr>
<tr>
<td>Bảng Đối Soát Coverage — dòng <code>REQ-LOGIN-42</code></td>
<td>1 TC · <em>giới hạn bởi <code>AMB-LOGIN-19</code></em></td>
<td>2 TC · <code>TC_026</code> cho AC1, <code>TC_051</code> cho AC2</td>
</tr>
<tr>
<td>Bảng đối soát 4 vòng — <code>V3 · Security</code></td>
<td>8 TC</td>
<td>9 TC — thêm <code>TC_051</code>. Tiêu đề file, dải TC ID và mã kế tiếp (<code>052</code>) sửa theo</td>
</tr>
<tr>
<td>Bảng ISO/IEC 25010 — <code>Reliability</code></td>
<td><code>TC_026</code> (hết hạn phiên)</td>
<td>Thêm <code>TC_051</code></td>
</tr>
<tr>
<td>Bộ chạy đề xuất — <code>@Slow</code></td>
<td>1 TC · ~65 phút</td>
<td>2 TC · ~65 + ~70 phút</td>
</tr>
</tbody>
</table>

Dòng cuối là dòng hay bị quên nhất và lại **ảnh hưởng trực tiếp tới lịch**: bộ chạy riêng tăng hơn gấp đôi thời gian. Người lập kế hoạch đợt kiểm thử cần biết điều đó trước khi xếp lịch, không phải sau.

> 📌 Đợt này còn kéo theo một việc **cấu trúc**: đây là lần đầu một lệnh sinh/cập nhật chạm lại module Đăng nhập kể từ khi kit có tầng nền tảng, nên bộ TC được chuyển **một lần** sang `web/test_cases_login_web.md`, file cũ thành index (nay là `TEST_CASES_LOGIN_SUMMARY.md`). Mã TC giữ nguyên, việc chuyển được ghi vào Nhật ký. Kit cố ý không bắt chuyển hàng loạt khi chỉ đọc — chỉ chuyển khi đằng nào cũng phải sửa.

> ⚠️ Lệnh có một câu hỏi lan toả mà bạn nên thuộc lòng: **ticket có đụng thứ nhìn thấy được trên màn hình không** — thêm/bớt field, đổi nhãn, đổi thứ tự, đổi giá trị mặc định? Có thì TC `UI cơ bản` ở **Vòng 1** phải sửa, không chỉ TC validation ở Vòng 2. Bốn nhóm đó còn **bắt buộc mở evidence** trước khi sửa; chưa có ảnh màn hình mới thì gắn `@NeedsVerify`, không sửa theo suy đoán.

### 5.5. Hai đầu ra phải có khi APPLY xong

**Nhật ký thay đổi** ở cuối file index — mỗi đợt một dòng: ngày, nguồn, TC nào đổi gì, và **mốc git trước khi sửa**. Bạn thêm lên đầu, không viết đè.

**Delta TC List** — **ghi ra file** `docs/testcases/login/impact/delta_tc_adhoc_2026-09-19.md`, là đầu vào cho bước 3 của bạn và cho đội Automation. Chat chỉ hiện tóm tắt theo nền tảng kèm đường dẫn file. Rút gọn từ [file thật](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/impact/delta_tc_adhoc_2026-09-19.md):

```none
# Delta TC List — adhoc_2026-09-19 · module LOGIN

| Mục                   | Giá trị                                              |
|-----------------------|------------------------------------------------------|
| Mã delta              | adhoc_2026-09-19 — PO trả lời qua chat (AMB-LOGIN-19) |
| Kế hoạch đã duyệt     | impact_plan_adhoc_2026-09-19.md                      |
| Mốc git trước khi sửa | web → @ 05efd17                                      |
| Trạng thái            | ✅ ĐÃ ĐỒNG BỘ                                         |

## TC đã xử lý

| TC ID            | Nền tảng | Vòng · Nhánh  | Hành động | Đổi cái gì (cho automation)                         |
|------------------|----------|---------------|-----------|-----------------------------------------------------|
| CRM_LOGIN_TC_026 | web      | V3 · Security | ✏️ Đã sửa | Gỡ @AssumptionBased. Automation Partial → No,       |
|                  |          |               |           | thêm @PersonalOnly → không viết script              |
| CRM_LOGIN_TC_051 | web      | V3 · Security | ➕ Mới     | Vế gia hạn phiên của REQ-LOGIN-42. Automation = No, |
|                  |          |               |           | @PersonalOnly → không viết script                   |
```

> 💡 Để ý cột cuối: cả hai TC đều `Automation = No` — người dùng quyết định QA tự chạy và theo dõi hai TC chờ hơn một tiếng này — nên file ghi rõ *"không có việc cho `/update-automation-from-impact`"*. Một Delta TC List tốt không chỉ nói **sửa gì**, mà còn nói **phía sau không cần làm gì**, để đội Automation khỏi phải tự đoán.

Bốn luật của file này — mỗi luật chặn đúng một kiểu hỏng ở phía sau:

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Phải là file</strong>, không chỉ nằm trong chat</td>
<td>Bước 3 và đội Automation thường làm ở phiên khác, có khi hôm sau, có khi do người khác làm. Đóng phiên là mất đầu vào</td>
</tr>
<tr>
<td>Chỉ ghi ở mode <strong>APPLY</strong>, sau khi TC đã sửa xong</td>
<td><code>impact_plan_</code> là kế hoạch, có thể bị bạn gạch bớt lúc duyệt. Phía sau chỉ được đọc thứ <strong>đã thật sự sửa</strong></td>
</tr>
<tr>
<td>Bắt buộc cột <strong>Nền tảng</strong>: <code>web</code> · <code>mobile · @Android</code> / <code>@iOS</code> · <code>api</code></td>
<td>TC ID đánh chung cả module, nhìn mã không biết TC thuộc web, app hay API. Thiếu cột này thì đội Automation không biết sửa ở project nào, chạy lại trên Android hay iOS. Bộ TC Đăng nhập của CRM demo hiện chỉ có web</td>
</tr>
<tr>
<td>TC chưa sửa được vì thiếu evidence <strong>vẫn ghi</strong>, hành động <code>⏸️ @NeedsVerify — chưa sửa</code></td>
<td>Bỏ dòng đi thì phía sau tưởng TC không bị ảnh hưởng. Ghi rõ để họ biết mà <strong>không chạm</strong> vào script của TC đó</td>
</tr>
</tbody>
</table>

> 📌 Mọi file của một ticket dùng **chung một hậu tố**: `impact_TICKET-123.md` → `impact_plan_TICKET-123.md` → `delta_tc_TICKET-123.md` → `automation_plan_TICKET-123.md`. Không có ticket thì hậu tố là `adhoc_<YYYY-MM-DD>` như đợt này. Một mã tra ra đủ các tầng. Chạy APPLY lại cho cùng ticket (ví dụ sau khi có ảnh cho TC `⏸️`) thì sửa tại chỗ file cũ và thêm dòng Nhật ký — không tạo `delta_tc_TICKET-123_v2.md`.

Rồi mới chạy `/review-testcases` lên đúng hai TC vừa sửa/thêm — lúc này rubric chất lượng mới có ý nghĩa.

## 6. Bước 3 — Execute lại: chạy đúng phần bị ảnh hưởng

`/execute-test-cases` bắt buộc có đầu vào **Phạm vi chạy** — không có thì agent hỏi, không tự chạy hết. Sau một đợt delta, phạm vi nên đi theo ba vòng lan dần ra:

<table class="rt-table">
<thead>
<tr>
<th>Vòng</th>
<th>Chọn gì</th>
<th>Ca <code>AMB-LOGIN-19</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Delta</strong> — bắt buộc</td>
<td>Mọi TC trong Delta TC List (✏️ và ➕)</td>
<td><code>TC_026</code>, <code>TC_051</code> — cả hai gắn <code>@PersonalOnly</code>, xem 6.1</td>
</tr>
<tr>
<td><strong>2. Cùng REQ / cùng Story</strong></td>
<td>TC map về REQ vừa đổi và các REQ cùng Story</td>
<td><code>STORY-LOGIN-04</code> "Bảo vệ phiên &amp; điều hướng" gồm <code>REQ-LOGIN-17</code> → <code>22</code>, <code>42</code> và <code>44</code> — tra cột <code>REQ ID</code> để ra danh sách TC</td>
</tr>
<tr>
<td><strong>3. Luồng dùng chung</strong></td>
<td>Chỉ mở khi thay đổi đụng thành phần dùng chung</td>
<td>Cơ chế phiên dùng chung cho <strong>mọi</strong> module sau đăng nhập — nhưng đây là thay đổi <em>tài liệu</em>, hệ thống chưa đổi gì → không mở vòng 3</td>
</tr>
</tbody>
</table>

Cách chọn theo vòng này **mượn từ `/retest-fixed-bugs`** (bước chọn phạm vi regression, trần mặc định 15 TC). `/execute-test-cases` không tự chọn phạm vi cho bạn — nó nhận phạm vi theo tag, theo nhóm hoặc theo TC ID mà bạn đưa vào. Vượt trần thì chạy cả module cho gọn, đừng nhét hết vào một lượt "chạy lại một ít".

```none
/execute-test-cases
File TC: docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md
Phạm vi: TC của STORY-LOGIN-04
Môi trường dùng chung: Có
```

Đưa file index là đủ — lệnh đọc mục `Bản đồ tài liệu` rồi tự sang file nền tảng `web/test_cases_login_web.md`.

### 6.1. Ba điều khác đi khi chạy lại sau delta

**Một — mỗi lần chạy một `run_id` mới, không ghi đè lần cũ.** Kết quả `TC_026` trong `run_1787215085` là của **phiên bản TC cũ**. Hai lần chạy nằm cạnh nhau thì người đọc biết TC đã đổi giữa hai lần; ghi đè là xoá bằng chứng.

**Hai — TC trong delta không được lặng lẽ SKIPPED lần nữa.** Ở lần chạy 20/08, `TC_026` đã SKIPPED vì thiếu thời gian. Sau đợt delta, đây lại chính là TC bị ảnh hưởng. Nếu tiếp tục SKIPPED thì `REQ-LOGIN-42` đi tới cuối đợt mà **chưa có một lần kiểm nào** — và nhớ luật từ bài trước: SKIPPED không nằm trong mẫu số pass rate, nên báo cáo trông vẫn đẹp.

Đợt thật xử lý bằng tag `@PersonalOnly`: `/execute-test-cases` loại hai TC này khỏi phạm vi của agent, **QA tự chạy** rồi đưa kết quả vào report — `TC_026` và `TC_051` đều PASS, ghi trong [run\_1789759574](https://github.com/anhtester/claude-testing-skills/blob/main/docs/executions/login/web/run_1789759574/execution_report.md) ngày 19/09.

> ⚠️ `@PersonalOnly` **không có nghĩa là bỏ** — nó chỉ đổi **người chạy**. Gắn tag rồi không ai chạy, không ghi kết quả vào report nào, thì bạn vừa dựng lại đúng cái lỗ SKIPPED ở trên bằng một tên khác.

**Ba — vẫn là TC làm chuẩn.** TC vừa sửa mà chạy ra FAIL thì ghi FAIL. **Không** quay lại sửa TC cho khớp — bạn vừa đồng bộ TC với REQ mới xong, lệch lúc này là hệ thống chưa đạt luật mới. Nếu `TC_051` FAIL (bị đăng xuất dù đang thao tác), đó là **bug mới** của `REQ-LOGIN-42` AC2, không phải lý do để sửa lại TC.

## 7. Bước 4 — Retest khi Requirements đã đổi

### 7.1. Ba loại "chạy lại" — đừng gọi chung một tên

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Nguyên nhân</th>
<th>Lệnh</th>
<th>Chuẩn chấm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Chạy lại TC đã sửa</strong></td>
<td>Requirements đổi → TC đổi</td>
<td><code>/execute-test-cases</code> (mục 6)</td>
<td>Expected của <strong>TC mới</strong></td>
</tr>
<tr>
<td><strong>Retest bug</strong></td>
<td>Dev báo đã fix</td>
<td><code>/retest-fixed-bugs</code></td>
<td>Expected trong <strong>bug report gốc</strong></td>
</tr>
<tr>
<td><strong>Regression</strong></td>
<td>Một thay đổi code có thể làm hỏng chỗ khác</td>
<td>Mode FULL của <code>/retest-fixed-bugs</code>, hoặc chạy cả module</td>
<td>Expected của các TC xung quanh</td>
</tr>
</tbody>
</table>

Cột cuối là lý do phải tách: `/retest-fixed-bugs` chấm theo **Expected của bug gốc** và cấm sửa bug gốc. Vậy nếu chính Expected đó vừa bị REQ mới vô hiệu thì sao? Chạy retest lúc này là chấm một bug theo một luật không còn tồn tại.

### 7.2. Xét lại bug trước khi retest

Sau mỗi đợt delta, mở danh mục `docs/bugs/README.md`, lọc các bug có `REQ ID` hoặc `TC ID` nằm trong Impact Report, rồi xếp mỗi bug vào đúng một trong ba ô:

<table class="rt-table">
<thead>
<tr>
<th>Tình huống</th>
<th>Xử lý</th>
<th>Không được làm</th>
</tr>
</thead>
<tbody>
<tr>
<td>REQ đổi nhưng <strong>Expected của bug vẫn đúng</strong></td>
<td>Giữ bug mở. Dev fix xong thì retest như bình thường</td>
<td>—</td>
</tr>
<tr>
<td>REQ mới <strong>chấp nhận hành vi</strong> mà bug đã báo</td>
<td>Chuyển trạng thái đóng, ghi một dòng vào <code>Lịch sử retest</code>: <em>không còn là lỗi — REQ đổi theo &lt;mã đợt&gt;</em>. Cập nhật danh mục</td>
<td>Chạy <code>/retest-fixed-bugs</code> rồi chấm FIXED — dev không sửa gì cả. Sửa Expected trong bug gốc cho khớp</td>
</tr>
<tr>
<td>REQ mới đặt <strong>kỳ vọng khác</strong> và hệ thống chưa đạt</td>
<td>Bug cũ đóng như ô trên; hành vi lệch luật mới là <strong>bug mới</strong> qua <code>/create-bug-report</code>, trỏ về TC/REQ đang có hiệu lực</td>
<td>Mở lại bug cũ rồi sửa nội dung — mất dấu vết bug cũ báo cái gì</td>
</tr>
</tbody>
</table>

**Ví dụ thật cho ô đầu** xảy ra cùng ngày 19/09. PO trả lời điểm mờ `AMB-LOGIN-20`: truy cập qua `http://` **bắt buộc** tự chuyển sang `https://`. Kết quả là một REQ 🟢 mới — `REQ-LOGIN-44`. Đo lại cùng ngày, hệ thống **chưa đạt**, nên bug `BUG_login_1785678750_TC039` (Critical/P1) **giữ nguyên trạng thái đang mở**. Thứ duy nhất đổi là cột REQ của `TC_039`: từ `REQ-LOGIN-01` (REQ đó không nói gì về HTTPS — truy vết nhầm) sang `REQ-LOGIN-44`. Trước đợt này, dev có thể phản bác bug vì không REQ nào ràng buộc; giờ thì bug có REQ chống lưng.

**Ô giữa** chưa có ca thật, nhưng bug `BUG_login_1787226513_TC004` (bấm logo không về trang chủ công khai) tự nêu khả năng này: *có thể là thiết kế có chủ đích — nếu vậy thì sửa `REQ-LOGIN-04`*. Nếu PO xác nhận như thế, chuỗi đúng để đóng bug là:

```none
PO xác nhận: root URL chuyển sang cổng khách hàng là thiết kế có chủ đích
   ↓  /update-requirements-from-ticket   → REQ-LOGIN-04 🟡 + Impact Report
   ↓  /update-testcases-from-impact      → TC_004 sửa Expected + delta_tc_
   ↓  /execute-test-cases (TC_004)       → PASS trên hệ thống hiện tại
   ↓  bug TC004: đóng, Lịch sử retest ghi "không còn là lỗi — REQ đổi theo <mã đợt>"
```

Đảo thứ tự — đóng bug trước rồi tính sau — là để REQ, TC và bug nói ba điều khác nhau về cùng một hành vi.

> 📌 Bug `TC018` cũng đóng ngày 19/09, nhưng **không thuộc bảng này**: không REQ nào đổi. Ranh giới 64 ký tự đã có trong REQ từ đợt recon 11/09 — chính bug report mới là thứ kỳ vọng sai. Nó đóng với trạng thái *không phải lỗi*, và `TC_018` được sửa qua `/review-testcases` (mục 5.1). Bảng 7.2 chỉ dành cho bug bị chạm bởi một **thay đổi requirements**.

> 🚫 **Đừng đi đường tắt ngược lại:** thấy TC FAIL liên tục ở một chỗ "có vẻ không quan trọng" rồi tự sửa Expected cho xanh. Chỉ **quyết định của PO** ghi vào Requirements mới được đổi kỳ vọng. Tester tự sửa kỳ vọng cho khớp hệ thống là tự tay xoá một bug — đúng luật "hiện trạng là lỗi thì REQ đổi phe" bạn đã học ở bài Chuẩn hoá Requirements, chỉ là theo chiều ngược lại.

### 7.3. Khi ticket đến từ dev, không phải từ PO

Ca `AMB-LOGIN-19` chỉ đổi tài liệu — hệ thống không đổi dòng code nào, nên không có regression thật. Ticket kiểu *"sprint này đổi luật phiên thành 1 giờ tính từ lúc đăng nhập"* thì khác: **code đã đổi**. Khi đó:

- Bước 1–2 giữ nguyên.
- Bước 3 phải chạy trên **build mới**, và vòng 3 (luồng dùng chung) **được mở** — cơ chế phiên đụng mọi module sau đăng nhập.
- Bug đang mở trong vùng code đó (dù không liên quan REQ đổi) nên retest luôn ở mode FULL: bản build mới có thể đã vô tình sửa, hoặc làm hỏng thêm.

## 8. Sau một vòng delta — chuỗi truy vết phải còn nguyên

Bài trước bạn dựng chuỗi truy vết bốn mắt xích. Một vòng delta chạm cả bốn, và mỗi tầng có một chỗ ghi lại **đã đổi gì**:

<table class="rt-table">
<thead>
<tr>
<th>Tầng</th>
<th>Chỗ ghi thay đổi</th>
<th>Kiểm gì sau đợt delta</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>requirements</strong></td>
<td>Nhật ký thay đổi — cột <code>TC cần xử lý</code> · file <code>impact/</code></td>
<td>Cột <code>TC cần xử lý</code> là <strong>mắt xích cảnh báo duy nhất</strong> cho tester biết TC nào đã lỗi thời — bỏ qua nó là chạy test trên bộ TC sai mà không biết</td>
</tr>
<tr>
<td><strong>testcases</strong></td>
<td>Nhật ký thay đổi (kèm mốc git) · <code>impact/impact_plan_*.md</code> · <code>impact/delta_tc_*.md</code></td>
<td>Mọi TC ID cũ còn nguyên · danh mục <code>docs/testcases/README.md</code> cập nhật số TC</td>
</tr>
<tr>
<td><strong>executions</strong></td>
<td><code>run_id</code> mới, lần chạy cũ giữ nguyên</td>
<td>Report ghi rõ phạm vi là chạy lại sau đợt delta nào</td>
</tr>
<tr>
<td><strong>bugs</strong></td>
<td><code>Lịch sử retest</code> trong từng bug · danh mục</td>
<td>Không bug nào còn trỏ vào Expected đã bị REQ mới vô hiệu</td>
</tr>
</tbody>
</table>

Cuối cùng chạy lại `/generate-traceability-matrix` để ma trận khớp với REQ và TC mới. Một ticket để lại tới bốn file cùng hậu tố — đừng nhầm vai của chúng:

<table class="rt-table">
<thead>
<tr>
<th>File</th>
<th>Loại</th>
<th>Nói gì</th>
<th>Ai đọc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>requirements/&lt;module&gt;/impact/impact_&lt;TICKET&gt;.md</code></td>
<td><strong>Báo cáo</strong></td>
<td>Cái gì đã đổi</td>
<td>Bước 2</td>
</tr>
<tr>
<td><code>testcases/&lt;module&gt;/impact/impact_plan_&lt;TICKET&gt;.md</code></td>
<td><strong>Kế hoạch</strong> — trước khi duyệt</td>
<td>Sẽ sửa TC nào, sửa gì</td>
<td>Bạn duyệt</td>
</tr>
<tr>
<td><code>testcases/&lt;module&gt;/impact/delta_tc_&lt;TICKET&gt;.md</code></td>
<td><strong>Kết quả</strong> — sau khi áp</td>
<td>Đã sửa TC nào, ở nền tảng nào</td>
<td>Bước 3 · <code>/update-automation-from-impact</code></td>
</tr>
<tr>
<td><code>testcases/&lt;module&gt;/impact/automation_plan_&lt;TICKET&gt;.md</code></td>
<td>Kế hoạch + kết quả tầng automation</td>
<td>Script nào đã sửa</td>
<td>Do đội Automation ghi</td>
</tr>
</tbody>
</table>

## 9. Nghiệm thu một vòng delta

### 9.1. Checklist

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Kiểm</th>
<th>Hỏng thì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>REQ đổi được xếp đúng nhóm — không có REQ mới nào mô tả lại hành vi đã có mã</td>
<td>RTM đếm độ phủ sai vĩnh viễn</td>
</tr>
<tr>
<td>2</td>
<td>Impact Report nằm trong file, không chỉ trong chat</td>
<td>Phiên sau không có đầu vào cho bước 2</td>
</tr>
<tr>
<td>3</td>
<td>Delta TC List nằm trong file <code>delta_tc_&lt;TICKET-ID&gt;.md</code>, có cột <strong>Nền tảng</strong> và đủ dòng <code>⏸️</code> của TC chưa sửa được</td>
<td>Bước 3 không biết chạy lại TC nào; đội Automation dừng vì thiếu đầu vào, hoặc sửa nhầm script</td>
</tr>
<tr>
<td>4</td>
<td>Mọi TC ID giữ nguyên · không dòng TC nào bị xoá · không có file <code>_improved</code> / <code>_v2</code> hay thư mục <code>archive/</code> · Nhật ký có mốc git</td>
<td>Gãy truy vết sang execution, bug, automation</td>
</tr>
<tr>
<td>5</td>
<td>Đã sửa đủ các bảng tổng hợp (Giả định · Coverage · 4 vòng · ISO · Bộ chạy)</td>
<td>File TC tự mâu thuẫn — bảng nói một đằng, TC nói một nẻo</td>
</tr>
<tr>
<td>6</td>
<td>Mọi TC trong Delta TC List đã có kết quả trên <code>run_id</code> mới — kể cả TC <code>@Slow</code>, và TC <code>@PersonalOnly</code> do QA tự chạy</td>
<td>REQ vừa đổi đi tới cuối đợt mà chưa ai kiểm</td>
</tr>
<tr>
<td>7</td>
<td>Bug liên quan REQ đổi đã được xếp vào 1 trong 3 ô ở mục 7.2</td>
<td>Retest chấm theo luật không còn tồn tại</td>
</tr>
</tbody>
</table>

### 9.2. Bốn lỗi hay gặp nhất

**Lỗi 1 — Sinh lại cả bộ TC "cho sạch".** Chạy `/generate-testcases-manual-rbt` lên module đã có TC là sinh trùng và đánh lại TC ID. Module Đăng nhập từng đánh lại TC ID một lần (82 TC → 41 TC) — và việc đó chỉ chấp nhận được vì **lúc ấy chưa có execution report, bug hay RTM nào trỏ vào**. Tới đợt 19/09 thì đã có execution report và 6 bug trỏ vào từng TC ID.

**Lỗi 2 — Dùng `/review-testcases` mode FIX để đồng bộ.** TC stale vẫn đạt 12/12 điểm rubric nên không bị sửa, và lệnh không sinh Delta TC List nên đội Automation không biết script nào phải đổi. Kết quả: bạn tưởng đã đồng bộ, còn TC và script vẫn mô tả luật cũ.

**Lỗi 3 — "Trùng giả định thì khỏi làm".** Đợt `AMB-LOGIN-19` cho thấy ngược lại: trùng giả định vẫn phải gỡ nhãn giả định, và REQ được viết rõ hơn thành hai tiêu chí nên sinh thêm một TC mới. Bỏ qua thì `REQ-LOGIN-42` AC2 không có TC nào — một nửa luật phiên không ai kiểm.

**Lỗi 4 — Chạy lại sai phạm vi.** Hoặc chạy lại cả module cho mỗi ticket nhỏ — đợt kiểm thử không bao giờ xong; hoặc không chạy lại gì vì *"chỉ sửa tài liệu thôi mà"* — trong khi chính TC vừa sửa chưa từng được chạy lần nào, như `TC_026`.

## 10. Bài tập thực hành

**Bài tập 1 — Chạy lại đợt `AMB-LOGIN-19` từ mốc git.** Clone repo bộ kit, tạo một nhánh riêng từ mốc `05efd17` (`git switch -c thuc-hanh-delta 05efd17`) — đây là trạng thái trước đợt, còn đủ `AMB-19` ❓ và 50 TC. Chạy `/update-requirements-from-ticket` với câu trả lời của PO ở mục 3, rồi `/update-testcases-from-impact` mode PLAN. Đối chiếu kế hoạch AI vừa sinh với [kế hoạch thật](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/impact/impact_plan_adhoc_2026-09-19.md) trên nhánh `main` và bảng sáu chỗ lan toả ở mục 5.4 — AI bỏ sót chỗ nào? Nó có gợi ý gộp `TC_051` làm biến thể của `TC_026` không?

**Bài tập 2 — Thử đáp án ngược.** Làm lại bài tập 1 nhưng PO trả lời *"1 giờ tính từ lúc đăng nhập, đang thao tác cũng bị đăng xuất"* — **khác** giả định tạm. Impact Report lúc này khác gì? `TC_026` còn đúng không? TC mới phải kiểm điều gì — và nó khác `TC_051` thật ở bước nào, kỳ vọng nào? Viết câu trả lời **trước** khi chạy lệnh, rồi so.

**Bài tập 3 — Xét lại 5 bug đang mở.** Mở `docs/bugs/README.md`. Với **từng** bug đang mở, tự trả lời: nếu PO chấp nhận hành vi bug đang báo, REQ nào sẽ đổi, TC nào stale, bug xếp vào ô nào của bảng mục 7.2? Bắt đầu bằng bug `TC004` vì chính bug report đã nêu sẵn khả năng này. Rồi đọc bug `TC018` đã đóng và giải thích vì sao nó **không** đi qua chuỗi delta.

**Bài tập 4 — Áp vào dự án của bạn.** Chọn một ticket **đã đổi yêu cầu** gần nhất ở công ty — loại ticket mà hồi đó bạn sửa TC bằng tay. Liệt kê lại: bạn đã sửa những TC nào, và theo bảng 5.4 thì còn những chỗ nào lẽ ra phải sửa theo mà không ai sửa. Đây là bài tập cho thấy rõ nhất vì sao cần chế độ delta.

## 11. Tổng kết

- **Nguy hiểm nhất là Test Case stale** — TC viết đúng về một hành vi đã bị thay. Nó cho PASS giả trên hệ thống chưa đạt luật mới, và không lệnh review nào bắt được bằng cách đọc chính TC.
- **Chuỗi delta bốn bước:** `/update-requirements-from-ticket` → `/update-testcases-from-impact` → `/execute-test-cases` theo phạm vi → xét lại bug rồi mới `/retest-fixed-bugs`. Mỗi bước ghi ra file làm đầu vào cho bước sau.
- **Update Requirements khi đã có TC:** đưa thư mục TC vào để Impact Report chỉ đúng TC stale. Cùng hành vi khác tham số là SỬA, không cấp mã mới. AMB được trả lời — **trùng hay khác** giả định tạm — thì mọi TC dựa trên giả định đó đều phải vào Impact Report.
- **Update Test Cases bằng delta, không bằng review:** câu hỏi chọn lệnh là *REQ có đổi không*. Delta giữ TC ID, không xoá dòng (TC gỡ thì gắn `@Deprecated`), không `_improved`, không `archive/` — ghi mốc git trước khi sửa, bám độ hạt đang có. Và soát tác động lan toả — một câu trả lời của PO chạm tới sáu chỗ trong file TC.
- **Execute lại theo ba vòng** — delta · cùng REQ/Story · luồng dùng chung khi code thật sự đổi. Mỗi lần một `run_id` mới; TC trong delta không được SKIPPED thêm lần nữa — gắn `@PersonalOnly` thì QA phải tự chạy và ghi kết quả vào report.
- **Retest khi REQ đổi phải xét lại bug trước.** Bug có Expected bị REQ mới vô hiệu thì đóng kèm lý do, không chấm FIXED; lệch luật mới là bug mới. Chỉ quyết định của PO ghi vào Requirements mới được đổi kỳ vọng.
- Bài kế tiếp: **Thực hành chỉnh lại bộ Skills cho phù hợp dự án thực tế** — sau khi đã chạy cả vòng thuận lẫn vòng delta, bạn sẽ biết chính xác luật nào trong bộ kit cần sửa cho khớp quy trình công ty mình.