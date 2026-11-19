# Bài 7 - Thực hiện phân tích Requirements với AI Agent

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/333](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/333)

✅ Phân tích Requirements từ file docs có sẵn  
✅ Thực hiện tạo Requirements từ hệ thống đang chạy

## 1. Vì sao phải bắt đầu từ Requirements?

Ở bài trước bạn đã cài xong bộ Testing Skills và thuộc bản đồ 8 chặng. Bài này là **chặng 0 và chặng 1** — hai chặng đầu tiên, và cũng là hai chặng hay bị bỏ qua nhất.

Tình huống quen thuộc: sếp đưa cho bạn một cái link, một tài khoản test, và nói "em test giùm anh cái này". Không có tài liệu. Không có spec. Không có bộ Test Case nào. Phản xạ tự nhiên là mở AI lên và gõ ngay *"viết test case cho trang đăng nhập này"*.

Đó là chỗ hỏng. Hãy nhìn cái giá phải trả:

<table class="rt-table">
<thead>
<tr>
<th>Nếu bỏ qua bước Requirements</th>
<th>Hậu quả xuất hiện lúc nào</th>
<th>Chi phí sửa</th>
</tr>
</thead>
<tbody>
<tr>
<td>Test Case không có mã <code>REQ ID</code></td>
<td>Tận chặng 6, khi cần chứng minh độ phủ trước release</td>
<td><strong>Viết lại toàn bộ Test Case</strong></td>
</tr>
<tr>
<td>AI tự bịa validation message vì không được xem UI thật</td>
<td>Lúc chạy tay, TC FAIL hàng loạt dù hệ thống đúng</td>
<td>Chạy lại cả đợt kiểm thử</td>
</tr>
<tr>
<td>Không ai ghi lại điểm mờ để hỏi PO</td>
<td>Lúc bug bị dev trả về "cái này đúng theo thiết kế"</td>
<td>Tranh cãi, mất uy tín, không có căn cứ</td>
</tr>
</tbody>
</table>

Bước phân tích Requirements không phải thủ tục giấy tờ. Nó tạo ra **ba thứ mà mọi bước sau đều cần**:

- **Mã `REQ ID`** — sợi dây truy vết xuyên suốt cả chuỗi, như bạn đã học ở bài trước.
- **Evidence** — ảnh chụp màn hình thật, để bước sinh Test Case *không phải đoán*.
- **Danh sách điểm mờ** — những câu hỏi phải gửi PO/BA, kèm giả định tạm để không bị kẹt chờ trả lời.

> 💡 Điểm hay nhất của việc dùng AI ở bước này: AI **đọc được UI nhanh hơn người**. Nó mở từng form, bấm từng validation, đọc DOM, bắt network — những việc mà tester làm tay mất cả buổi và vẫn sót. Cái nó *không* làm được là hiểu nghiệp vụ công ty bạn — và đó chính là lý do có các checkpoint dừng lại hỏi ở mục 3.3.

## 2. Hai chặng, hai lệnh — đừng gộp làm một

Phân tích Requirements không phải một lệnh, mà là **hai lệnh chạy nối tiếp**, ở hai cấp độ khác nhau:

<table class="rt-table">
<thead>
<tr>
<th>Chặng</th>
<th>Lệnh</th>
<th>Trả lời câu hỏi gì</th>
<th>Chạy bao nhiêu lần</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>0</strong></td>
<td><code>/discover-system</code></td>
<td><em>"Hệ thống này có những module nào?"</em></td>
<td><strong>1 lần</strong> cho cả hệ thống</td>
</tr>
<tr>
<td><strong>1</strong></td>
<td><code>/generate-requirements-from-website</code><br/>(web — app và API có lệnh riêng, xem mục 5)</td>
<td><em>"Module này có những yêu cầu gì?"</em></td>
<td><strong>N lần</strong> — mỗi module × mỗi nền tảng một lần</td>
</tr>
</tbody>
</table>

Điều quan trọng nhất phải nhớ về ranh giới giữa hai lệnh:

<table class="rt-table">
<thead>
<tr>
<th><code>/discover-system</code> <strong>CÓ</strong> làm</th>
<th><code>/discover-system</code> <strong>KHÔNG</strong> làm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liệt kê toàn bộ module / trang / entity của hệ thống</td>
<td>❌ <strong>Tuyệt đối không gán mã <code>REQ-XXX-NN</code></strong></td>
</tr>
<tr>
<td>Cấp <strong>prefix</strong> cho từng module (<code>LOGIN</code>, <code>CUST</code>, <code>PRJ</code>...) và đăng ký chống trùng</td>
<td>❌ Không sinh Field Spec, validation message, ma trận phân quyền chi tiết</td>
</tr>
<tr>
<td>Đánh giá risk sơ bộ + đề xuất thứ tự khảo sát</td>
<td>❌ Không trigger validation từng field</td>
</tr>
<tr>
<td>Khởi tạo file danh mục <code>docs/requirements/README.md</code></td>
<td>❌ Không sinh Test Case</td>
</tr>
<tr>
<td>Tự nhận hệ thống có <strong>mấy mặt</strong> — web, app mobile, API — rồi ghép tất cả vào <strong>một</strong> bản đồ, <strong>một</strong> bộ prefix</td>
<td>❌ Không cấp prefix riêng cho app hay API (❌ <code>LOGIN_APP</code>, <code>MCUST</code>)</td>
</tr>
</tbody>
</table>

