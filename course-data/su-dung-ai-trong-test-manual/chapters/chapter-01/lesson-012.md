# Bài 12 - Thực hành chỉnh lại bộ Skills cho phù hợp dự án thực tế

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/360](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/360)

✅ Cách chỉnh lại bộ Skills cho phù hợp dự án thực tế  
✅ Thực hiện chạy lại các nội dung đã học cho dự án đang làm

## 1. Bộ kit là chuẩn chung — quy trình của công ty bạn có chuẩn riêng

Ở bài trước bạn đã chạy trọn vòng delta của Manual Tester trên CRM demo: Requirements đổi → cập nhật Test Case → chạy lại đúng phần bị ảnh hưởng → xét lại bug rồi retest. Cộng với các bài trước đó, bạn đã đi hết một chu kỳ đầy đủ — phân tích yêu cầu, lập Test Plan, sinh Test Case, chạy, log bug, cập nhật. Mọi thứ AI sinh ra đều theo đúng luật của bộ kit: mã TC dạng `CRM_LOGIN_TC_012`, bảng TC có 13 cột metadata, bug nằm trong `docs/bugs/`, evidence nằm cạnh lần chạy sinh ra nó.

Rồi bạn mang bộ kit vào dự án thật ở công ty, và bắt đầu nghe những câu như:

- *"Bên mình mã test case là `TC_LOGIN_001`, cả bộ tài liệu cũ đang như vậy."*
- *"Khách hàng tính công theo số test case trên TestRail — mỗi case một dòng, không gộp."*
- *"Bug report phải có trường Sprint và trường Module Owner, QA Lead mới duyệt."*
- *"Môi trường staging dùng chung với team Business, tuyệt đối không được xoá dữ liệu."*

Không câu nào trong số đó là lỗi của bộ kit — bộ kit không thể biết công ty bạn quy định gì. Nhưng nếu bạn chỉ nhắc AI trong chat, thì **mỗi phiên mới lại phải nhắc lại**, người khác trong đội không biết để nhắc, và bộ TC sinh ra hôm thứ Hai khác bộ TC hôm thứ Sáu. Tệ hơn: những thứ này không sai rõ ràng như một dòng code lỗi cú pháp. Một bộ TC đánh mã sai chuẩn vẫn đọc được, vẫn chạy được — chỉ là ba tháng sau không ai ghép nó vào hệ thống quản lý test của công ty được nữa.

Ở bài **Cách thiết lập SKILL, RULE cho AI Agent trên Claude + Codex** bạn đã biết cấu trúc RULE / SKILL / COMMAND và tự viết thử một file RULE cho dự án manual. Bài này là phần thực hành của đúng câu đó, nhưng lần này trên **bộ kit có sẵn**: sửa ở đâu, sửa thế nào, chỗ nào tuyệt đối không được đụng, và sửa xong thì kiểm ra sao.

