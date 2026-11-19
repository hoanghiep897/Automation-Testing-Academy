# Bài 8 - Chuẩn hoá Requirements và tạo Test Plan trước khi viết test cases

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/364](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/364)

✅ Chuẩn hoá Requirements trước khi sinh test cases  
✅ Tạo Test Plan

## 1. Khoảng trống giữa Requirements và Test Case

Ở bài trước bạn đã chạy xong **chặng 0 và chặng 1**: có bản đồ module, có tài liệu Requirements mang mã `REQ ID`, có evidence, có danh sách điểm mờ `AMB-XX`. Phản xạ tự nhiên là đưa ngay bộ tài liệu đó cho AI sinh Test Case.

Khoan đã. Tài liệu vừa sinh ra là **bản nháp đầu tiên**, chưa phải đầu vào sạch. Hãy nhìn lịch sử thật của module Đăng nhập trên CRM demo — từ lúc AI sinh tài liệu tới lúc bắt đầu sinh Test Case:

<table class="rt-table">
<thead>
<tr>
<th>Mốc</th>
<th>Tổng REQ</th>
<th>AMB còn treo</th>
<th>Chuyện gì xảy ra</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>2026-08-14</strong> — AI sinh tài liệu từ UI</td>
<td>35</td>
<td>14</td>
<td>Bản nháp đầu tiên của <code>/generate-requirements-from-website</code></td>
</tr>
<tr>
<td><strong>2026-08-18</strong> — Rà soát chất lượng</td>
<td>40</td>
<td>17</td>
<td>Phát hiện chính AI viết sai: đếm nhầm phần tử bị ẩn, phép thử không chứng minh được kết luận, token thật bị chép vào tài liệu. <strong>10 REQ phải sửa</strong></td>
</tr>
<tr>
<td><strong>2026-08-18</strong> — PO chốt đợt A</td>
<td>41</td>
<td>13</td>
<td>PO trả lời 4 điểm mờ: không có cơ chế khoá tài khoản, 2 REQ ra ngoài phạm vi</td>
</tr>
<tr>
<td><strong>2026-08-18</strong> — PO chốt đợt B</td>
<td>43</td>
<td>1</td>
<td>PO trả lời 13 điểm mờ còn lại và cấp tài khoản đủ 3 vai trò. <strong>2 REQ đảo từ "ghi hiện trạng" sang "ghi kỳ vọng đúng"</strong></td>
</tr>
<tr>
<td><strong>Bắt đầu sinh Test Case</strong></td>
<td>43</td>
<td>1 🟡</td>
<td><strong>39 REQ</strong> trong phạm vi viết TC, 4 REQ ngoài phạm vi có ghi lý do</td>
</tr>
</tbody>
</table>

Tức là **trước khi có dòng TC nào**: thêm 8 REQ, sửa 15 REQ, đưa 4 REQ ra ngoài phạm vi, đóng 18/19 điểm mờ. Nếu sinh Test Case ngay từ bản ngày 14/08 thì:

- Ba REQ ghi tiêu đề tab là `Dashboard` trong khi thật ra là `(16) Dashboard` — con số đầu là số thông báo, thay đổi liên tục. **TC đỏ hàng loạt dù hệ thống chạy đúng.**
- Hai REQ ghi theo hành vi đang chạy — mà PO sau đó xác nhận là **lỗi**. **TC xanh trên một hệ thống đang sai**, và bug không bao giờ được mở.
- Một REQ khai "có hai lối đăng xuất" vì AI đếm được 2 phần tử trong DOM — một cái bị ẩn trên desktop. **TC kiểm một nút mà người dùng không bao giờ bấm được.**

Và còn một khoảng trống nữa, không nằm trong tài liệu Requirements nào: **chưa ai chốt đợt này test module nào, không test gì, bắt đầu khi nào, và thế nào thì coi là xong**. CRM demo có 23 module, mới khảo sát 3. Thiếu câu trả lời đó thì bạn không biết nên sinh Test Case cho module nào trước.

> 💡 Bài này gồm hai nửa: **chuẩn hoá Requirements** — biến bản nháp AI sinh ra thành đầu vào đáng tin; và **lập Test Plan** — chốt phạm vi và luật chơi trước khi bỏ công viết TC. Cả hai đều **rẻ nhất khi làm trước dòng TC đầu tiên**: sửa REQ lúc chưa có TC thì không TC nào phải sửa theo.

## 2. Bốn việc, bốn lệnh — bản đồ của bài

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Việc</th>
<th>Lệnh</th>
<th>Khi nào cần</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>Gom tài liệu rời rạc (ticket, <code>.docx</code>, file Excel field, mockup) về <strong>một khuôn</strong> có mã REQ</td>
<td><code>/analyze-requirement-document</code></td>
<td>Dự án có tài liệu — rất hay gặp khi làm cho khách hàng</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>Rà soát chất lượng từng REQ</td>
<td>Không có lệnh riêng — bạn soát theo bảng kiểm của Skill <code>skills-requirements-analyzer</code></td>
<td><strong>Luôn luôn</strong>, kể cả khi AI báo đã tự soát</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Ghi quyết định của PO cho các điểm mờ vào tài liệu</td>
<td><code>/update-requirements-from-ticket</code></td>
<td>Mỗi lần PO/BA trả lời một đợt <code>AMB-XX</code></td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Lập kế hoạch kiểm thử</td>
<td><code>/generate-master-test-plan</code></td>
<td>Mỗi đợt kiểm thử cần kế hoạch chính thức — khách hàng/PM yêu cầu tài liệu để duyệt</td>
</tr>
</tbody>
</table>

Trong [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md), `/analyze-requirement-document` được xếp là biến thể của chặng 1, còn `/generate-master-test-plan` có mốc muộn nhất là **trước chặng 4** (chạy tay). Bài này kéo cả hai lên **trước chặng 2** — lý do nằm ở mục 7.1.

> 📌 Bài này **không** nhắc lại quy ước `REQ ID`, cấu trúc `AMB-XX`/`RISK-XX` hay luật evidence — bạn đã học kỹ ở bài trước. Bài này cũng không nói tới việc đồng bộ bộ Test Case khi yêu cầu thay đổi — đó là bài **Update Requirements → Update Test Cases → Execute Test Cases → Retest**.

### 2.1. Gọi lệnh trên Claude Code, Codex và Antigravity

Như các bài trước, ba bộ kit dùng **chung tên lệnh** — chỉ khác ký tự gõ đầu, chỗ đặt file và cách viết tên skill nền tảng:

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
<td><strong>Chuẩn hoá tài liệu</strong></td>
<td><code>/analyze-requirement-document</code></td>
<td><code>$analyze-requirement-document</code></td>
<td><code>/analyze-requirement-document</code></td>
</tr>
<tr>
<td><strong>Ghi quyết định PO</strong></td>
<td><code>/update-requirements-from-ticket</code></td>
<td><code>$update-requirements-from-ticket</code></td>
<td><code>/update-requirements-from-ticket</code></td>
</tr>
<tr>
<td><strong>Lập Test Plan</strong></td>
<td><code>/generate-master-test-plan</code></td>
<td><code>$generate-master-test-plan</code></td>
<td><code>/generate-master-test-plan</code></td>
</tr>
<tr>
<td><strong>File lệnh nằm ở</strong></td>
<td><code>.claude/commands/</code></td>
<td><code>.agents/skills/&lt;tên-lệnh&gt;/SKILL.md</code></td>
<td><code>.agent/workflows/</code></td>
</tr>
<tr>
<td><strong>Skill nền tảng chính</strong></td>
<td><code>skills-requirements-analyzer</code><br/><code>skills-test-summary-reporter</code></td>
<td><code>requirements-analyzer</code><br/><code>test-summary-reporter</code></td>
<td><code>requirements_analyzer</code><br/><code>test_summary_reporter</code></td>
</tr>
</tbody>
</table>

Toàn bài viết theo cú pháp Claude Code. Dùng Codex thì thay `/` bằng `$`; dùng Antigravity thì gõ y hệt Claude Code.

> 📌 AI Agent chưa có bộ kit riêng (Cursor, Kiro…) thì dùng prompt mẫu trong thư mục [prompts/](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/README.md): `prompt_20_analyze_requirement_document.txt`, `prompt_21_update_requirements_from_ticket.txt`, `prompt_25_generate_master_test_plan.txt`.

## 3. Khi yêu cầu đến từ tài liệu — `/analyze-requirement-document`

Bài trước đi đường "hệ thống chạy sẵn, không có tài liệu". Dự án làm cho khách hàng thì thường ngược lại: bạn nhận về một mớ — ticket Jira, file `.docx` đặc tả, file Excel danh sách field, vài ảnh mockup, và một luồng comment dài. Lệnh này gom tất cả về **một tài liệu phân tích** theo khuôn cố định: có mã REQ, có nguồn của từng dòng, có điểm mờ.

```none
/analyze-requirement-document
```

Đầu ra nằm **trong thư mục của module** mà ticket tác động, để giữ liên kết ticket ↔ module:

```none
docs/requirements/<module>/analysis/analysis_<TICKET-ID>.md
```

Bảng metadata đầu tài liệu có hai dòng bạn nên đọc đầu tiên: **`Nguồn phân tích`** — liệt kê *mọi* file và nguồn AI đã đọc; và **`Mức độ đầy đủ`** — ghi thẳng *"Đủ AC để sinh test case"* hoặc *"⚠️ Thiếu AC — chưa đủ"*. Luật nối tiếp mã ở bài trước áp nguyên ở đây: module đã dùng tới `REQ-PRJ-65` thì ticket này bắt đầu từ `REQ-PRJ-66`, và phân tích xong phải **cập nhật ngược** dải mã vào file index `requirements_<module>.md`.

> ⚠️ **Lệnh này KHÔNG sinh Test Case.** Nó chỉ phân tích, phân rã và săn điểm mờ. Tách "hiểu yêu cầu" khỏi "viết TC" là cố ý: giữa hai việc cần một chỗ dừng để bạn đọc lại — chính là phần còn lại của bài này.

### 3.1. Chốt chặn đầu vào — đưa nhầm file là sinh ra rác

Lỗi rất hay gặp: đưa cho lệnh này một file thật ra là **đầu ra** của lệnh khác. AI sẽ ngoan ngoãn "phân tích" nó và sinh ra một bản diễn đạt lại tài liệu đã có — không có mã ticket, lại có nguy cơ cấp trùng dải REQ. Vì vậy việc đầu tiên của lệnh là mở file ra kiểm dấu hiệu, trúng thì **dừng và hỏi bạn**:

