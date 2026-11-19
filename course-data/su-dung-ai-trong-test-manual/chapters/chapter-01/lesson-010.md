# Bài 10 - Review Test Cases -> Execute Test Cases -> Log Bug report

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/335](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/335)

✅ Review test cases  
✅ Execute test cases  
✅ Log Bug report với test cases bị Fail

## 1. Ba việc, một vòng lặp

Ở bài trước bạn đã sinh ra bộ Test Case: có `REQ ID`, có độ hạt đã chốt, có bảng đối soát 4 vòng. Nhưng bộ TC nằm trong file thì chưa tìm ra bug nào cả. Bài này là **chặng 3, 4 và 5** — ba việc nối nhau thành một vòng lặp chạy tới khi hết bug:

```none
chặng 3          chặng 4           chặng 5
/review-        /execute-        /analyze-test-report
testcases   →   test-cases   →   /create-bug-report
                                        ↓
                                   dev fix
                                        ↓
                                 /retest-fixed-bugs
                                        ↓
                              còn lỗi → quay lại
```

Ba việc này hay bị làm tắt theo cùng một kiểu: bỏ review, chạy thẳng, rồi log bug bằng một dòng chat gửi cho dev. Cái giá phải trả:

<table class="rt-table">
<thead>
<tr>
<th>Làm tắt ở đâu</th>
<th>Hậu quả</th>
<th>Chi phí sửa</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bỏ chặng 3 (review)</strong></td>
<td>Chạy tay 50 TC rồi mới phát hiện một nửa viết sai kỳ vọng</td>
<td>Chạy lại cả đợt. Review 30 phút rẻ hơn nhiều</td>
</tr>
<tr>
<td><strong>Sửa TC ngay trong lúc chạy</strong></td>
<td>Lần chạy đó mất dấu vết: không biết TC gốc là gì, không biết đã sửa vì lý do nào</td>
<td>Cả execution report thành vô giá trị</td>
</tr>
<tr>
<td><strong>Log bug ngay khi thấy FAIL</strong></td>
<td>12 TC FAIL thành 12 bug, trong khi thực ra chỉ có 2 nguyên nhân</td>
<td>Dev nhận 12 ticket trùng, mất uy tín cả bảng báo cáo</td>
</tr>
</tbody>
</table>

