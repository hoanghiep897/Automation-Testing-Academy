# Bài 9 - Thực hiện tạo Test Cases manual với AI Agent từ Requirements

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/334](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/334)

✅ Sử dụng skills để tạo Test Cases manual từ Requirements  
✅ Xây dựng tools View Test Cases chuyên nghiệp, thuận tiện

## 1. Từ Requirements sang Test Case — chỗ dễ hỏng nhất của cả chuỗi

Ở bài trước bạn đã chạy xong **chặng 0 và chặng 1**: khám phá hệ thống, sinh tài liệu Requirements có mã `REQ ID`, có evidence, có danh sách điểm mờ `AMB-XX`. Bài này là **chặng 2** — biến tập tài liệu đó thành bộ Test Case mà một tester khác mở ra là chạy được ngay.

Nghe thì đơn giản: "đưa requirements cho AI, bảo nó viết test case". Nhưng đây chính là chặng mà bộ TC hỏng theo kiểu **không ai phát hiện ra** — vì TC sinh ra đọc rất thuyết phục, bảng rất đẹp, số lượng rất nhiều. Ba kiểu hỏng hay gặp:

<table class="rt-table">
<thead>
<tr>
<th>Kiểu hỏng</th>
<th>Nhìn vào bộ TC thấy gì</th>
<th>Hậu quả thật</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Đủ độ phủ REQ nhưng thiếu nguyên một lớp test</strong></td>
<td>Bảng đối soát coverage xanh 100%, REQ nào cũng có TC</td>
<td>Không có TC nào kiểm nhãn, thứ tự field, trạng thái mặc định của màn hình. Bug giao diện lọt thẳng ra production</td>
</tr>
<tr>
<td><strong>TC viết bằng ngôn ngữ DevTools</strong></td>
<td>Expected Result ghi <code>document.title</code>, <code>querySelector</code>, mã HTTP</td>
<td>Tester nghiệp vụ mở ra không chạy được dòng nào. Bộ TC thành tài liệu để ngắm</td>
</tr>
<tr>
<td><strong>TC suy diễn từ chữ, không đối chiếu ảnh</strong></td>
<td>Bảng TC dày dặn, test data cụ thể</td>
<td>Nhãn nút sai một chữ, thứ tự Tab sai → FAIL giả hàng loạt lúc chạy tay, mất cả buổi truy nguyên</td>
</tr>
</tbody>
</table>

Bộ kit của Anh Tester chống ba kiểu hỏng này bằng **bốn cơ chế**, và phần lớn bài này là để bạn hiểu bốn cơ chế đó — vì hiểu rồi thì bạn *đọc được* bộ TC AI sinh ra, thay vì chỉ đếm số dòng rồi tin:

- **Độ hạt GỘP / TÁCH** — chốt cách trình bày trước dòng TC đầu tiên (mục 4).
- **Mức rủi ro quyết định độ sâu** — chống bơm TC rác (mục 5).
- **Bản đồ 4 vòng** — chống bỏ sót nguyên một lớp test (mục 6).
- **Evidence + Ngôn ngữ kiểm chứng** — chống bịa và chống viết TC không ai chạy được (mục 9).