<table class="rt-table">
<thead>
<tr>
<th>File bạn đưa vào</th>
<th>Thực chất là</th>
<th>Lệnh đúng</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>requirements_&lt;module&gt;.md</code>, hoặc có bảng <code>REQ ID</code> / <code>Dải mã đã dùng</code> / <code>Nhật ký thay đổi</code></td>
<td>Đầu ra của chặng 1</td>
<td>Có ticket sửa yêu cầu → <code>/update-requirements-from-ticket</code></td>
</tr>
<tr>
<td><code>system_map.md</code>, hoặc file nằm trong <code>_discovery/</code></td>
<td>Đầu ra của chặng 0</td>
<td><code>/generate-requirements-from-website</code> cho từng module</td>
</tr>
<tr>
<td>Swagger/OpenAPI, Postman collection, hoặc <code>.docx</code> chủ yếu là bảng method–path–mã lỗi mà <strong>không có Ticket ID</strong></td>
<td>Đặc tả API</td>
<td><code>/generate-requirements-from-api</code></td>
</tr>
<tr>
<td>File không xác định được Ticket ID</td>
<td>—</td>
<td>Dừng và hỏi bạn</td>
</tr>
</tbody>
</table>

> 🚫 AI bị cấm **"cố suy ra" một Ticket ID** từ tên module hay ngày tháng để chạy tiếp. Không có ID thì không đặt được tên file đầu ra, và không ai truy được REQ nào đến từ đợt phân tích nào.

### 3.2. Đọc đúng định dạng — và khai thác đúng thứ giá trị nhất

<table class="rt-table">
<thead>
<tr>
<th>Định dạng</th>
<th>Cách AI đọc</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.md</code> <code>.txt</code> <code>.html</code> <code>.xml</code> <code>.json</code>; file <code>.doc</code> export từ Jira</td>
<td>Đọc trực tiếp. File <code>.doc</code> của Jira thực chất là HTML — đọc rồi bóc thẻ</td>
</tr>
<tr>
<td><code>.docx</code> · <code>.xlsx</code>/<code>.csv</code> · <code>.pdf</code> · <code>.pptx</code></td>
<td>Uỷ quyền cho skill <code>docx</code> / <code>xlsx</code> / <code>pdf</code> / <code>pptx</code>. Đọc thẳng file nhị phân chỉ ra toàn ký tự rác</td>
</tr>
<tr>
<td>URL Jira / Confluence</td>
<td><strong>Không tự fetch.</strong> Chuyển sang <code>/fetch-jira-requirements</code>. Chưa kết nối được Jira thì dừng và báo bạn — tuyệt đối không bịa nội dung ticket</td>
</tr>
</tbody>
</table>

> 💡 **File bảng đính kèm thường giá trị hơn cả phần mô tả.** Danh sách field kèm kiểu dữ liệu, bắt buộc, độ dài → map gần như 1:1 sang Field Spec. Bảng thông báo lỗi → Validation Messages. Ma trận role × chức năng → Ma trận phân quyền. Khi trích từ file bảng, cột `Nguồn` phải ghi tới từng dòng: `field_spec.xlsx · sheet "Fields" · dòng 12` — ghi "theo tài liệu" là không ai mở lại đối chiếu được.
>
> 📌 Và **đọc hết comment**. Comment thường chứa quyết định mới nhất, đè lên phần mô tả gốc của ticket.

### 3.3. Nhiều nguồn nói khác nhau — bên nào thắng?

Có từ 2 nguồn trở lên thì AI **bắt buộc** lập bảng đối chiếu chéo trước khi viết phần phân tích:

<table class="rt-table">
<thead>
<tr>
<th>Hạng mục</th>
<th>Mô tả ticket</th>
<th>Comment</th>
<th>Mockup</th>
<th>File đính kèm</th>
<th>Kết luận</th>
</tr>
</thead>
<tbody>
<tr>
<td>Độ dài tối đa trường Tên</td>
<td>không nói</td>
<td>255</td>
<td>—</td>
<td>200</td>
<td>⚠️ Xung đột → <code>AMB-XX</code></td>
</tr>
</tbody>
</table>

Thứ tự ưu tiên mặc định khi các nguồn mâu thuẫn:

```none
1. Comment / quyết định mới nhất có ghi ngày   ← mới nhất thắng
2. AC trong phần mô tả ticket                   ← cam kết chính thức
3. File đặc tả đính kèm (CSV / XLSX / DOCX)
4. Mockup / wireframe                           ← dễ lỗi thời nhất
```

> ⚠️ **Thứ tự ưu tiên chỉ quyết định tạm test theo bên nào — xung đột vẫn phải thành một `AMB-XX`.** Bạn test theo 255 ký tự của comment, nhưng dev lại code theo file Excel ghi 200. Không có dòng AMB thì khi TC FAIL, không ai biết đó là mâu thuẫn tài liệu hay là bug — và cuộc tranh cãi bắt đầu từ con số không.

### 3.4. Tài liệu thiếu — không bao giờ viết AC thay PO

<table class="rt-table">
<thead>
<tr>
<th>Tình huống</th>
<th>Cách xử lý đúng</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ticket <strong>không có AC nào</strong>, chỉ 1–2 dòng mô tả</td>
<td>❌ Không tự viết AC. Ghi đúng những gì có, liệt kê câu hỏi dạng <code>AMB-XX</code> mức 🔴 High, và ghi thẳng ở đầu tài liệu: <em>"chưa đủ để sinh test case"</em></td>
</tr>
<tr>
<td>AC mơ hồ: "hoạt động đúng", "như module cũ"</td>
<td>Vẫn gán <code>REQ ID</code>, kèm ngay một <code>AMB-XX</code> hỏi tiêu chí cụ thể</td>
</tr>
<tr>
<td>Tham chiếu "giống module X"</td>
<td>Module X đã có tài liệu → trích REQ tương ứng và link chéo. Chưa có → <code>AMB-XX</code>, không tự suy diễn</td>
</tr>
<tr>
<td>Không nói gì về phân quyền / trạng thái</td>
<td>Ghi <strong>"Không đề cập trong tài liệu"</strong> kèm <code>AMB-XX</code></td>
</tr>
</tbody>
</table>

> 🚫 **AC do AI tự viết đọc rất hợp lý** — và đó chính là vấn đề. TC sinh từ nó rất đẹp, và cả chuỗi kiểm thử phía sau đi kiểm một hệ thống do AI tưởng tượng ra. Bộ kit xếp luật này ngang hàng với "không đoán locator": vi phạm là tài liệu mất giá trị hoàn toàn.
>
> ⚠️ **"Không đề cập" và "Không áp dụng" là hai chuyện khác nhau.** "Không áp dụng" = đã cân nhắc và kết luận không liên quan. "Không đề cập" = tài liệu thiếu, phải hỏi. Ghi nhầm cái trước cho cái sau là biến một lỗ hổng tài liệu thành một kết luận — và sẽ không ai hỏi lại nữa.

## 4. Rà soát chất lượng REQ — đừng tin bản nháp đầu tiên

Dù đi đường UI hay đường tài liệu, AI đều chạy **Cổng tự soát** trước khi ghi file — bạn đã gặp nó ở bài trước. Nhưng Cổng tự soát là **AI tự chấm bài của chính nó**. Nó bắt được những loại lỗi đã từng gặp; không có gì bảo đảm nó bắt được loại lỗi mới.

### 4.1. Những gì một lượt rà soát thật tìm ra

Ngày 2026-08-18, tài liệu module Đăng nhập của CRM demo được rà soát lại và kiểm chứng lại trên UI. Đây là một phần những gì tìm được:

<table class="rt-table">
<thead>
<tr>
<th>Lỗi phát hiện</th>
<th>Loại lỗi</th>
<th>Nếu sinh TC luôn từ bản này</th>
</tr>
</thead>
<tbody>
<tr>
<td>Giá trị cookie <code>autologin</code> thật bị chép vào 2 chỗ trong tài liệu</td>
<td>🔒 Lộ dữ liệu nhạy cảm</td>
<td>Nằm vĩnh viễn trong lịch sử Git, dù sau đó có sửa file</td>
</tr>
<tr>
<td><code>REQ-LOGIN-09</code> kết luận "không cấp cookie mới" chỉ vì <em>giá trị cookie không đổi</em> — không phân biệt được "không cấp" với "cấp lại trùng giá trị", lại bị nhiễu bởi cookie sót từ phiên trước</td>
<td>Phép thử không chứng minh được kết luận</td>
<td>TC kế thừa nguyên một phép thử vô hiệu — đúng hay sai đều không ai chứng minh được</td>
</tr>
<tr>
<td><code>REQ-LOGIN-06</code>, <code>19</code>, <code>20</code> ghi tiêu đề tab khớp tuyệt đối <code>Dashboard</code>; thật ra là <code>(16) Dashboard</code></td>
<td>Assert khớp tuyệt đối lên giá trị có phần động</td>
<td>TC đỏ hàng loạt dù hệ thống đúng</td>
</tr>
<tr>
<td><code>REQ-LOGIN-29</code> khai "hai lối đăng xuất" vì đếm 2 phần tử trong DOM — một cái có kích thước <code>0×0</code>, nằm trong khung mobile đang <code>display:none</code> ở desktop</td>
<td>Có trong DOM ≠ người dùng dùng được</td>
<td>TC kiểm một nút người dùng desktop không bao giờ bấm được</td>
</tr>
<tr>
<td><code>REQ-LOGIN-05</code> và <code>07</code> mỗi REQ gộp hai rule</td>
<td>Một REQ chứa nhiều rule</td>
<td>TC map vào REQ gộp không chứng minh được đã phủ rule nào</td>
</tr>
<tr>
<td>Danh mục evidence khai "menu đang mở" trong khi ảnh chụp menu đóng; 2 ảnh Dashboard full-page lộ tên khách hàng, số tiền</td>
<td>📸 Evidence khai sai + chưa vệ sinh dữ liệu</td>
<td>Bước sinh TC tin danh mục, rồi suy diễn phần không có trong ảnh</td>
</tr>
</tbody>
</table>

Kết quả của một lượt rà soát: **sửa 10 REQ, thêm 5 REQ, mở thêm 3 điểm mờ**. Và điều đáng nói nhất: toàn bộ luật rút ra từ lượt này đã được đưa ngược vào Skill `skills-requirements-analyzer` — **nhiều luật trong Cổng tự soát bạn thấy bây giờ sinh ra chính từ những lỗi mà người rà soát tìm được**. Cổng giúp dự án sau không lặp lại lỗi cũ; nó không thay được việc bạn đọc lại tài liệu của dự án mình.

### 4.2. Chín câu tự hỏi khi đọc lại một tài liệu Requirements