> 💡 Toàn bộ ví dụ "chuẩn công ty" trong bài là **một bộ quy định minh hoạ** cho dự án CRM, được đặt ra để thực hành. Còn mọi tên file, đoạn nội dung, con số trích từ bộ kit đều là **thật** — bạn mở [.claude/](https://github.com/anhtester/claude-testing-skills/tree/main/.claude) ra đối chiếu từng dòng được.

## 2. Bản đồ chỗ sửa — muốn đổi gì thì mở file nào

Bộ kit có bốn tầng file. Mỗi tầng trả lời một câu hỏi khác nhau, nên một quy định của công ty chỉ nên nằm ở **một** tầng:

<table class="rt-table">
<thead>
<tr>
<th>Tầng</th>
<th>Trả lời câu hỏi</th>
<th>Ví dụ quy định công ty đặt vào đây</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CLAUDE.md</code></td>
<td>Luật chung cho mọi tác vụ trong dự án</td>
<td>Ngôn ngữ báo cáo · cấu trúc thư mục <code>docs/</code> · định dạng ngày tháng · những việc AI tuyệt đối không được làm</td>
</tr>
<tr>
<td><code>.claude/rules/</code></td>
<td>Tài liệu sinh ra phải <strong>trông như thế nào</strong></td>
<td>Định dạng mã TC · độ hạt mặc định · các trường bắt buộc của bug report · quy ước đặt tên file</td>
</tr>
<tr>
<td><code>.claude/skills/</code></td>
<td>Làm một việc <strong>theo quy trình nào</strong>, dùng mẫu nào</td>
<td>Template bug report · rubric review TC · quy tắc auto-skip · bảng Severity/Priority</td>
</tr>
<tr>
<td><code>.claude/commands/</code></td>
<td>Chuỗi bước của <strong>một lệnh</strong> — đầu vào, đầu ra, checkpoint</td>
<td>Hiếm khi cần sửa — xem mục 3</td>
</tr>
</tbody>
</table>

Tra nhanh cho những yêu cầu hay gặp nhất của một đội Manual:

<table class="rt-table">
<thead>
<tr>
<th>Công ty yêu cầu</th>
<th>Sửa ở đâu</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mã TC theo định dạng riêng</td>
<td>Tạo mới <code>rules/testcase_rules.md</code> + dòng "Tiền tố TC ID" trong <code>docs/testcases/README.md</code> — mục 5</td>
</tr>
<tr>
<td>Thêm/bớt cột trong bảng Test Case</td>
<td>⚠️ Đọc mục 6 trước — tên cột là hợp đồng đọc của công cụ, không phải nhãn tự do</td>
</tr>
<tr>
<td>Mỗi biến thể một dòng TC (không gộp)</td>
<td><code>rules/testcase_rules.md</code> — đặt độ hạt mặc định là <code>TÁCH</code> — mục 7</td>
</tr>
<tr>
<td>Bug report có thêm trường của công ty</td>
<td><code>skills/skills-bug-reporter/SKILL.md</code> — mục 8</td>
</tr>
<tr>
<td>Quy tắc chạy trên môi trường dùng chung</td>
<td><code>skills/skills-manual-test-executor/SKILL.md</code> + dòng "Môi trường" trong danh mục — mục 9</td>
</tr>
<tr>
<td>Thêm tiêu chí review TC của công ty</td>
<td><code>skills/skills-testcase-reviewer/SKILL.md</code> — thêm tiêu chí vào rubric, <strong>không</strong> thay 6 tiêu chí có sẵn</td>
</tr>
</tbody>
</table>

### 2.1. Điểm khác của track Manual — bộ kit chưa có file RULE nào cho bạn

Mở [.claude/rules/](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/rules) ra, bạn sẽ thấy đúng 6 file: `automation_rules.md`, `locator_strategy.md`, `playwright_rules.md`, `selenium_rules.md`, `appium_rules.md`, `reporting_rules.md`. **Không file nào nói về Test Case manual, bug report hay execution report.** Ngay cả `CLAUDE.md` cũng mở đầu bằng dòng *"GLOBAL AUTOMATION AGENT RULES"* với phạm vi ghi rõ là "mọi tác vụ Test Automation".

Đây không phải thiếu sót — đó là hệ quả của việc bộ kit sinh ra từ nhu cầu automation trước. Nhưng nó đổi hẳn cách bạn tuỳ biến so với đồng nghiệp bên Automation:

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Tester Automation</th>
<th>Tester Manual (bạn)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Luật về đầu ra nằm ở đâu</strong></td>
<td>6 file trong <code>.claude/rules/</code> — mở ra sửa là xong</td>
<td>Nằm <strong>bên trong SKILL</strong> — <code>skills-rbt-manual-testing</code> giữ gần hết: định dạng bảng TC, độ hạt, 4 vòng, quy tắc xuất file</td>
</tr>
<tr>
<td><strong>Việc đầu tiên phải làm</strong></td>
<td>Sửa file RULE có sẵn</td>
<td><strong>Tạo mới</strong> file RULE cho Manual, rồi mới tính tới sửa SKILL</td>
</tr>
<tr>
<td><strong>Rủi ro chính</strong></td>
<td>Sửa một nửa quy định (hai file RULE nói ngược nhau)</td>
<td>Sửa thẳng vào SKILL những thứ đáng lẽ thuộc RULE → mất sạch khi cập nhật kit</td>
</tr>
</tbody>
</table>

Vẫn có phần của `CLAUDE.md` áp cho bạn dù tiêu đề ghi "Automation": mục 1 (báo cáo bằng Tiếng Việt), mục 5 (bảng liệt kê skill, trong đó có đủ các skill manual), mục 6b (cấu trúc thư mục `docs/`, quy tắc bất biến về prefix và mã, định dạng ngày `DD-MM-YYYY`). Đây chính là chỗ tuỳ biến đầu tiên và rẻ nhất: **thêm một dòng phạm vi** vào đầu `CLAUDE.md` của dự án bạn, ghi rõ file này áp cho cả tác vụ manual — để người mới vào đội không đọc tiêu đề rồi tưởng không liên quan.

### 2.2. Ba bộ kit — cùng tên file, khác thư mục

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
<td><strong>File luật chung</strong></td>
<td><code>CLAUDE.md</code></td>
<td><code>AGENTS.md</code></td>
<td><code>GEMINI.md</code></td>
</tr>
<tr>
<td><strong>RULE</strong></td>
<td><code>.claude/rules/</code></td>
<td><code>.agents/rules/</code></td>
<td><code>.agent/rules/</code></td>
</tr>
<tr>
<td><strong>Skill sinh TC manual</strong></td>
<td><code>.claude/skills/skills-rbt-manual-testing/</code></td>
<td><code>.agents/skills/rbt-manual-testing/</code></td>
<td><code>.agent/skills/rbt_manual_testing/</code></td>
</tr>
<tr>
<td><strong>Cách RULE được nạp</strong></td>
<td>Nạp hết lúc mở phiên (không khai <code>paths</code>)</td>
<td><code>AGENTS.md</code> dặn chỉ đọc file liên quan việc đang làm</td>
<td>Theo cơ chế rule của Antigravity</td>
</tr>
</tbody>
</table>

Toàn bài minh hoạ trên Claude Code. Dùng Codex hay Antigravity thì sửa đúng file cùng tên trong thư mục tương ứng — nội dung cần sửa giống hệt, chỉ khác đường dẫn.

## 3. Nguyên tắc sửa: RULE trước, SKILL sau, COMMAND sau cùng

Ba loại file có "độ nguy hiểm khi sửa" rất khác nhau:

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Sửa sai thì hỏng gì</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>RULE</strong></td>
<td>Tài liệu sinh ra lệch chuẩn — mở file ra là thấy, review là bắt được</td>
<td>RULE là mô tả <em>kết quả mong muốn</em>. Không lệnh nào đọc RULE để lấy đường dẫn file hay tên đầu ra</td>
</tr>
<tr>
<td><strong>SKILL</strong></td>
<td>Có thể làm hỏng lệnh gọi tới nó</td>
<td>Lệnh của kit khai skill cần nạp bằng <strong>tên thư mục</strong> — <code>/generate-testcases-from-requirements</code> khai <code>skills-rbt-manual-testing</code>, <code>/execute-test-cases</code> khai <code>skills-manual-test-executor</code>. Đổi tên thư mục là lệnh không tìm thấy skill</td>
</tr>
<tr>
<td><strong>COMMAND</strong></td>
<td>Gãy cả chuỗi mà không báo lỗi gì</td>
<td>Đầu ra của lệnh này là đầu vào của lệnh sau. Đổi tên file đầu ra ở một lệnh, lệnh sau vẫn chạy — chỉ là đọc không thấy gì</td>
</tr>
</tbody>
</table>

Với Manual, ví dụ rõ nhất của tầng COMMAND là chuỗi delta bạn vừa học ở bài trước: `/update-testcases-from-impact` ghi ra `impact/delta_tc_<TICKET-ID>.md`, và `/update-automation-from-impact` bên đội Automation **chỉ đọc đúng file đó**. Bạn đổi tên file đầu ra cho "gọn hơn", lệnh của bạn vẫn chạy xanh, chỉ là bên Automation mở ra không thấy gì và tưởng đợt này không có TC nào đổi.

Vì vậy: **quy định về *tài liệu trông thế nào* thì vào RULE.** Chỉ sửa SKILL khi cần đổi *mẫu* hoặc *quy trình*. Chỉ sửa COMMAND khi quy trình công ty khác hẳn — và khi đó đọc mục "Mối quan hệ với workflows khác" ở cuối file lệnh trước, để biết lệnh nào đang đọc đầu ra của nó.

> ⚠️ **Đừng đổi tên file hay tên thư mục trong bộ kit.** Muốn thêm luật riêng thì thêm nội dung vào file có sẵn, hoặc tạo file RULE mới. Tên lệnh, tên skill, tên file RULE được nhắc chéo nhau ở nhiều chỗ — `CLAUDE.md` mục 4 và mục 5 liệt kê từng file bằng đường dẫn, và mỗi file lệnh mở đầu bằng một dòng *"BẮT BUỘC nạp skill…"* ghi rõ đường dẫn tới `SKILL.md`.

## 4. Bước 0 — gom chuẩn công ty thành một bảng quyết định

Đừng mở file ra sửa ngay. Việc đầu tiên là **ghi ra giấy** mọi quy định đang áp dụng, lấy từ ba nguồn: tài liệu quy trình QA của công ty (nếu có) · comment của QA Lead trong các lần review TC gần nhất · **bộ tài liệu test đang dùng thật** của dự án (đây là nguồn trung thực nhất — quy trình viết trên giấy có thể cũ, bộ TC đang chạy thì không).

Bảng quyết định minh hoạ cho dự án CRM trong bài:

<table class="rt-table">
<thead>
<tr>
<th>Chủ đề</th>
<th>Bộ kit đang ghi</th>
<th>Công ty quy định</th>
<th>Sửa ở</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mã Test Case</td>
<td><code>CRM_&lt;MODULE&gt;_TC_&lt;3 số&gt;</code></td>
<td><code>TC_&lt;MODULE&gt;_&lt;3 số&gt;</code> — bộ tài liệu cũ đang vậy</td>
<td>RULE mới + danh mục</td>
</tr>
<tr>
<td>Độ hạt TC</td>
<td>GỘP (mặc định)</td>
<td>TÁCH — khách tính công theo số TC trên TestRail</td>
<td>RULE mới</td>
</tr>
<tr>
<td>Trường bug report</td>
<td>13 trường ở mục "Thông tin chung"</td>
<td>Thêm <code>Sprint</code> và <code>Module Owner</code></td>
<td>Mẫu trong SKILL</td>
</tr>
<tr>
<td>Môi trường chạy</td>
<td>Auto-skip TC phá huỷ khi dùng chung</td>
<td>Staging dùng chung — bật, và cấm cả tạo dữ liệu mới ngoài giờ</td>
<td>SKILL + danh mục</td>
</tr>
<tr>
<td><strong>Không sửa</strong></td>
<td>13 cột bảng TC · khung 4 vòng · 4 trạng thái chạy · 4 trạng thái retest · cấm sửa TC cho khớp thực tế</td>
<td>Giữ nguyên</td>
<td>—</td>
</tr>
</tbody>
</table>

Dòng cuối quan trọng không kém bốn dòng đầu: nó ghi rõ **những luật của kit mà bạn cố ý giữ**. Sáu tháng sau có người đề nghị "TC này chạy không ra kết quả, sửa Expected cho khớp hệ thống đi", bảng này là chỗ trả lời — và bạn trả lời được bằng một dòng đã chốt từ trước, không phải bằng tranh luận.

> 📌 Bảng quyết định nên đặt ngay trong repo dự án, cạnh thư mục `.claude/`, và ghi ngày chốt. Nó là **lý do** của mọi chỗ bạn sửa trong bộ kit — thiếu nó, người sau chỉ thấy file khác bản gốc mà không biết vì sao, và thường sẽ "sửa lại cho giống bản gốc".

## 5. Thực hành 1 — mã Test Case: dọn hai chuẩn đang cãi nhau

### 5.1. Hai chuẩn TC ID bạn đang cầm trên tay

Nếu bạn đã làm bài tập ở bài **Cách thiết lập SKILL, RULE cho AI Agent trên Claude + Codex**, bạn đang có một file `CLAUDE.md` tự viết với dòng:

```none
- Mã Test Case theo định dạng: TC_<MODULE>_<số thứ tự 3 chữ số>.
```

Còn bộ kit thì quy định khác — và quy định ở **hai** chỗ:

<table class="rt-table">
<thead>
<tr>
<th>Nguồn</th>
<th>Nói gì</th>
<th>Thuộc tầng nào</th>
</tr>
</thead>
<tbody>
<tr>
<td>File RULE tự viết ở bài 331</td>
<td><code>TC_LOGIN_001</code></td>
<td>RULE của bạn</td>
</tr>
<tr>
<td><code>docs/testcases/README.md</code> của kit</td>
<td>Tiền tố <code>CRM_</code> → <code>CRM_&lt;MODULE&gt;_TC_&lt;3 số&gt;</code></td>
<td>Dữ liệu dự án — <strong>không phải</strong> RULE</td>
</tr>
<tr>
<td><code>skills-rbt-manual-testing</code></td>
<td>Mọi ví dụ dùng <code>CRM_LOGIN_TC_012</code></td>
<td>SKILL — ví dụ minh hoạ</td>
</tr>
</tbody>
</table>

Nếu bạn để nguyên cả ba, AI đọc được hai mệnh lệnh khác nhau cho cùng một việc. Tài liệu chính thức của Claude Code nói thẳng hậu quả: *hai luật mâu thuẫn thì Claude có thể chọn một trong hai một cách tuỳ ý* ([How Claude remembers your project](https://code.claude.com/docs/en/memory)). Module này ra `TC_LOGIN_001`, module sau ra `CRM_CUST_TC_001` — và chỉ phát hiện khi đối chiếu RTM.

Điểm quan trọng: **hai nguồn này không ngang hàng nhau.**

<table class="rt-table">
<thead>
<tr>
<th>Chỗ ghi</th>
<th>Thuộc loại</th>
<th>Xử lý</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>docs/testcases/README.md</code> — dòng "Tiền tố TC ID"</td>
<td><strong>Dữ liệu của dự án</strong>, do chính bạn ghi khi lập danh mục</td>
<td>Sửa thành tiền tố của công ty. Đây là nơi có thẩm quyền cao nhất về mã</td>
</tr>
<tr>
<td>Ví dụ <code>CRM_LOGIN_TC_012</code> trong SKILL</td>
<td><strong>Ví dụ minh hoạ</strong> cách trình bày, không phải quy định</td>
<td>Để nguyên. Sửa hàng chục chỗ ví dụ trong file 124 KB là tự chuốc việc và sẽ mất khi cập nhật kit</td>
</tr>
<tr>
<td>File RULE của bạn</td>
<td><strong>Quy định</strong></td>
<td>Đây là chỗ viết chuẩn của công ty — xem 5.2</td>
</tr>
</tbody>
</table>

### 5.2. Viết file RULE Manual đầu tiên của dự án

Vì `.claude/rules/` chưa có file nào cho Manual, bạn tạo mới. Đặt tên theo đúng kiểu của kit (chữ thường, gạch dưới, hậu tố `_rules`) để nhìn là biết cùng một họ:

```none
.claude/rules/testcase_rules.md
```

Nội dung tối thiểu:

```none
# Quy Tắc Manual Test Case — Dự án CRM

> Chuẩn công ty, chốt 18-09-2026. File này ĐÈ LÊN mọi ví dụ trong
> skills-rbt-manual-testing khi hai bên khác nhau.

## 1. Mã Test Case

- Định dạng: `TC_<MODULE>_<3 số>` — VD `TC_LOGIN_001`
- Tiền tố module tra ở `docs/testcases/README.md`, KHÔNG tự đặt mới
- Dải mã dùng chung toàn module, đánh tiếp qua mọi nền tảng
- KHÔNG đánh lại mã khi cập nhật TC — xem mục 3

## 2. Độ hạt mặc định

- Mặc định `TÁCH` — mỗi biến thể một dòng TC
- Lý do: khách hàng theo dõi tiến độ theo số TC trên TestRail
- Đổi sang GỘP phải có xác nhận của QA Lead, ghi vào danh mục

## 3. Bất biến (không được đổi kể cả khi user yêu cầu)

- Tên cột bảng TC giữ nguyên Tiếng Anh theo skill
- TC đã có execution report hoặc bug trỏ vào: KHÔNG đổi mã, KHÔNG đổi độ hạt
- Không sửa Expected Result cho khớp hành vi thực tế
```

Ba điều đáng chú ý trong file trên:

<table class="rt-table">
<thead>
<tr>
<th>Chi tiết</th>
<th>Vì sao viết như vậy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dòng <em>"File này ĐÈ LÊN mọi ví dụ trong skill"</em></td>
<td>Bạn không xoá được hết ví dụ trong SKILL, nên phải nói rõ <strong>ai thắng</strong>. Không có dòng này thì đúng là hai luật ngang nhau và AI chọn tuỳ ý</td>
</tr>
<tr>
<td>Ghi <strong>lý do</strong> của độ hạt TÁCH</td>
<td>Người sau đọc thấy "TÁCH" mà không biết vì sao sẽ đổi lại GỘP cho gọn. Lý do gắn với khách hàng thì không ai dám đổi bừa</td>
</tr>
<tr>
<td>Mục "Bất biến" đặt ngay trong RULE</td>
<td>Đây là phần bảng quyết định ghi "giữ nguyên". Viết vào RULE để AI không bị user trong phiên thuyết phục đổi</td>
</tr>
</tbody>
</table>

> 📌 Bài thiết lập SKILL/RULE có hướng dẫn khai `paths` để RULE chỉ nạp khi Claude đọc tới file khớp mẫu. Với RULE manual, cân nhắc kỹ: luật về mã TC cần có mặt **lúc AI bắt đầu sinh**, mà lúc đó có thể chưa file TC nào được đọc. Bộ kit gốc không khai `paths` cho file nào là có lý do — nếu thêm, phải kiểm chứng theo mục 10.

### 5.3. Bộ TC đã chạy rồi thì đừng đánh lại mã

Đây là chỗ dễ hỏng nhất khi tuỳ biến, và hỏng không có cách phát hiện tự động. Bộ kit ghi rõ trong `CLAUDE.md` mục 6b: *không đổi / đánh lại TC ID khi cập nhật* — vì TC ID là khoá nối sang ba nơi cùng lúc:

<table class="rt-table">
<thead>
<tr>
<th>Nơi đang giữ TC ID</th>
<th>Đánh lại mã thì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Execution report các lần chạy cũ</td>
<td>Báo cáo cũ trỏ vào mã không còn tồn tại — mất lịch sử PASS/FAIL của chính chức năng đó</td>
</tr>
<tr>
<td>Bug report — trường "Test case liên quan"</td>
<td>Bug trỏ vào mã đã đổi nghĩa còn tệ hơn không trỏ: người đọc tin nhầm và retest sai TC</td>
</tr>
<tr>
<td>Nhãn <code>testId</code> trong script automation</td>
<td>Ma trận truy vết vẫn báo "đã phủ" trong khi script đang kiểm một TC khác</td>
</tr>
</tbody>
</table>

Nên chuẩn mã mới chỉ áp cho **module chưa sinh TC**. Module đã có bộ TC chạy rồi thì giữ nguyên mã cũ và ghi một dòng vào danh mục: *"Module LOGIN dùng tiền tố cũ `CRM_LOGIN_TC_`, giữ nguyên để không gãy truy vết; module mới từ 18-09-2026 dùng `TC_<MODULE>_`."* Hai chuẩn cùng tồn tại mà **có ghi chép** thì sống được nhiều năm. Một chuẩn duy nhất nhưng đánh lại mã của bộ TC đang chạy thì hỏng ngay tuần sau.

## 6. Thực hành 2 — tên cột bảng TC là hợp đồng đọc, không phải nhãn trình bày

Yêu cầu *"đổi tên cột cho dễ đọc"* hoặc *"dịch tên cột sang Tiếng Việt cho khách xem"* nghe rất vô hại. Nó không vô hại.

Bộ kit có ba trang xem tĩnh trong `scripts/` (mở bằng cách nhấp đúp, chạy offline): `testcases-viewer` để duyệt/lọc/xuất Excel bộ TC, `execution-viewer` cho kết quả chạy, `bugs-viewer` cho danh mục bug. Trang xem TC **nhận diện cột theo tên**, và cách nhận diện không giống nhau giữa các cột:

<table class="rt-table">
<thead>
<tr>
<th>Nhóm cột</th>
<th>Cách khớp</th>
<th>Nghĩa là</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TC ID</code> · <code>REQ ID</code> · <code>Module</code> · <code>Priority</code> · <code>Automatable</code> · <code>Tags</code></td>
<td><strong>Khớp chính xác</strong> (không phân biệt hoa thường, bỏ dấu <code>*</code>)</td>
<td>Thêm một chữ là mất cột. <code>TC ID liên quan</code>, <code>Mã TC</code>, <code>Priority (P1-P3)</code> đều không được nhận</td>
</tr>
<tr>
<td><code>Risk</code> · <code>Scenario</code>/<code>Test Title</code> · <code>Pre-Condition</code> · <code>Test Steps</code> · <code>Test Data</code> · <code>Expected</code> · <code>Auto Type</code></td>
<td><strong>Khớp theo chuỗi con</strong></td>
<td><code>Expected Result</code> và <code>Expected Output</code> đều nhận được, vì đều chứa <code>expected</code></td>
</tr>
<tr>
<td>Cột lạ</td>
<td>Bị bỏ qua</td>
<td>Thêm cột riêng của công ty <strong>không làm hỏng</strong> gì — chỉ là trang xem không hiển thị nó</td>
</tr>
</tbody>
</table>

Còn một cơ chế nữa dễ bị bỏ sót: trang xem chỉ nhận một bảng là bảng Test Case khi nó có cột `TC ID` **và** ít nhất một trong ba cột nội dung (`Scenario`/`Test Steps`/`Expected`). Đó là lý do bảng tóm tắt kiểu `| TC ID | REQ | Vì sao FAIL | Trạng thái |` không bị đếm nhầm thành test case.

<table class="rt-table">
<thead>
<tr>
<th>Yêu cầu của công ty</th>
<th>Làm thế nào cho đúng</th>
</tr>
</thead>
<tbody>
<tr>
<td>"Khách muốn đọc bảng bằng Tiếng Việt"</td>
<td>✅ Nội dung ô viết Tiếng Việt (skill vốn đã vậy), <strong>tên cột giữ nguyên</strong>. Cần bản Tiếng Việt cho khách thì xuất Excel từ trang xem rồi đổi tiêu đề ở bản xuất</td>
</tr>
<tr>
<td>"Thêm cột <code>Sprint</code> và <code>Người thực hiện</code>"</td>
<td>✅ Thêm được — ghi vào <code>testcase_rules.md</code> là cột bổ sung, đặt <strong>sau</strong> 13 cột chuẩn. Trang xem bỏ qua, mọi thứ khác vẫn chạy</td>
</tr>
<tr>
<td>"Bỏ cột <code>Risk Level</code> cho gọn"</td>
<td>❌ Trang xem có cột Risk và cho sắp xếp theo nó — bỏ thì cả cột hiện <code>—</code> và mất chức năng sắp xếp. Muốn gọn thì ẩn lúc xem, đừng bỏ lúc sinh</td>
</tr>
<tr>
<td>"Đổi <code>TC ID</code> thành <code>Mã TC</code>"</td>
<td>❌ Cột này khớp chính xác. Đổi là trang xem không nhận ra bảng nào là bảng test case nữa — file mở lên trống trơn</td>
</tr>
</tbody>
</table>

> 💡 Cách kiểm nhanh nhất: sửa xong thì mở `scripts/testcases-viewer/bundle.html`, kéo file TC vào. Số TC đếm ra đúng như dòng tóm tắt của AI là tên cột còn khớp. Đây là phép thử 30 giây cho một lỗi mà đọc file bằng mắt rất khó thấy.

## 7. Thực hành 3 — độ hạt GỘP/TÁCH: chốt một lần, ghi vào RULE

Cùng một module, cùng một mức bao phủ, số TC chênh nhau **gấp đôi** chỉ vì độ hạt. Bộ kit ghi con số điển hình cho module cỡ đăng nhập: **35–45 TC** ở độ hạt GỘP, **75–90 TC** ở độ hạt TÁCH. Và đây không phải lý thuyết — module Đăng nhập của CRM demo có sẵn cả hai bản để đối chiếu: bản đang dùng **50 TC · 70 biến thể** (GỘP), bản TÁCH **82 TC** nằm trong `login/archive/`. Độ phủ REQ y hệt nhau.

Bộ kit mặc định GỘP. Bốn điều kiện để chọn TÁCH đã ghi sẵn trong skill, và điều kiện đầu tiên chính là tình huống của nhiều dự án outsourcing:

<table class="rt-table">
<thead>
<tr>
<th>Chọn TÁCH khi</th>
<th>Vì sao ảnh hưởng tới cách trình bày</th>
</tr>
</thead>
<tbody>
<tr>
<td>Khách hàng / quy trình yêu cầu mỗi TC là một dòng trong Jira, TestRail, Xray</td>
<td>Tính công theo số TC, hoặc gán người thực hiện theo từng TC — một TC gộp 5 biến thể không chia được cho 5 người</td>
</tr>
<tr>
<td>Cần pass-rate theo từng biến thể</td>
<td>Ở độ hạt GỘP, một biến thể đỏ là cả TC đỏ — con số báo cáo thô hơn</td>
</tr>
<tr>
<td>Module thuộc diện kiểm định / audit</td>
<td>Cần vết thực thi rời cho từng case</td>
</tr>
<tr>
<td>User yêu cầu rõ</td>
<td>—</td>
</tr>
</tbody>
</table>

Vấn đề không nằm ở việc chọn cái nào, mà ở chỗ **chốt ở đâu**. Rất nhiều đội chọn lại độ hạt trong từng lần gõ lệnh — lệnh sinh TC nhận tham số độ hạt ngay trên dòng lệnh, nên ai nhớ thì gõ, ai quên thì nhận mặc định GỘP. Ba tháng sau bộ tài liệu có module 40 TC và module 85 TC, không ai biết bên nào mới là chuẩn.

<table class="rt-table">
<thead>
<tr>
<th>Cách làm</th>
<th>Kết quả</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ Ghi độ hạt mặc định vào <code>testcase_rules.md</code> kèm lý do</td>
<td>Mọi phiên, mọi người trong đội đều sinh cùng một kiểu. Ai muốn khác phải sửa RULE — tức là phải có lý do</td>
</tr>
<tr>
<td>✅ Ghi độ hạt từng module vào <code>docs/testcases/README.md</code></td>
<td>Danh mục của kit đã có sẵn cột "Độ hạt" và bảng giải thích vì sao chọn — điền vào, đừng để trống</td>
</tr>
<tr>
<td>❌ Nhớ gõ tham số mỗi lần</td>
<td>Bộ tài liệu pha trộn hai độ hạt. Và vì mỗi module vẫn phủ đủ REQ, <strong>không bảng đối soát nào bắt được</strong></td>
</tr>
<tr>
<td>❌ Đổi độ hạt của module đã có execution report / script</td>
<td>Đổi độ hạt là <strong>đánh lại toàn bộ TC ID</strong> — cắt cả ba mối nối ở mục 5.3 cùng lúc. Bộ kit ghi thẳng là cấm</td>
</tr>
</tbody>
</table>

> ⚠️ Chọn TÁCH thì **đừng quên phần đi kèm**: bộ TC dài gấp đôi nên ngưỡng tách file cũng đổi (kit đặt ≤ 40 TC cho TÁCH, ≤ 50 TC cho GỘP, đếm theo *từng nền tảng*). Module đăng nhập ở độ hạt TÁCH là 82 TC — vượt ngưỡng, phải chia `parts/` ngay từ lượt sinh đầu. Chọn độ hạt mà quên điều chỉnh cách chia file thì nhận về một file duy nhất không ai review nổi trong một lượt.

## 8. Chỉnh SKILL — mẫu bug report theo chuẩn công ty

### 8.1. Chỗ cần sửa

Skill [skills-bug-reporter](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/skills/skills-bug-reporter) giữ toàn bộ "hình dáng" của một bug report trong ba khối:

<table class="rt-table">
<thead>
<tr>
<th>Khối</th>
<th>Chứa gì — và sửa gì cho dự án CRM</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mục <strong>Bug Report Template</strong></td>
<td>13 trường ở "Thông tin chung" + các mục Steps / Expected / Actual / Evidence. Thêm <code>Sprint</code> và <code>Module Owner</code> vào cuối khối "Thông tin chung" — <strong>thêm</strong>, không thay thế trường có sẵn</td>
</tr>
<tr>
<td>Bảng <strong>Severity &amp; Priority</strong></td>
<td>4 mức Severity, 3 mức Priority kèm định nghĩa. Công ty có SLA riêng (VD P1 phải fix trong 24 giờ) thì thêm một cột SLA vào bảng Priority</td>
</tr>
<tr>
<td>Mục <strong>Workflow</strong> bước 6 — Deliver</td>
<td>Đường dẫn lưu <code>docs/bugs/&lt;module&gt;/&lt;nền-tảng&gt;/BUG_&lt;module&gt;_&lt;timestamp&gt;_&lt;TC_ID&gt;.md</code>. ⚠️ Đây là <strong>tầng COMMAND trá hình</strong> — <code>bugs-viewer</code> và các lệnh khác đọc theo mẫu này. Xem 8.2</td>
</tr>
</tbody>
</table>

Ví dụ đoạn thêm vào template — đặt ngay dưới dòng `Ngày phát hiện`:

```none
- **Sprint:** <mã sprint đang chạy, VD `SPR-2026-38`>
- **Module Owner:** <tên dev phụ trách module — lấy từ bảng phân công của đội>
```

Và một dòng ghi rõ vì sao có hai trường đó, đặt ngay dưới template:

```none
> Hai trường Sprint và Module Owner là bổ sung của dự án CRM (chốt 18-09-2026)
> — QA Lead dùng để lọc bug theo sprint khi họp review cuối tuần.
```

### 8.2. Ba điều không được chạm

<table class="rt-table">
<thead>
<tr>
<th>Không chạm</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tên thư mục skill</strong> và <strong>đường dẫn đầu ra</strong></td>
<td>Với skill trong project, lệnh <code>/tên</code> lấy từ <strong>tên thư mục</strong>, không phải từ trường <code>name</code> trong frontmatter (<a href="https://code.claude.com/docs/en/skills">tài liệu Skill</a>). Các lệnh của kit cũng gọi skill bằng tên thư mục. Còn đường dẫn <code>docs/bugs/&lt;module&gt;/&lt;nền-tảng&gt;/</code> là chỗ <code>bugs-viewer</code> và lệnh retest đi tìm — đổi là bug mồ côi</td>
</tr>
<tr>
<td><strong>Trường <code>description</code></strong> — trừ khi biết rõ mình làm gì</td>
<td>Claude dùng <code>description</code> để quyết định <strong>có tự nạp skill hay không</strong>. Viết lại cho "gọn" là có thể làm skill không bao giờ được gọi tới nữa</td>
</tr>
<tr>
<td><strong>Mục "Lịch sử retest" và 4 trạng thái retest</strong></td>
<td>Kit ghi rõ: <em>Lịch sử retest là phần DUY NHẤT được phép thêm vào bug report sau khi đã bàn giao</em> — Steps, Expected, Actual, Evidence là bằng chứng tại thời điểm phát hiện. Cho phép sửa Expected cho khớp build mới là xoá mất khái niệm <code>PARTIAL</code>, và mọi bug sẽ thành <code>FIXED</code></td>
</tr>
</tbody>
</table>

### 8.3. Khi nào tạo skill mới thay vì sửa skill cũ

Công ty có một quy trình riêng — ví dụ mỗi cuối sprint phải gom bug đang mở thành một bản tóm tắt gửi khách theo mẫu của khách. Đó không phải chuẩn trình bày tài liệu (RULE), cũng không phải biến thể của bug report (sửa mẫu). Đó là **một kỹ năng mới**. Tạo skill riêng theo cách bạn đã học ở bài **Cách thiết lập SKILL, RULE cho AI Agent trên Claude + Codex**, đặt tên có tiền tố riêng của công ty để không bao giờ đụng tên skill của kit khi cập nhật.

> ⚠️ **Bẫy trùng tên skill:** khi cùng một tên skill có ở `~/.claude/skills/` (cá nhân) và `.claude/skills/` (project), **bản cá nhân được ưu tiên** ([tài liệu Skill](https://code.claude.com/docs/en/skills)). Nếu bạn từng tự viết một skill trùng tên với kit trong thư mục cá nhân — như bài thiết lập SKILL đã hướng dẫn — thì mọi chỉnh sửa bạn làm vào bản trong project sẽ **không có tác dụng**, và bạn sẽ mất cả buổi tưởng AI không chịu nghe.

## 9. Chỉnh quy tắc chạy — môi trường dùng chung và danh sách auto-skip

Đây là tuỳ biến mang tính an toàn dữ liệu, và là chỗ khác biệt lớn nhất giữa dự án học và dự án thật. Skill `skills-manual-test-executor` có sẵn quy tắc **auto-skip**: trên môi trường dùng chung, agent tự chuyển `SKIPPED` và không thực thi các TC có dấu hiệu phá huỷ.

<table class="rt-table">
<thead>
<tr>
<th>Dấu hiệu bộ kit đã liệt kê</th>
<th>Ví dụ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tag <code>@ManualOnly</code> hoặc <code>Automatable = No</code> do rủi ro dữ liệu</td>
<td>TC thao tác hàng loạt trên danh sách khách hàng</td>
</tr>
<tr>
<td>Steps chứa thao tác xoá hàng loạt</td>
<td><em>Mass Delete</em>, <em>Select All</em> rồi xoá</td>
</tr>
<tr>
<td>Steps gọi trực tiếp URL phá huỷ</td>
<td>Gõ thẳng <code>/admin/clients/delete/{id}</code> lên thanh địa chỉ</td>
</tr>
<tr>
<td>Steps tải lên tệp thực thi</td>
<td><code>.exe</code>, <code>.sh</code>, <code>.bat</code></td>
</tr>
<tr>
<td>Steps sinh dữ liệu cực lớn</td>
<td>Chuỗi 255+ ký tự, import hàng trăm dòng</td>
</tr>
</tbody>
</table>

Ba việc cần làm để quy tắc này khớp dự án của bạn:

<table class="rt-table">
<thead>
<tr>
<th>Việc</th>
<th>Chi tiết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Khai báo đúng loại môi trường</strong></td>
<td>Kit yêu cầu tester khai "môi trường dùng chung hay riêng" ngay đầu buổi chạy, và ghi vào header execution report. Môi trường riêng thì agent <strong>tắt</strong> auto-skip. Khai sai một lần là xoá nhầm dữ liệu của người khác — ghi luôn vào <code>docs/testcases/README.md</code> dòng "Môi trường" để không phụ thuộc trí nhớ</td>
</tr>
<tr>
<td><strong>Bổ sung dấu hiệu riêng của dự án</strong></td>
<td>Dự án nào cũng có thao tác nguy hiểm đặc thù mà bảng chung không liệt kê — gửi email hàng loạt cho khách thật, đẩy hoá đơn sang hệ thống kế toán, đổi trạng thái hợp đồng. Thêm vào bảng auto-skip trong SKILL, mỗi dòng ghi rõ dấu hiệu nhận biết trong Steps</td>
</tr>
<tr>
<td><strong>Giữ nguyên phần dọn dữ liệu</strong></td>
<td>Kit bắt buộc mọi dữ liệu tạo ra phải traceable, ghi sổ trong lúc chạy, dọn cuối buổi, và report có mục "Dữ liệu đã tạo &amp; dọn dẹp" kèm đối chiếu số liệu hệ thống trước/sau. Đây là thứ <strong>không nên</strong> nới ra cho nhanh</td>
</tr>
</tbody>
</table>

> 🚫 Một kiểu "tuỳ biến" cần tránh: thêm dòng *"môi trường này an toàn, bỏ qua auto-skip"* vì suite đang có quá nhiều TC bị SKIPPED nên báo cáo trông xấu. TC bị SKIPPED là **thông tin đúng** — nó nói rằng phần đó cần chạy tay có giám sát. Che nó đi không làm phần đó được kiểm.

## 10. Kiểm chứng sau khi sửa — đừng tin là đã ăn

### 10.1. Mở phiên mới

Theo [tài liệu chính thức](https://code.claude.com/docs/en/memory), `CLAUDE.md` và các file RULE không khai `paths` được nạp **khi mở phiên**. Sửa RULE giữa chừng rồi hỏi tiếp trong phiên cũ thì kết quả không đáng tin. Skill thì khác: Claude Code theo dõi thư mục skill và nhận thay đổi **ngay trong phiên**. Cách an toàn cho cả hai: sửa xong thì **mở phiên mới**, gõ `/context` để thấy file đã được nạp.

### 10.2. Chạy lại một ca mẫu cố định

Chọn một module nhỏ mà bạn đã từng sinh TC trước khi sửa — hoặc dựng một module giả chỉ 5–6 REQ — và sinh lại bằng `/generate-testcases-from-requirements`. So bản mới với bảng quyết định:

<table class="rt-table">
<thead>
<tr>
<th>Quy định đã sửa</th>
<th>Nhìn vào đâu trong bộ TC mới</th>
</tr>
</thead>
<tbody>
<tr>
<td>Định dạng mã TC</td>
<td>Cột <code>TC ID</code> của vài dòng đầu — và quan trọng hơn: dòng kế hoạch batch AI công bố ra chat trước khi sinh</td>
</tr>
<tr>
<td>Độ hạt</td>
<td>Dòng kế hoạch batch <strong>bắt buộc</strong> nêu độ hạt đang dùng. Đọc một dòng là biết sẽ nhận ~46 TC hay ~85 TC — chặn lại được ngay nếu sai, không phải chờ sinh xong</td>
</tr>
<tr>
<td>Cột bảng TC</td>
<td>Mở bằng <code>scripts/testcases-viewer/bundle.html</code>, đếm số TC hiện ra so với dòng tóm tắt của AI</td>
</tr>
<tr>
<td>Trường bug report</td>
<td>Tạo một bug thử bằng <code>/create-bug-report</code>, kiểm có đủ <code>Sprint</code> và <code>Module Owner</code></td>
</tr>
<tr>
<td><strong>Luật giữ nguyên</strong></td>
<td>Vẫn đủ 4 vòng Smoke → Functional → Technical → Non-functional · vẫn có bảng đối soát coverage cuối tài liệu · vẫn ghi thẳng vào file thay vì in bảng ra chat — sửa chỗ này mà hỏng chỗ kia là chuyện thường gặp</td>
</tr>
</tbody>
</table>

Rồi chạy `/review-testcases` lên bộ TC mới. Nhưng nhớ đúng giới hạn của nó — rubric 6 tiêu chí chấm **cách viết từng TC**, không đối chiếu với chuẩn công ty bạn vừa đặt. Nó sẽ không báo lỗi khi mã TC sai định dạng. Cái nó giúp được là: nếu nó bỗng chấm điểm thấp ở chỗ trước đây vẫn tốt, nghĩa là bản sửa của bạn đã vô tình làm hỏng thứ khác.

> 💡 Muốn `/review-testcases` kiểm được cả chuẩn công ty thì thêm **tiêu chí thứ 7** vào rubric trong `skills-testcase-reviewer` — ví dụ *"Mã TC đúng định dạng của dự án, tra ở `testcase_rules.md`"*. Thêm vào, đừng thay 6 tiêu chí có sẵn: chúng là chuẩn chất lượng chung, không mâu thuẫn gì với chuẩn riêng của bạn.

## 11. Giữ được chỉnh sửa khi bộ kit ra bản mới

Bộ kit được cập nhật liên tục — chỉ trong tháng 9/2026 đã đổi tên một loạt lệnh và thêm cả một tầng thư mục nền tảng (`web/` · `mobile/` · `api/`) vào `docs/`. Nếu bạn copy `.claude/` vào dự án, sửa thẳng vào đó rồi quên, lần lấy bản mới sẽ **ghi đè sạch** mọi tuỳ biến. Ba thói quen giúp tránh chuyện đó:

<table class="rt-table">
<thead>
<tr>
<th>Thói quen</th>
<th>Làm thế nào</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Commit bản gốc trước, tuỳ biến sau</strong></td>
<td>Một commit chỉ chứa <code>.claude/</code> nguyên bản của kit, ghi rõ commit của kit. Các commit sau là tuỳ biến. <code>git diff</code> giữa hai mốc = đúng danh sách những gì bạn đã đổi</td>
</tr>
<tr>
<td><strong>Đánh dấu ngay trong file</strong></td>
<td>Mỗi đoạn tuỳ biến mở đầu bằng một dòng như <code>&gt; Chuẩn dự án CRM (chốt 18-09-2026)</code> — như ví dụ ở mục 5.2 và 8.1. Lúc so với bản mới, nhìn là biết đoạn nào của mình</td>
</tr>
<tr>
<td><strong>Lấy bản mới vào một nhánh riêng</strong></td>
<td>Chép bản mới của kit vào nhánh riêng, so với nhánh chính, đưa lại từng tuỳ biến theo bảng quyết định. Người làm việc này là <strong>bạn</strong> — <code>CLAUDE.md</code> của kit cấm AI tự chạy <code>git pull</code>, <code>git merge</code>, <code>git checkout</code></td>
</tr>
</tbody>
</table>

Tuỳ biến nào đặt ở **file mới do bạn tạo** (như `testcase_rules.md`) thì gần như không bao giờ bị ghi đè — đó là lý do mục 3 nói "RULE trước, SKILL sau". Mỗi quy định bạn kéo được ra khỏi SKILL và đưa vào RULE riêng là một thứ bớt phải làm lại sau mỗi lần cập nhật.

> ⚠️ Khi lấy bản mới, đọc kỹ phần thay đổi **tên lệnh** và **đường dẫn đầu ra** trước tiên. Lệnh bị đổi tên hoặc thư mục đầu ra thêm một tầng thì mọi tài liệu nội bộ, prompt mẫu, quy trình viết trên wiki của đội nhắc tới tên cũ đều phải sửa theo — tuỳ biến trong RULE không giúp gì ở đây.

## 12. Nghiệm thu một lần tuỳ biến

### 12.1. Checklist

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Kiểm</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Có bảng quyết định: quy định nào, sửa ở file nào, luật nào của kit cố ý giữ nguyên</td>
</tr>
<tr>
<td>2</td>
<td>Mỗi quy định có <strong>đúng một nguồn</strong>, và nguồn đó nói rõ mình đè lên ví dụ trong SKILL</td>
</tr>
<tr>
<td>3</td>
<td>Không đổi tên file, tên thư mục skill, tên lệnh, đường dẫn đầu ra nào của kit</td>
</tr>
<tr>
<td>4</td>
<td>Tên 13 cột bảng TC còn nguyên — đã mở lại bằng <code>testcases-viewer</code> và đếm đúng số TC</td>
</tr>
<tr>
<td>5</td>
<td>Module đã có execution report / bug / script trỏ vào: mã TC và độ hạt <strong>giữ nguyên</strong>, chuẩn mới chỉ áp cho module mới — và điều này có ghi trong danh mục</td>
</tr>
<tr>
<td>6</td>
<td><code>docs/testcases/README.md</code> đã cập nhật: tiền tố TC ID, độ hạt từng module, loại môi trường</td>
</tr>
<tr>
<td>7</td>
<td>Không có skill trùng tên ở <code>~/.claude/skills/</code> che mất bản trong project</td>
</tr>
<tr>
<td>8</td>
<td>Đã mở phiên mới, sinh lại một module mẫu, tạo thử một bug report và đối chiếu bảng quyết định</td>
</tr>
</tbody>
</table>

### 12.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Sửa ví dụ thay vì sửa quy định.** Mở `skills-rbt-manual-testing` ra tìm-thay toàn bộ `CRM_LOGIN_TC_` thành `TC_LOGIN_`. File 124 KB, sửa được vài chục chỗ, sót vài chỗ, và mất sạch ở lần cập nhật kit kế tiếp. Quy định thuộc về RULE; ví dụ trong SKILL cứ để nguyên — chỉ cần RULE nói rõ ai thắng.

**Lỗi 2 — Đổi thứ mà công cụ đang đọc.** Dịch tên cột sang Tiếng Việt cho khách dễ đọc, rút gọn đường dẫn `docs/bugs/<module>/<nền-tảng>/` thành `bugs/`, đổi tên file index cho khớp cách đặt tên của công ty. Mỗi quyết định đều hợp lý lúc làm, và cộng lại thành một bộ tài liệu mà không lệnh nào, không trang xem nào đọc được nữa — **mà vẫn không báo lỗi gì**.

**Lỗi 3 — Dùng tuỳ biến để hạ chuẩn cho đẹp báo cáo.** Bỏ auto-skip vì nhiều TC bị SKIPPED, cho phép sửa Expected Result cho khớp hệ thống vì nhiều TC FAIL, bỏ mục đối soát 4 vòng vì nó luôn chỉ ra chỗ thiếu. Đó không phải chỉnh bộ Skills cho phù hợp dự án; đó là **xoá chốt chặn** để khỏi thấy vấn đề.

## 13. Bài tập thực hành

**Bài tập 1 — Lập bảng quyết định cho dự án của bạn.** Mở bộ tài liệu test đang dùng thật ở công ty (hoặc bộ TC bạn đã sinh ở các bài trước) và điền bảng theo mẫu mục 4: tối thiểu 5 chủ đề, kèm dòng *"luật của kit cố ý giữ nguyên"*. Chưa sửa file nào.

**Bài tập 2 — Viết file RULE Manual đầu tiên.** Tạo `.claude/rules/testcase_rules.md` theo mục 5.2 cho chuẩn của công ty bạn. Bắt buộc có: dòng nói rõ file này đè lên ví dụ trong SKILL · lý do của mỗi lựa chọn · mục "Bất biến". Mở phiên mới, gõ `/context` kiểm file đã được nạp.

**Bài tập 3 — Thử phá rồi sửa lại.** Copy một file TC ra chỗ khác, đổi tiêu đề cột `TC ID` thành `Mã TC`, mở bằng `scripts/testcases-viewer/bundle.html`. Ghi lại chính xác trang xem hiển thị gì. Rồi thử đổi `Expected Result` thành `Expected Output` và xem kết quả có khác không. Bài tập này cho bạn cảm giác trực tiếp về sự khác nhau giữa cột khớp chính xác và cột khớp chuỗi con.

**Bài tập 4 — Đổi độ hạt trên module chưa có gì.** Chọn một module nhỏ chưa sinh TC. Sinh hai lần: một lần GỘP, một lần TÁCH. So số TC, số file, và thời gian bạn đọc review hết. Rồi trả lời: với cách khách hàng của bạn theo dõi tiến độ, độ hạt nào hợp hơn — và vì sao câu trả lời đó phải nằm trong RULE chứ không nằm trong trí nhớ của bạn.

**Bài tập 5 — Tập lấy bản mới.** Tạo một nhánh chứa `.claude/` đã tuỳ biến ở bài tập 2. Lấy bản mới nhất của bộ kit vào một nhánh khác và so hai nhánh. Ghi lại: tuỳ biến nào đưa lại được nguyên vẹn, tuỳ biến nào phải viết lại vì file gốc đã đổi cấu trúc. Kết quả thường rất rõ — tuỳ biến nằm ở file riêng thì sống, tuỳ biến nằm trong file của kit thì phải làm lại.

## 14. Tổng kết

- **Bộ kit là chuẩn chung, dự án có chuẩn riêng.** Nhắc AI trong chat thì mỗi phiên phải nhắc lại; ghi vào đúng file thì cả đội và mọi phiên đều theo.
- **Track Manual tuỳ biến khác track Automation.** `.claude/rules/` chưa có file nào cho Manual — luật về đầu ra đang nằm bên trong `skills-rbt-manual-testing`. Việc đầu tiên của bạn là **tạo mới** một file RULE, không phải sửa file có sẵn.
- **Bốn tầng, bốn câu hỏi:** `CLAUDE.md` luật chung · `rules/` tài liệu trông thế nào · `skills/` quy trình và mẫu · `commands/` chuỗi bước. Sửa RULE trước, SKILL sau, COMMAND sau cùng — vì đầu ra của lệnh này là đầu vào của lệnh sau.
- **Gom chuẩn công ty thành bảng quyết định trước khi sửa**, lấy từ bộ tài liệu đang dùng thật chứ không chỉ từ quy trình viết trên giấy — và ghi cả những luật của kit cố ý giữ nguyên.
- **Sửa quy định, đừng sửa ví dụ.** Mã TC là quy định → vào RULE mới, kèm một dòng nói rõ RULE đè lên ví dụ trong SKILL. Tìm-thay hàng chục chỗ trong file SKILL 124 KB là công toi.
- **Có thứ trông như nhãn nhưng là hợp đồng đọc.** Tên 13 cột bảng TC, đường dẫn `docs/bugs/<module>/<nền-tảng>/`, tên file index — công cụ và lệnh phía sau đọc theo đúng những chuỗi đó. Đổi là hỏng mà không báo lỗi.
- **Đừng đánh lại mã TC, đừng đổi độ hạt** của module đã có execution report, bug hoặc script trỏ vào. Chuẩn mới áp cho module mới; hai chuẩn cùng tồn tại có ghi chép thì sống được, đánh lại mã thì gãy ngay.
- **Sửa xong phải kiểm chứng:** mở phiên mới, sinh lại một module mẫu, đọc dòng kế hoạch batch, mở bộ TC bằng `testcases-viewer`, tạo thử một bug report. Và giữ tuỳ biến bằng git — commit bản gốc trước, đánh dấu từng đoạn, lấy bản mới vào nhánh riêng.
- Bài kế tiếp: **Xây dựng bộ nhớ Local dành riêng cho từng dự án chuyên biệt** — bộ kit đã khớp chuẩn công ty; tiếp theo là để AI nhớ được bối cảnh riêng của từng dự án qua các phiên làm việc.