> 💡 Toàn bộ ví dụ trong bài lấy từ hệ thống demo thật của khoá học: [crm.anhtester.com](https://crm.anhtester.com/) (Perfex CRM). Bộ TC module Đăng nhập nói tới ở đây là bộ **có thật** trong repo, bạn mở ra đọc từng dòng được: [docs/testcases/login/test\_cases\_login.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/login/test_cases_login.md).

## 2. Bốn mode, ba lệnh — chọn sai là sinh ra bộ TC thứ hai

Chặng 2 không phải một lệnh duy nhất. Skill [skills-rbt-manual-testing](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-rbt-manual-testing/SKILL.md) có **4 mode**, trong đó 3 mode có slash command riêng:

<table class="rt-table">
<thead>
<tr>
<th>Mode</th>
<th>Lệnh</th>
<th>Dùng khi</th>
<th>Đặc điểm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>QUICK</strong></td>
<td><code>/generate-testcases-from-requirements</code></td>
<td>Requirements đã rõ, phạm vi 1 module</td>
<td>Chạy <strong>1 lượt</strong>, không dừng hỏi giữa chừng</td>
</tr>
<tr>
<td><strong>FULL RBT</strong></td>
<td><code>/generate-testcases-manual-rbt</code></td>
<td>Phạm vi lớn, requirements còn mơ hồ, cần Traceability Matrix</td>
<td>Quy trình <strong>6 bước</strong>, dừng hỏi ở bước 2 và bước 4</td>
</tr>
<tr>
<td><strong>CHECKLIST</strong></td>
<td><code>/generate-checklist-test</code></td>
<td>Cần danh sách <strong>tick tay</strong> để chạy nhanh: smoke, sau hotfix, trước release</td>
<td>Không có steps đánh số. Rút gọn từ bộ TC đã có</td>
</tr>
<tr>
<td><strong>DELTA</strong></td>
<td><code>/update-testcases-from-impact</code></td>
<td>Module <strong>đã có</strong> bộ TC, requirements vừa đổi theo ticket</td>
<td>Chỉ sửa TC bị ảnh hưởng, giữ nguyên TC ID cũ</td>
</tr>
</tbody>
</table>

Khác biệt giữa CHECKLIST và hai mode đầu nằm ở câu hỏi mà nó trả lời: **checklist trả lời "đã rà hết chưa?", test case trả lời "rà bằng cách nào?"**. Cần giao cho automation, import Jira/TestRail, lưu trữ lâu dài thì dùng QUICK hoặc FULL RBT — checklist không thay thế được. Test Case cho **API** không đi qua bốn mode này mà có lệnh riêng — xem mục 8.

> 🚨 **Luật quan trọng nhất của mục này:** trước khi gõ QUICK hay FULL RBT, kiểm xem module đã có `docs/testcases/<module>/test_cases_<module>.md` chưa. **Đã có mà vẫn chạy QUICK/FULL RBT là sinh ra bộ TC thứ hai**: TC ID đánh lại từ `001`, mọi execution report cũ, mọi bug đã log, mọi `testId` trong script automation đều trỏ về hư không. Requirements đổi thì dùng **DELTA**.

### 2.1. Gọi lệnh trên Claude Code, Codex và Antigravity

Như bài trước, ba bộ kit dùng **chung tên lệnh** — chỉ khác ký tự gõ đầu, chỗ đặt file và cách viết tên skill nền tảng. Lấy lệnh FULL RBT làm ví dụ:

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
<td><strong>Gõ lệnh</strong></td>
<td><code>/generate-testcases-manual-rbt</code></td>
<td><code>$generate-testcases-manual-rbt</code></td>
<td><code>/generate-testcases-manual-rbt</code></td>
</tr>
<tr>
<td><strong>File lệnh nằm ở</strong></td>
<td><code>.claude/commands/</code></td>
<td><code>.agents/skills/generate-testcases-manual-rbt/</code></td>
<td><code>.agent/workflows/</code></td>
</tr>
<tr>
<td><strong>Skill nền tảng lệnh gọi tới</strong></td>
<td><code>skills-rbt-manual-testing</code></td>
<td><code>rbt-manual-testing</code></td>
<td><code>rbt_manual_testing</code></td>
</tr>
</tbody>
</table>

Ba lệnh còn lại trong bảng mode đổi y như vậy: `/generate-testcases-from-requirements` trên Codex là `$generate-testcases-from-requirements`, và cứ thế. Toàn bài viết theo cú pháp Claude Code.

> 📌 AI Agent chưa có bộ kit riêng (Cursor, Kiro…) thì dùng prompt mẫu copy-paste trong thư mục [prompts/](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/README.md): `prompt_02_generate_test_cases.txt`, `prompt_22_generate_testcases_quick.txt`, `prompt_15_generate_checklist.txt`. Codex và Antigravity **không cần** tới prompt nữa — bộ kit của hai công cụ này đã có sẵn đúng các lệnh trên.

## 3. Quy trình FULL RBT 6 bước — hai chỗ AI dừng lại hỏi bạn

Mode FULL RBT chạy tuần tự 6 bước, **không gộp bước**:

<table class="rt-table">
<thead>
<tr>
<th>Bước</th>
<th>Tên</th>
<th>Làm gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>Khởi tạo ngữ cảnh ⏸️</td>
<td>Chốt tên dự án, mô tả hệ thống, tài liệu nguồn — và <strong>chốt độ hạt GỘP / TÁCH</strong> kèm số TC ước tính theo từng độ hạt. <strong>Chờ bạn xác nhận</strong></td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>Phân tích &amp; Q&amp;A ⏸️</td>
<td>Xác định Happy / Alternate / Exception Path, phát hiện điểm mờ, đặt câu hỏi đánh số <code>Q1</code>, <code>Q2</code>… kèm assumption tạm. <strong>DỪNG chờ bạn trả lời</strong></td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Phân rã hệ thống</td>
<td>Chia tính năng thành Module / Sub-module, mô tả phụ thuộc giữa chúng</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Đảm bảo độ bao phủ ⏸️</td>
<td>Map Module → <code>REQ ID</code>, liệt kê kịch bản cấp cao <strong>xếp theo 4 vòng</strong>, chấm mức rủi ro và độ sâu tương ứng. <strong>Chờ bạn review</strong></td>
</tr>
<tr>
<td><strong>5</strong></td>
<td>Sinh Test Case chi tiết</td>
<td>Sinh <strong>tuần tự theo 4 vòng</strong>, mỗi batch 15–25 TC, ghi thẳng vào file, báo một dòng tiến độ. <strong>Không dừng hỏi giữa các batch</strong></td>
</tr>
<tr>
<td><strong>6</strong></td>
<td>Chuẩn hoá format &amp; metadata</td>
<td>Đóng gói vào bảng chuẩn, chạy <strong>Self-Quality Gate 11 tiêu chí</strong>, cập nhật danh mục</td>
</tr>
</tbody>
</table>

Ba dấu ⏸️ ở trên là ba chỗ bạn được can thiệp. Trong đó **bước 4 là chỗ chặn rẻ nhất của cả chặng**: nhìn một bảng 4 vòng là biết ngay bộ TC sắp sinh có bỏ sót lớp nào không — rẻ hơn rất nhiều so với phát hiện sau khi đã sinh xong 50 TC và đã có người chạy tay.

> 📋 AI tạo file `task.md` ở gốc project khi dự kiến sinh trên 30 TC, cập nhật sau mỗi batch. Đây cũng là chỗ nó ghi lại phần còn dang dở nếu phải dừng giữa chừng — mở file này ra là biết nó đang ở batch nào.

Mode QUICK **không có** ba checkpoint đó: nó chạy một mạch. Đổi lại, bạn phải đọc kỹ **dòng kế hoạch batch đầu tiên** mà nó in ra chat — đó là chỗ duy nhất nó công bố độ hạt, mức rủi ro và độ sâu đã chọn. Không chặn ở dòng đó thì chặn ở đâu cũng muộn.

## 4. Độ hạt GỘP / TÁCH — chốt trước dòng TC đầu tiên

### 4.1. Cùng độ phủ, số TC chênh gấp đôi

Đây là thứ khiến người mới ngạc nhiên nhất: cùng một module, cùng một mức bao phủ, số TC có thể chênh nhau **gấp đôi** chỉ vì cách trình bày.

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th><strong>GỘP</strong> — mặc định ⭐</th>
<th><strong>TÁCH</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Nguyên tắc</strong></td>
<td>Biến thể cùng nhóm nằm chung 1 TC, liệt kê trong <strong>Bảng biến thể</strong></td>
<td>1 biến thể = 1 TC</td>
</tr>
<tr>
<td><strong>Số TC (module cỡ Login)</strong></td>
<td>35–45</td>
<td>75–90</td>
</tr>
<tr>
<td><strong>Chạy tay</strong></td>
<td>Nhanh — mở form 1 lần, chạy hết biến thể</td>
<td>Chậm — lặp lại setup cho từng TC</td>
</tr>
<tr>
<td><strong>Báo cáo khi FAIL</strong></td>
<td>Phải ghi rõ <strong>biến thể nào</strong>: <code>CRM_LOGIN_TC_012-c FAIL</code></td>
<td>Tự động chỉ đúng TC fail</td>
</tr>
<tr>
<td><strong>Sang automation</strong></td>
<td>Map thành <strong>data-driven</strong> (<code>@DataProvider</code>, <code>test.each</code>, <code>parametrize</code>)</td>
<td>Map thành 1 test method / TC</td>
</tr>
</tbody>
</table>

Module Đăng nhập của CRM demo đã đi đúng con đường này: lượt sinh đầu tiên ở độ hạt TÁCH ra **82 TC**, sinh lại ở độ hạt GỘP còn **41 TC** — **độ phủ REQ không đổi, không case nào bị bỏ**. Đó là bằng chứng rõ nhất rằng đây là lựa chọn *trình bày*, không phải lựa chọn *chất lượng*.

### 4.2. Khi nào chọn TÁCH

Mặc định luôn là GỘP. Chỉ chọn TÁCH khi có ít nhất một trong các điều kiện sau:

- Khách hàng hoặc quy trình yêu cầu **mỗi TC là một dòng** trong Jira / TestRail / Xray — tính công theo số TC, hoặc gán người thực hiện theo từng TC.
- Cần **pass-rate theo từng biến thể** để báo cáo chất lượng.
- Module thuộc diện **kiểm định / audit**, cần vết thực thi rời cho từng case.

> 🔒 **Đổi độ hạt sau khi đã có script automation, execution report hoặc RTM trỏ vào là CẤM.** Đổi độ hạt nghĩa là đánh lại toàn bộ TC ID — cắt cả ba mối nối cùng lúc và không có cách nào phát hiện tự động. Muốn gọn hơn thì sinh **checklist** để chạy tay, giữ nguyên bộ TC làm nguồn cho automation. Vì vậy chốt độ hạt ở **lượt sinh đầu tiên** là rẻ nhất.

### 4.3. Sáu trường hợp CẤM gộp — bất kể đang dùng độ hạt nào

<table class="rt-table">
<thead>
<tr>
<th>Không được gộp</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Khác trường nhập liệu</strong> (Email với Password)</td>
<td>FAIL không chỉ ra được trường nào hỏng — mất luôn giá trị chẩn đoán</td>
</tr>
<tr>
<td><strong>Khác LOẠI phản hồi</strong> (một cái bị trình duyệt chặn, một cái tới máy chủ mới báo lỗi)</td>
<td>Hai cơ chế khác nhau, gộp lại thì Expected Result không phát biểu được thành một câu</td>
</tr>
<tr>
<td>Gộp TC <code>@Smoke</code> với TC thuộc <strong>nhóm hành vi khác</strong></td>
<td>Bộ smoke cần vết thực thi rời cho từng luồng sống còn — đây là thứ chạy đầu tiên khi có sự cố</td>
</tr>
<tr>
<td><strong>TC được thiết kế để FAIL</strong> (bám REQ trong khi hệ thống đang lỗi)</td>
<td>Mỗi TC loại này gắn với <strong>một</strong> bug riêng; gộp là mất ánh xạ TC ↔ bug</td>
</tr>
<tr>
<td><strong>Khác REQ ID mà mỗi REQ chỉ có đúng TC đó</strong></td>
<td>Gộp xong REQ vẫn "có TC" nhưng không còn TC nào <strong>chỉ</strong> kiểm nó → bảng coverage mất ý nghĩa</td>
</tr>
<tr>
<td><strong>Khác nhóm chức năng / khác màn hình</strong></td>
<td>Hỏng ranh giới tách file và ranh giới giao việc</td>
</tr>
</tbody>
</table>

Khi đã dùng GỘP thì có ba ràng buộc bắt buộc: **mỗi biến thể có mã riêng** (`a`, `b`, `c`…), **trần 6 biến thể / TC**, và **phải đếm rồi công bố số biến thể**. Ràng buộc thứ ba là quan trọng nhất — bảng coverage đếm theo REQ nên *không bắt được* việc rụng case. Không có con số "50 TC · 70 biến thể" thì gộp trở thành cái cớ để mất case mà không ai phát hiện.

## 5. Mức rủi ro quyết định độ sâu — cơ chế chống thừa

### 5.1. AI tự chấm, không hỏi bạn

Bảng 4 vòng ở mục sau chống **bỏ sót**. Mục này chống **thừa** — bơm 50 TC cho một trang "Giới thiệu" tĩnh cũng tai hại ngang bỏ quên lớp giao diện của màn thanh toán: nó ngốn công viết, công chạy, công bảo trì, và làm loãng bộ TC thật.

<table class="rt-table">
<thead>
<tr>
<th>Mức</th>
<th>Điều kiện</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cao</strong></td>
<td>Chỉ cần <strong>MỘT</strong> dấu hiệu: đụng tiền · đụng xác thực/phân quyền · đụng dữ liệu cá nhân khách hàng · có thao tác <strong>không hồi lại được</strong> (xoá cứng, gửi mail ra ngoài) · là <strong>cổng vào</strong> module khác</td>
</tr>
<tr>
<td><strong>Thấp</strong></td>
<td>Phải đủ <strong>CẢ BỐN</strong>: chỉ hiển thị · không có field nhập · hỏng thì không ai mất dữ liệu và không chặn việc gì · sửa lại được trong vài phút</td>
</tr>
<tr>
<td><strong>Trung bình</strong></td>
<td>Phần còn lại — mặc định khi lưỡng lự</td>
</tr>
</tbody>
</table>

> 🚨 **Lưỡng lự thì chấm mức CAO HƠN.** Chấm nhầm Cao chỉ tốn công viết thừa vài TC; chấm nhầm Thấp là bỏ lọt lỗi ra production. Hai sai lầm này **không cùng giá**.
>
> AI **tự chấm và ghi căn cứ**, không hỏi bạn thêm câu nào. Bạn phủ quyết ở checkpoint bước 4 (FULL RBT) hoặc ở dòng kế hoạch batch (QUICK).

### 5.2. Ba mức độ sâu — và bốn thứ không bao giờ rút

<table class="rt-table">
<thead>
<tr>
<th>Vòng</th>
<th>Đầy đủ (rủi ro Cao)</th>
<th>Tiêu chuẩn (Trung bình)</th>
<th>Tối giản (Thấp)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>V1 Smoke</strong></td>
<td>Đủ 6 nhánh</td>
<td>Đủ 6 nhánh</td>
<td><strong>Đủ 6 nhánh — KHÔNG rút</strong></td>
</tr>
<tr>
<td><strong>V2 Functional</strong></td>
<td>Đủ mọi nhánh kích hoạt</td>
<td>Đủ mọi nhánh kích hoạt</td>
<td>Chỉ <code>Required</code> + <code>Validation</code></td>
</tr>
<tr>
<td><strong>V3 Technical</strong></td>
<td>Đủ 6 nhánh</td>
<td><code>Permission</code> + <code>Security</code></td>
<td><code>Permission</code> (nếu ≥2 role)</td>
</tr>
<tr>
<td><strong>V4 Non-functional</strong></td>
<td>Đủ 6 nhánh</td>
<td><code>Responsive</code> + <code>Accessibility</code></td>
<td>Toàn bộ bỏ qua</td>
</tr>
<tr>
<td><strong>Số TC điển hình</strong></td>
<td>40–60</td>
<td>20–30</td>
<td>8–12</td>
</tr>
</tbody>
</table>

Bốn thứ **không bao giờ rút**, dù rủi ro thấp đến đâu:

- **Toàn bộ V1.** Bỏ V1 thì không biết chức năng *có chạy được không*. Sáu TC là cái giá rẻ nhất để biết điều đó.
- **`Required` + `Validation` khi có field nhập.** Có ô nhập là có người nhập sai. Trang "chỉ hiển thị" mà có ô nhập thì nó không còn là "chỉ hiển thị" — chấm lại mức rủi ro.
- **`Permission` khi hệ thống có ≥2 vai trò.** Lỗi phân quyền không tỷ lệ với độ quan trọng của chức năng: một trang xem báo cáo tưởng vô hại vẫn có thể lộ dữ liệu cả công ty.
- **`Security` khi chức năng chạm dữ liệu của người dùng khác.** Cùng lý do trên.

CRM demo có đủ **3 vai trò** để kiểm nhánh `Permission` cho ra hồn — đây là thứ nhiều hệ thống demo không có:

<table class="rt-table">
<thead>
<tr>
<th>Vai trò</th>
<th>Điểm vào</th>
<th>Tài khoản</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Admin</strong></td>
<td><code>/admin/authentication</code></td>
<td><code>admin@example.com</code></td>
</tr>
<tr>
<td><strong>Project Manager</strong></td>
<td><code>/admin/authentication</code></td>
<td><code>projectmanager@example.com</code></td>
</tr>
<tr>
<td><strong>Customer</strong></td>
<td><code>/authentication/login</code></td>
<td><code>customer@example.com</code></td>
</tr>
</tbody>
</table>

> 🔒 **Mật khẩu KHÔNG bao giờ ghi vào tài liệu TC.** Bộ kit quy định lưu ở `.env` (`ADMIN_*`, `PM_*`, `CUSTOMER_*`) và tài liệu chỉ ghi *tên biến*. Tập thói quen này ngay từ hệ thống demo — vì bộ TC của dự án thật rất hay bị đem đi copy, gửi qua chat, đính vào ticket.

## 6. Bản đồ 4 vòng — chống bỏ sót nguyên một lớp test

### 6.1. Bốn vòng và thứ tự bắt buộc

Đây là cơ chế giá trị nhất của skill, và cũng là thứ phân biệt bộ TC do người biết việc làm với bộ TC do AI phun ra. Nó trả lời câu hỏi **"bộ TC đã đi qua đủ các LOẠI kiểm thử chưa, và theo thứ tự nào"** — khác hẳn câu "trường này phải test gì".

```none
VÒNG 1 – SMOKE            → màn hình dựng được, luồng sống còn không vỡ
VÒNG 2 – FUNCTIONAL       → phần thân của mọi bộ TC (~60–70% số TC)
VÒNG 3 – TECHNICAL        → phần lớn cần DevTools/DB → tag @TechCheck
VÒNG 4 – NON-FUNCTIONAL   → phần lớn chấm "không áp dụng" ở app nghiệp vụ
```

Sinh **tuần tự V1 → V4, không nhảy cóc**. Lý do không phải hình thức: **V1 fail thì mọi TC V2 đều BLOCKED** — biết trong 10 phút đầu để dừng, thay vì chạy hết 40 TC rồi mới phát hiện form không mở được.

<table class="rt-table">
<thead>
<tr>
<th>Vòng</th>
<th>Các nhánh</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>V1 Smoke</strong></td>
<td><code>UI cơ bản</code> · <code>Open form</code> · <code>Display</code> · <code>Input valid data</code> · <code>Save</code> · <code>Verify data</code></td>
</tr>
<tr>
<td><strong>V2 Functional</strong></td>
<td><code>UI Behavior</code> · <code>Required</code> · <code>Validation</code> · <code>Equivalence Partitioning</code> · <code>Boundary Value Analysis</code> · <code>Business Rule</code> · <code>Decision Table</code> · <code>State Transition</code> · <code>Dependency</code> · <code>Use Case</code> · <code>CRUD</code> · <code>Error Guessing</code></td>
</tr>
<tr>
<td><strong>V3 Technical</strong></td>
<td><code>Permission</code> · <code>Security</code> · <code>API</code> · <code>Database</code> · <code>Integration</code> · <code>Logging/Audit</code></td>
</tr>
<tr>
<td><strong>V4 Non-functional</strong></td>
<td><code>Compatibility</code> · <code>Responsive</code> · <code>Accessibility</code> · <code>Performance</code> · <code>Regression</code> · <code>E2E</code></td>
</tr>
</tbody>
</table>

> 🚨 **Nhánh `UI cơ bản` của V1 là chỗ bị bỏ sót nhiều nhất.** Bộ TC không có TC nào kiểm nhãn nguyên văn, thứ tự field, trạng thái mặc định của màn hình là **thiếu hẳn một lớp** — dù phần validation đầy đủ đến đâu. Đây là lý do bảng coverage xanh 100% mà bug giao diện vẫn lọt.

### 6.2. Bốn trạng thái — và chỗ hay bị giấu

Mỗi nhánh phải được chấm, không bỏ trống ô nào. Có **bốn** trạng thái, không phải ba:

<table class="rt-table">
<thead>
<tr>
<th>Ký hiệu</th>
<th>Nghĩa</th>
<th>Bắt buộc ghi kèm</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅</td>
<td>Có TC</td>
<td>TC ID, kèm số biến thể nếu dùng độ hạt GỘP</td>
</tr>
<tr>
<td>➖</td>
<td><strong>Không áp dụng</strong> — không có thứ đó để kiểm</td>
<td>Lý do kỹ thuật</td>
</tr>
<tr>
<td>⏭️</td>
<td><strong>Cố ý bỏ</strong> — có, kiểm được, nhưng quyết định không kiểm vì rủi ro thấp</td>
<td><strong>Lý do + ai quyết định + điều kiện rà lại</strong></td>
</tr>
<tr>
<td>🔴</td>
<td>Thiếu — phải bổ sung trước khi xuất</td>
<td> </td>
</tr>
</tbody>
</table>

**➖ và ⏭️ không được dùng lẫn.** ➖ là *sự thật kỹ thuật* ("hệ thống không có cái đó"). ⏭️ là *một quyết định có người chịu trách nhiệm* ("có, nhưng chúng tôi chấp nhận rủi ro không kiểm"). Khi có sự cố production, hai câu đó dẫn tới hai cuộc họp hoàn toàn khác nhau. Ghi ➖ cho thứ thật ra là ⏭️ chính là **giấu quyết định** — nguy hiểm hơn cả bỏ trống ô.

Dòng ⏭️ đạt yêu cầu trông như thế này — để ý ba thành phần bắt buộc:

```none
| 4 | Compatibility | ⏭️ Cố ý bỏ | Trang tĩnh, rủi ro Thấp — chỉ kiểm Chrome.
  Quyết định: QA lead, 2026-09-11.
  Rà lại khi trang có thêm field nhập hoặc khi hệ thống cam kết hỗ trợ trình duyệt mới |
```

So với dòng không đạt: `| 4 | Compatibility | ⏭️ | Không cần thiết |` — không biết ai quyết, không biết bao giờ rà lại, tức là quyết định đó sẽ bị quên vĩnh viễn.

> 💡 **Đây là chỗ bảng 4 vòng chứng minh giá trị của nó trên chính CRM demo.** Bộ TC module Đăng nhập từng có **39/39 REQ đều xanh** — coverage 100%. Chấm bảng 4 vòng lên bộ TC đó phát hiện **6 nhánh trống hoặc quá nông**: `UI Behavior` trống, `Boundary Value Analysis` trống, `Validation` chưa đối soát đủ mục của bảng Password/Email, `Logging` chưa chấm, `Compatibility` trống, `Responsive` chỉ có 1 TC. Kết quả: bổ sung 9 TC (`TC_042` → `TC_050`), **không đụng một dòng nào của TC\_001 → TC\_041** nên execution report và các bug đang mở vẫn truy vết đúng.
>
> Bài học: **bảng coverage xanh không có nghĩa là bộ TC đủ.** Coverage đếm theo REQ; 4 vòng đếm theo *loại* kiểm thử. Chạy cả hai.

## 7. Đầu ra — bảng 13 cột và bộ file sinh ra

### 7.1. Tên cột là hợp đồng, không phải nhãn trình bày

```none
| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition |
  Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
```

<table class="rt-table">
<thead>
<tr>
<th>Cột</th>
<th>Vì sao phải có</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>REQ ID</code></td>
<td>Mắt xích truy vết về tài liệu Requirements ở bài trước. Thiếu cột này thì chặng 6 (ma trận truy vết) không chạy được. 1 TC có thể cover nhiều REQ, phân cách bằng dấu phẩy</td>
</tr>
<tr>
<td><code>Risk Level</code></td>
<td><code>High</code> / <code>Medium</code> / <code>Low</code>. <strong>Không được bỏ</strong> — web viewer của bộ kit có cột Risk và cho sort theo nó, thiếu cột thì cả cột hiện <code>—</code></td>
</tr>
<tr>
<td><code>Automatable</code> + <code>Auto Type</code></td>
<td><code>Yes/No/Partial</code> và <code>UI/API/Unit/N-A</code> — đây là đầu vào để bên Automation biết TC nào đáng chuyển thành script</td>
</tr>
<tr>
<td><code>Tags</code></td>
<td><code>@Smoke</code>, <code>@Regression</code>, <code>@CriticalPath</code>, <code>@Security</code>, <code>@TechCheck</code>, <code>@NeedsVerify</code> — dùng để dựng các <strong>bộ chạy</strong> khác nhau từ cùng một file</td>
</tr>
</tbody>
</table>

> ⚠️ **Đừng dịch tên cột sang tiếng Việt, và đừng thêm chữ vào tên cột.** Web viewer map cột theo **tên**: `TC ID`, `REQ ID`, `Module`, `Priority`, `Automatable`, `Tags` phải khớp chính xác — đổi thành `TC ID liên quan` là mất cột. Thứ tự cột thì đổi được. Nội dung trong ô viết tiếng Việt bình thường.

### 7.2. File sinh ra ở đâu

```none
docs/testcases/
├── README.md                              # danh mục — ĐỌC TRƯỚC TIÊN
└── login/
    ├── test_cases_login.md                # INDEX — tổng hợp · Bản đồ tài liệu · coverage, KHÔNG chứa dòng TC
    ├── web/
    │   ├── test_cases_login_web.md        # TC chạy trên web
    │   └── parts/part_NN_web_<slug>.md    # khi file web vượt ngưỡng
    └── archive/                           # các bản trước khi sửa
        └── test_cases_login_web_vN.md
```

Bốn quy tắc về file mà bạn nên biết để kiểm lại AI:

- **`README.md` là danh mục bắt buộc.** Nó ghi module nào đã có TC, **dải TC ID nào đã bị chiếm**, mã kế tiếp, độ phủ so với requirements, và số TC của từng nền tảng (ví dụ `Web 52 · Mobile 24 · API 18`). Đây là thứ chống việc hai người cùng sinh TC rồi trùng mã. Dự án mới chưa có file này thì AI phải **tạo trước** với bảng rỗng.
- **`test_cases_<module>.md` luôn là index** — giữ nguyên tên để mọi lệnh phía sau tìm thấy, và **không chứa dòng TC nào**. TC nằm hết ở file nền tảng `<nền-tảng>/test_cases_<module>_<nền-tảng>.md`; Bảng Đối Soát Coverage chỉ nằm ở index.
- **Ngưỡng tách file đếm theo từng nền tảng:** file nền tảng quá 40 TC (độ hạt TÁCH) hoặc 50 TC (GỘP) thì tách vào `<module>/<nền-tảng>/parts/part_NN_<nền-tảng>_<slug>.md`, cắt tại ranh giới nhóm chức năng. Tên file phải mang hậu tố nền tảng vì web viewer phân biệt tài liệu theo **tên file** — hai file trùng tên thì file nạp sau ghi đè file trước.
- **Write-first.** AI ghi thẳng vào file theo từng batch, chat chỉ hiện kế hoạch batch → tiến độ → bảng đối soát. **Nó không in cả bảng TC ra chat** — thấy nó đang phun bảng TC dài dằng dặc ra màn hình là nó đang làm sai, và bạn sắp mất token vô ích.

> 📌 Bộ TC Đăng nhập của CRM demo nói ở mục 1 được sinh **trước** khi bộ kit có tầng nền tảng, nên vẫn là một file `test_cases_login.md` chứa thẳng 50 TC. Kit không bắt chuyển ngay: lần đầu bạn chạy DELTA hoặc sinh thêm TC cho module này, AI chuyển **một lần** vào `web/test_cases_login_web.md`, TC ID giữ nguyên, bản cũ cất vào `archive/`.

## 8. TC cho app mobile và API — ba nền tảng, một dải TC ID

Ở bài trước bạn đã thấy tài liệu Requirements chia tầng `web/` · `mobile/` · `api/`. Bộ TC đi theo đúng ba tầng đó — nhưng không phải nền tảng nào cũng dùng chung lệnh:

<table class="rt-table">
<thead>
<tr>
<th>Nền tảng</th>
<th>Lệnh</th>
<th>Khác web ở đâu</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Web</strong></td>
<td>Các lệnh ở mục 2</td>
<td>— (đường chính của bài này)</td>
</tr>
<tr>
<td><strong>App mobile</strong></td>
<td>Vẫn là các lệnh ở mục 2</td>
<td>TC gắn tag <code>@Android</code> / <code>@iOS</code>, ghi vào <code>mobile/</code>. AI mở ảnh evidence ở <code>requirements/&lt;module&gt;/mobile/evidence/</code> — không mượn ảnh web</td>
</tr>
<tr>
<td><strong>API</strong></td>
<td><code>/generate-testcases-api</code></td>
<td>Tự nhận nguồn là URL hay file spec, <strong>kiểm chứng bằng gọi thật</strong>, phủ đủ 12 mã HTTP chuẩn và checklist bảo mật OWASP API, ghi vào <code>api/</code>. Lệnh này <strong>không sinh code</strong> — chuyển TC API thành script là việc của khoá Automation</td>
</tr>
</tbody>
</table>

### 8.1. Năm luật của tầng nền tảng

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Mỗi TC nằm ở đúng một file nền tảng</strong></td>
<td>TC là thứ để <strong>chạy</strong>, và mỗi lần chạy thuộc đúng một nền tảng. Không có "TC dùng chung"</td>
</tr>
<tr>
<td>REQ dùng chung ≥ 2 nền tảng → <strong>mỗi nền tảng một TC</strong>, cùng <code>REQ ID</code></td>
<td>Bước thao tác trên web và trên app khác nhau hoàn toàn — gộp vào một TC thì không ai chạy nổi</td>
</tr>
<tr>
<td><strong>Dải TC ID chung toàn module</strong>, đánh tiếp qua mọi file nền tảng</td>
<td><code>CRM_LOGIN_TC_051</code> là duy nhất trong module dù nằm ở <code>web/</code> hay <code>mobile/</code> — ma trận truy vết và nhãn <code>testId</code> trong script automation không cần biết đường dẫn file</td>
</tr>
<tr>
<td>Phân biệt nền tảng bằng <strong>tag</strong> (<code>@Web</code>, <code>@Android</code>, <code>@iOS</code>, <code>@API</code>), <strong>không</strong> thêm cột <code>Nền tảng</code></td>
<td>Web viewer map cột theo tên — cột lạ bị bỏ qua, đúng như chuyện đổi tên cột ở mục 7.1. Tag bắt buộc khi module có từ 2 nền tảng</td>
</tr>
<tr>
<td><strong>Coverage tính riêng từng nền tảng</strong></td>
<td>REQ khai áp cho web và app mà mới có TC web thì coverage của app là ❌ — <strong>không</strong> được tính "đã phủ" nhờ TC của nền tảng kia</td>
</tr>
</tbody>
</table>

> 🚨 **Đừng mở dải TC ID riêng cho mobile hay API.** Cùng lý do với chuyện không tách prefix ở bài trước: hai dải mã cho cùng một nghiệp vụ là hai bộ TC sẽ lệch nhau dần mà không ai phát hiện.
>
> 📌 Bài kế tiếp sẽ chạy tay bộ TC. Lưu ý trước: lệnh chạy tay của kit hiện **chỉ chạy được TC web** — TC `@Android` / `@iOS` / `@API` được chạy bằng automation.

## 9. Hai luật làm nên chất lượng thật của bộ TC

### 9.1. Evidence — ảnh thắng tài liệu

Tài liệu requirements là **mô tả bằng chữ**; ảnh trong `docs/requirements/<module>/<nền-tảng>/evidence/` là **bằng chứng** (tài liệu cũ chưa có tầng nền tảng thì ảnh vẫn ở `<module>/evidence/`). AI chỉ mở ảnh của **đúng nền tảng đang sinh TC** — ảnh web không chống lưng được cho TC app. Thứ tự tin cậy khi ba nguồn mâu thuẫn:

```none
DOM thật (đọc trực tiếp) > Ảnh evidence > Tài liệu chữ
```

Luật áp dụng cho cả 4 mode, chạy **trước batch đầu tiên**:

<table class="rt-table">
<thead>
<tr>
<th>Tình huống</th>
<th>AI bắt buộc làm gì</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bắt đầu sinh TC</td>
<td>Mở <strong>TỪNG</strong> ảnh trong thư mục evidence, không bỏ ảnh nào vì "tên file nghe không liên quan". <strong>Chưa mở xong thì chưa được ghi dòng TC đầu tiên</strong></td>
</tr>
<tr>
<td>Tài liệu ghi một đằng, ảnh cho thấy một nẻo</td>
<td>Viết TC theo <strong>ảnh</strong>, ghi một dòng <code>ASM-XX</code> nêu rõ xung đột kèm tên tệp ảnh, và báo bạn ngay — đây là tín hiệu requirements đã lỗi thời</td>
</tr>
<tr>
<td>Vùng không có ảnh chống lưng</td>
<td>Vẫn viết TC nhưng <strong>bắt buộc gắn tag <code>@NeedsVerify</code></strong>. <strong>NGHIÊM CẤM</strong> khẳng định chắc chắn về thứ tự Tab, nhãn nút, định dạng hiển thị khi không nhìn thấy trong ảnh</td>
</tr>
</tbody>
</table>

Bốn nhóm TC **bắt buộc** phải có evidence chống lưng, vì suy diễn ở đây là sai chắc chắn: **bố cục và thứ tự** (form 2 cột làm thứ tự Tab khác hẳn thứ tự đọc từ trên xuống) · **nhãn nguyên văn** (sai một chữ là FAIL giả) · **giá trị mặc định** (chỗ tài liệu lỗi thời nhiều nhất) · **định dạng hiển thị** (`$1,403.00`, `dd-mm-yyyy`, badge màu).

> 💡 **Có Playwright MCP thì đọc thẳng DOM, đừng chỉ nhìn ảnh.** Ảnh độ phân giải thường **không phân biệt nổi** ô đang `disabled` với ô *không tick* — mà hai thứ này khác nhau hoàn toàn về ý nghĩa nghiệp vụ. Phát hiện phần tử disabled nghĩa là có **business rule phụ thuộc** mà requirements có thể đã bỏ sót → phải sinh TC cho cả hai chiều và mở một `AMB-XX`.

### 9.2. Ngôn ngữ kiểm chứng — TC viết cho người chạy

Đây là chỗ tinh tế nhất, và là kết quả của một lần sửa lớn trên chính bộ TC của CRM demo. Hai khâu dùng **hai ngôn ngữ khác nhau**:

- AI đọc DOM để **biết sự thật** — dùng ngôn ngữ kỹ thuật.
- TC viết ra để **người khác kiểm chứng lại sự thật đó** — dùng ngôn ngữ nhìn thấy được bằng mắt.

Nên phần chính của mọi TC **không được chứa** `document.`, `querySelector`, `checkValidity`, `className`, selector CSS/XPath hay mã HTTP. Một tester nghiệp vụ phải chạy được **toàn bộ** bộ TC mà không cần mở DevTools.

Nhưng có những yêu cầu thật sự **không có biểu hiện nhìn thấy được** — cookie ghi nhớ đăng nhập, mã chống CSRF, header bảo mật. Chúng không bị vứt đi, mà tách xuống một dòng riêng:

```none
🔧 Ghi chú kỹ thuật (cần DevTools): request tài liệu trả HTTP 200;
   body mang class login_admin
```

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th> </th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ai chạy phần chính</strong></td>
<td>Tester nghiệp vụ — chỉ dùng trình duyệt</td>
</tr>
<tr>
<td><strong>Ai chạy dòng 🔧</strong></td>
<td>Tester có kỹ năng DevTools, hoặc để dành cho automation</td>
</tr>
<tr>
<td><strong>TC có dòng 🔧</strong></td>
<td>Gắn tag <code>@TechCheck</code> → dựng được một bộ chạy riêng</td>
</tr>
<tr>
<td><strong>Bỏ qua dòng 🔧 được không</strong></td>
<td>✅ Được. TC vẫn chấm PASS/FAIL bình thường ở phần chính, chỉ ghi <code>— (bỏ phần 🔧)</code> vào báo cáo</td>
</tr>
</tbody>
</table>

Cơ chế này giải quyết gọn một mâu thuẫn cũ: bộ TC vừa phải *chặt về kỹ thuật*, vừa phải *giao được cho người không rành kỹ thuật*. Trên CRM demo, 25/50 TC có dòng 🔧 — nghĩa là một nửa bộ TC vẫn chạy được bởi tester nghiệp vụ, và nửa phần kỹ thuật kia có chỗ trú đàng hoàng thay vì bị bỏ đi.

## 10. Nghiệm thu trước khi sang bài Review

### 10.1. Self-Quality Gate — AI tự chấm, bạn kiểm lại 6 mục

Ở bước 6, AI chạy **Self-Quality Gate 11 tiêu chí** rồi mới xuất file. Bạn không cần thuộc cả 11, nhưng phải tự kiểm 6 mục dễ hỏng nhất:

- **Độ hạt nhất quán.** Toàn bộ theo *một* độ hạt đã chốt; nếu GỘP thì mọi biến thể có mã riêng và không TC nào quá 6 biến thể.
- **Steps ↔ Expected khớp 1-1.** Steps đánh số, mỗi bước một hành động; Expected đánh số khớp đúng số bước.
- **Test Data cụ thể.** `Nhập mã: KH-2026-0012`, không phải `Nhập mã hợp lệ`. `Nhập 256 ký tự vào trường Name (max 255)`, không phải `Nhập giá trị vượt giới hạn`.
- **Requirement Coverage.** Mọi REQ trong phạm vi có ít nhất 1 TC — REQ nào 0 TC phải sinh bổ sung *trước* khi xuất.
- **Evidence-verified.** Có bảng đối soát cho thấy đã mở 100% ảnh; vùng không có ảnh đã gắn `@NeedsVerify`.
- **Đối soát 4 vòng.** Bảng cuối tài liệu, mọi nhánh V1–V4 đều được chấm, ba nhánh `UI cơ bản` / `Validation` / `Permission` **không được** ➖ hay ⏭️.

### 10.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Chạy QUICK/FULL RBT lên module đã có bộ TC.**  
Hậu quả: bộ TC thứ hai, TC ID đánh lại từ `001`. Execution report cũ, bug đã log, `testId` trong script automation đều trỏ về hư không — và **không có cách nào phát hiện tự động**. Requirements đổi thì dùng `/update-testcases-from-impact`.

**Lỗi 2 — Tin bảng coverage xanh 100%.**  
Coverage đếm theo REQ, không đếm theo *loại* kiểm thử. Bộ TC của CRM demo từng xanh 39/39 REQ trong khi thiếu 6 nhánh của bảng 4 vòng. Mở tới **Bảng đối soát loại kiểm thử** ở cuối tài liệu mới thấy chỗ trống.

**Lỗi 3 — Để AI gộp TC mà không đếm biến thể.**  
Gộp là đổi *cách trình bày*; biến thể bị bỏ đi là **giảm độ phủ**. Nếu bộ TC không ghi con số dạng `50 TC · 70 biến thể` thì case rụng đi mà không ai phát hiện — vì bảng coverage đếm theo REQ nên hoàn toàn không bắt được.

## 11. Bài tập thực hành

**Bài tập 1 — Sinh bộ TC đầu tiên.** Dùng tài liệu Requirements bạn đã sinh ở bài trước, chạy `/generate-testcases-from-requirements docs/requirements/<module>/requirements_<module>.md`. Đọc **dòng kế hoạch batch đầu tiên** mà AI in ra và ghi lại ba thứ nó công bố: độ hạt đang dùng, mức rủi ro đã chấm, độ sâu tương ứng. Nếu thiếu một trong ba thứ đó, yêu cầu nó nêu đủ rồi mới cho chạy tiếp.

**Bài tập 2 — So hai độ hạt.** Sinh lại đúng module đó với tham số `TÁCH` vào một thư mục khác. Đếm số TC của hai bản, rồi đối chiếu **Bảng Đối Soát Coverage** của cả hai. Mục tiêu: tự chứng minh được rằng số TC chênh nhau gần gấp đôi nhưng độ phủ REQ y hệt — đây là thứ bạn sẽ phải giải thích cho khách hàng hoặc sếp.

**Bài tập 3 — Chấm bảng 4 vòng lên bộ TC của chính bạn.** Mở **Bảng đối soát loại kiểm thử** ở cuối tài liệu vừa sinh. Tìm mọi ô ➖ và tự hỏi từng ô: *đây thật sự là "hệ thống không có cái đó", hay thật ra là "có nhưng mình không kiểm"?* Ô nào thuộc vế sau thì sửa thành ⏭️ và điền đủ ba thành phần: lý do, ai quyết, điều kiện rà lại.

**Bài tập 4 — Soi ngôn ngữ kiểm chứng.** Tìm trong bộ TC của bạn mọi chỗ có `querySelector`, `className`, mã HTTP hay selector CSS nằm ở **phần chính** của TC. Mỗi chỗ tìm được là một vi phạm. Yêu cầu AI chuyển chúng xuống dòng `🔧 Ghi chú kỹ thuật` và gắn tag `@TechCheck`. Đây là bài tập quan trọng nhất — nó quyết định bộ TC của bạn có **giao được cho người khác** hay không.

## 12. Tổng kết

- **Bốn mode, ba lệnh.** QUICK chạy một mạch, FULL RBT 6 bước có checkpoint, CHECKLIST để tick tay, DELTA để cập nhật bộ TC đã có. Kiểm module đã có file TC chưa **trước** khi gõ lệnh — sinh bộ TC thứ hai là hỏng toàn bộ truy vết. Trên Codex gõ `$` thay cho `/`; Antigravity gõ y hệt Claude Code.
- **Độ hạt GỘP / TÁCH phải chốt trước dòng TC đầu tiên**, vì đổi về sau là đánh lại toàn bộ TC ID. Cùng độ phủ, số TC chênh gấp đôi — đây là lựa chọn trình bày, không phải lựa chọn chất lượng.
- **Mức rủi ro quyết định độ sâu.** AI tự chấm và ghi căn cứ; lưỡng lự thì chấm mức cao hơn. Nhưng bốn thứ không bao giờ rút: toàn bộ V1, `Required`+`Validation` khi có field nhập, `Permission` khi có ≥2 vai trò, `Security` khi chạm dữ liệu người khác.
- **Bảng coverage xanh không có nghĩa là bộ TC đủ.** Coverage đếm theo REQ, bảng 4 vòng đếm theo loại kiểm thử. Bộ TC của CRM demo từng xanh 39/39 REQ mà vẫn thiếu 6 nhánh. Chạy cả hai bảng.
- **➖ và ⏭️ là hai chuyện khác nhau.** ➖ là sự thật kỹ thuật, ⏭️ là quyết định có người chịu trách nhiệm. Ghi ➖ cho thứ thật ra là ⏭️ chính là giấu quyết định.
- **Bộ TC chia tầng `web/` · `mobile/` · `api/`** dưới cùng một thư mục module: index `test_cases_<module>.md` không chứa dòng TC, mỗi TC nằm ở đúng một file nền tảng, dải TC ID chung toàn module, nền tảng phân biệt bằng tag. TC API dùng lệnh riêng `/generate-testcases-api`.
- **Ảnh thắng tài liệu, DOM thắng ảnh.** Nhưng TC viết ra phải dùng *ngôn ngữ nhìn thấy được* — phần kỹ thuật tách xuống dòng 🔧 và gắn `@TechCheck`, để tester nghiệp vụ vẫn chạy được toàn bộ bộ TC.

Bài kế tiếp: **Review Test Cases → Execute Test Cases → Log Bug report** — đem chính bộ TC bạn vừa sinh ra đi soi lại, chạy thật trên hệ thống, và biến mỗi TC FAIL thành một bug report có evidence đầy đủ.