Đây là bảng kiểm nhanh ở mục 4.3.10 của [skills-requirements-analyzer](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-requirements-analyzer/SKILL.md), viết lại theo góc nhìn người review:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Câu tự hỏi</th>
<th>Nhận ra bằng cách nào</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Tên REQ và AC có cùng <strong>một mệnh đề</strong> không?</td>
<td><code>REQ-LOGIN-16</code> bản cũ: tên nói "người dùng thấy ô email rỗng", AC lại kiểm "máy chủ không trả <code>value</code>". Hai chuyện khác nhau — trình duyệt vẫn có thể tự điền</td>
</tr>
<tr>
<td>2</td>
<td>Khẳng định phủ định ("không sinh", "không gửi", "không lưu") có đủ <strong>4 bước trạng thái sạch</strong>?</td>
<td>Phải đủ: xoá sạch → xác nhận đã sạch → thực hiện hành động → kiểm có xuất hiện không. Thiếu bước 2 là phép thử vô hiệu</td>
</tr>
<tr>
<td>3</td>
<td>AC có chứa token, id, timestamp <strong>cụ thể</strong>?</td>
<td>Chuỗi dài ngẫu nhiên nằm trong AC — lần chạy sau chắc chắn khác</td>
</tr>
<tr>
<td>4</td>
<td>Tên REQ có chữ <strong>"và" / "hoặc"</strong> nối hai rule?</td>
<td>Tách ra — giữ nguyên mã cũ cho phần ở lại, cấp mã mới cho phần tách</td>
</tr>
<tr>
<td>5</td>
<td>Phần tử khai "dùng được" đã kiểm <strong>hiển thị thật</strong> chưa?</td>
<td>Đếm được trong DOM không có nghĩa là nhìn thấy, bấm được</td>
</tr>
<tr>
<td>6</td>
<td>Chuỗi thông báo là của <strong>ứng dụng</strong> hay của <strong>trình duyệt</strong>?</td>
<td>Thông báo mặc định của Chrome không phải validation của hệ thống — chuyển sang Firefox là khác</td>
</tr>
<tr>
<td>7</td>
<td>Giá trị có phần động được assert bằng <strong>"chứa"</strong> hay bằng <strong>"="</strong>?</td>
<td>Tiêu đề tab có số đếm thông báo, class có token theo cấu hình → phải là "chứa"</td>
</tr>
<tr>
<td>8</td>
<td>Tính năng sinh ra một thứ (cookie, email, file xuất) có đủ <strong>2 REQ</strong>: <em>được tạo đúng</em> và <em>dùng được đúng mục đích</em>?</td>
<td>Remember Me của CRM demo: cookie có được cấp — nhưng có tự đăng nhập lại không? Thiếu REQ thứ hai thì bảng độ phủ vẫn xanh mà tính năng không được kiểm</td>
</tr>
<tr>
<td>9</td>
<td>Các bất thường kỹ thuật có được <strong>nghi ngờ nhất quán</strong>?</td>
<td>Đã mở AMB cho mã chuyển hướng <code>307</code> bất thường thì mã <code>419</code> bất thường ở chỗ khác cũng phải được đối xử như vậy</td>
</tr>
</tbody>
</table>

### 4.3. Bốn mức tin cậy của cột `Nguồn`

Khi có **cả tài liệu lẫn hệ thống đang chạy** (mode HYBRID ở bài trước), cột `Nguồn` của mỗi REQ phân biệt 4 mức. Đọc cột này là biết REQ nào tin được tới đâu:

<table class="rt-table">
<thead>
<tr>
<th>Giá trị cột <code>Nguồn</code></th>
<th>Nghĩa</th>
<th>Khi review</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Tài liệu · &lt;file&gt; · &lt;vị trí&gt;</code></td>
<td>Chỉ có trong tài liệu, <strong>chưa</strong> mở UI kiểm</td>
<td>Là ý định, chưa phải sự thật của hệ thống</td>
</tr>
<tr>
<td><code>Tài liệu + kiểm chứng thực tế</code></td>
<td>Tài liệu nêu, đã mở UI xác nhận khớp</td>
<td><strong>Mức tin cậy cao nhất</strong></td>
</tr>
<tr>
<td><code>UI thực tế</code> / <code>Kiểm chứng thực tế</code></td>
<td>Chỉ có ở UI, tài liệu không nói</td>
<td>Tính năng ngoài tài liệu — kiểm xem đã có <code>AMB-XX</code> đi kèm chưa</td>
</tr>
<tr>
<td><code>API · &lt;method&gt; &lt;endpoint&gt;</code></td>
<td>Lấy từ request mà UI tự phát sinh</td>
<td>Thường là validation phía server — thứ ảnh chụp không thể hiện được</td>
</tr>
</tbody>
</table>

> ⚠️ **Không dùng tài liệu bán phần để suy ra vùng nó không phủ.** Spec của form tạo mới không nói gì về form sửa — dù hai form nhìn giống hệt nhau. Vùng tài liệu bỏ trắng phải khảo sát đầy đủ, không rút gọn với lý do "chắc cũng giống".

## 5. Chốt điểm mờ với PO — biến câu trả lời thành yêu cầu chính thức

Danh sách `AMB-XX` chỉ có giá trị khi được trả lời. Nhưng câu trả lời của PO thường đến qua tin nhắn, qua cuộc họp — không phải qua ticket. Nếu bạn chỉ *nhớ* câu trả lời rồi đi viết TC, tài liệu vẫn ghi câu hỏi đang treo, và lần sau AI đọc lại vẫn test theo Assumption tạm cũ.

Lệnh [update-requirements-from-ticket](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/update-requirements-from-ticket.md) ghi đúng tình huống này trong danh sách "khi nào dùng": *PO/BA vừa trả lời một AMB đang treo → cần chốt thành yêu cầu chính thức*.

```none
/update-requirements-from-ticket
```

**Không có file ticket cũng không sao.** Module Đăng nhập của CRM demo chốt hai đợt quyết định trong cùng một ngày, AI tự đặt mã đợt theo ngày để truy vết: `PO-2026-08-18` (4 điểm mờ) và `PO-2026-08-18-B` (13 điểm mờ còn lại, kèm tài khoản đủ 3 vai trò). Mỗi đợt sinh một **Impact Report** ở `docs/requirements/login/impact/`, mở đầu bằng bảng **quyết định gốc ghi nguyên văn** — kể cả những câu cộc lốc kiểu *"bỏ qua case này"*.

> 💡 **Ghi nguyên văn để làm gì?** Để sáu tháng sau, khi có người hỏi *"sao không test luồng gửi mail đặt lại mật khẩu?"*, câu trả lời là một dòng có ngày tháng và nguồn: `AMB-04` — "bỏ qua case này" — `PO-2026-08-18`. Không phải trí nhớ của một ai đó đã nghỉ việc.

### 5.1. Ba kết cục của một điểm mờ

<table class="rt-table">
<thead>
<tr>
<th>Kết cục</th>
<th>Ví dụ thật — module Đăng nhập</th>
<th>Tài liệu thay đổi thế nào</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ <strong>Đã trả lời</strong></td>
<td><code>AMB-02</code> → "không khoá" tài khoản sau nhiều lần đăng nhập sai</td>
<td>Chốt thành REQ mới <code>REQ-LOGIN-41</code>. Câu trả lời <strong>trùng</strong> Assumption tạm đã ghi → kể cả khi đã có TC thì cũng không TC nào phải sửa</td>
</tr>
<tr>
<td>⏭️ <strong>Bỏ qua</strong></td>
<td><code>AMB-15</code> → "Remember Me không hoạt động, bỏ qua"</td>
<td><code>REQ-LOGIN-40</code> ra <strong>ngoài phạm vi viết TC</strong> — giữ nguyên dòng và mã, <strong>không</strong> đổi thành 🔴 Deprecated</td>
</tr>
<tr>
<td>⏭️ <strong>Chuyển module</strong></td>
<td><code>AMB-14</code> → "để cho module khác kiểm chứng" (popup cảnh báo bộ đếm giờ)</td>
<td><code>REQ-LOGIN-30</code> vẫn thuộc <code>LOGIN</code>, ghi phụ thuộc chéo; TC của nó gắn nhãn <code>assumption-based</code> cho tới khi khảo sát module <code>TASK</code> rồi cập nhật ngược</td>
</tr>
</tbody>
</table>

> ⚠️ **Vì sao "bỏ qua" không phải Deprecated?** Deprecated nghĩa là tính năng *đã bị gỡ khỏi hệ thống*. Remember Me vẫn nằm đó — checkbox vẫn hiển thị, vẫn tích được, vẫn khiến hệ thống cấp cookie. Đánh Deprecated là **nói sai về hệ thống**; ghi "ngoài phạm vi" là **nói đúng về quyết định**. Và vì tính năng vẫn còn, AI mở thêm `RISK-08`: checkbox vẫn cấp cookie dù tính năng không hoạt động.

Quyết định của PO còn làm đổi trạng thái rủi ro: `RISK-03` (nguy cơ khoá cả đội test) **đóng** vì không có cơ chế khoá; `RISK-01` chuyển từ *nghi ngờ* sang **xác nhận** — không CAPTCHA, không giới hạn tần suất, không khoá tài khoản, tức là không có lớp nào chống thử mật khẩu hàng loạt.

### 5.2. Khi PO nói "hiện trạng là lỗi"

Đây là tình huống quan trọng nhất của cả bước chuẩn hoá. Ở đợt `PO-2026-08-18-B`, PO xác nhận hai hành vi đang chạy trên hệ thống là **lỗi**:

<table class="rt-table">
<thead>
<tr>
<th>REQ</th>
<th>Hành vi đúng — theo PO</th>
<th>Hiện trạng hệ thống</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>REQ-LOGIN-16</code></td>
<td>Sau khi đăng nhập lỗi, máy chủ <strong>phải</strong> trả lại email người dùng đã nhập</td>
<td>Ô email không nhận lại giá trị → người dùng mất email vừa gõ</td>
</tr>
<tr>
<td><code>REQ-LOGIN-25</code></td>
<td>Quên mật khẩu mà bỏ trống email <strong>phải</strong> báo trường bắt buộc</td>
<td>Báo <code>Email not found</code> — sai bản chất lỗi</td>
</tr>
</tbody>
</table>

Hai REQ này được viết lại theo **hành vi đúng**, không theo hiện trạng. Hệ quả: TC sinh từ chúng **sẽ FAIL** trên bản hiện tại — và **đó là kết quả đúng**.