> 💡 Toàn bộ số liệu trong bài lấy từ tài liệu **có thật** của hệ thống demo [crm.anhtester.com](https://crm.anhtester.com/) trong bộ kit: báo cáo review [testcase\_review\_report\_web\_20260919.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/review/testcase_review_report_web_20260919.md), hai lần chạy [run\_1787215085](https://github.com/anhtester/claude-testing-skills/blob/main/docs/executions/login/web/run_1787215085/execution_report.md) · [run\_1789759574](https://github.com/anhtester/claude-testing-skills/blob/main/docs/executions/login/web/run_1789759574/execution_report.md) và 6 bug trong [docs/bugs/README.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/bugs/README.md). Bạn mở ra đọc từng dòng được.

## 2. Chặng 3 — Review Test Cases

### 2.1. Rubric 6 tiêu chí — chấm từng TC

Lệnh `/review-testcases` chấm mỗi TC theo 6 tiêu chí, mỗi tiêu chí 0–2 điểm, tối đa 12:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Tiêu chí</th>
<th>Câu hỏi kiểm tra</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>Rõ ràng</strong></td>
<td>Người chưa biết tính năng đọc có làm theo được không? Steps có đánh số, mỗi bước một hành động?</td>
</tr>
<tr>
<td>2</td>
<td><strong>Expected đo được</strong></td>
<td>❌ <em>"hoạt động đúng"</em> — ✅ <em>"hiển thị thông báo X, chuyển về <code>/dashboard</code>"</em></td>
</tr>
<tr>
<td>3</td>
<td><strong>Độc lập</strong></td>
<td>TC tự dựng pre-condition, hay phụ thuộc TC khác phải chạy trước?</td>
</tr>
<tr>
<td>4</td>
<td><strong>Test data cụ thể</strong></td>
<td>Dữ liệu ghi rõ chưa? Trường cần unique có ghi chú phải random chưa?</td>
</tr>
<tr>
<td>5</td>
<td><strong>Truy vết được</strong></td>
<td>TC có link về <code>REQ ID</code> không?</td>
</tr>
<tr>
<td>6</td>
<td><strong>Đúng trọng tâm</strong></td>
<td>Một TC kiểm một mục tiêu, không gộp nhiều kịch bản</td>
</tr>
</tbody>
</table>

Xếp loại: 🟢 **10–12** dùng được ngay · 🟡 **6–9** cần sửa · 🔴 **0–5** phải viết lại. Mọi nhận xét **bắt buộc kèm ví dụ sửa cụ thể** — AI không được chê chung chung kiểu "TC này chưa rõ".

### 2.2. Thứ mà rubric không nhìn thấy

Đây là điểm quan trọng nhất của mục này, và nó là chỗ rất nhiều người hiểu nhầm về review.

> 🚨 **Rubric chấm cách viết của TỪNG TC — nó không nhìn thấy phần thiếu.** Một bộ TC chỉ có 12 TC validation, viết cực đẹp, vẫn ra 🟢 toàn bộ 12/12 điểm. Rubric không biết bộ TC đang thiếu hẳn lớp giao diện, thiếu phân quyền, thiếu boundary.

Nên bước 3 của lệnh làm một việc hoàn toàn khác: **đối soát ở mức bộ TC**, và đây mới là chỗ bắt được lỗ hổng thật:

- **Đối soát bảng 4 vòng** — duyệt mọi nhánh V1–V4, chấm `✅` / `🟡 nông` / `🔴 thiếu` / `➖ không áp dụng` / `⏭️ cố ý bỏ`. Soi kỹ ba nhánh hay mất nhất: `UI cơ bản`, `Validation`, `Permission`.
- **Danh sách loại trừ lập trước khi chấm** — mục *Ngoài phạm vi* của requirements, REQ đã Deprecated, AMB mà PO chốt *"không viết TC"*, rủi ro đã chấp nhận. Những phần này **không** bị tính là gap. Thiếu bước này thì báo cáo đầy "lỗ hổng" mà thật ra là quyết định có chủ đích của PO.
- **Đối soát bảng 15 loại field** — với từng trường, so từng mục của dòng loại field tương ứng. Thiếu mục nào phải nêu **đích danh mục đó**.
- **Coverage gap ghi kèm vòng/nhánh** — không được ghi "thiếu negative case" suông.
- **Độ hạt GỘP thì đếm số biến thể** — tổng biến thể ít bất thường nghĩa là đã rụng case, dù bảng coverage theo REQ vẫn xanh.

### 2.3. Ba mode — và FIX sửa thẳng vào file đang dùng

<table class="rt-table">
<thead>
<tr>
<th>Mode</th>
<th>Làm gì</th>
<th>Ghi ra đâu</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>REVIEW</strong> (mặc định)</td>
<td>Chỉ báo cáo, <strong>không sửa file TC nào</strong></td>
<td><code>docs/testcases/&lt;module&gt;/review/testcase_review_report_&lt;nền-tảng&gt;_&lt;YYYYMMDD&gt;.md</code></td>
</tr>
<tr>
<td><strong>FIX</strong></td>
<td>Như REVIEW, rồi dừng cho bạn duyệt danh sách TC sẽ sửa. Duyệt xong thì <strong>sửa tại chỗ</strong> đúng các TC đó trong file đang dùng, giữ nguyên TC ID, đồng bộ file index và ghi 1 dòng Nhật ký kèm <strong>mốc git</strong></td>
<td>Chính file TC đang dùng (cùng tên, cùng chỗ) + báo cáo như REVIEW</td>
</tr>
<tr>
<td><strong>AUTOMATION</strong></td>
<td>Chấm độc lập từng TC <code>Yes</code> / <code>Partial</code> / <code>No</code> xem có làm automation được không, kèm căn cứ trích từ TC và danh sách điều kiện cần xin dev</td>
<td><code>review/automation_review_&lt;nền-tảng&gt;_&lt;YYYYMMDD&gt;.md</code></td>
</tr>
</tbody>
</table>

Nói *"sửa luôn"* / *"cải thiện giùm"* là AI tự chuyển sang FIX; nói *"case nào automate được"* là chuyển sang AUTOMATION. Mode AUTOMATION là điểm bàn giao sang đội automation — tester manual chạy nó để trả lời trước câu hỏi *"bàn giao bộ TC này thì làm được bao nhiêu, cần chuẩn bị gì"*, còn cách đọc và dùng kết quả được dạy kỹ ở khoá Automation.

> ⚠️ **Bẫy 1 — FIX ghi đè file đang dùng, nên phải commit trước.** Trước khi sửa, AI ghi lại **mốc git** (hash commit gần nhất của file TC) vào Nhật ký. Muốn xem bản cũ thì `git show <mốc>:<đường dẫn file>`. File đang có thay đổi chưa commit thì AI **dừng** và đề nghị bạn commit trước — vì lúc đó mốc git không còn trỏ đúng bản trước khi sửa. File khách gửi (Excel, CSV) không nằm trong git thì AI phải **hỏi** trước khi ghi đè, vì không có cách lấy lại bản cũ.
>
> 📌 **Nếu bạn từng dùng bộ kit trước 19/09/2026:** mode FIX khi đó sinh file `_improved` riêng và giữ nguyên file gốc. Kit đã bỏ cách này, và cũng bỏ luôn thư mục `archive/`: một bộ TC nằm cạnh bản sao của chính nó là hai nguồn sự thật — lệnh phía sau đọc bản cũ, còn người thì sửa bản mới. Tên file TC giờ là **bất biến**, lịch sử để git giữ.
>
> 🚨 **Bẫy 2 — đừng dùng lệnh này để cập nhật TC theo requirements đã đổi.** Rubric chấm *cách viết*, không đối chiếu với REQ mới. Một TC mô tả rất hay về hành vi **đã bị thay đổi** vẫn đạt 12/12 — lệnh này **không bắt được TC lỗi thời**, và cũng không sinh danh sách TC thay đổi cho automation. Requirements đổi thì thứ tự đúng là: `/update-testcases-from-impact` đồng bộ nội dung **trước**, rồi mới `/review-testcases` chấm chất lượng.

### 2.4. Một lượt review FIX có thật

Ngày 19/09/2026, bộ TC Đăng nhập (51 TC) được chạy `/review-testcases` mode FIX. Kết quả trong [báo cáo review](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/review/testcase_review_report_web_20260919.md):

<table class="rt-table">
<thead>
<tr>
<th>Hạng mục</th>
<th>Kết quả</th>
</tr>
</thead>
<tbody>
<tr>
<td>Xếp loại</td>
<td>🟢 46 · 🟡 5 · 🔴 0 — điểm trung bình <strong>11.2/12</strong></td>
</tr>
<tr>
<td>Lỗi chính</td>
<td>Không nằm ở cách viết mà ở <strong>ghi chú đã cũ</strong>: 10 TC còn mang <code>@NeedsVerify</code> / <em>"⚠️ chưa có evidence"</em> trong khi hai lượt chạy đã kiểm chứng xong. AI đọc cả execution report để phát hiện điều này — đây là bước mới của lệnh: <strong>đối chiếu kết quả chạy</strong> trước khi xuất báo cáo</td>
</tr>
<tr>
<td>TC <code>TC_018</code></td>
<td>Biến thể <code>a</code> (email 260 ký tự) kỳ vọng sai và trùng với <code>TC_046-c</code> → bỏ biến thể đó, giữ nguyên TC ID</td>
</tr>
<tr>
<td>TC <code>TC_004</code>, <code>TC_029</code></td>
<td>Đang FAIL, bug đang mở → <strong>không sửa Expected</strong>. TC là chuẩn, chỉ PO mới được quyết định hành vi hiện tại là chấp nhận được</td>
</tr>
<tr>
<td>Nhật ký ở file index</td>
<td>Liệt kê TC nào sửa gì, kèm dòng <code>Mốc git trước khi sửa: web/test_cases_login_web.md @ 4550fd6</code></td>
</tr>
</tbody>
</table>

> 💡 Dòng `TC_004`, `TC_029` đáng đọc lại hai lần. Một reviewer vội sẽ "sửa cho TC khớp với hệ thống" để hết đỏ — và thế là hai bug biến mất khỏi mọi báo cáo mà không ai quyết định chuyện đó.

## 3. Chặng 4 — Thực thi Test Case trên browser thật

`/execute-test-cases` mở browser thật qua Playwright MCP, chạy đúng từng bước trong TC, đối chiếu Expected với thực tế, chấm trạng thái và thu evidence. Nó **không sinh code automation** — đây vẫn là chạy tay, chỉ là có AI thao tác thay bạn và ghi chép giùm.

### 3.1. Bốn trạng thái — và quy tắc vàng

<table class="rt-table">
<thead>
<tr>
<th>Trạng thái</th>
<th>Khi nào</th>
<th>Bắt buộc kèm</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ <strong>PASS</strong></td>
<td><strong>Mọi</strong> Expected đánh số đều đã verify khớp thực tế</td>
<td> </td>
</tr>
<tr>
<td>❌ <strong>FAIL</strong></td>
<td>Có ít nhất 1 Expected không khớp</td>
<td>Screenshot <strong>ngay tại bước fail</strong> + ghi Actual vs Expected</td>
</tr>
<tr>
<td>⚠️ <strong>BLOCKED</strong></td>
<td>Không chạy được vì lý do <strong>ngoài phạm vi TC</strong>: pre-condition không dựng được, môi trường lỗi, hoặc có Expected không quan sát được</td>
<td>Ghi rõ nguyên nhân chặn</td>
</tr>
<tr>
<td>⏭️ <strong>SKIPPED</strong></td>
<td>Cố ý bỏ: thao tác phá huỷ trên môi trường dùng chung, hoặc ngoài phạm vi chạy đã chọn</td>
<td>Ghi rõ lý do</td>
</tr>
</tbody>
</table>

> 📌 **Quy tắc vàng:** không verify được một Expected thì TC là **BLOCKED**, **không phải PASS**. Cấm suy đoán "chắc là đúng". Đây là chỗ phân biệt một đợt kiểm thử thật với một bảng báo cáo cho đẹp.
>
> 🗑️ TC gắn tag `@Deprecated` (chức năng đã gỡ) bị **loại ngay lúc lọc phạm vi** — không chạy, không tính vào tổng, và **không** tính là SKIPPED. SKIPPED là nợ kiểm thử; TC Deprecated thì không còn gì để kiểm. Header report chỉ ghi số TC đã loại.

### 3.2. Hai luật cứng lúc chạy

**Luật 1 — TC là chuẩn, TUYỆT ĐỐI không sửa TC trong lúc chạy.** Thực tế lệch TC thì ghi FAIL. TC viết sai thì chạy xong mới quay về `/review-testcases` mode FIX. Sửa giữa chừng là lần chạy đó mất hết dấu vết — không ai biết TC lúc chạy là bản nào.

**Luật 2 — Fail-forward, không dừng cả buổi vì một TC đỏ.** FAIL thì chụp ảnh, ghi lại, khôi phục trạng thái sạch rồi chạy tiếp. Chỉ dừng trong đúng ba trường hợp:

<table class="rt-table">
<thead>
<tr>
<th>Điều kiện dừng</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>3 TC liên tiếp FAIL cùng một nguyên nhân hạ tầng</td>
<td>Đăng nhập hỏng, server 500, mất mạng — chạy tiếp chỉ tạo báo cáo rác</td>
</tr>
<tr>
<td>Không đăng nhập được ngay từ đầu</td>
<td>Toàn bộ suite không chạy được</td>
</tr>
<tr>
<td>Phát hiện đã ảnh hưởng dữ liệu người khác</td>
<td>Ưu tiên dừng và khắc phục</td>
</tr>
</tbody>
</table>

### 3.3. Môi trường dùng chung — auto-skip và dọn dữ liệu

Đây là phần mà tester mới hay bỏ qua, và là phần đồng nghiệp của bạn quan tâm nhất. Khi bạn khai báo môi trường **dùng chung**, AI tự chuyển SKIPPED và **không thực thi** những TC sau:

<table class="rt-table">
<thead>
<tr>
<th>Dấu hiệu</th>
<th>Ví dụ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tag <code>@PersonalOnly</code> — QA tự chạy và tự theo dõi ngoài workflow</td>
<td><code>TC_026</code> phải chờ 65 phút không thao tác để phiên hết hạn</td>
</tr>
<tr>
<td>Steps chứa thao tác xoá hàng loạt</td>
<td><code>Mass Delete</code>, <code>Select All</code> rồi xoá</td>
</tr>
<tr>
<td>Steps gọi trực tiếp URL phá huỷ</td>
<td><code>/admin/clients/delete/{id}</code> gõ thẳng thanh địa chỉ</td>
</tr>
<tr>
<td>Steps tải lên tệp thực thi</td>
<td><code>.exe</code>, <code>.sh</code>, <code>.bat</code></td>
</tr>
<tr>
<td>Steps sinh <strong>khối lượng</strong> dữ liệu lớn</td>
<td>Import hàng trăm dòng, tạo hàng loạt bản ghi bằng vòng lặp</td>
</tr>
</tbody>
</table>

> ⚠️ **Hai thứ trông giống lý do bỏ qua nhưng KHÔNG phải:**
>
> - **Cột `Automation = No`** chỉ nói TC không làm automation. Chạy tay thì vẫn chạy bình thường — bỏ qua nó là bỏ luôn những TC khó nhất, đúng loại cần người kiểm.
> - **Nhập một chuỗi dài vào một field** (VD 256 ký tự vào ô tối đa 255) là TC giá trị biên, chỉ tạo tối đa một bản ghi và được dọn như mọi dữ liệu khác. Coi nó là "dữ liệu cực lớn" rồi skip là rụng cả lớp kiểm tra biên mà không ai biết.

Về dữ liệu: mọi bản ghi tạo ra phải **traceable** (`Auto_<Module>_<timestamp>`), AI **ghi sổ** từng bản ghi đã tạo, và cuối buổi **dọn sạch**. Report bắt buộc có mục *"Dữ liệu đã tạo & dọn dẹp"*, bản nào chưa xoá được phải ghi rõ để người khác xử lý.

> 💡 **Không bao giờ tạo dữ liệu mà không có kế hoạch xoá tương ứng.** Vài lần chạy không dọn là môi trường thành bãi rác — và người lãnh hậu quả là đồng nghiệp, không phải bạn. Đây là thứ quyết định bạn có được tin tưởng giao môi trường hay không.

### 3.4. TC đặc biệt — chạy và chấm thế nào

Bộ TC sinh ở bài trước không phải TC nào cũng "một chuỗi bước, một kết quả". Có bốn loại cần cách chấm riêng, và lệnh đã quy định sẵn:

<table class="rt-table">
<thead>
<tr>
<th>Loại TC</th>
<th>Cách chạy</th>
<th>Cách chấm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>GỘP — Bảng biến thể</strong> (mã <code>a</code>, <code>b</code>, <code>c</code>…)</td>
<td>Chạy <strong>từng biến thể</strong>, cùng chuỗi bước, đổi giá trị theo bảng</td>
<td>PASS khi <strong>mọi</strong> biến thể PASS. Lệch một biến thể → TC FAIL, ghi đủ mã biến thể: <code>CRM_LOGIN_TC_012-c</code></td>
</tr>
<tr>
<td><strong>GỘP — Bảng kiểm</strong> (mục <code>1</code>, <code>2</code>, <code>3</code>…)</td>
<td>Đối chiếu từng mục trên cùng một màn hình</td>
<td>PASS khi mọi mục đạt. Lệch → ghi số mục và REQ của mục đó</td>
</tr>
<tr>
<td><strong><code>@TechCheck</code></strong> — có dòng 🔧 Ghi chú kỹ thuật</td>
<td>Chấm phần chính như bình thường. Phần 🔧 (cookie, request mạng…) kiểm nếu công cụ đang có làm được</td>
<td>Phần chính quyết định PASS/FAIL. Phần 🔧 không kiểm được thì ghi <em>"🔧 chưa kiểm — &lt;lý do&gt;"</em>, không hạ kết quả</td>
</tr>
<tr>
<td><strong><code>@NeedsVerify</code></strong> — Expected ghi <em>"⚠️ chưa có evidence"</em></td>
<td>Chạy bình thường, <strong>ghi nguyên văn</strong> điều quan sát được</td>
<td>Khớp → PASS, đề nghị gỡ tag. Lệch → FAIL kèm ghi chú <em>"Expected chưa có evidence — đối chiếu lại TC trước khi báo bug"</em></td>
</tr>
</tbody>
</table>

> 📌 **Vì sao phải ghi mã biến thể:** *"TC\_012 FAIL"* với một TC gộp 5 biến thể là bắt người sửa đoán xem hỏng ở ca nào. *"TC\_012-c FAIL"* chỉ đúng một dòng trong Bảng biến thể — dev mở ra là thấy giá trị đã nhập.

## 4. Đọc một execution report thật

Lần chạy `run_1787215085` trên module Đăng nhập của CRM demo — 41 TC, khoảng 23 phút:

<table class="rt-table">
<thead>
<tr>
<th>Trạng thái</th>
<th>Số lượng</th>
<th>Tỷ lệ</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ PASS</td>
<td>32</td>
<td>78.0%</td>
</tr>
<tr>
<td>❌ FAIL</td>
<td>6</td>
<td>14.6%</td>
</tr>
<tr>
<td>⚠️ BLOCKED</td>
<td>2</td>
<td>4.9%</td>
</tr>
<tr>
<td>⏭️ SKIPPED</td>
<td>1</td>
<td>2.4%</td>
</tr>
<tr>
<td><strong>Tổng</strong></td>
<td><strong>41</strong></td>
<td>100%</td>
</tr>
</tbody>
</table>

Con số đáng chú ý nhất không nằm trong bảng, mà ở dòng ngay dưới nó: **Pass rate (không tính SKIPPED): 32/40 = 80.0%**.

> 🚨 **Tính SKIPPED vào mẫu số là làm đẹp số liệu sai lệch** — một trong những anti-pattern bị cấm của skill. SKIPPED nghĩa là *chưa kiểm*, không phải *đã kiểm và đạt*. Gộp nó vào mẫu số là đang khai báo độ phủ cao hơn thực tế.

Report gồm **6 mục cố định**, và giá trị nằm ở ba mục cuối — thứ mà báo cáo tự viết tay hay bỏ:

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Vì sao quan trọng</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Tổng kết · 2. Kết quả từng TC</td>
<td>Phần ai cũng có</td>
</tr>
<tr>
<td>3. Chi tiết FAIL</td>
<td>Actual vs Expected + ảnh tại đúng bước fail — đây là đầu vào của bug report</td>
</tr>
<tr>
<td><strong>4. TC BLOCKED</strong></td>
<td>Đây là <strong>nợ kiểm thử</strong>, không phải TC đã xong. Trong lần chạy trên: TC_014 cần tài khoản có mật khẩu chứa chữ cái, TC_034 cần một task đang chạy bộ đếm giờ — cả hai đều là thiếu điều kiện, không phải hệ thống hỏng</td>
</tr>
<tr>
<td><strong>5. Dữ liệu đã tạo &amp; dọn dẹp</strong></td>
<td>Bằng chứng bạn trả môi trường về nguyên trạng</td>
</tr>
<tr>
<td><strong>6. Đề xuất bước tiếp theo</strong></td>
<td>Nối thẳng sang chặng 5</td>
</tr>
</tbody>
</table>

### 4.1. Trả nợ kiểm thử — lần chạy thứ hai

Mục 4 của report không phải để đọc cho biết. Một tháng sau, lần chạy `run_1789759574` (19/09/2026) được mở ra chỉ để **trả đúng khoản nợ đó**: 13 TC gồm các TC chưa có kết quả của lần trước (`TC_014`, `TC_026`, `TC_034`) cộng nhóm TC bổ sung chưa chạy lần nào.

<table class="rt-table">
<thead>
<tr>
<th>TC</th>
<th>Lần 1 (20/08)</th>
<th>Lần 2 (19/09) — cách gỡ</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TC_034</code></td>
<td>⚠️ BLOCKED — cần task đang chạy bộ đếm giờ</td>
<td>✅ PASS — agent <strong>tự dựng pre-condition</strong>: tạo task <code>Auto_LOGIN_TC034_&lt;timestamp&gt;</code>, bật timer, chạy xong thì dọn</td>
</tr>
<tr>
<td><code>TC_014</code></td>
<td>⚠️ BLOCKED — mật khẩu demo không có chữ cái</td>
<td>✅ PASS — người dùng tạo tài khoản test riêng và <strong>chạy tay</strong></td>
</tr>
<tr>
<td><code>TC_026</code></td>
<td>⏭️ SKIPPED — phải chờ 65 phút</td>
<td>✅ PASS — tag <code>@PersonalOnly</code>, <strong>QA tự chạy</strong> rồi báo kết quả để ghi vào report</td>
</tr>
</tbody>
</table>

> 💡 Đây là lý do BLOCKED và SKIPPED phải có mục riêng, ghi rõ nguyên nhân: chúng là **danh sách việc cho lần chạy sau**. Gộp chúng vào "đã xong" thì sẽ không bao giờ có lần chạy thứ hai.

## 5. Chặng 5 — gom nhóm trước, viết bug sau

### 5.1. Vì sao không log bug ngay

Thấy 6 TC FAIL, phản xạ tự nhiên là mở 6 ticket. Nhưng **12 TC FAIL thường chỉ là 2 bug** — nhiều TC cùng chết vì một nguyên nhân gốc. Nên chạy `/analyze-test-report` trước để gom nhóm, rồi mới viết bug.

Lệnh này có **hai nhánh**, và nó phải xác định nhánh *trước khi* parse: nhánh AUTOMATION đọc Allure/JUnit/TestNG, nhánh MANUAL đọc `execution_report.md`. Không được áp bảng phân loại lỗi của automation lên report manual — report manual không có stack trace, không có retry, không có tên page object.

Ba tín hiệu riêng của manual mà lệnh bắt buộc kiểm:

- **Tỷ lệ BLOCKED > 20%** → ⛔ **không được kết luận chất lượng**. Lần chạy đó thiếu dữ liệu, phải dựng lại môi trường rồi chạy lại.
- **SKIPPED do auto-skip** → gom thành danh sách "nợ kiểm thử, cần chạy tay có giám sát", không để lẫn vào phần đã xong.
- **Dữ liệu chưa dọn** → cảnh báo môi trường bẩn cho lần chạy sau.

Hai loại TC ở mục 3.4 cũng được phân loại riêng: TC gộp FAIL ở vài biến thể thì phân loại **từng biến thể** (biến thể `b` có thể là bug thật trong khi `d` là TC viết sai), và TC `@NeedsVerify` FAIL thì xét khả năng **TC viết sai trước** — Expected của nó chưa từng được kiểm chứng.

### 5.2. Ranh giới quan trọng nhất của cả bài

Với **từng** TC FAIL, phải gán được nguyên nhân gốc trước khi quyết định làm gì tiếp:

🐛 Bug ứng dụng · 📝 TC viết sai/mơ hồ · 📄 Requirement đã lệch · 🌐 Môi trường/pre-condition · 📊 Test data · 🔁 Regression sau fix

Trong đó ranh giới giữa hai loại đầu là thứ quyết định bạn có được tin hay không:

<table class="rt-table">
<thead>
<tr>
<th>Câu hỏi</th>
<th>Nếu…</th>
<th>Kết luận</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expected có căn cứ <code>REQ ID</code> không?</td>
<td><strong>Có</strong>, và app làm khác</td>
<td>🐛 <strong>Bug ứng dụng</strong> → <code>/create-bug-report</code></td>
</tr>
<tr>
<td>Expected có căn cứ <code>REQ ID</code> không?</td>
<td><strong>Không</strong> — Expected là suy đoán của người viết TC</td>
<td>📝 <strong>TC viết sai</strong> → <code>/review-testcases</code></td>
</tr>
<tr>
<td>App làm đúng logic <strong>mới</strong>, TC theo logic <strong>cũ</strong>?</td>
<td>Đúng vậy</td>
<td>📄 <strong>Requirement lệch</strong> → <code>/update-requirements-from-ticket</code> rồi <code>/update-testcases-from-impact</code></td>
</tr>
</tbody>
</table>

> 🚨 **Báo nhầm "TC viết sai" thành bug là gửi dev đi sửa thứ không hỏng.** Làm vài lần là cả bảng báo cáo của bạn mất uy tín — và lần sau bug thật cũng bị nghi ngờ. Đây là lý do cột `REQ ID` mà bạn cực khổ duy trì từ bài đầu tiên cuối cùng lại có giá trị ở đúng chỗ này: nó là **căn cứ** để nói "đây là bug", chứ không phải ý kiến cá nhân.

## 6. Viết Bug Report đạt chuẩn

### 6.1. Luật, template và thang đo

`/create-bug-report` có một luật chặn ngay từ bước 1: **phải tái hiện được lỗi ít nhất 1 lần** trước khi viết. Không tái hiện được thì nghi là flaky, đề xuất `/analyze-flaky-tests` chứ không báo bug. Và **không bịa evidence** — chỉ đính kèm ảnh/log thực tế thu được.

<table class="rt-table">
<thead>
<tr>
<th>Severity</th>
<th>Định nghĩa</th>
<th>Ví dụ</th>
</tr>
</thead>
<tbody>
<tr>
<td>🔴 <strong>Critical</strong></td>
<td>Chặn luồng chính, mất dữ liệu, crash, lỗ hổng bảo mật</td>
<td>Không đăng nhập được, thanh toán sai tiền</td>
</tr>
<tr>
<td>🟠 <strong>Major</strong></td>
<td>Chức năng chính sai nhưng có cách đi vòng</td>
<td>Lọc sai kết quả, xuất file thiếu cột</td>
</tr>
<tr>
<td>🟡 <strong>Minor</strong></td>
<td>Chức năng phụ sai, giao diện lệch có ảnh hưởng sử dụng</td>
<td>Thông báo lỗi sai, sắp xếp không đúng</td>
</tr>
<tr>
<td>🟢 <strong>Trivial</strong></td>
<td>Lỗi hiển thị nhỏ, không ảnh hưởng chức năng</td>
<td>Sai chính tả, lệch lề</td>
</tr>
</tbody>
</table>

> 📌 **Severity và Priority là hai giá trị độc lập.** Severity đo **mức ảnh hưởng kỹ thuật**, Priority (`P1` hotfix / `P2` sprint sau / `P3` backlog) đo **mức khẩn cấp nghiệp vụ**. Một lỗi Trivial vẫn có thể P1 nếu nó nằm trên ảnh chụp màn hình mà sếp sắp mang đi demo.

Tên file theo quy ước `BUG_<module>_<timestamp>_<TC_ID>.md`, đặt trong `docs/bugs/<module>/<nền-tảng>/` — hậu tố TC ID để **nhìn tên là biết ngay thuộc TC nào**, không phải mở file ra tra. Thêm hai quy định nhỏ nhưng hay sai:

- **TC gộp thì ghi kèm mã biến thể** ở dòng *Test case liên quan* (`CRM_LOGIN_TC_012-c`), và TC đó phải còn hiệu lực — không trỏ vào TC `@Deprecated`.
- **Ảnh evidence link về ảnh gốc** trong thư mục `evidence/` của lần chạy, **không chép** ảnh sang `docs/bugs/`. Một ảnh, một chỗ — chép ra là có hai bản, sửa một bản thì bản kia thành ảnh sai.

### 6.2. Bug report giỏi khác bug report tồi ở đâu

Mở bug thật `BUG_login_1787226513_TC004` của CRM demo. Lỗi rất nhỏ: bấm logo trên trang đăng nhập không về trang chủ công khai. Nhưng cách viết thì đáng học:

<table class="rt-table">
<thead>
<tr>
<th>Thứ bug report đó có</th>
<th>Vì sao nó tạo ra khác biệt</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tái hiện độc lập</strong></td>
<td>Không chỉ bấm logo, mà còn gõ thẳng URL gốc — <strong>cùng kết quả</strong>. Nhờ vậy chỉ ra được nguyên nhân không nằm ở logic của logo mà ở route <code>/</code> của hệ thống</td>
</tr>
<tr>
<td><strong>Tần suất tái hiện</strong></td>
<td>Ghi rõ "luôn luôn, qua cả 2 cách" — dev không phải đoán lỗi có ngẫu nhiên không</td>
</tr>
<tr>
<td><strong>Workaround</strong></td>
<td>Ghi rõ không chặn luồng nghiệp vụ nào — đây là căn cứ để chấm <code>P3</code> thay vì gào lên</td>
</tr>
<tr>
<td><strong>Nghi ngờ root cause + đề xuất</strong></td>
<td>Thẳng thắn nêu: <em>có thể đây là quyết định thiết kế có chủ đích</em>, và đề nghị xác nhận với PO — nếu đúng thì sửa <code>REQ-LOGIN-04</code> và TC cho khớp, <strong>chứ không phải bắt dev fix</strong></td>
</tr>
</tbody>
</table>

> 💡 **Dòng cuối cùng là thứ tách tester có nghề với tester mới.** Bug report không phải chỗ để chứng minh mình tìm ra lỗi — nó là chỗ để đội biết **nên làm gì tiếp**. Đôi khi câu trả lời đúng là "sửa tài liệu", không phải "sửa code".
>
> Trên chính module này còn một ví dụ nữa: bug `TC_018` (email 260 ký tự trả thông báo khác chuẩn) — về sau đợt rà soát 4 vòng khảo sát lại và phát hiện mốc 64 ký tự đó là **ranh giới chuẩn RFC 5321, không phải lỗi**. Ngày 19/09/2026 bug được **đóng với trạng thái *không phải lỗi***, và việc kéo theo được làm đủ: `TC_018` bỏ biến thể email dài (trùng `TC_046-c`) qua `/review-testcases` mode FIX, danh mục bug ghi *"⚪ Đã đóng — không phải lỗi"*. Bug report sai không đáng sợ; **không bao giờ rà lại mới đáng sợ**.

## 7. Đóng vòng lặp — retest bug đã fix

### 7.1. Bốn trạng thái retest

Dev báo fix xong thì chạy `/retest-fixed-bugs`. Kết quả có bốn khả năng, và **chỉ một** trong số đó cho phép đóng bug:

<table class="rt-table">
<thead>
<tr>
<th>Kết quả</th>
<th>Nghĩa</th>
<th>Làm gì tiếp</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ <strong>FIXED</strong></td>
<td>Chạy đúng steps gốc, khớp Expected, lặp ≥ 2 lần</td>
<td>Đề xuất đóng bug</td>
</tr>
<tr>
<td>❌ <strong>NOT_FIXED</strong></td>
<td>Lỗi cũ vẫn còn</td>
<td>Mở lại <strong>bug cũ</strong>, không tạo bug trùng</td>
</tr>
<tr>
<td>🟡 <strong>PARTIAL</strong></td>
<td>Hết lỗi gốc nhưng vẫn lệch Expected</td>
<td>Giữ bug mở, ghi rõ phần nào còn</td>
</tr>
<tr>
<td>⚠️ <strong>CANNOT_VERIFY</strong></td>
<td>Không dựng được pre-condition</td>
<td><strong>Không</strong> được chấm FIXED</td>
</tr>
</tbody>
</table>

### 7.2. Ba chốt chặn

**Chốt 1 — build phải khác build lúc log bug.** Giống hệt thì ⛔ dừng, báo người: retest trên đúng build đã lỗi là vô nghĩa, kết quả chỉ tái hiện lại bug cũ.

**Chốt 2 — không chấm FIXED vì "không thấy lỗi nữa".** Phải chạy **đúng Steps to Reproduce trong bug gốc**, không rút gọn, không đi đường khác. Và **không sửa bug report gốc** cho khớp hành vi mới — chỉ *thêm* mục `Lịch sử retest`. Nội dung gốc là bằng chứng lịch sử.

**Chốt 3 — bug Critical/Major luôn chạy mode FULL.** Verify xong phải chạy regression quanh vùng vừa sửa. Bản fix làm hỏng chỗ khác là **chuyện thường xuyên**, không phải ngoại lệ. Và TC regression FAIL là **bug MỚI** — tách riêng, link về bug gốc. Gộp vào bug cũ là mất dấu vết nguyên nhân.

### 7.3. Cập nhật trạng thái ở cả hai nơi

Kết quả retest được ghi vào mục `Lịch sử retest` trong file bug, **và** vào cột `Trạng thái` của danh mục `docs/bugs/README.md` theo đúng từ khoá:

<table class="rt-table">
<thead>
<tr>
<th>Kết quả retest</th>
<th>Ghi vào cột <code>Trạng thái</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ FIXED</td>
<td><code>🟢 Đã đóng (retest &lt;DD-MM-YYYY&gt;)</code></td>
</tr>
<tr>
<td>❌ NOT_FIXED</td>
<td><code>🔴 Đang mở — NOT_FIXED &lt;DD-MM-YYYY&gt;</code></td>
</tr>
<tr>
<td>🟡 PARTIAL</td>
<td><code>🔴 Đang mở — PARTIAL &lt;DD-MM-YYYY&gt;</code></td>
</tr>
<tr>
<td>⚠️ CANNOT_VERIFY</td>
<td><code>⚠️ Cần rà lại — CANNOT_VERIFY &lt;DD-MM-YYYY&gt;</code></td>
</tr>
</tbody>
</table>

> ⚠️ Chỉ sửa file bug mà quên danh mục là hai nơi báo hai trạng thái: người đọc danh mục (và công cụ xem bug) vẫn thấy bug đã fix là *Đang mở*. Checklist cuối của `/retest-fixed-bugs` có riêng một dòng cho việc này.

## 8. Chuỗi truy vết bốn mắt xích

Tới đây bạn đã dựng xong đủ bốn tầng tài liệu, mỗi tầng nối vào tầng trước bằng một mã:

```none
requirements  →  testcases  →  executions  →  bugs
   REQ ID          TC ID         run_id       BUG ID (đuôi TC_ID)
```

Cả bốn tầng dùng chung một kiểu thư mục: `<module>/<nền-tảng>/`, với nền tảng chỉ nhận đúng 3 tên `web` · `mobile` · `api`. Module Đăng nhập của CRM demo hiện nằm như sau:

```none
docs/requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md     ← index (IN HOA)
docs/requirements/login/web/requirements_login_web.md
docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md          ← index (IN HOA)
docs/testcases/login/web/test_cases_login_web.md          ← 51 TC
docs/testcases/login/review/testcase_review_report_web_20260919.md
docs/executions/login/web/run_1787215085/execution_report.md
docs/bugs/login/web/BUG_login_1787226513_TC004.md
```

> 📌 File index viết **IN HOA** (`TEST_CASES_LOGIN_SUMMARY.md`) để nhìn là phân biệt được với file nền tảng (`test_cases_login_web.md`) — trước đây hai file tên gần giống nhau, rất dễ mở nhầm. Có tầng nền tảng ngay từ đầu dù module mới chỉ có web, để sau này thêm app hay API thì **không phải di chuyển file nào**.

Mỗi tầng có một file `README.md` làm **danh mục**, và đây là thứ phải đọc **trước tiên** mỗi khi động vào tầng đó:

<table class="rt-table">
<thead>
<tr>
<th>Danh mục</th>
<th>Trả lời câu hỏi</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>docs/testcases/README.md</code></td>
<td>Module nào đã có TC · dải TC ID nào <strong>đã bị chiếm</strong> · mã kế tiếp · độ phủ so với requirements</td>
</tr>
<tr>
<td><code>docs/bugs/README.md</code></td>
<td>Bug nào đang mở · mã nào đã chiếm · bug nào đã fix mà <strong>chưa retest</strong></td>
</tr>
</tbody>
</table>

Danh mục bug của CRM demo hiện có 6 bug, và bảng thống kê theo trạng thái cho thấy ngay tình hình: **5 đang mở · 0 chờ retest · 0 đã đóng · 1 đóng — không phải lỗi** (bug `TC018` ở mục 6.2). Nhìn một bảng là biết đợt kiểm thử đang tắc ở đâu — đó chính là mục đích của danh mục.

> ⚠️ **Cột `Mã bug` và `Trạng thái` là bắt buộc** trong danh mục — thiếu một trong hai là công cụ xem trực quan bỏ qua cả bảng. Cũng giống chuyện tên cột của bảng TC ở bài trước: **tên cột là hợp đồng đọc, không phải nhãn trình bày**.

## 9. Nghiệm thu trước khi bàn giao đợt kiểm thử

### 9.1. Tám thứ tự kiểm

- **Pass rate không tính SKIPPED vào mẫu số.**
- **Không TC nào chấm PASS mà chưa verify hết Expected đánh số.** Không verify được là BLOCKED.
- **Mọi TC FAIL có ảnh chụp tại đúng bước fail**, không phải ảnh chụp sau khi đã điều hướng đi chỗ khác.
- **Mục "Dữ liệu đã tạo & dọn dẹp" có đủ**, bản nào chưa xoá được đã ghi rõ.
- **Mỗi FAIL đã được gán nguyên nhân gốc** (🐛 / 📝 / 📄 / 🌐 / 📊 / 🔁) trước khi quyết định mở bug.
- **Mọi bug có link ngược về TC ID, REQ ID và run\_id**, và đã có dòng trong `docs/bugs/README.md`.
- **TC gộp FAIL có ghi mã biến thể** (`<TC ID>-<mã>`) ở cả report lẫn bug report.
- **Retest xong đã cập nhật cột `Trạng thái`** trong danh mục bug, khớp với dòng mới nhất của `Lịch sử retest`.

### 9.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Chấm PASS thay vì BLOCKED.**  
Một Expected không quan sát được, tester nghĩ "chắc là đúng" rồi chấm PASS. Đây là loại sai nguy hiểm nhất vì nó **không để lại dấu vết nào**: báo cáo đẹp hơn thực tế, và không ai biết để quay lại kiểm.

**Lỗi 2 — Mở bug trước khi gom nhóm.**  
6 TC FAIL không có nghĩa là 6 bug. Chạy `/analyze-test-report` trước, gán nguyên nhân gốc cho từng FAIL, rồi mới quyết định mở bao nhiêu bug. Trong đó phải tách bằng được **bug ứng dụng** với **TC viết sai** — căn cứ là có `REQ ID` chống lưng hay không.

**Lỗi 3 — Chấm FIXED vì chạy thử thấy ổn.**  
Phải chạy đúng Steps to Reproduce của bug gốc, lặp ít nhất 2 lần, và với bug Critical/Major thì chạy thêm regression quanh vùng fix. "Không thấy lỗi nữa" không phải là bằng chứng — nhất là khi bạn thao tác theo đường khác đường lúc phát hiện lỗi.

## 10. Bài tập thực hành

**Bài tập 1 — Review bộ TC của chính mình.** Chạy `/review-testcases` ở mode REVIEW lên bộ TC bạn sinh ở bài trước. Đọc báo cáo và tách làm hai phần: phần chấm *từng TC* (rubric 6 tiêu chí) và phần đối soát *mức bộ TC* (4 vòng + 15 loại field). Câu hỏi tự trả lời: *có TC nào 🟢 nhưng bộ TC vẫn bị báo thiếu nhánh không?* — nếu có, bạn vừa tận mắt thấy rubric không nhìn được phần thiếu.

**Bài tập 2 — Chạy thật một bộ smoke.** Chạy `/execute-test-cases` với phạm vi `@Smoke` trên CRM demo, khai báo rõ **môi trường dùng chung**. Ngồi nhìn agent thao tác (headed mode bắt buộc có lý do của nó). Sau khi xong, mở report và kiểm đúng ba chỗ: pass rate có tính SKIPPED không · TC BLOCKED có ghi nguyên nhân không · mục dữ liệu đã dọn có đủ không.

**Bài tập 3 — Phân loại FAIL bằng tay trước khi hỏi AI.** Lấy danh sách TC FAIL từ bài tập 2. Với **từng** TC, tự gán nguyên nhân gốc trước, rồi mới chạy `/analyze-test-report` và so với kết quả của AI. Chỗ hai bên lệch nhau là chỗ đáng đọc kỹ nhất — thường là ranh giới bug ứng dụng ↔ TC viết sai.

**Bài tập 4 — Soi một bug report có sẵn.** Mở `docs/bugs/login/web/` của bộ kit, chọn một bug bất kỳ và tự chấm: có tái hiện độc lập không · có ghi tần suất không · có workaround không · có nêu nghi ngờ root cause và đề xuất không. Rồi đem chính bốn câu đó chấm lại bug gần nhất **bạn từng log ở công ty**. Đây là bài tập quan trọng nhất — nó cho bạn thấy khoảng cách giữa "báo lỗi" và "viết bug report".

## 11. Tổng kết

- **Ba chặng là một vòng lặp, không phải đường thẳng.** Review → chạy → gom nhóm → log bug → dev fix → retest → còn lỗi thì quay lại. Bỏ chặng review 30 phút để rồi chạy lại cả đợt 50 TC là đổi rẻ lấy đắt.
- **Rubric 6 tiêu chí không nhìn thấy phần thiếu.** Một bộ TC hụt hẳn lớp giao diện vẫn 🟢 toàn bộ. Chỉ có đối soát ở *mức bộ TC* — bảng 4 vòng và bảng 15 loại field — mới bắt được.
- **`/review-testcases` có ba mode, và FIX sửa tại chỗ.** Không còn file `_improved` hay thư mục `archive/` — commit trước khi FIX, bản cũ tra bằng mốc git ghi trong Nhật ký.
- **TC là chuẩn, không sửa TC trong lúc chạy.** Lệch thì ghi FAIL. Và không verify được một Expected thì là **BLOCKED, không phải PASS**.
- **Pass rate không tính SKIPPED vào mẫu số.** SKIPPED là *chưa kiểm*, không phải *đã đạt* — gộp vào là khai báo độ phủ cao hơn thực tế.
- **Gom nhóm trước, viết bug sau.** 12 TC FAIL thường chỉ là 2 bug. Và ranh giới quyết định uy tín của bạn là: Expected có `REQ ID` chống lưng thì là **bug ứng dụng**, không có thì là **TC viết sai**.
- **Bug report tốt nói cho đội biết nên làm gì tiếp**, chứ không chỉ chứng minh có lỗi — kể cả khi câu trả lời đúng là "sửa tài liệu, không phải sửa code".
- **Chỉ FIXED mới được đóng bug**, và phải chạy đúng steps gốc trên **build khác** build lúc log. Bug Critical/Major thì kèm regression — bản fix làm hỏng chỗ khác là chuyện thường.

Bài kế tiếp: **Update Requirements → Update Test Cases → Execute Test Cases → Retest** — vòng lặp bạn vừa chạy giả định requirements đứng yên. Thực tế PO đổi ý giữa sprint, và bài sau dạy cách cho thay đổi đó chảy qua đủ bốn tầng tài liệu mà không làm đứt chuỗi truy vết.