Sơ đồ đầy đủ của cả 8 chặng: [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md). Prompt mẫu copy-paste cho hai chặng này (dùng khi AI Agent của bạn không có bộ kit riêng — ví dụ Cursor, Kiro): [prompts/](https://github.com/anhtester/claude-testing-skills/blob/main/prompts/README.md) — file `prompt_00_discover_system.txt` và `prompt_01_generate_requirements.txt`.

> **Vì sao tách bạch đến vậy?** Mã REQ là lớp truy vết **bất biến**. Gán mã ở tầng khám phá — khi chưa mở từng form, chưa bấm thử validation nào — thì **chắc chắn** sẽ phải đánh lại số ở bước sau. Mà đánh lại số là vỡ toàn bộ traceability. Nên tầng khám phá **chỉ cấp prefix, không cấp số**.

### 2.1. Gọi lệnh trên Claude Code, Codex và Antigravity

Bộ kit có ba bản, mỗi bản cho một AI Agent. **Tên lệnh giống hệt nhau** ở cả ba — chỉ khác ký tự gõ đầu và chỗ đặt file:

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
<td><code>/discover-system</code></td>
<td><code>$discover-system</code></td>
<td><code>/discover-system</code></td>
</tr>
<tr>
<td><strong>File lệnh nằm ở</strong></td>
<td><code>.claude/commands/discover-system.md</code></td>
<td><code>.agents/skills/discover-system/SKILL.md</code></td>
<td><code>.agent/workflows/discover-system.md</code></td>
</tr>
<tr>
<td><strong>Skill nền tảng lệnh gọi tới</strong></td>
<td><code>skills-requirements-analyzer</code></td>
<td><code>requirements-analyzer</code></td>
<td><code>requirements_analyzer</code></td>
</tr>
<tr>
<td><strong>File quy tắc chung (tự nạp)</strong></td>
<td><code>CLAUDE.md</code></td>
<td><code>AGENTS.md</code></td>
<td><code>GEMINI.md</code></td>
</tr>
</tbody>
</table>

Toàn bài viết theo cú pháp Claude Code. Dùng Codex thì thay `/` bằng `$`; dùng Antigravity thì gõ y hệt Claude Code.

> 💡 **Vì sao Codex là `$`?** Trên Codex, **mọi thứ đều là skill** — cả kỹ năng nền tảng lẫn quy trình từng bước đều nằm trong `.agents/skills/`, và `$` là cú pháp gọi đích danh một skill ([tài liệu Codex](https://learn.chatgpt.com/docs/build-skills)). Dấu `/` trên Codex dành cho lệnh có sẵn của chính Codex, ví dụ `/skills` để mở danh sách skill. Codex cũng tự chọn skill khi yêu cầu của bạn khớp phần mô tả của skill — gõ `$` chỉ để **chắc chắn** chạy đúng quy trình, không phải để AI đoán.
>
> 📌 Antigravity gọi workflow bằng `/tên-workflow` ([tài liệu Antigravity](https://antigravity.google/docs/ide/workflows/)); Claude Code tạo lệnh `/tên-file` từ mỗi file trong `.claude/commands/` ([tài liệu Claude Code](https://code.claude.com/docs/en/skills)). Để ý tên skill nền tảng ở ba bản viết theo ba kiểu khác nhau — khi tra file trong repo, đừng tìm `skills-requirements-analyzer` bên Codex.

## 3. Chặng 0 — Khám phá hệ thống với `/discover-system`

### 3.1. Chuẩn bị trước khi gõ lệnh

Lệnh này sẽ hỏi bạn vài thứ mà AI **không thể tự suy ra được**. Chuẩn bị sẵn thì chạy trơn:

<table class="rt-table">
<thead>
<tr>
<th>Cần chuẩn bị</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>URL hệ thống</strong> (mặt web)</td>
<td>Bắt buộc khi hệ thống có web, trừ khi bạn chỉ có tài liệu mà chưa có account.</td>
</tr>
<tr>
<td><strong>File app hoặc package id + thiết bị</strong> (nếu có app mobile)</td>
<td>Để AI mở app thật qua Appium MCP. Lưu ý: iOS chỉ khám phá được trên máy macOS — máy Windows chỉ làm được Android.</td>
</tr>
<tr>
<td><strong>Nguồn tài liệu API</strong> — Swagger, Scalar, Postman, file <code>.docx</code> (nếu có API)</td>
<td>AI tải bản gốc của spec về lưu làm bằng chứng. Spec là một dạng tài liệu, nên mặt API luôn chạy mode HYBRID hoặc DOC — xem mục 3.2.</td>
</tr>
<tr>
<td><strong>Bạn có được gọi API trực tiếp không?</strong></td>
<td>Quyền gọi API là thứ <strong>phải hỏi</strong>, không suy ra được từ việc có Swagger. Chưa được phép thì mọi yêu cầu của mặt API chỉ dừng ở mức "theo spec".</td>
</tr>
<tr>
<td><strong>Tài khoản — càng nhiều role càng tốt</strong></td>
<td>Thiếu role nào thì ma trận phân quyền của role đó chỉ là suy diễn, không phải kiểm chứng. Web và app dùng chung tài khoản thì chỉ cần một bộ.</td>
</tr>
<tr>
<td><strong>Tên hệ thống viết tắt</strong> (<code>CRM_</code>, <code>ERP_</code>, <code>HRM_</code>)</td>
<td>Dùng làm tiền tố cho TC ID về sau. AI sẽ đề xuất, bạn xác nhận một câu.</td>
</tr>
<tr>
<td><strong>Môi trường này có dùng chung không?</strong></td>
<td>Đây là câu AI <em>không có cách nào</em> tự biết. Dùng chung ⟹ bật ngay quy tắc <strong>chỉ đọc, không tạo/sửa/xoá dữ liệu</strong> trong suốt quá trình khảo sát.</td>
</tr>
<tr>
<td><strong>Tài liệu sẵn có</strong> (nếu có): spec, user story, ticket, file Excel field, mockup</td>
<td>Có tài liệu thì AI chuyển sang mode HYBRID — xem mục 3.2.</td>
</tr>
</tbody>
</table>

> 📌 **URL, tài khoản, base URL của API, package id của bản build nội bộ lưu ở `.env`, KHÔNG ghi vào bất kỳ tài liệu nào trong `docs/`.** Thư mục `docs/` được commit lên Git, và lịch sử Git **không xoá được bằng cách sửa file**. Tài liệu chỉ được mô tả *hình dạng* của mật khẩu/token, không được chép giá trị thật.
>
> 🔒 Khám phá hệ thống **không cần ghi dữ liệu** — mở form ra xem có field gì là đủ, **không bấm Save**.

### 3.2. Ba chế độ — AI tự chọn, bạn không cần khai

Bạn chỉ cần gõ:

```none
/discover-system
```

AI tự nhận diện chế độ từ đầu vào bạn đưa:

<table class="rt-table">
<thead>
<tr>
<th>Mode</th>
<th>Khi nào</th>
<th>Đặc điểm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>UI</strong><br/>(mặc định)</td>
<td>Chỉ có hệ thống đang chạy, không tài liệu</td>
<td>Sự thật 100% nằm ở UI. Mọi thứ chưa quan sát được đánh <code>❔ Chưa rõ</code>, <strong>không suy diễn</strong>.</td>
</tr>
<tr>
<td><strong>HYBRID</strong></td>
<td>Có hệ thống chạy <strong>+ một phần tài liệu</strong>. Mặt API có spec <strong>và</strong> được gọi thật cũng là HYBRID</td>
<td><strong>Phổ biến nhất trong thực tế.</strong> Tài liệu cho biết <em>ý định</em>, UI cho biết <em>thực tế</em>. Bắt buộc lập Bản đồ phủ tài liệu.</td>
</tr>
<tr>
<td><strong>DOC</strong></td>
<td>Chỉ có tài liệu, chưa có account để vào hệ thống. Mặt API chỉ có spec mà <strong>không</strong> được gọi thật cũng là DOC</td>
<td>Chỉ dựng được bản đồ <em>dự kiến</em>. Mọi module đánh <code>⬜ Chưa khảo sát UI</code> — không được coi là đã xác minh.</td>
</tr>
</tbody>
</table>

Ngoài ra còn hai chế độ chạy bổ sung **khi đã có bản đồ từ trước**:

- **Mode ADD** — bạn nói thẳng *"còn thiếu module Báo cáo, vào bằng `/admin/reports`"* → AI chỉ xử lý đúng module đó, không crawl lại từ đầu. Hệ thống đã có bản đồ, nay mới có thêm app hoặc Swagger — *"hệ thống còn có app mobile"* — cũng là mode ADD: AI chỉ khám phá **mặt mới**, ghép vào module đã có, giữ nguyên prefix.
- **Mode DELTA** — bạn nói *"rà lại xem có gì mới"* → AI crawl lại toàn bộ và báo phần chênh.

> **AI bắt buộc công bố mode và mặt hệ thống ngay câu đầu tiên**, kèm lý do một dòng — ví dụ: *"Chạy mode HYBRID · 2 mặt Web + API — có URL web và Swagger, gọi API được. Sẽ khám phá web trước để lấy tên module."*
>
> Để ý vế cuối: **khám phá web trước**. Mặt có giao diện cho bạn *tên nghiệp vụ mà người dùng nhìn thấy* ("Khách hàng", "Dự án"). Khám phá API trước thì tên module sẽ bị đặt theo tên controller kỹ thuật (`CustomerController`, tag `Contacts`) — và prefix đã ghi ra thì không đổi được nữa.
>
> Sai mode thì bạn **chặn ngay ở câu đó**, chưa tốn công gì. Bạn luôn có quyền chỉ định đè: *"chạy mode UI thôi, bỏ tài liệu đó đi, nó cũ rồi"*.
>
> ⚠️ Mode **không đổi giữa chừng**. Đang HYBRID mà phát hiện tài liệu quá cũ thì *không* tự hạ xuống UI — vẫn giữ HYBRID và đánh dấu vùng đó `⚠️ Nghi lỗi thời`. Lệch pha giữa tài liệu và UI là **thông tin có giá trị**; vứt tài liệu đi là mất luôn thông tin đó.

### 3.3. ⏸️ Checkpoint — chỗ AI dừng lại hỏi bạn

Trước khi ghi bất kỳ file nào, AI **dừng lại** và trình bày cho bạn: bảng module phát hiện được (tên, prefix đề xuất, loại màn hình, risk, ước số REQ), danh sách nghi vấn, lệch pha tài liệu ↔ UI, và thứ tự khảo sát đề xuất.

Rồi hỏi đúng 3 câu — thêm câu thứ 4 khi hệ thống có từ 2 mặt trở lên:

1. **Danh sách module đã đủ chưa? Có module nào tôi không thấy được** vì thiếu quyền, nằm sâu trong menu, hoặc chỉ vào được bằng URL / deep link trực tiếp?
2. Ranh giới tách/gộp module có đúng cách team hiểu không?
3. Thứ tự khảo sát ưu tiên thế nào?
4. *(≥ 2 mặt)* Chỗ tôi ghép màn hình app / tag API vào module có đúng không? Có tag nào thực chất là một nghiệp vụ riêng?

> **Câu số 1 là câu quan trọng nhất của cả bài học này.** Bạn — người đang làm dự án — thường biết những module mà AI *không có cách nào* nhìn thấy. Trả lời ở đây thì chưa file nào bị ghi. Phát hiện sau đó thì phải chạy lại mode ADD để bổ sung.
>
> ⚠️ **Prefix ghi ra rồi là bất biến.** Sửa sau tốn hơn hỏi trước rất nhiều — vì đổi prefix nghĩa là đổi mọi REQ ID của module đó và mọi Test Case map về nó.

### 3.4. Đầu ra của chặng 0

```none
docs/requirements/
├── README.md                          ← DANH MỤC — mọi module đang ⬜
└── _discovery/
    ├── system_map.md                  ← BẢN ĐỒ web + app, tên file BẤT BIẾN
    ├── api_map.md                     ← BẢN ĐỒ mặt API — chỉ khi có spec
    ├── modules/module_NN_<slug>.md    ← chỉ khi > 8 module
    ├── doc_inventory.md               ← chỉ mode HYBRID/DOC
    ├── sources/                       ← bản gốc tài liệu bạn cung cấp · snapshot spec API
    └── evidence/
        ├── <module>_overview_fullpage.png      ← web
        └── <android|ios>_<module>_overview.png ← app mobile
```

Trong file danh mục `README.md`, mỗi module một dòng với cột **Trạng thái recon**:

<table class="rt-table">
<thead>
<tr>
<th>Ký hiệu</th>
<th>Nghĩa</th>
<th>Hành động tiếp theo</th>
</tr>
</thead>
<tbody>
<tr>
<td>⬜</td>
<td><strong>Chưa khảo sát</strong> — mới chỉ phát hiện ra tên</td>
<td>Chạy <code>/generate-requirements-from-website</code></td>
</tr>
<tr>
<td>🟨</td>
<td><strong>Đang khảo sát</strong> — recon dở dang</td>
<td>Tiếp tục, nêu rõ đang dở ở đâu</td>
</tr>
<tr>
<td>✅</td>
<td><strong>Đã có tài liệu</strong> — đã phát hành <code>requirements_&lt;module&gt;.md</code></td>
<td>Sẵn sàng sinh Test Case</td>
</tr>
<tr>
<td>⏸️</td>
<td><strong>Hoãn</strong> — bạn chốt là ngoài phạm vi đợt này</td>
<td>Ghi lý do, <strong>vẫn giữ prefix</strong></td>
</tr>
<tr>
<td>⚪</td>
<td><strong>Chưa implement</strong> — thấy qua tài liệu/API, UI chưa có</td>
<td>Viết TC trước, đánh dấu <code>skip</code></td>
</tr>
</tbody>
</table>

**Cột này xanh hết ✅ nghĩa là bạn đã khảo sát xong hệ thống.** Đó là thước đo tiến độ của cả chặng 0–1.

## 4. Chặng 1 — Sinh Requirements với `/generate-requirements-from-website`

Chạy **lặp, mỗi lần một module × một nền tảng**, theo thứ tự đã chốt ở checkpoint chặng 0. CRM demo của khoá học chỉ có mặt web, nên mục này đi đường web; app mobile và API dùng hai lệnh anh em ở mục 5.

```none
/generate-requirements-from-website
```

### 4.1. AI thực sự làm gì?

Đây là phần đáng tiền nhất của bộ Skills. AI không chỉ "nhìn màn hình rồi mô tả":

<table class="rt-table">
<thead>
<tr>
<th>Việc</th>
<th>Chi tiết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Đọc bản đồ chặng 0 trước</strong></td>
<td>Lấy sẵn route, prefix đã cấp, mức phủ tài liệu — khỏi phải dò đường lại. <strong>Không tự đặt lại prefix.</strong></td>
</tr>
<tr>
<td><strong>Trigger từng validation</strong></td>
<td>Bấm thử từng trường hợp lỗi để lấy <strong>thông báo nguyên văn</strong> từ UI thật — không diễn đạt lại, không chép từ code cũ, không suy ra từ tên field.</td>
</tr>
<tr>
<td><strong>Đọc DOM</strong></td>
<td>Lấy những dữ kiện mà <em>ảnh không thể hiện được</em>: số <code>&lt;option&gt;</code> thật của dropdown, <code>disabled</code> hay chỉ là "chưa tick", <code>value</code> của từng option, phần tử ẩn bằng class nhưng vẫn nằm trong DOM.</td>
</tr>
<tr>
<td><strong>Bắt tầng network</strong></td>
<td>Quan sát request do UI phát sinh để lấy: schema entity thật, field ẩn trong payload, <strong>validation phía server</strong>, enum trạng thái, endpoint không có UI.</td>
</tr>
<tr>
<td><strong>Chụp evidence</strong></td>
<td>Ảnh cho từng trạng thái động — xem mục 8.</td>
</tr>
<tr>
<td><strong>Sinh mã <code>REQ-&lt;PREFIX&gt;-NN</code></strong></td>
<td>Nối tiếp đúng số, không đánh lại — xem mục 6.</td>
</tr>
</tbody>
</table>

> 🚫 **AI bị cấm gọi thẳng API để dò hành vi** (curl, fetch, gọi endpoint trong console). Nó chỉ được **quan sát thụ động** những request mà UI tự phát sinh. Gọi thẳng API là kiểm thử xâm nhập, và cũng không chứng minh được gì về hành vi của UI — thứ mà bạn đang cần đặc tả.
>
> 📌 Luật này chỉ áp cho **nhánh web**. Nhánh API ở mục 5 thì ngược lại: không có UI nào làm nguồn sự thật, nên gọi thật là **bắt buộc** — nhưng chỉ khi bạn đã cho phép ở bước chuẩn bị.

### 4.2. Tài liệu đầu ra gồm những mục gì?

Bản mới của bộ kit tách tài liệu một module thành **hai tầng**: file **index** giữ phần dùng chung cho mọi nền tảng, file **nền tảng** giữ phần chỉ đúng với web. Nắm được cái gì nằm ở đâu thì bạn review nhanh hơn nhiều:

<table class="rt-table">
<thead>
<tr>
<th>Mục</th>
<th>Nội dung</th>
<th>Nằm ở</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bảng metadata</strong></td>
<td>Dải mã đã dùng · Mã kế tiếp · dòng <code>Nền tảng</code> của module</td>
<td>Index</td>
</tr>
<tr>
<td><strong>Bản đồ tài liệu</strong></td>
<td>Liệt kê các file nền tảng (và file story nếu có) kèm dải REQ. Mọi lệnh phía sau đọc index trước, rồi theo mục này sang đúng file nền tảng</td>
<td>Index</td>
</tr>
<tr>
<td><strong>Yêu cầu chức năng</strong></td>
<td>Bảng có cột <code>REQ ID</code> · Tên yêu cầu · Mô tả · Acceptance Criteria · Trạng thái · Nguồn. REQ áp cho <strong>≥ 2 nền tảng</strong> nằm ở index kèm cột <code>Nền tảng</code>; REQ chỉ áp web nằm ở file web</td>
<td>Cả hai</td>
</tr>
<tr>
<td><strong>Đặc tả trường dữ liệu</strong></td>
<td>Bảng từng field: Label · Loại UI · Bắt buộc? · Ràng buộc (min/max/format/default) · REQ liên quan</td>
<td>File web</td>
</tr>
<tr>
<td><strong>Business Rules &amp; Validation Messages</strong></td>
<td>Mỗi dòng: REQ ID · Rule/Trigger · <strong>Thông báo lỗi nguyên văn</strong></td>
<td>File web</td>
</tr>
<tr>
<td><strong>Trình duyệt và viewport khảo sát</strong></td>
<td>Mọi kết luận về hiển thị chỉ đúng với viewport đó</td>
<td>File web</td>
</tr>
<tr>
<td><strong>Ma trận phân quyền</strong></td>
<td>Nếu hệ thống có nhiều role. Thiếu account role nào thì dùng thang 3 mức, kèm dòng tổng <em>Đã kiểm chứng / Suy diễn / Chưa rõ</em></td>
<td>Index</td>
</tr>
<tr>
<td><strong>Ma trận trạng thái</strong></td>
<td>Nếu entity có status flow (Nháp → Chờ duyệt → Đã duyệt...)</td>
<td>Index</td>
</tr>
<tr>
<td><strong>Điểm mơ hồ &amp; Rủi ro</strong></td>
<td>Bảng <code>AMB-XX</code> và <code>RISK-XX</code>, đánh số toàn module — xem mục 7</td>
<td>Index</td>
</tr>
<tr>
<td><strong>Danh mục Evidence</strong></td>
<td>Mỗi ảnh một dòng: tên file · màn hình · trạng thái · REQ nào nó chống lưng</td>
<td>File web</td>
</tr>
<tr>
<td><strong>Nhật ký thay đổi</strong></td>
<td>Bắt buộc ở mọi tài liệu module, có cột <code>TC cần xử lý</code></td>
<td>Index</td>
</tr>
</tbody>
</table>

Đầu ra lưu đúng chỗ:

```none
docs/requirements/<module>/
├── requirements_<module>.md          ← INDEX, tên file BẤT BIẾN — phần chung + Bản đồ tài liệu
└── web/                              ← TẦNG NỀN TẢNG — chỉ nhận 3 tên: web · mobile · api
    ├── requirements_<module>_web.md  ← REQ chỉ áp web · Field Spec · Validation
    ├── evidence/*.png
    └── stories/story_NN_<slug>.md    ← chỉ khi file web vượt ngưỡng
```

> **Module chỉ có web thì sao vẫn phải có thư mục `web/`?** Để hôm sau dự án có thêm app hay API, bạn chỉ việc thêm `mobile/` hoặc `api/` bên cạnh — **không phải di chuyển file nào**. Di chuyển file là gãy link evidence, và gãy link thì bước sinh Test Case không tìm thấy ảnh để đối chiếu.
>
> 📌 Bộ tài liệu CRM có sẵn trong repo kit được sinh **trước** khi có tầng nền tảng nên vẫn nằm ở cấu trúc cũ (`login/requirements_login.md` + `login/evidence/`). Kit quy định không phải chuyển ngay: lần đầu một lệnh sinh hoặc cập nhật chạm lại module, AI chuyển **một lần**, mã REQ giữ nguyên và ghi vào Nhật ký thay đổi.

Đồng thời **cập nhật ngược file danh mục** `docs/requirements/README.md`: đổi trạng thái recon từ ⬜ sang ✅ (module nhiều nền tảng thì chỉ ✅ khi mọi nền tảng của nó đã xong), ghi dải REQ đã dùng, mã kế tiếp, AMB còn treo.

> **Cột `Mã kế tiếp` trong danh mục là thứ dễ trôi nhất.** Danh mục là *bản phái sinh* do AI ghi tay qua nhiều phiên; thư mục `docs/requirements/` mới là *sự thật*. Một phiên quên cập nhật là danh mục lệch vĩnh viễn — mà cơ chế chống trùng mã lại đọc từ chính danh mục đó. Vì vậy lệnh này có bước **tự đối chiếu danh mục** sau mỗi lần chạy. Nguyên tắc phân xử: **tài liệu module thắng, sửa danh mục theo tài liệu** — trừ prefix, prefix lệch thì phải hỏi bạn.

## 5. Hệ thống có cả app mobile và API — ba nền tảng, một bộ mã

CRM demo chỉ có web. Nhưng dự án thật rất hay có thêm app Android/iOS cho người dùng cuối và API cho đối tác. Bản mới của bộ kit xử lý ba mặt đó bằng **ba lệnh anh em** ở chặng 1 — cùng gọi Skill `skills-requirements-analyzer`, cùng ghi vào **một** thư mục module, cùng **một** dải REQ:

<table class="rt-table">
<thead>
<tr>
<th>Nền tảng</th>
<th>Lệnh chặng 1</th>
<th>AI khảo sát bằng</th>
<th>Ghi vào</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Web</strong></td>
<td><code>/generate-requirements-from-website</code></td>
<td>Playwright MCP — mở trình duyệt thật</td>
<td><code>&lt;module&gt;/web/</code></td>
</tr>
<tr>
<td><strong>App mobile</strong><br/>(Native, Flutter, Hybrid)</td>
<td><code>/generate-requirements-from-mobile</code></td>
<td>Appium MCP — mỗi nền tảng Android / iOS một lượt</td>
<td><code>&lt;module&gt;/mobile/</code></td>
</tr>
<tr>
<td><strong>API</strong><br/>(Swagger, Scalar, Postman, <code>.docx</code>)</td>
<td><code>/generate-requirements-from-api</code></td>
<td>Tải bản gốc của spec + gọi thật có kiểm soát</td>
<td><code>&lt;module&gt;/api/</code></td>
</tr>
</tbody>
</table>

Một module có đủ ba mặt sẽ trông như thế này:

```none
docs/requirements/login/
├── requirements_login.md                ← INDEX: REQ dùng chung · phân quyền · AMB/RISK · Bản đồ tài liệu
├── web/requirements_login_web.md
├── mobile/requirements_login_mobile.md  ← ảnh: mobile/evidence/android_*.png · ios_*.png
└── api/requirements_login_api.md        ← Endpoint Catalog
```

**Thứ tự nên chạy: web → mobile → API** — cùng lý do như ở chặng 0: mặt có giao diện cho tên nghiệp vụ. Lượt chạy sau đối chiếu với REQ đã có: rule chạy giống nhau thì REQ được **chuyển lên index, giữ nguyên mã**; rule chạy khác thì tách REQ riêng kèm một `AMB` hỏi PO. Prompt mẫu tương ứng: `prompt_30_generate_requirements_from_mobile.txt` và `prompt_29_generate_requirements_from_api.txt`.

### 5.1. Một nghiệp vụ = một prefix, dù chạy trên bao nhiêu nền tảng

<table class="rt-table">
<thead>
<tr>
<th>Quy tắc</th>
<th>Ví dụ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Prefix gắn với nghiệp vụ, không gắn với nền tảng</strong></td>
<td>Đăng nhập trên web, app hay API đều là <code>LOGIN</code>. ❌ <code>LOGIN_APP</code>, <code>MLOGIN</code>, thư mục <code>login_mobile/</code></td>
</tr>
<tr>
<td>Rule <strong>giống nhau</strong> trên ≥ 2 nền tảng → <strong>1 REQ</strong>, nằm ở index</td>
<td>"Khoá tài khoản sau 5 lần đăng nhập sai" — thường là rule nằm ở server, cột <code>Nền tảng</code> ghi <code>Tất cả</code></td>
</tr>
<tr>
<td>Rule <strong>khác nhau</strong> → REQ riêng, nằm ở file nền tảng đó</td>
<td>Web giữ lại email sau khi đăng nhập lỗi, app xoá trắng → 1 REQ ở <code>web/</code>, 1 REQ ở <code>mobile/</code></td>
</tr>
<tr>
<td><strong>Chưa khảo sát nền tảng nào thì không khai REQ cho nền tảng đó</strong></td>
<td>REQ khảo sát trên web ghi <code>Web</code>, <strong>không</strong> ghi <code>Tất cả</code> khi chưa mở app. Nền tảng chưa kiểm là <code>❔</code>, không phải "chắc cũng giống"</td>
</tr>
</tbody>
</table>

> **Vì sao không tách prefix cho gọn?** Tách prefix theo nền tảng là **nhân đôi REQ cho cùng một rule**. Sửa rule ở web quên sửa ở app, ma trận truy vết vẫn báo phủ đủ trong khi hai bản đã lệch nhau từ lâu. Khác biệt giữa các nền tảng mà không rõ là cố ý hay lỗi — message web khác app, API nhận giá trị mà UI chặn — thì mở `AMB-XX`, và **mặc định nghi là lỗi**.

### 5.2. Hai cái bẫy riêng của app và API

<table class="rt-table">
<thead>
<tr>
<th>Nền tảng</th>
<th>Khác web ở đâu</th>
<th>Bẫy phải nhớ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>App mobile</strong></td>
<td>Phải xét đủ <strong>8 nhóm yêu cầu riêng của mobile</strong>: quyền runtime · vòng đời app · mất mạng · xoay màn hình · bàn phím · deep link · push notification · cập nhật bắt buộc. Nhóm nào không áp dụng thì ghi "Không áp dụng" kèm lý do, không bỏ trống</td>
<td>App <strong>Flutter chưa bật semantics</strong> thì Appium chỉ thấy một khung <code>FlutterView</code> rỗng — AI phải dừng lại báo dev, <strong>cấm</strong> bấm theo toạ độ để tự dò. Và không suy iOS từ Android: mỗi nền tảng khảo sát riêng</td>
</tr>
<tr>
<td><strong>API</strong></td>
<td>Gọi thật là <strong>bắt buộc</strong> để kiểm chứng — nhưng chỉ khi bạn đã cho phép. Mỗi chỗ spec nói một đằng, hệ thống làm một nẻo được ghi thành một phát hiện <code>F-nn</code> kèm bằng chứng đã che dữ liệu nhạy cảm</td>
<td>🚨 <strong>Spec không phải hành vi</strong>: Swagger khai <code>403</code> không có nghĩa hệ thống trả <code>403</code>. Và AI <strong>chỉ được ghi/xoá bản ghi do chính nó tạo ra</strong> — kiểm quyền truy cập chéo bằng 2 tài khoản tự tạo, cấm lấy <code>id</code> từ API danh sách rồi sửa/xoá. Luật này có vì từng có lần xoá mất tài khoản gốc của một hệ thống demo</td>
</tr>
</tbody>
</table>

## 6. `REQ ID` — mã truy vết bất biến

Đây là quy ước quan trọng nhất của cả chuỗi. Nắm kỹ ở bài này thì các bài sau nhẹ hẳn. Toàn bộ quy ước nằm trong Skill [skills-requirements-analyzer](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/skills/skills-requirements-analyzer/SKILL.md) — chính là Skill mà `/discover-system` và cả ba lệnh chặng 1 đều gọi tới.

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Format</th>
<th>Ví dụ</th>
<th>Dùng cho</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Requirement</strong></td>
<td><code>REQ-&lt;MODULE&gt;-&lt;SỐ&gt;</code></td>
<td><code>REQ-LOGIN-01</code></td>
<td>Từng yêu cầu chức năng, business rule, validation rule</td>
</tr>
<tr>
<td><strong>Story</strong></td>
<td><code>STORY-&lt;MODULE&gt;-&lt;SỐ&gt;</code></td>
<td><code>STORY-PRJ-03</code></td>
<td>Nhóm REQ thành đơn vị công việc (bắt buộc khi ≥ 25 REQ)</td>
</tr>
<tr>
<td><strong>Ambiguity</strong></td>
<td><code>AMB-&lt;SỐ&gt;</code></td>
<td><code>AMB-03</code></td>
<td>Điểm mờ cần hỏi lại PO/BA</td>
</tr>
<tr>
<td><strong>Risk</strong></td>
<td><code>RISK-&lt;SỐ&gt;</code></td>
<td><code>RISK-02</code></td>
<td>Rủi ro kiểm thử</td>
</tr>
</tbody>
</table>

### 6.1. Bốn luật không được phá

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Không bao giờ đánh lại số REQ từ <code>01</code></strong> khi module đã có tài liệu. Module đã dùng tới <code>REQ-PRJ-65</code> thì đợt sau bắt đầu từ <code>REQ-PRJ-66</code>.</td>
<td>Cùng một module có thể được phân tích nhiều lần bằng nhiều lệnh khác nhau (từ web, từ app, từ API, từ ticket Jira...). Mỗi lần đánh lại từ 01 là các dải mã đụng nhau và <strong>RTM map sai hoàn toàn</strong>.</td>
</tr>
<tr>
<td><strong>Không bao giờ xoá dòng REQ.</strong> Tính năng bị gỡ thì đổi trạng thái sang 🔴 Deprecated.</td>
<td>Xoá dòng là mất dấu vết. Và mã đã cấp thì <strong>chết vĩnh viễn</strong> — không được tái sử dụng cho yêu cầu khác.</td>
</tr>
<tr>
<td><strong>Mỗi REQ đủ nhỏ để test được độc lập.</strong> Một câu chứa nhiều rule thì tách thành nhiều REQ.</td>
<td>REQ gộp nhiều rule thì Test Case map vào nó không chứng minh được đã phủ hết rule nào.</td>
</tr>
<tr>
<td><strong>Mỗi REQ phải có cột <code>Nguồn</code></strong>, không được để trống hay ghi chung chung.</td>
<td>Phân biệt rõ <code>UI thực tế</code> (chỉ quan sát) với <code>Kiểm chứng thực tế</code> (đã tương tác và xác nhận) — hai mức tin cậy khác nhau.</td>
</tr>
</tbody>
</table>

### 6.2. Bảng trạng thái REQ — thứ báo cho bạn biết TC nào đã lỗi thời

<table class="rt-table">
<thead>
<tr>
<th>Ký hiệu</th>
<th>Nghĩa</th>
<th>Hệ quả với Test Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢</td>
<td><strong>Active</strong> — đang hiệu lực, chưa từng sửa</td>
<td>TC giữ nguyên</td>
</tr>
<tr>
<td>🟡</td>
<td><strong>Changed</strong> — đã bị ticket sau sửa nội dung</td>
<td>⚠️ TC map vào REQ này <strong>phải review lại</strong></td>
</tr>
<tr>
<td>🔴</td>
<td><strong>Deprecated</strong> — tính năng đã bị gỡ</td>
<td>TC map vào REQ này phải archive. <strong>Không xoá dòng REQ</strong></td>
</tr>
<tr>
<td>⚪</td>
<td><strong>Chưa implement</strong> — tài liệu có, hệ thống chưa build</td>
<td>TC viết trước, đánh dấu <code>skip</code></td>
</tr>
</tbody>
</table>

## 7. Ambiguity & Risk — phần giá trị nhất của bước này

Nếu bạn chỉ nhớ được một thứ từ bài này, hãy nhớ mục này. Sinh ra bảng field spec thì AI nào cũng làm được. Cái khiến tài liệu *dùng được trong dự án thật* là **danh sách những chỗ hệ thống không nói rõ**.

Mỗi điểm mờ được ghi thành một dòng `AMB-XX` gồm: **Câu hỏi · Nguy cơ nếu không giải quyết · Mức độ (🔴 High / 🟡 Medium / 🟢 Low) · Assumption tạm**.

> **Cột "Assumption tạm" là thứ cứu bạn khỏi bị kẹt.** PO đi họp cả tuần không trả lời, nhưng bạn vẫn phải test. Ghi rõ *"tạm giả định giới hạn là 100 ký tự"* thì bạn test tiếp được ngay, và khi PO trả lời khác thì bạn biết chính xác phải sửa TC nào.

AI được hướng dẫn săn điểm mờ theo những hướng cụ thể sau:

- **Từ khoá mơ hồ** trong tài liệu: "where applicable", "as needed", "similar to", "hợp lý", "v.v."
- **Validation thiếu:** không nói min/max, không nói format, không nói bắt buộc hay không, không nói giá trị mặc định.
- **Edge case chưa quy định:** mất mạng giữa chừng, hai người sửa cùng lúc, danh sách rỗng, timeout.
- **Mâu thuẫn** giữa tài liệu và UI thực tế — tên cột khác, format khác, layout khác.
- **Ngưỡng/config chưa xác định:** bao nhiêu ngày thì gọi là "sắp đến hạn"?
- **Phân quyền chưa rõ:** role nào được làm hành động này?
- **Trạng thái chưa rõ:** từ trạng thái X có được nhảy thẳng sang Y không?

### 7.1. Cổng tự soát — AI kiểm lại chính nó

Có một cơ chế nữa đáng biết: trước khi ghi file, AI phải rà lại **từng REQ vừa viết** qua một bộ câu hỏi tự soát. Điểm khác biệt:

<table class="rt-table">
<thead>
<tr>
<th>Cơ chế</th>
<th>Bắt loại lỗi nào</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ambiguity (<code>AMB-XX</code>)</strong></td>
<td>Cái mà <strong>hệ thống/tài liệu</strong> không nói rõ → hỏi PO</td>
</tr>
<tr>
<td><strong>Cổng tự soát</strong></td>
<td>Cái mà <strong>chính AI vừa viết sai</strong> → sửa ngay, không mở AMB</td>
</tr>
</tbody>
</table>

Vài lỗi mà cổng này bắt, đáng để bạn cũng tự soi khi review tài liệu:

- **Tên REQ và Acceptance Criteria không cùng một mệnh đề** — tên nói một đằng, AC kiểm một nẻo.
- **Một REQ gộp nhiều rule** không kiểm được độc lập.
- **AC chứa giá trị biến thiên theo phiên** — ví dụ chép nguyên một session id vào AC, chạy lần sau là sai.
- **Tồn tại trong DOM ≠ người dùng dùng được** — element có trong DOM nhưng bị ẩn bởi thẻ cha, không ai bấm được.
- **Chuỗi do trình duyệt sinh ra không phải hành vi của ứng dụng** — thông báo mặc định của Chrome không phải validation của hệ thống bạn đang test.

> ⚠️ Đây là loại lỗi **nguy hiểm hơn cả điểm mờ**, vì nó *trông như* đã được kiểm chứng — có số liệu DOM hẳn hoi — và không bước nào phía sau phát hiện ra. Test Case sinh từ một AC sai sẽ FAIL mà không ai biết lỗi nằm ở tài liệu.

## 8. Evidence — bằng chứng, không phải ảnh minh hoạ

Evidence là **nguồn sự thật** cho bài kế tiếp. Ở bước sinh Test Case, AI bị bắt buộc **mở toàn bộ ảnh evidence của nền tảng đang sinh TC trước khi viết TC** — và *ảnh thắng tài liệu* khi hai bên mâu thuẫn. Ảnh cắt cụt khiến AI phải suy diễn phần không nhìn thấy, và **không ai phát hiện được chỗ nào là suy diễn**.

<table class="rt-table">
<thead>
<tr>
<th>Quy tắc</th>
<th>Chi tiết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ảnh phải chứa trọn đối tượng cần chứng minh</strong></td>
<td>Form dài thì chụp full-page, vì chụp viewport là mất nút Save và các field cuối. Nhưng mục đích là <em>không cắt cụt</em>, không phải chụp càng nhiều càng tốt.</td>
</tr>
<tr>
<td><strong>Chụp theo trạng thái, không chỉ trạng thái mặc định</strong></td>
<td>Mỗi trạng thái động một ảnh riêng: dropdown <strong>đang mở</strong> (thấy đủ option), form <strong>sau khi submit lỗi</strong> (thấy message inline), checkbox <strong>disabled vs enabled</strong>, từng tab.</td>
</tr>
<tr>
<td>🔍 <strong>Chụp xong phải mở lại ảnh xác nhận</strong></td>
<td>Rất hay gặp: lệnh mở dropdown thất bại âm thầm, hoặc ảnh chụp trước khi menu kịp render → danh mục ghi "menu đang mở" mà ảnh là menu đóng.</td>
</tr>
<tr>
<td>🔒 <strong>Vệ sinh dữ liệu</strong></td>
<td>Ảnh full-page của màn hình nghiệp vụ kéo theo tên khách hàng, số tiền, email, nhật ký hoạt động — không liên quan gì tới REQ mà vẫn <strong>bị commit lên Git</strong>. Đối tượng nằm gọn trong viewport thì chụp viewport.</td>
</tr>
<tr>
<td><strong>Đặt tên nêu rõ trạng thái và phạm vi chụp</strong></td>
<td><code>&lt;màn_hình&gt;_&lt;trạng_thái&gt;_&lt;fullpage|viewport&gt;.png</code> — ví dụ <code>project_new_form_default_fullpage.png</code>. Ảnh chụp trên app mobile thêm tiền tố <code>android_</code> / <code>ios_</code>.</td>
</tr>
</tbody>
</table>

> **Dòng danh mục evidence sai còn nguy hiểm hơn không có ảnh** — vì nó tạo cảm giác REQ đã có bằng chứng, và không ai đi kiểm lại nữa.
>
> **Ảnh và DOM bổ sung cho nhau, không thay thế nhau.** Ảnh không cho biết một checkbox là `disabled` hay chỉ màu nhạt, không đếm được option trong multi-select bị cắt chuỗi. Ngược lại, đếm được phần tử trong DOM *không* chứng minh người dùng nhìn thấy nó.

## 9. Hai biến thể thường gặp

Không phải lúc nào cũng là "hệ thống chạy sẵn, không tài liệu". Hai tình huống rất phổ biến khác — cả hai đều nằm trong [bộ 38 command](https://github.com/anhtester/claude-testing-skills/tree/main/.claude/commands) của kit:

<table class="rt-table">
<thead>
<tr>
<th>Tình huống</th>
<th>Lệnh</th>
<th>Khác gì đường chính</th>
</tr>
</thead>
<tbody>
<tr>
<td>Có <strong>ticket Jira / tài liệu</strong> thay vì UI để khảo sát</td>
<td><code>/analyze-requirement-document</code></td>
<td>Đầu ra là <code>analysis_&lt;TICKET-ID&gt;.md</code> — tài liệu <strong>phân tích ticket</strong>, khác với tài liệu đặc tả module. Vẫn có AMB/RISK và quy tắc nối tiếp mã.</td>
</tr>
<tr>
<td>Tài liệu <strong>đã có</strong>, giờ có ticket sửa đổi yêu cầu</td>
<td><code>/update-requirements-from-ticket</code></td>
<td>Chạy <strong>delta mode</strong> — chỉ sửa phần liên quan, và sinh ra <strong>Impact Report</strong> nói rõ TC nào đã lỗi thời.</td>
</tr>
</tbody>
</table>

> 🔁 **Hệ thống đang phát triển thì ticket sẽ liên tục sửa yêu cầu — đừng sinh lại tài liệu từ đầu.** Chạy `/update-requirements-from-ticket` để có Impact Report, rồi mới đồng bộ bộ Test Case theo report đó. Cột `TC cần xử lý` trong Nhật ký thay đổi là **mắt xích cảnh báo duy nhất** cho tester biết TC nào đã stale. Bỏ qua nó là chạy test trên bộ TC sai mà không hề biết.

## 10. Nghiệm thu trước khi sang bài Test Case

### 10.1. Checklist

Tick đủ trước khi chuyển sang bài kế tiếp — đây là điều kiện để bước sinh Test Case không phải đoán:

- ☐ Mọi yêu cầu đều có `REQ ID`, cột `Nguồn` không để trống
- ☐ Error message ghi **nguyên văn** từ UI, không diễn đạt lại
- ☐ Evidence có ảnh cho **từng trạng thái động** (dropdown mở, form lỗi, từng tab), và đã mở lại xác nhận
- ☐ Ma trận phân quyền có **dòng tổng** *Đã kiểm chứng / Suy diễn / Chưa rõ*
- ☐ Ambiguity 🔴 High đã gửi PO — hoặc đã ghi **Assumption tạm** để test tiếp được
- ☐ File danh mục `docs/requirements/README.md` đã cập nhật, cột `Mã kế tiếp` khớp với REQ cuối trong tài liệu
- ☐ Tài liệu nằm đúng tầng: index `requirements_<module>.md` có mục **Bản đồ tài liệu**, phần riêng của web nằm ở `web/requirements_<module>_web.md`, ảnh ở `web/evidence/`
- ☐ Không có REQ nào ghi `Tất cả` nền tảng trong khi mới khảo sát mỗi web
- ☐ Không có mật khẩu / token / session id thật lọt vào `docs/`

### 10.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Chạy `/generate-requirements-from-website` khi chưa chạy `/discover-system`.**  
AI phải tự dò đường, tự đặt prefix. Đến module thứ ba thì prefix bắt đầu trùng nhau, và không có chỗ nào phát hiện ra cho tới khi bạn làm ma trận truy vết. Chưa biết hệ thống có module nào thì **luôn bắt đầu bằng chặng 0**.

**Lỗi 2 — Bấm qua checkpoint cho nhanh.**  
Checkpoint tồn tại đúng ở những chỗ AI *không thể tự quyết đúng*: ranh giới module, module bị ẩn vì thiếu quyền, thứ tự khảo sát. Gõ "tiếp tục" cho nhanh là đẩy sai lầm xuống tận lúc chạy test mới lộ.

**Lỗi 3 — Coi tài liệu Requirements là sản phẩm cuối, không đọc lại.**  
Nó là **đầu vào** của mọi bước sau. Bỏ 20 phút đọc lại phần Ambiguity và Danh mục Evidence rẻ hơn rất nhiều so với việc phát hiện tài liệu sai ở chặng 4, khi đã sinh xong 60 Test Case dựa trên nó.

## 11. Bài tập thực hành

**Bài tập 1 — Chạy chặng 0.** Chọn một hệ thống bạn có tài khoản test (hoặc một web demo công khai), chạy `/discover-system`. Quan sát và ghi lại: AI công bố **mode gì** ở câu đầu tiên và lý do, nó phát hiện được mấy module, và nó đề xuất **prefix** gì cho từng module.

**Bài tập 2 — Trả lời checkpoint cho tử tế.** Ở checkpoint, đừng gõ "ok tiếp tục". Hãy trả lời thật câu hỏi *"có module nào tôi không thấy được không?"* — nếu hệ thống bạn chọn có phần chỉ vào được bằng URL trực tiếp hoặc cần role khác, hãy nói ra. So sánh bảng module **trước và sau** khi bạn trả lời.

**Bài tập 3 — Chạy chặng 1 cho đúng một module.** Chọn module đơn giản nhất (thường là Đăng nhập), chạy `/generate-requirements-from-website`. Sau đó mở file index `requirements_<module>.md` cùng file `web/requirements_<module>_web.md` và tự chấm: có bao nhiêu REQ? Có bao nhiêu `AMB-XX`? **Có REQ nào ghi `Kiểm chứng thực tế` mà không truy được về ảnh evidence nào không?**

**Bài tập 4 — Soi evidence.** Mở thư mục `docs/requirements/<module>/web/evidence/`, xem từng ảnh và đối chiếu với bảng Danh mục Evidence trong tài liệu. Tìm xem có dòng nào **khai một đằng, ảnh một nẻo** không (ví dụ khai "dropdown đang mở" mà ảnh là dropdown đóng). Đây là bài tập quan trọng nhất — nó dạy bạn thói quen **không tin tài liệu AI sinh ra mà không đối chiếu**.

## 12. Tổng kết

- Phân tích Requirements là **hai lệnh nối tiếp**, không phải một: `/discover-system` trả lời *"hệ thống có module nào"* (chạy 1 lần), `/generate-requirements-from-website` trả lời *"module này có yêu cầu gì"* (chạy N lần). App mobile và API dùng hai lệnh anh em `/generate-requirements-from-mobile` và `/generate-requirements-from-api`.
- **Tên lệnh giống nhau ở cả ba bộ kit** — Claude Code gõ `/lệnh`, Codex gõ `$lệnh`, Antigravity gõ `/lệnh`. Chỉ tên skill nền tảng và chỗ đặt file là khác.
- **Tầng khám phá chỉ cấp prefix, không cấp số REQ.** Gán mã khi chưa mở form là chắc chắn phải đánh lại — mà đánh lại là vỡ traceability.
- **Một nghiệp vụ = một prefix trên mọi nền tảng.** Tài liệu chia tầng `web/` · `mobile/` · `api/` bên dưới **cùng một** thư mục module; file index `requirements_<module>.md` giữ nguyên tên và giữ phần dùng chung.
- **`REQ ID` là bất biến:** không đánh lại từ 01, không xoá dòng, mã đã cấp thì chết vĩnh viễn. Tính năng bị gỡ thì đổi trạng thái 🔴 Deprecated.
- Giá trị lớn nhất của bước này không phải bảng field spec, mà là **danh sách điểm mờ `AMB-XX` kèm Assumption tạm** — thứ giúp bạn test tiếp được khi PO chưa trả lời, và có căn cứ khi dev nói "cái này đúng thiết kế".
- **Evidence là bằng chứng, không phải ảnh minh hoạ.** Bài kế tiếp sẽ đọc chính những ảnh này để viết Test Case — ảnh cắt cụt là Test Case bị suy diễn mà không ai biết.
- Đừng bấm qua checkpoint. Đó là chỗ duy nhất bạn đưa được vào hệ thống thứ mà AI không có cách nào tự biết: **nghiệp vụ và bối cảnh dự án của bạn**.
- Bài kế tiếp: **Thực hiện tạo Test Cases manual với AI Agent từ Requirements** — dùng đúng bộ tài liệu bạn vừa sinh ra ở bài này làm đầu vào.