> 🚫 **Tuyệt đối không sửa REQ hay TC cho khớp hiện trạng để được màu xanh.** Làm vậy là tự tay xoá mất một bug. Bài trước dạy ghi *nguyên văn hiện trạng* — vì lúc đó chưa ai biết hiện trạng đúng hay sai. Khi PO đã nói đó là lỗi, REQ phải đổi phe.
>
> 📌 Cả hai đợt quyết định diễn ra khi module **chưa có TC nào** — Impact Report ghi rõ *không có TC nào phải sửa hay archive*, bước tiếp theo là sinh TC thẳng. Đây chính là lý do nên chuẩn hoá trước: cùng những thay đổi đó mà đến sau khi đã có 50 TC thì là cả một vòng cập nhật TC và chạy lại — bài **Update Requirements → Update Test Cases → Execute Test Cases → Retest** sẽ đi sâu vòng đó.

## 6. Cổng sẵn sàng — khi nào được phép sinh Test Case

Chuẩn hoá không có nghĩa là mọi điểm mờ đều phải được trả lời — PO có thể đi họp cả tuần. Câu hỏi đúng là: **module này đã đủ điều kiện sinh TC chưa, và phần chưa đủ đã được ghi rõ chưa?** Nhìn [danh mục Requirements](https://github.com/anhtester/claude-testing-skills/blob/main/docs/requirements/README.md) thật của CRM demo tại cùng một thời điểm:

<table class="rt-table">
<thead>
<tr>
<th>Module</th>
<th>REQ</th>
<th>AMB 🔴 còn treo</th>
<th>Việc còn phải làm trước khi sinh TC</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>LOGIN</code></td>
<td>43 — <strong>39 trong phạm vi viết TC</strong></td>
<td>0 <em>(còn 1 🟡 có Assumption tạm)</em></td>
<td>✅ Không còn — không Story nào bị chặn</td>
</tr>
<tr>
<td><code>CUST</code></td>
<td>79</td>
<td>4</td>
<td>Ma trận phân quyền còn 24 ô <code>❔</code> — đã có tài khoản, cần chạy lại phần này bằng tài khoản Project Manager · một điểm mờ (xoá khách hàng đang có hoá đơn) cần môi trường riêng mới kiểm chứng được</td>
</tr>
<tr>
<td><code>PRJ</code></td>
<td>104</td>
<td>6</td>
<td>Ma trận phân quyền còn 28 ô <code>❔</code> · phạm vi cổng khách hàng chưa chốt, đang chặn <code>STORY-PRJ-03</code> (11 REQ) · 4 điểm mờ khác chờ PO: số dự án đếm lệch giữa bảng tổng quan và danh sách, dự án không có công việc báo tiến độ 100%, ngày kết thúc được phép sớm hơn ngày bắt đầu, xoá thành công nhưng chuyển tới trang báo lỗi</td>
</tr>
<tr>
<td>20 module còn lại</td>
<td>—</td>
<td>—</td>
<td>Chưa khảo sát</td>
</tr>
</tbody>
</table>

Không cần chờ cả hệ thống sạch mới được bắt đầu. `LOGIN` sinh TC được ngay; `CUST` và `PRJ` phải đợi — và **lý do phải đợi đã nằm sẵn trong danh mục**, ai mở ra cũng thấy, không cần hỏi lại người khảo sát.

### 6.1. Checklist cổng sẵn sàng — cho từng module

- ☐ Tài liệu đã qua **một lượt rà soát** theo 9 câu ở mục 4.2 — không chỉ dựa vào Cổng tự soát của AI
- ☐ Mọi `AMB-XX` 🔴 High: đã có quyết định PO ghi vào tài liệu, **hoặc** có Assumption tạm để test tiếp được
- ☐ Quyết định PO đã ghi qua `/update-requirements-from-ticket`: có mã đợt, có nguyên văn, có dòng trong Nhật ký thay đổi
- ☐ Tài liệu ghi rõ **số REQ trong phạm vi viết TC** và danh sách REQ ngoài phạm vi kèm lý do
- ☐ REQ "ghi kỳ vọng đúng mà hệ thống chưa đạt" được đánh dấu rõ — để không ai "sửa cho xanh"
- ☐ Không Story nào còn bị chặn — hoặc phần bị chặn được loại khỏi lượt sinh TC này
- ☐ Tài liệu phân tích từ ticket có `Mức độ đầy đủ` = *Đủ AC để sinh test case*
- ☐ Dòng **Năng lực kiểm thử của QA** đã có trong `docs/requirements/README.md`

> 🔒 **Năng lực kiểm thử của QA** — có quyền gọi API không, truy vấn CSDL không, kiểm tầng tích hợp không, xem nhật ký hoạt động không — là thuộc tính của **cả dự án**, không phải của từng module. Trước đây không có chỗ ghi nên AI phải hỏi lại ở từng module. Bộ kit nay chốt luật: **hỏi một lần, đo được thì đo luôn, ghi ngay vào danh mục**.
>
> CRM demo ghi: gọi API ❌, truy vấn CSDL ❌, kiểm tầng tích hợp ❌ — cả ba do đội Dev xác minh; xem nhật ký hoạt động ❌ — **đã đo thật**, trang Activity Log trả "Từ chối truy cập" với tài khoản Admin demo; DevTools trình duyệt ✅. Khi sinh TC, AI đọc đúng dòng này để quyết định nhánh kiểm thử kỹ thuật nào bạn tự làm được, nhánh nào phải ghi rõ là đội khác chịu — thay vì hỏi lại bạn ở từng module.

## 7. Test Plan — chọn đúng loại, lập đúng lúc

Requirements trả lời *"hệ thống phải làm gì"*. Nó không trả lời: đợt này test module nào, không test gì, ai làm, tốn bao nhiêu công, khi nào bắt đầu được, thế nào thì coi là xong. Đó là việc của Test Plan. Bộ kit có **ba lệnh mang chữ "plan"** — và chúng sinh ra ba loại tài liệu khác nhau hoàn toàn:

<table class="rt-table">
<thead>
<tr>
<th>Bạn cần</th>
<th>Lệnh</th>
<th>Đầu ra</th>
<th>Lưu ý</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>"Tài liệu kế hoạch gửi PM / khách hàng duyệt"</em></td>
<td><code>/generate-master-test-plan</code></td>
<td><code>docs/test-plans/test_plan_&lt;mốc&gt;.md</code> — phạm vi, chiến lược, tiêu chí vào/ra, môi trường, dữ liệu, quản lý lỗi, nhân lực, lịch, ước lượng, rủi ro</td>
<td><strong>Không</strong> sinh scenario, không sinh TC</td>
</tr>
<tr>
<td><em>"Test cái gì trước, có những kịch bản nào"</em> — khi chưa có tài liệu requirements</td>
<td><code>/generate-application-test-plan</code></td>
<td><code>test_plan.md</code> — module, user flow, scenario kèm priority P1–P4</td>
<td>Scenario <strong>không có REQ ID</strong> — không truy vết được</td>
</tr>
<tr>
<td><em>"Tính năng đi qua nhiều module nối tiếp, kết quả phụ thuộc tổ hợp lựa chọn"</em></td>
<td><code>/generate-cross-module-test-plan</code></td>
<td>Bản đồ module + ma trận kết hợp (Output-Class, Pairwise…)</td>
<td>Một form đơn lẻ thì không cần lệnh này</td>
</tr>
</tbody>
</table>

Đi theo đúng chuỗi của khoá học — đã có requirements, đã có `REQ ID` — thì loại bạn cần là **Master Test Plan**. Application test plan là lối tắt cho lúc chưa có tài liệu: nó không cấp prefix, không ghi danh mục Requirements, chạy xong vẫn phải khám phá lại nếu sau đó muốn sinh requirements.

### 7.1. Vì sao lập plan trước khi viết Test Case

Bộ kit đặt mốc muộn nhất cho Master Test Plan là trước khi chạy tay. Bài này kéo lên sớm hơn — ngay sau khi chuẩn hoá xong requirements — vì ba thứ chốt trong plan quyết định bạn bỏ công vào đâu ở bước sinh TC:

<table class="rt-table">
<thead>
<tr>
<th>Thứ chốt trong plan</th>
<th>Nếu để tới sau khi đã viết TC</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Phạm vi và ngoài phạm vi</strong></td>
<td>Đã tốn công sinh và review TC cho module, cho nền tảng, cho REQ mà PM không định test trong đợt này</td>
</tr>
<tr>
<td><strong>Tiêu chí ra (exit)</strong></td>
<td>Nhìn kết quả rồi mới đặt ngưỡng — bộ kit gọi thẳng tên việc đó: <em>hợp thức hoá kết quả, không phải đánh giá</em></td>
</tr>
<tr>
<td><strong>Loại test trong phạm vi, đội nào làm</strong></td>
<td>TC nhánh API, CSDL được viết ra cho một đội QA không có quyền chạy chúng</td>
</tr>
</tbody>
</table>

> 💡 Plan lập trước TC sẽ còn nhiều ô chưa có số — số TC, độ phủ. Không sao. **Plan là tài liệu có phiên bản**: bản đầu chốt các quyết định, bản sau bổ sung khi TC đã có. Cách cập nhật đúng nằm ở mục 9.4 — tóm lại là **sửa phiếu đầu vào rồi chạy lại lệnh, không viết đè plan**, vì plan là tài liệu đã được duyệt, viết đè là mất dấu vết thứ đã thống nhất.

### 7.2. Plan không đứng một mình — ba tài liệu nối bằng một mã mốc

Plan công bố phạm vi và tiêu chí **trước** đợt. Trong đợt có báo cáo tiến độ theo dõi lịch của plan; cuối đợt có báo cáo tổng hợp chấm lại đúng bộ tiêu chí đó. Ba tài liệu dùng **chung một mã mốc** (chữ thường, không dấu, ví dụ `release_1.0`) — đó là mối nối để lệnh sau tự tìm ra tài liệu trước, không phải hỏi lại bạn:

```none
docs/test-plans/test_plan_release_1.0.md                 ← Master Test Plan — lập TRƯỚC đợt
docs/test-plans/test_plan_release_1.0.input.yaml         ← bản lưu phiếu đầu vào đã dùng
docs/executions/test_progress_release_1.0_<YYYYMMDD>.md  ← báo cáo tiến độ từng kỳ TRONG đợt
docs/executions/test_summary_release_1.0_<timestamp>.md  ← báo cáo tổng hợp CUỐI đợt
```

<table class="rt-table">
<thead>
<tr>
<th>Lệnh</th>
<th>Khi nào</th>
<th>Trả lời câu hỏi nào</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/generate-master-test-plan</code></td>
<td>1 lần / đợt, gọi lại khi phạm vi hay lịch đổi</td>
<td>Đợt này test gì, không test gì, ai làm, khi nào coi là xong</td>
</tr>
<tr>
<td><code>/generate-test-progress-report</code></td>
<td>Mỗi kỳ theo lịch của plan — thường hằng tuần</td>
<td>Kỳ này làm được gì, có kịp mốc không, đang vướng gì, kỳ tới làm gì. <strong>Không</strong> khuyến nghị có nên release</td>
</tr>
<tr>
<td><code>/generate-test-summary-report</code></td>
<td>Mỗi mốc release</td>
<td>Có nên release không — chấm lại tiêu chí exit mà plan đã công bố</td>
</tr>
</tbody>
</table>

> 📌 Báo cáo tiến độ **không có plan thì không kết luận được "trễ" hay "đúng hạn"** — vẫn có số liệu, nhưng không có mốc để so. Và cần đổi lịch hay phạm vi thì báo cáo tiến độ chỉ **đề xuất**; cập nhật thật phải đi qua `/generate-master-test-plan`. Sửa ngầm trong báo cáo là mất dấu thứ đã được duyệt. Trên Codex gọi `$generate-test-progress-report`; bộ kit Antigravity hiện chưa có lệnh này.

## 8. Lập Master Test Plan với `/generate-master-test-plan`

```none
/generate-master-test-plan
```

### 8.1. Hai nguồn dữ liệu — AI đọc repo, bạn điền phiếu

Lệnh tách rạch ròi hai loại thông tin, và **không trộn vai**: thứ suy ra được thì AI tự lấy từ `docs/`, không hỏi lại bạn; thứ chỉ người mới biết thì lấy từ một **phiếu YAML** do bạn điền.

<table class="rt-table">
<thead>
<tr>
<th>AI tự đọc</th>
<th>Lấy ra</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>docs/requirements/README.md</code></td>
<td>Module, prefix, số REQ, điểm mờ 🔴 còn treo, REQ ⚪ đã loại kèm lý do · môi trường dùng chung hay riêng · vai trò tài khoản · <strong>năng lực kiểm thử của QA</strong></td>
</tr>
<tr>
<td><code>docs/requirements/_discovery/system_map.md</code></td>
<td>Nền tảng của từng module · phụ thuộc · vùng đã loại khỏi phạm vi</td>
</tr>
<tr>
<td><code>docs/requirements/&lt;module&gt;/…</code></td>
<td>Rủi ro sản phẩm đã ghi (<code>RISK-xx</code>) · phiên bản tài liệu làm cơ sở kiểm thử</td>
</tr>
<tr>
<td><code>docs/testcases/</code> <em>(nếu đã có)</em></td>
<td>Số TC theo nền tảng · bộ chạy đề xuất · mọi ô <code>➖ Ngoài phạm vi</code> ở bảng ISO/IEC 25010 → chép thẳng vào mục Ngoài phạm vi của plan</td>
</tr>
<tr>
<td><code>docs/bugs/</code> · <code>docs/executions/</code></td>
<td>Bug đang mở theo Severity · lần chạy đã có · thời lượng thực tế của đợt trước (dữ liệu cho ước lượng)</td>
</tr>
<tr>
<td>Project automation, file CI <em>(nếu có)</em></td>
<td>Đã có framework, pipeline, bao nhiêu script</td>
</tr>
</tbody>
</table>

Phần còn lại bạn điền vào [plans/master-test-plan/test\_plan.config.yaml](https://github.com/anhtester/claude-testing-skills/blob/main/plans/master-test-plan/test_plan.config.yaml). Tên ô viết tiếng Việt, chú thích cạnh mỗi ô ghi sẵn giá trị hợp lệ. Muốn xem một phiếu đã điền đủ thì mở [test\_plan.template.yaml](https://github.com/anhtester/claude-testing-skills/blob/main/plans/master-test-plan/test_plan.template.yaml) (hệ thống hư cấu) cùng plan sinh ra từ nó. Đây là đoạn đầu phiếu thật của CRM demo:

```none
Mốc:
  Tên: Release 1.0
  Mã mốc: release_1.0           # chữ thường, không dấu, nối bằng _ — dùng đặt tên file
  Phiên bản phần mềm: v1.0.0    # số build / version của đợt — DEV cung cấp

Phạm vi:
  Trong phạm vi:
    - Module: LOGIN
      Nền tảng: [web]           # web | mobile | api — được ghi nhiều
    - Module: CUST
      Nền tảng: [web]
    - Module: PRJ
      Nền tảng: [web]
```

Chỉ hai nhóm **Mốc** và **Phạm vi** là bắt buộc. Các nhóm khác gom theo đúng người thường nắm thông tin:

<table class="rt-table">
<thead>
<tr>
<th>Nhóm trong phiếu</th>
<th>Vì sao AI không tự biết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Mốc · Phạm vi</strong></td>
<td>Release nào, cặp module × nền tảng nào, ngoài phạm vi bổ sung — là quyết định kinh doanh</td>
</tr>
<tr>
<td><strong>Lịch · Nhân lực</strong></td>
<td>Ngày duyệt plan, bắt đầu thực thi, code freeze, release · tần suất báo cáo tiến độ · ai phụ trách cặp nào</td>
</tr>
<tr>
<td><strong>Môi trường · Dữ liệu kiểm thử · Công cụ</strong></td>
<td>Môi trường đợt này có khác môi trường đã khảo sát không · dữ liệu nền lấy từ đâu, có dữ liệu thật của khách hàng không, ai dọn · Jira hay file trong repo là nguồn chính khi lệch</td>
</tr>
<tr>
<td><strong>Cấp độ · Độc lập · Loại kiểm thử · Phi chức năng</strong></td>
<td>Đợt gồm cấp độ nào, đội test độc lập tới mức nào · hiệu năng, bảo mật, tương thích có làm không, ngưỡng chấp nhận bao nhiêu</td>
</tr>
<tr>
<td><strong>Chiến lược tự động hoá</strong></td>
<td>Tự động cái gì, không tự động cái gì, chạy khi nào, ai bảo trì — chỉ điền khi đợt có automation</td>
</tr>
<tr>
<td><strong>Ước lượng · Ngân sách</strong></td>
<td>Kỹ thuật ước lượng và con số công sức (người-ngày) · có ngân sách riêng không</td>
</tr>
<tr>
<td><strong>Quản lý lỗi</strong></td>
<td>Dùng quy trình và thang Severity/Priority mặc định hay workflow Jira riêng · ai phân loại lỗi · thời hạn phản hồi và sửa theo Severity</td>
</tr>
<tr>
<td><strong>Tiêu chí</strong></td>
<td>Bộ tiêu chí ra mặc định hay thêm/riêng · ai được chấp nhận dừng khi hết thời gian · dùng ngưỡng tạm dừng đề xuất không</td>
</tr>
<tr>
<td><strong>Bên liên quan · Phê duyệt · Chuẩn tổ chức</strong></td>
<td>Ai nhận tài liệu nào, qua kênh gì · ai duyệt · khách có template riêng không · tổ chức có Test Policy/Test Strategy không</td>
</tr>
</tbody>
</table>

Phiếu có một quy ước nhỏ nhưng quan trọng — phân biệt **chưa chốt** với **đã quyết là không**:

<table class="rt-table">
<thead>
<tr>
<th>Bạn ghi</th>
<th>Nghĩa</th>
<th>Plan ghi</th>
</tr>
</thead>
<tbody>
<tr>
<td>Để trống</td>
<td><strong>Chưa chốt</strong></td>
<td><code>❓</code> + đưa vào danh sách ô còn treo</td>
</tr>
<tr>
<td><code>không</code></td>
<td><strong>Đã quyết định là không</strong></td>
<td>Ghi rõ "không" — <strong>không</strong> phải ô treo</td>
</tr>
<tr>
<td><code>có</code></td>
<td>Đã quyết định là có</td>
<td>Nội dung tương ứng</td>
</tr>
</tbody>
</table>

> 💡 **Không muốn điền phiếu?** Gọi lệnh kèm tên mốc, AI hỏi **một lượt** theo đúng các nhóm trên rồi tự ghi câu trả lời vào `test_plan.config.yaml`. Lần cập nhật sau đã có phiếu để sửa, không phải hỏi lại từ đầu. Ngày trong phiếu viết `DD-MM-YYYY` (ví dụ `17-09-2026`) — AI **không** hiểu theo kiểu Mỹ, `05-10-2026` là ngày 5 tháng 10.

> 🚫 **Không bịa lịch, nhân lực, công sức, ngân sách, tên người, thời hạn xử lý lỗi** — AI không có cách nào biết những thứ đó. Thiếu thì ô ghi `❓ Chờ <ai> cung cấp`, và **danh sách ô còn treo nằm ở đầu tài liệu**, gom theo người phải trả lời, để người duyệt thấy ngay plan chưa hoàn chỉnh ở đâu. Một plan điền đủ số trông chuyên nghiệp hơn — và nguy hiểm hơn: PM ký duyệt một lịch trình mà không ai cam kết. 🔒 URL, tài khoản, token nằm ở `.env` — không ghi vào plan, cũng không ghi vào phiếu, vì phiếu được commit cùng plan.

### 8.2. Plan gồm những gì

Plan mở đầu bằng mục **Kiểm soát tài liệu** (phiên bản, trạng thái, người lập, người review, mức phân loại, lịch sử thay đổi, danh sách ô còn treo), rồi tới 12 mục:

**Kiểm soát tài liệu**

- Thông tin tài liệu
- Lịch sử thay đổi

**1. Mục tiêu & Cơ sở kiểm thử**

- 1.1 Mục tiêu kiểm thử
- 1.2 Cơ sở kiểm thử (Test basis)

**2. Phạm vi**

- 2.1 Trong phạm vi
- 2.2 NGOÀI phạm vi (out of scope)
- 2.3 Giả định & Ràng buộc
- 2.4 Các bên liên quan & Giao tiếp

**3. Chiến lược kiểm thử (Test approach)**

- 3.1 Cấp độ kiểm thử
- 3.2 Loại kiểm thử
  - 3.2.1 Kiểm thử phi chức năng
- 3.3 Kỹ thuật thiết kế test
- 3.4 Mức độc lập của kiểm thử
- 3.5 Retest & Regression
- 3.6 Chỉ số theo dõi
- 3.7 Chiến lược tự động hoá

**4. Tiêu chí Vào / Ra**

- 4.1 Tiêu chí VÀO (Entry): chưa đủ thì CHƯA bắt đầu test
- 4.2 Tiêu chí RA (Exit)
- 4.3 Tiêu chí TẠM DỪNG (Suspension) & tiếp tục

**5. Môi trường, Dữ liệu & Công cụ**

- 5.1 Môi trường kiểm thử
- 5.2 Quản lý dữ liệu kiểm thử
- 5.3 Công cụ

**6. Nhân lực & Phân công**

**7. Lịch trình, Ước lượng & Ngân sách**

- 7.1 Lịch trình & Mốc
- 7.2 Ước lượng công sức
- 7.3 Ngân sách

**8. Rủi ro**

- 8.1 Rủi ro DỰ ÁN & biện pháp
- 8.2 Rủi ro SẢN PHẨM (tóm tắt)

**9. Quản lý lỗi**

- 9.1 Quy trình trạng thái lỗi
- 9.2 Thang Severity
- 9.3 Thang Priority
- 9.4 Phân loại lỗi & thời hạn xử lý

**10. Sản phẩm bàn giao**

**11. Phê duyệt**

**12. Ánh xạ chuẩn tài liệu**

- 12.1 Đối chiếu mục
- 12.2 Điểm làm khác chính sách & chiến lược kiểm thử chung (Deviations)

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Người duyệt đọc ra được gì</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Mục tiêu &amp; Cơ sở kiểm thử</td>
<td>Đợt này nhắm tới điều gì đo được · tài liệu nào làm căn cứ</td>
</tr>
<tr>
<td>2. Phạm vi</td>
<td>Trong phạm vi theo <strong>cặp module × nền tảng</strong> · ngoài phạm vi · giả định, ràng buộc · ai nhận tài liệu nào</td>
</tr>
<tr>
<td>3. Chiến lược kiểm thử</td>
<td>Cấp độ · loại kiểm thử (kể cả <strong>phi chức năng</strong>) · kỹ thuật thiết kế test · mức độc lập · retest &amp; regression · chỉ số theo dõi · <strong>chiến lược tự động hoá</strong></td>
</tr>
<tr>
<td>4. Tiêu chí vào / ra / tạm dừng</td>
<td>Khi nào được bắt đầu, khi nào coi là xong, khi nào phải dừng — mục 9 của bài</td>
</tr>
<tr>
<td>5. Môi trường, Dữ liệu &amp; Công cụ</td>
<td>Môi trường nào · <strong>dữ liệu kiểm thử</strong> lấy từ đâu, che dữ liệu thật thế nào, ai dọn · công cụ nào là nguồn chính</td>
</tr>
<tr>
<td>6. Nhân lực &amp; Phân công</td>
<td>Ai phụ trách cặp nào, có cần đào tạo hay tuyển thêm</td>
</tr>
<tr>
<td>7. Lịch trình, Ước lượng &amp; Ngân sách</td>
<td>Các mốc · <strong>công sức ước lượng</strong> kèm công thức để người duyệt tự tính lại · ngân sách</td>
</tr>
<tr>
<td>8. Rủi ro</td>
<td>8.1 rủi ro <strong>dự án</strong> kèm biện pháp · 8.2 <strong>tóm tắt</strong> rủi ro <strong>sản phẩm</strong>, link về tài liệu gốc</td>
</tr>
<tr>
<td>9. Quản lý lỗi</td>
<td>Quy trình trạng thái lỗi · thang Severity/Priority · ai phân loại · thời hạn xử lý</td>
</tr>
<tr>
<td>10–12</td>
<td>Sản phẩm bàn giao · Phê duyệt · Ánh xạ chuẩn tài liệu và điểm làm khác chiến lược chung</td>
</tr>
</tbody>
</table>

> 📌 Thang Severity/Priority mặc định ở mục 9 lấy nguyên văn từ Skill `skills-bug-reporter`. Lý do giống hệt tiêu chí exit: tiêu chí #1, #2 đếm bug theo Severity — plan và bug report dùng hai thang khác nhau là đếm lệch.

### 8.3. Mục "Ngoài phạm vi" — dòng bảo vệ chính đội QA

Khi có sự cố trên production, câu hỏi đầu tiên luôn là *"sao QA không test cái này?"*. Plan ghi rõ *"pentest không thuộc phạm vi đợt này — đã thống nhất ngày …"* thì đó là **quyết định đã thống nhất từ trước**, không phải QA bỏ sót. Bộ kit gọi đây là mục có giá trị pháp lý cao nhất trong plan. Ba dòng trong plan thật của CRM demo:

<table class="rt-table">
<thead>
<tr>
<th>Không kiểm thử</th>
<th>Lý do</th>
<th>Ai chịu trách nhiệm</th>
<th>Nguồn quyết định</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cổng khách hàng (khu ngoài <code>/admin</code>)</td>
<td>Loại khỏi đợt — 11 REQ của <code>PRJ</code> chỉ kiểm được mức biểu mẫu ghi nhận đúng</td>
<td>Chờ PO chốt phạm vi cổng khách hàng</td>
<td>QA Lead, 17-09-2026</td>
</tr>
<tr>
<td>Kiểm chứng tầng API · CSDL · tích hợp</td>
<td>QA không có quyền</td>
<td>Đội Dev xác minh</td>
<td>Dòng Năng lực kiểm thử của QA trong danh mục</td>
</tr>
<tr>
<td>Pentest · quét lỗ hổng</td>
<td>Ngoài năng lực manual TC</td>
<td>Đội bảo mật / đối tác độc lập</td>
<td>Bảng ISO/IEC 25010 của <code>test_cases_login.md</code></td>
</tr>
</tbody>
</table>

Mỗi dòng đủ bốn cột. Để ý cột cuối: phần lớn các dòng **AI tự lấy từ repo** — quyết định PO ở mục 5.1, vùng đã loại trong `system_map.md`, ô `➖` của bảng ISO/IEC 25010. Bạn chỉ khai thêm phần **chưa có** trong `docs/`. Một lưu ý nữa: module có mặt mobile hay API mà đợt này **không kiểm** thì phải ghi vào đây — không được im lặng chỉ khai phần web.

### 8.4. Chuẩn tài liệu — ghi đúng, đừng nói quá

Template của lệnh bám khung **Test Plan của ISO/IEC/IEEE 29119-3** — chuẩn hiện hành về tài liệu kiểm thử, thay thế họ IEEE 829 — và phủ đủ **nội dung điển hình của test plan** mà giáo trình **ISTQB CTFL v4.0** liệt kê ở mục 5.1.1. Cuối plan có bảng ánh xạ sang **cả ba**: 29119-3, ISTQB, và khung 16 mục của **IEEE 829-1998** mà nhiều khách hàng, công ty outsourcing vẫn quen mặt. Khi nghiệm thu hợp đồng hay audit, người duyệt hỏi *"plan này theo chuẩn nào"* — có bảng ánh xạ thì trả lời bằng một trang. Nhưng ghi chuẩn có luật:

<table class="rt-table">
<thead>
<tr>
<th>Được viết</th>
<th>Không được viết</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>"Biên soạn <strong>theo cấu trúc</strong> ISO/IEC/IEEE 29119-3"</em></td>
<td><em>"Tuân thủ ISO/IEC/IEEE 29119"</em></td>
<td>Tuân thủ là kết luận của đánh giá viên, không phải của người viết tài liệu</td>
</tr>
<tr>
<td>Tên mục của chuẩn: <em>Test strategy — Suspension and resumption criteria</em></td>
<td>Số điều khoản của 29119-3 hay 829: <em>clause 7.3.2</em></td>
<td>Số điều khoản đổi giữa các bản phát hành, và AI không có bản chuẩn trong tay để tra — ghi số là bịa. Riêng ISTQB được ghi số mục (<em>5.1.1</em>) vì bộ kit đã đối chiếu trực tiếp giáo trình v4.0</td>
</tr>
<tr>
<td>Khách yêu cầu đúng <strong>IEEE 829-2008</strong> → xin file template của khách rồi ánh xạ theo file đó</td>
<td>Dùng bảng ánh xạ 829-1998 cho khách yêu cầu 829-2008</td>
<td>Hai bản 829 có cấu trúc khác nhau: bản 2008 tách Master Test Plan và Level Test Plan với dàn mục lồng nhau</td>
</tr>
<tr>
<td>Mục <em>Điểm làm khác chiến lược chung</em> có nội dung, hoặc ghi <code>Không áp dụng</code></td>
<td>Để bảng trống</td>
<td>Trống nghĩa là "chưa ai xem xét" — khác hẳn "đã xem và không có gì khác biệt"</td>
</tr>
</tbody>
</table>

### 8.5. Plan thật của CRM demo — Release 1.0

Repo bộ kit có sẵn một plan đã lập cho CRM demo: [docs/test-plans/test\_plan\_release\_1.0.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/test-plans/test_plan_release_1.0.md), kèm bản lưu phiếu [test\_plan\_release\_1.0.input.yaml](https://github.com/anhtester/claude-testing-skills/blob/main/docs/test-plans/test_plan_release_1.0.input.yaml). Mở ra đọc cùng bảng dưới — đây là những gì một plan trung thực trông như thế nào:

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Nội dung</th>
<th>Lấy từ đâu</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Kiểm soát tài liệu</strong></td>
<td>Phiên bản <code>v1.3</code> · 🟨 Draft · <strong>12 ô còn treo</strong> ở đầu tài liệu, gom theo người phải trả lời (QA Lead · QA Lead cùng PO · đội Dev)</td>
<td>Mọi ô trống trong phiếu</td>
</tr>
<tr>
<td><strong>Trong phạm vi</strong></td>
<td>3 cặp: <code>LOGIN</code> × web (50 TC, đã chạy 41/50) · <code>CUST</code> × web (79 REQ, 0 TC) · <code>PRJ</code> × web (104 REQ, 0 TC)</td>
<td>Phiếu (cặp nào) + <code>docs/</code> (số REQ, TC, lần chạy)</td>
</tr>
<tr>
<td><strong>REQ đưa lại</strong></td>
<td>5 REQ ⚪ trước đây bị loại <strong>chỉ vì</strong> khảo sát trên môi trường dùng chung — đợt này có môi trường riêng nên đưa lại, kèm việc phải khảo sát bổ sung trước khi sinh TC</td>
<td>Phiếu: <code>Đưa lại REQ bị loại vì môi trường: có</code></td>
</tr>
<tr>
<td><strong>Lịch</strong></td>
<td>Duyệt plan 21-09 · xong TC 02-10 · môi trường sẵn sàng 05-10 · bắt đầu thực thi 06-10 · code freeze 19-11 · release 15-12-2026 · báo cáo tiến độ thứ Sáu hằng tuần</td>
<td>Phiếu</td>
</tr>
<tr>
<td><strong>Ước lượng</strong></td>
<td>Ba điểm: <strong>19,0 ± 1,3 người-ngày</strong>, chưa gồm automation — kèm công thức E = (a + 4m + b) / 6</td>
<td>Phiếu (a, m, b) · AI tính</td>
</tr>
<tr>
<td><strong>Tiêu chí ra</strong></td>
<td>Bộ mặc định · tại ngày lập, tiêu chí <strong>#1 chưa đạt</strong> vì bug Critical <code>TC039</code> (trang đăng nhập chạy HTTP) còn mở</td>
<td><code>skills-test-summary-reporter</code> + <code>docs/bugs/</code></td>
</tr>
<tr>
<td><strong>Rủi ro dự án</strong></td>
<td>13 dòng, ví dụ: <code>R7</code> môi trường sẵn sàng ngay trước ngày bắt đầu — không còn ngày đệm cho smoke · <code>R12</code> ước lượng thấp bất thường so với 183 REQ chưa có TC</td>
<td>AI đối chiếu phiếu với dữ liệu repo</td>
</tr>
</tbody>
</table>

> 💡 Để ý `R12`: con số 19,0 người-ngày do người điền phiếu đưa ra. AI thấy nó thấp so với khối lượng — riêng bộ Regression của `LOGIN` đã mất khoảng 3 giờ 40 phút một lượt — nhưng **không tự sửa con số**. Nó giữ nguyên số của bạn và đưa nghi ngờ thành một dòng rủi ro kèm căn cứ. Quyết định vẫn là của người lập kế hoạch; việc của AI là để nghi ngờ đó không bị ai bỏ qua.

> 📌 Plan tách **rủi ro dự án** (8.1 — rủi ro của việc kiểm thử: môi trường, lịch, nhân lực, dữ liệu) khỏi **rủi ro sản phẩm** (8.2 — module nào hỏng thì thiệt hại lớn). Mục 8.2 chỉ **tóm tắt** vài rủi ro cao nhất mỗi module kèm link về `RISK-xx` trong tài liệu requirements; nguồn chính vẫn là tài liệu đó và đánh giá RBT khi sinh TC ở bài kế tiếp. Sửa rủi ro ở tài liệu nguồn, không sửa trong plan. Trộn hai loại vào một bảng thì PM không biết dòng nào là việc của mình phải xử lý.

## 9. Tiêu chí vào, ra, tạm dừng — hợp đồng chốt trước khi có kết quả

### 9.1. Tiêu chí vào — chưa đủ thì chưa bắt đầu

Tiêu chí vào chia ba nhóm theo ISTQB CTFL v4.0: **nguồn lực** đã sẵn · **testware** đã sẵn · **chất lượng ban đầu** của đối tượng kiểm thử đủ để bắt đầu.

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Nhóm</th>
<th>Điều kiện</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Nguồn lực</td>
<td>Nhân lực đã phân công, đủ người cho mọi cặp module × nền tảng</td>
</tr>
<tr>
<td>2</td>
<td>Nguồn lực</td>
<td>Môi trường test sẵn sàng, có dữ liệu nền</td>
</tr>
<tr>
<td>3</td>
<td>Nguồn lực</td>
<td>Tài khoản test đủ mọi vai trò trong phạm vi</td>
</tr>
<tr>
<td>4</td>
<td>Nguồn lực</td>
<td>Công cụ sẵn sàng: quản lý bug · quản lý kết quả · automation</td>
</tr>
<tr>
<td>5</td>
<td>Nguồn lực</td>
<td>Ngân sách đã duyệt <em>(khi có ngân sách riêng)</em></td>
</tr>
<tr>
<td>6</td>
<td>Testware</td>
<td>Tài liệu requirements của mọi cặp module × nền tảng trong phạm vi đã có</td>
</tr>
<tr>
<td>7</td>
<td>Testware</td>
<td>Điểm mờ 🔴 đã được giải đáp, hoặc người duyệt chấp nhận để treo</td>
</tr>
<tr>
<td>8</td>
<td>Testware</td>
<td>Test case đã viết <strong>và đã review</strong> — đủ từng nền tảng</td>
</tr>
<tr>
<td>9</td>
<td>Chất lượng ban đầu</td>
<td>Build đã deploy và truy cập được</td>
</tr>
<tr>
<td>10</td>
<td>Chất lượng ban đầu</td>
<td>Smoke test đã pass</td>
</tr>
<tr>
<td>11</td>
<td>Chất lượng ban đầu</td>
<td><em>(có mobile)</em> Bản build app cài được trên thiết bị · app Flutter đã bật semantics</td>
</tr>
<tr>
<td>12</td>
<td>Chất lượng ban đầu</td>
<td><em>(có API)</em> Snapshot spec khớp build đang test · có quyền gọi thử</td>
</tr>
</tbody>
</table>

> ⚠️ **Bắt đầu test khi chưa đạt tiêu chí vào** là nguyên nhân số một khiến kết quả kiểm thử không dùng được: BLOCKED tràn lan, phải chạy lại từ đầu. Thiếu điều kiện nào thì báo PM — đừng bắt đầu rồi chữa sau. Để ý điều kiện 8: plan lập trước TC, nên ở bản đầu dòng này chắc chắn **chưa đạt** — plan CRM demo ghi `🟨 1/3` vì `CUST` và `PRJ` chưa có TC, và ghi đúng như vậy là trung thực. Plan không cần mọi tiêu chí vào đều xanh lúc lập; nó cần chúng xanh **trước khi bắt đầu chạy test**. Dòng 11, 12 chỉ giữ lại khi phạm vi có mobile hay API.

### 9.2. Tiêu chí ra — một bộ, dùng cho cả hai đầu đợt kiểm thử

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Tiêu chí</th>
<th>Ngưỡng mặc định</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Bug Critical đang mở</td>
<td><strong>0</strong></td>
</tr>
<tr>
<td>2</td>
<td>Bug Major đang mở</td>
<td>0, hoặc có workaround được PM chấp nhận bằng văn bản</td>
</tr>
<tr>
<td>3</td>
<td>Pass rate TC Priority High</td>
<td><strong>≥ 95%</strong></td>
</tr>
<tr>
<td>4</td>
<td>Pass rate toàn bộ TC đã chạy</td>
<td>≥ 90%</td>
</tr>
<tr>
<td>5</td>
<td>Tỷ lệ BLOCKED</td>
<td>≤ 5%</td>
</tr>
<tr>
<td>6</td>
<td>REQ mức Critical có ít nhất 1 TC PASS</td>
<td>100%</td>
</tr>
<tr>
<td>7</td>
<td>Module trong phạm vi đã có TC và đã chạy — tính trên <strong>từng cặp module × nền tảng</strong></td>
<td>100%</td>
</tr>
</tbody>
</table>

Bộ này **không do lệnh lập plan tự nghĩ ra**. Nó lấy nguyên văn từ Skill [skills-test-summary-reporter](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-test-summary-reporter/SKILL.md) — chính skill mà `/generate-test-summary-report` dùng để chấm cuối đợt. **Plan công bố trước, báo cáo tiến độ theo dõi trong đợt, báo cáo tổng hợp chấm lại sau — cùng một bộ.** Hai bên lệch nhau thì đến lúc release sẽ cãi nhau về chuẩn thay vì bàn về chất lượng. Có plan rồi thì lệnh báo cáo tổng hợp tự đọc mục 4.2 của plan, không hỏi lại bạn.

<table class="rt-table">
<thead>
<tr>
<th>Điểm cần hiểu</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>#7 chấm theo <strong>cặp module × nền tảng</strong></td>
<td>Module đã chạy trên web nhưng mặt mobile trong phạm vi chưa chạy thì cặp mobile là <strong>chưa đạt</strong> — không được tính đủ nhờ lần chạy web</td>
</tr>
<tr>
<td>Dự án muốn thêm tiêu chí → ghi vào <strong>bảng bổ sung</strong>, đánh số tiếp từ #8</td>
<td>Bảng mặc định giữ nguyên văn để plan nào cũng so được với nhau. Gợi ý của ISTQB cho bảng bổ sung: mật độ lỗi · đã review requirements và TC · mọi lỗi tìm thấy đã được báo cáo</td>
</tr>
<tr>
<td><strong>Dừng vì hết thời gian hoặc ngân sách</strong> là hợp lệ — có điều kiện</td>
<td>Chỉ khi người có quyền (khai ở phiếu) đã xem xét và <strong>chấp nhận bằng văn bản</strong> rủi ro phát hành. Báo cáo tổng hợp vẫn ghi tiêu chí nào chưa đạt và ai chấp nhận — <strong>không</strong> chấm lại thành "Đạt"</td>
</tr>
</tbody>
</table>

> ⚠️ **Chỉ có Đạt / Không đạt / Không áp dụng — không có "gần đạt".** Pass rate TC High 94.8% so với ngưỡng 95% là **không đạt**. Có thể chấp nhận, nhưng phải ghi là ngoại lệ có người duyệt. Và cho tới khi PM chọn giữ hay thay, plan phải ghi rõ đây là *bộ mặc định của agent — chờ PM xác nhận*.

### 9.3. Tạm dừng và tiếp tục

Plan còn chốt trước **lúc nào phải dừng**. Template của bộ kit đề xuất: môi trường sập quá 4 giờ · build lỗi đến mức không đăng nhập được · hơn 30% TC BLOCKED cùng một nguyên nhân · phát hiện bug Critical chặn luồng chính · *(có mobile)* bản build không cài hoặc không mở được. Tiếp tục khi nguyên nhân đã được xử lý, có build mới, và đã chạy lại smoke. Các ngưỡng này là **đề xuất của agent** — phiếu ghi `Dùng ngưỡng tạm dừng đề xuất: có` thì plan ghi *đã xác nhận*, ghi `không` thì bạn khai danh sách riêng.

> 💡 **Vì sao phải viết ra từ trước?** Vì giữa đợt, khi deadline đang dí, không ai muốn là người đề nghị dừng. Có sẵn một dòng đã được PM duyệt thì việc dừng là **làm đúng plan**, không phải ý kiến cá nhân của tester.

### 9.4. Cập nhật plan giữa đợt — sửa phiếu, không viết đè plan

Phạm vi, lịch hay nhân lực đổi giữa đợt là chuyện thường. Cách đúng:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Việc</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Sửa <code>test_plan.config.yaml</code> rồi gọi lại <code>/generate-master-test-plan</code></td>
<td>Plan đã có thì lệnh <strong>không</strong> viết lại từ đầu</td>
</tr>
<tr>
<td>2</td>
<td>AI so phiếu mới với bản lưu <code>test_plan_&lt;mốc&gt;.input.yaml</code>, liệt kê đúng các mục đổi cho bạn xác nhận</td>
<td>Bản lưu chính là lý do phiếu được commit cùng plan — không có nó thì không biết đổi gì</td>
</tr>
<tr>
<td>3</td>
<td>Sửa đúng các mục đó · tăng phiên bản: đổi nội dung <code>v1.0 → v1.1</code>, đổi phạm vi lớn hoặc đổi tiêu chí exit <code>→ v2.0</code> · thêm dòng <strong>Lịch sử thay đổi</strong></td>
<td>Người duyệt đọc lịch sử là biết bản mới khác bản đã ký ở đâu</td>
</tr>
<tr>
<td>4</td>
<td>Trạng thái về 🟨 Draft, thêm dòng phê duyệt mới</td>
<td>Chữ ký của bản cũ <strong>không</strong> tự áp cho bản mới</td>
</tr>
<tr>
<td>5</td>
<td>Đổi tiêu chí exit <strong>sau khi đã chạy test</strong> → ghi rõ lý do và thời điểm</td>
<td>Báo cáo tổng hợp sẽ nêu việc này ra — đổi ngưỡng sau khi đã thấy số là đúng thứ bộ kit cấm</td>
</tr>
</tbody>
</table>

Plan CRM demo đã đi qua bốn phiên bản trong cùng một ngày. Bản `v1.2` chẳng hạn: phiếu bổ sung build, lịch mới, ước lượng, và quyết định đưa lại 5 REQ — Lịch sử thay đổi ghi đủ các mục đổi và chốt thêm một dòng *"**Không** đổi tiêu chí exit"*. Chính dòng đó cho người duyệt biết bản mới vẫn giữ nguyên chuẩn chấm.

## 10. Nghiệm thu trước khi sang bài Test Case

### 10.1. Checklist

**Phần Requirements** — checklist cổng sẵn sàng ở mục 6.1 đã tick đủ cho mọi module sắp sinh TC.

**Phần Test Plan:**

- ☐ Phiếu đã điền đủ hai nhóm bắt buộc **Mốc** và **Phạm vi**; ô chưa chốt để trống, ô đã quyết là không ghi `không`
- ☐ Plan và bản lưu phiếu nằm ở `docs/test-plans/`, cùng một mã mốc
- ☐ Phạm vi khai theo **cặp module × nền tảng**, khớp trạng thái khảo sát thật trong `docs/requirements/README.md`
- ☐ Mục **Ngoài phạm vi** đã điền, mỗi dòng đủ lý do, người chịu trách nhiệm và nguồn quyết định — kể cả nền tảng không kiểm
- ☐ Tiêu chí exit mặc định **khớp nguyên văn** bộ của `skills-test-summary-reporter`; tiêu chí thêm nằm ở bảng bổ sung
- ☐ Mọi ô không suy ra được đều là `❓` — không có ngày, tên người, công sức, ngân sách, thời hạn xử lý lỗi bịa
- ☐ Danh sách ô còn treo nằm ở **đầu** tài liệu
- ☐ Nghi ngờ về con số (công sức thiếu, lịch không còn ngày đệm) nằm ở bảng rủi ro dự án — không bị sửa ngầm
- ☐ Rủi ro dự án tách bạch với rủi ro sản phẩm; rủi ro sản phẩm chỉ tóm tắt và link về tài liệu gốc
- ☐ URL, tài khoản nằm ở `.env` — không có trong plan, không có trong phiếu
- ☐ Mục điểm làm khác chiến lược chung đã điền hoặc ghi `Không áp dụng`
- ☐ Không có số điều khoản của 29119-3 hay 829, không có câu "tuân thủ ISO/IEC/IEEE 29119"
- ☐ Plan đã gửi PM duyệt

### 10.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Sinh Test Case từ bản Requirements đầu tiên AI vừa sinh ra.**  
Tài liệu trông rất đầy đủ, có bảng, có mã, có ảnh, nên người ta tin ngay. Hậu quả đo được trên CRM demo: 3 REQ assert sai tiêu đề tab → TC đỏ hàng loạt dù hệ thống đúng; 2 REQ ghi theo hành vi lỗi → TC xanh trên hệ thống sai. Sửa REQ lúc chưa có TC là sửa một file; sửa sau khi đã có TC là cả một vòng cập nhật TC và chạy lại.

**Lỗi 2 — "Sửa cho xanh".**  
PO đã nói hiện trạng là lỗi, nhưng TC FAIL nhìn khó chịu, nên REQ hoặc Assumption tạm bị chỉnh lại cho khớp hệ thống. Biến thể nhẹ hơn: đổi REQ "bỏ qua" thành Deprecated cho bảng độ phủ gọn. Hậu quả: bug bị xoá bằng tay, và tài liệu nói sai về hệ thống. REQ ghi kỳ vọng đúng thì TC FAIL là kết quả đúng — việc tiếp theo là mở bug, không phải sửa REQ.

**Lỗi 3 — Để trống mục Ngoài phạm vi, hoặc điền đủ mọi ô cho plan trông hoàn chỉnh.**  
Cả hai đều xuất phát từ mong muốn nộp một tài liệu "đẹp". Hậu quả: khi có sự cố, không có căn cứ nào cho thấy vùng đó đã được thống nhất loại trừ; còn lịch trình bịa thì được PM ký duyệt mà không ai cam kết. Plan có nhiều ô `❓` nằm ở đầu tài liệu là một plan **trung thực**, không phải một plan yếu.

## 11. Bài tập thực hành

**Bài tập 1 — Rà soát tài liệu của chính bạn.** Mở tài liệu Requirements bạn đã sinh ở bài trước, soát từng REQ theo 9 câu ở mục 4.2. Đếm có bao nhiêu REQ trượt ít nhất một câu, và câu nào bị trượt nhiều nhất. Mỗi lỗi tìm được, ghi lại nó thuộc loại nào — đây là danh sách những thứ bạn sẽ soi đầu tiên ở dự án sau.

**Bài tập 2 — Chuẩn hoá một tài liệu có thật.** Lấy một tài liệu đặc tả bạn đang có (ticket Jira export, file `.docx`, kèm file Excel field nếu có), chạy `/analyze-requirement-document`. Kiểm ba thứ: bảng đối chiếu chéo có mặt không; mọi xung đột có thành `AMB-XX` không, hay AI tự chọn một bên rồi im lặng; dòng `Mức độ đầy đủ` ghi gì. Thử thêm: cố tình đưa nhầm file `requirements_<module>.md` vào — AI có dừng lại ở chốt chặn không?

**Bài tập 3 — Đóng một đợt điểm mờ.** Chọn 3 `AMB-XX` trong tài liệu của bạn và tự đóng vai PO: một câu trả lời trùng Assumption tạm, một câu "bỏ qua", một câu "hiện trạng là lỗi". Chạy `/update-requirements-from-ticket` với đợt quyết định đó. Đọc Impact Report và kiểm: REQ "bỏ qua" có bị đổi thành Deprecated không? REQ "hiện trạng là lỗi" có được viết lại theo hành vi đúng không? Đây là **bài tập quan trọng nhất** — nó dạy bạn phân biệt *quyết định về phạm vi* với *sự thật về hệ thống*, thứ mà rất nhiều tester lẫn lộn.

**Bài tập 4 — Lập Master Test Plan bản đầu tiên.** Mở `plans/master-test-plan/test_plan.config.yaml`, chỉ điền nhóm **Mốc** và **Phạm vi** cho đúng các module đã qua cổng sẵn sàng; nhóm **Lịch** và **Nhân lực** cố tình để trống, riêng `Cần tuyển thêm người` ghi `không`. Chạy `/generate-master-test-plan` rồi mở plan ra kiểm: ô lịch, nhân lực có ghi `❓` không, hay AI tự điền ngày? Ô `không` có bị đưa nhầm vào danh sách treo không? Danh sách ô treo có nằm ở đầu tài liệu không? Tiêu chí exit có khớp bộ mặc định ở mục 9.2 không? Cuối cùng so plan của bạn với plan thật `test_plan_release_1.0.md` của CRM demo ở mục 8.5.

## 12. Tổng kết

- **Tài liệu Requirements AI sinh ra là bản nháp đầu tiên, chưa phải đầu vào sạch.** Module Đăng nhập của CRM demo đi từ 35 lên 43 REQ, sửa 15 REQ, đóng 18/19 điểm mờ — tất cả trước dòng TC đầu tiên. Sửa lúc chưa có TC thì không TC nào phải sửa theo.
- **Đầu vào là tài liệu thì dùng `/analyze-requirement-document`:** chốt chặn đầu vào, đọc đúng định dạng, đối chiếu chéo nguồn, mọi xung đột thành `AMB-XX` — và không bao giờ viết AC thay PO. "Không đề cập" khác "Không áp dụng".
- **Cổng tự soát là AI tự chấm bài của mình.** Bạn vẫn phải rà soát — chính những lỗi người rà soát tìm ra đã trở thành luật của cổng.
- **Câu trả lời của PO phải vào tài liệu qua `/update-requirements-from-ticket`**: có mã đợt, có nguyên văn, có Nhật ký thay đổi. "Bỏ qua" là ngoài phạm vi, không phải Deprecated. "Hiện trạng là lỗi" thì REQ đổi theo hành vi đúng, TC sẽ FAIL — và đó là kết quả đúng.
- **Cổng sẵn sàng tính theo từng module.** Module nào đủ thì sinh TC ngay; module nào chưa thì lý do phải nằm sẵn trong danh mục. Năng lực kiểm thử của QA hỏi một lần, ghi ngay cho cả dự án.
- **Ba lệnh "plan" sinh ba loại tài liệu.** Đã có requirements với `REQ ID` thì dùng `/generate-master-test-plan`: thứ suy ra được AI tự đọc từ `docs/`, thứ chỉ người biết lấy từ phiếu `test_plan.config.yaml`; ô trống thành `❓` thay vì bịa lịch, nhân lực hay công sức. Plan nằm ở `docs/test-plans/`, dùng chung mã mốc với báo cáo tiến độ và báo cáo tổng hợp.
- **Ngoài phạm vi và tiêu chí exit chốt trước khi viết TC.** Tiêu chí exit lấy nguyên từ `skills-test-summary-reporter` để plan và báo cáo cuối đợt chấm cùng một bộ — nhìn kết quả rồi mới đặt ngưỡng là hợp thức hoá kết quả. Tiêu chí #7 chấm theo từng cặp module × nền tảng. Plan có phiên bản: đổi thì sửa phiếu và chạy lại lệnh, không viết đè.
- **Tên lệnh giống nhau ở cả ba bộ kit** — Codex gõ `$` thay cho `/`, Antigravity gõ y hệt Claude Code.
- Bài kế tiếp: **Thực hiện tạo Test Cases manual với AI Agent từ Requirements** — dùng đúng bộ requirements đã chuẩn hoá và phạm vi đã chốt trong plan làm đầu vào.