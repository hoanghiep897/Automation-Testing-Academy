# Bài 13 - Xây dựng bộ nhớ Local dành riêng cho từng dự án chuyên biệt

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/336](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/336)

✅ Xây dựng bộ nhớ Local dành riêng cho từng dự án chuyên biệt để giúp AI hiểu toàn bộ dự án và có thể mang sang máy tính khác chạy dễ dàng  
✅ Thực hành chạy lại quy trình phân tích Requirements, tạo Test Cases, Execute Tests

## 1. Bộ nhớ của AI không nằm trong khung chat

Ở bài trước bạn đã chỉnh bộ Skills cho khớp chuẩn công ty: mã Test Case, độ hạt, mẫu bug report, quy tắc chạy trên môi trường dùng chung. Tất cả đã nằm trong file, nên mọi phiên và mọi người trong đội đều theo.

Nhưng đó mới là **luật**. Còn **bối cảnh** thì vẫn đang nằm trong đầu bạn:

- *"Module Đăng nhập đã dùng tới mã `CRM_LOGIN_TC_050` rồi, mã kế tiếp là 051."*
- *"Staging dùng chung với team Business — đừng đụng vào dữ liệu khách hàng."*
- *"PO chưa trả lời câu hỏi về thời hạn phiên đăng nhập, TC đó đang treo."*
- *"Bên mình QA không có quyền truy vấn cơ sở dữ liệu, nên mấy TC kiểm dữ liệu ngầm không chạy được."*

Không cái nào trong số đó là quy tắc để viết vào RULE. Chúng là **sự thật của riêng dự án này**, và bạn đang phải gõ lại mỗi lần mở phiên mới.

Nhiều người nghĩ AI sẽ tự nhớ vì "hôm qua mình vừa nói mà". Tài liệu chính thức của Claude Code nói rõ điều ngược lại: mỗi phiên bắt đầu bằng một **cửa sổ ngữ cảnh trống**. Đáng chú ý hơn là chuyện xảy ra *ngay trong một phiên dài* — khi ngữ cảnh đầy và bị nén lại, tài liệu ghi:

> 📌 `CLAUDE.md` ở gốc dự án **sống sót qua lần nén**: sau khi nén, Claude đọc lại nó từ đĩa và tiêm lại vào phiên. Còn *"nếu một chỉ dẫn biến mất sau khi nén, thì nó đã chỉ được đưa ra trong hội thoại"* ([How Claude remembers your project](https://code.claude.com/docs/en/memory)).

Đó là toàn bộ lý do của bài này. **Thứ nằm trong file thì đọc lại được; thứ chỉ nói trong chat thì mất.** Chữ *Local* trong tên bài mang đúng nghĩa đó: bộ nhớ là **file thật nằm trên máy, trong repo** — bạn mở ra xem được, sửa được, commit cho cả đội được — chứ không phải trông chờ AI nhớ giùm.

> 💡 Bài này minh hoạ trên Claude Code với dự án CRM demo. Mọi cơ chế nạp file đều trích từ tài liệu chính thức và có link kèm theo. Cấu trúc thư mục bộ nhớ là mô hình bạn dựng thêm — bộ kit chưa có sẵn, và đó là chủ ý: thêm mới thì cập nhật bộ kit không ghi đè mất, đúng như bài trước đã dạy.

## 2. Sơ đồ bộ nhớ bạn sẽ dựng

Đây là toàn bộ mô hình của bài, gói trong một cây thư mục:

```none
<gốc dự án>/
├── CLAUDE.md              ← có RULE: "luôn đọc memories/MEMORY.md trước"
├── memories/
│   ├── MEMORY.md          ← SƠ ĐỒ — đọc đầu tiên, chỉ ra phải mở file nào tiếp
│   ├── login.md           ← lưu ý riêng của module Đăng nhập
│   ├── customers.md       ← lưu ý riêng của module Khách hàng
│   └── _project.md        ← lưu ý cấp dự án (môi trường, quyền hạn, đầu mối)
└── docs/                  ← tài liệu sản phẩm do workflow sinh (REQ, TC, execution, bug)
```

Ba thành phần, ba vai trò tách bạch:

<table class="rt-table">
<thead>
<tr>
<th>Thành phần</th>
<th>Vai trò</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CLAUDE.md</code></td>
<td>Chứa <strong>một câu luật</strong> bắt AI luôn đọc <code>memories/MEMORY.md</code>. Không có câu này thì cả cơ chế đứng im — vì thư mục <code>memories/</code> tự nó không được nạp tự động</td>
</tr>
<tr>
<td><code>memories/MEMORY.md</code></td>
<td><strong>Sơ đồ</strong>: mỗi dòng một file bộ nhớ kèm một móc câu ngắn. AI đọc file này để biết <em>cần mở file nào tiếp theo</em>. Bản thân nó <strong>không chứa</strong> lưu ý chi tiết</td>
</tr>
<tr>
<td><code>memories/&lt;module&gt;.md</code></td>
<td>Lưu ý thật của từng module: bẫy đã gặp, quyết định đã chốt, quirk môi trường, chỗ hay sai</td>
</tr>
</tbody>
</table>

Ba luồng vận hành:

<table class="rt-table">
<thead>
<tr>
<th>Luồng</th>
<th>Thứ tự</th>
<th>Vì sao phải đúng thứ tự này</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Đọc</strong></td>
<td><code>CLAUDE.md</code> → <code>MEMORY.md</code> → file MD của <strong>đúng module đang làm</strong></td>
<td>Mở thẳng file module mà bỏ qua sơ đồ thì không biết còn file nào liên quan. Mở hết mọi file thì tràn ngữ cảnh — đúng cái bộ nhớ sinh ra để tránh</td>
</tr>
<tr>
<td><strong>Ghi</strong></td>
<td>Đọc <code>MEMORY.md</code> <strong>trước</strong> → rồi mới ghi / cập nhật / thêm file MD</td>
<td>Không đọc sơ đồ trước thì AI đẻ ra file trùng nội dung với file đã có, và file mới không ai biết là nó tồn tại</td>
</tr>
<tr>
<td><strong>Reset</strong></td>
<td>Dự án mới → <strong>xoá thư mục <code>memories/</code></strong></td>
<td>Bộ nhớ gom một chỗ nên reset là một lệnh. Rải ghi chú thẳng vào <code>CLAUDE.md</code> thì mỗi lần chuyển dự án phải ngồi dò từng đoạn</td>
</tr>
</tbody>
</table>

Ba mục tiếp theo giải thích *vì sao* mô hình phải như vậy — cơ chế nạp file của công cụ quyết định gần hết các lựa chọn ở trên. Từ mục 5 mới bắt tay vào dựng.

## 3. Cơ chế — Claude Code nạp gì, vào lúc nào

Bạn đã gặp `CLAUDE.md` và `.claude/rules/` ở bài thiết lập SKILL, RULE. Mục này bổ sung đúng phần quyết định cách tổ chức bộ nhớ: **cái nào nạp lúc mở phiên, cái nào nạp theo nhu cầu.**

### 3.1. Bốn cấp CLAUDE.md — nối chồng, không đè nhau

<table class="rt-table">
<thead>
<tr>
<th>Cấp</th>
<th>Vị trí</th>
<th>Dùng cho</th>
<th>Ai thấy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chính sách tổ chức</td>
<td>Thư mục hệ thống do IT triển khai</td>
<td>Chuẩn toàn công ty, quy định bảo mật</td>
<td>Mọi người trong tổ chức</td>
</tr>
<tr>
<td>Cá nhân</td>
<td><code>~/.claude/CLAUDE.md</code></td>
<td>Thói quen riêng của bạn, áp cho <strong>mọi</strong> dự án</td>
<td>Chỉ bạn</td>
</tr>
<tr>
<td>Dự án</td>
<td><code>./CLAUDE.md</code> hoặc <code>./.claude/CLAUDE.md</code></td>
<td>Chuẩn của đội, commit lên repo</td>
<td>Cả đội qua git</td>
</tr>
<tr>
<td>Riêng máy bạn</td>
<td><code>./CLAUDE.local.md</code></td>
<td>Thứ không nên commit: URL sandbox riêng, dữ liệu test ưa dùng</td>
<td>Chỉ bạn, trong dự án này</td>
</tr>
</tbody>
</table>

Ba điều quan trọng về cách nạp, theo [tài liệu chính thức](https://code.claude.com/docs/en/memory):

- Mọi file tìm thấy được **nối vào ngữ cảnh**, không phải cấp dưới đè cấp trên. Nội dung xếp từ gốc hệ thống xuống thư mục bạn mở phiên, nên chỉ dẫn gần chỗ bạn làm nhất được đọc sau cùng.
- `CLAUDE.md` trong **thư mục con** của nơi bạn mở phiên **không** nạp lúc khởi động — nó chỉ được đưa vào khi Claude thực sự đọc file trong thư mục đó.
- `CLAUDE.local.md` được nối **sau** `CLAUDE.md` cùng thư mục — ghi chú riêng của bạn là thứ cuối cùng Claude đọc ở cấp đó.

> ⚠️ Tài liệu nói thẳng một điều mà Tester cần nhớ: `CLAUDE.md` được đưa vào như **một tin nhắn người dùng sau system prompt**, tức là *ngữ cảnh* chứ không phải cấu hình cưỡng chế — *"không có gì bảo đảm tuân thủ nghiêm ngặt, nhất là với chỉ dẫn mơ hồ hoặc mâu thuẫn"*. Muốn **chặn cứng** một hành động bất kể AI nghĩ gì thì phải dùng [hook](https://code.claude.com/docs/en/hooks-guide), không phải viết vào bộ nhớ. Đây là lý do mục 5.2 dành hẳn một phần cho cách viết câu luật.

### 3.2. `.claude/rules/` — nạp lúc mở phiên hay theo đường dẫn

<table class="rt-table">
<thead>
<tr>
<th>Loại</th>
<th>Nạp khi nào</th>
</tr>
</thead>
<tbody>
<tr>
<td>File RULE <strong>không</strong> khai <code>paths</code></td>
<td>Nạp <strong>lúc mở phiên</strong>, cùng mức ưu tiên với <code>.claude/CLAUDE.md</code></td>
</tr>
<tr>
<td>File RULE có khai <code>paths</code></td>
<td>Chỉ kích hoạt khi Claude <strong>đọc file khớp mẫu</strong> — không phải ở mọi lượt gọi công cụ</td>
</tr>
<tr>
<td><code>~/.claude/rules/</code></td>
<td>Chuẩn cá nhân, áp cho mọi dự án trên máy. Nạp <strong>trước</strong> rule của dự án, nên rule dự án ưu tiên cao hơn</td>
</tr>
</tbody>
</table>

Mọi file `.md` trong `.claude/rules/` đều được tìm thấy **đệ quy**, nên xếp rule vào thư mục con (`rules/manual/`, `rules/api/`) vẫn chạy. Đây là chi tiết dùng tới ở mục 10.

### 3.3. Import `@` — gom file, không tiết kiệm ngữ cảnh

`CLAUDE.md` kéo file khác vào bằng cú pháp `@đường/dẫn`. Bốn điều cần biết trước khi dùng:

<table class="rt-table">
<thead>
<tr>
<th>Đặc điểm</th>
<th>Hệ quả với bộ nhớ</th>
</tr>
</thead>
<tbody>
<tr>
<td>File được import <strong>nạp lúc khởi động</strong> cùng file gọi nó</td>
<td>Import <strong>không</strong> làm nhẹ ngữ cảnh — chỉ giúp chia file cho gọn. Đây là lý do <strong>không</strong> import toàn bộ <code>memories/</code> vào <code>CLAUDE.md</code>: làm vậy là nạp hết mọi module vào mọi phiên</td>
</tr>
<tr>
<td>Import lồng nhau tối đa <strong>4 chặng</strong></td>
<td>Đủ cho mọi cấu trúc hợp lý; chạm trần nghĩa là bạn đang lồng quá sâu</td>
</tr>
<tr>
<td>Đường dẫn tương đối tính từ <strong>file chứa dòng import</strong>, không phải thư mục làm việc</td>
<td>Chuyển file đi chỗ khác là phải sửa lại import</td>
</tr>
<tr>
<td>Cú pháp import <strong>bỏ qua</strong> phần nằm trong dấu backtick</td>
<td>Muốn <em>nhắc tên</em> file mà không import thì bọc trong backtick. Viết <code>@README</code> trần là import thật</td>
</tr>
</tbody>
</table>

Hai lệnh dùng để kiểm, nhớ kỹ vì mục 13 sẽ dùng lại: `/context` cho biết **phiên hiện tại đã nạp file nào** (xem mục *Memory files*), còn `/memory` liệt kê và mở các file bộ nhớ để sửa.

## 4. Vì sao phải tách thư mục riêng, không nhồi hết vào CLAUDE.md

Câu hỏi hợp lý: đã có `CLAUDE.md` nạp mỗi phiên, sao không viết thẳng mọi thứ vào đó? Bốn lý do, và cả bốn đều có thể kiểm chứng:

<table class="rt-table">
<thead>
<tr>
<th>Lý do</th>
<th>Chi tiết</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ngân sách dòng</strong></td>
<td>Tài liệu khuyến nghị mỗi <code>CLAUDE.md</code> <strong>dưới 200 dòng</strong>: <em>file dài hơn tốn ngữ cảnh và làm giảm độ tuân thủ</em>. Một dự án 8 module, mỗi module 15 dòng lưu ý là đã 120 dòng chỉ riêng bối cảnh — chưa tính luật</td>
</tr>
<tr>
<td><strong>Đa số lưu ý không dùng tới</strong></td>
<td>Hôm nay bạn làm module Đăng nhập thì lưu ý của module Khách hàng và Dự án chỉ ngồi chiếm chỗ. Tách file thì <strong>đọc theo nhu cầu</strong></td>
</tr>
<tr>
<td><strong>Reset gọn</strong></td>
<td>Dự án mới: xoá một thư mục. Nếu ghi chú nằm rải trong <code>CLAUDE.md</code> thì phải dò từng đoạn, và thường sót</td>
</tr>
<tr>
<td><strong>Luật và bối cảnh có tuổi thọ khác nhau</strong></td>
<td>Luật (mã TC, độ hạt) ổn định hàng năm; bối cảnh (mã đã dùng tới đâu, AMB nào còn treo) đổi hằng tuần. Trộn chung một file thì mỗi lần sửa bối cảnh lại chạm vào file chứa luật</td>
</tr>
</tbody>
</table>

### 4.1. Claude Code đã có sẵn một bộ nhớ tự động — vì sao vẫn cần `memories/`

Điều thú vị: Claude Code có sẵn cơ chế **auto memory**, và nó dùng đúng hình dạng bạn sắp dựng — một thư mục bộ nhớ có file `MEMORY.md` làm chỉ mục cộng với các file chủ đề. Nhưng nó **không thay thế được** thư mục `memories/` trong repo:

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Auto memory có sẵn</th>
<th><code>memories/</code> bạn dựng</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ai viết</strong></td>
<td>Claude tự ghi, dựa trên các lần bạn chỉnh nó</td>
<td>Bạn viết, và bảo AI ghi thêm khi phát hiện điều đáng nhớ</td>
</tr>
<tr>
<td><strong>Nằm ở đâu</strong></td>
<td>Thư mục cấu hình của Claude Code trên máy, <strong>ngoài repo</strong></td>
<td>Trong repo dự án</td>
</tr>
<tr>
<td><strong>Đội có thấy không</strong></td>
<td>❌ <strong>Không.</strong> Tài liệu ghi rõ: bộ nhớ này là <em>machine-local</em>, không chia sẻ sang máy khác hay môi trường đám mây</td>
<td>✅ Có — commit lên git, người mới clone về là có ngay</td>
</tr>
<tr>
<td><strong>Bật/tắt</strong></td>
<td>Bật sẵn; tắt được bằng cấu hình</td>
<td>Do bạn dựng, luôn có</td>
</tr>
</tbody>
</table>

Nói cách khác: auto memory giúp **bạn** đỡ phải nhắc lại; `memories/` giúp **cả đội và người đến sau** không phải hỏi lại. Một dự án kiểm thử thật cần cả hai, nhưng thứ đem bàn giao được là cái thứ hai.

> 💡 Hình dạng "một file chỉ mục + nhiều file chủ đề" không phải bạn nghĩ ra, cũng không phải Anthropic nghĩ ra hộ bạn — nó là cách **duy nhất** giải được bài toán "nạp ít mà tra được nhiều". Chỉ mục đủ nhỏ để luôn đọc; chi tiết nằm ngoài, mở khi cần.

## 5. Dựng `memories/` — ba bước

### 5.1. Bước 1 — tạo thư mục và file sơ đồ

Ở gốc dự án (ngang hàng với `CLAUDE.md` và `docs/`):

```none
memories/
├── MEMORY.md
└── _project.md
```

Đặt ở **gốc dự án**, không nhét vào `.claude/`. Lý do rất thực tế: `.claude/` là khung dùng lại được cho mọi dự án (kit, rule, skill), còn `memories/` là thứ **chết theo dự án**. Để tách hẳn hai thứ thì lúc xoá không sợ tay trượt vào bộ kit.

### 5.2. Bước 2 — viết câu luật vào CLAUDE.md

Đây là bước quan trọng nhất và cũng là bước hay bị làm hỏng nhất. Thư mục `memories/` **không** được công cụ nạp tự động; nó chỉ được đọc vì có một câu luật bảo thế. Mà như mục 3.1 đã nói, câu luật là *ngữ cảnh* chứ không phải cưỡng chế — viết mơ hồ là AI bỏ qua.

Thêm vào `CLAUDE.md` của dự án:

```none
## Bộ nhớ dự án (BẮT BUỘC)

- **Trước khi làm bất kỳ việc gì**, đọc `memories/MEMORY.md` để biết
  module đang làm có file bộ nhớ nào. Chỉ mở file của đúng module đó.
- **Trước khi ghi/sửa/thêm** file trong `memories/`, đọc `MEMORY.md` trước
  để không tạo file trùng. Thêm file mới thì thêm luôn một dòng vào `MEMORY.md`.
- `memories/` chỉ chứa **lưu ý** — không chép nội dung `docs/` sang, chỉ trỏ link.
- KHÔNG ghi mật khẩu, token vào `memories/`. Chỉ ghi tên biến trong `.env`.
```

So sánh cách viết — cùng một ý, độ tuân thủ khác hẳn:

<table class="rt-table">
<thead>
<tr>
<th>❌ Viết như thế này thì AI bỏ qua</th>
<th>✅ Viết như thế này</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>"Nên tham khảo bộ nhớ dự án nếu cần"</em></td>
<td><em>"<strong>Trước khi làm bất kỳ việc gì</strong>, đọc <code>memories/MEMORY.md</code>"</em></td>
</tr>
<tr>
<td><em>"Ghi chú lại những gì quan trọng"</em></td>
<td><em>"Thêm file mới thì thêm luôn một dòng vào <code>MEMORY.md</code>"</em></td>
</tr>
<tr>
<td><em>"Chú ý bảo mật thông tin"</em></td>
<td><em>"KHÔNG ghi mật khẩu, token. Chỉ ghi tên biến trong <code>.env</code>"</em></td>
</tr>
</tbody>
</table>

Nguyên tắc rút ra từ tài liệu chính thức: **cụ thể tới mức kiểm chứng được**. Tài liệu lấy ví dụ *"dùng thụt lề 2 khoảng trắng"* thay vì *"định dạng code cho gọn"* — với bộ nhớ cũng vậy, phải nêu rõ *đọc file nào*, *vào lúc nào*, *làm gì sau đó*.

### 5.3. Bước 3 — thêm `memories` vào lệnh dọn dự án

Bộ kit có sẵn một lệnh dọn khi chuyển sang dự án mới. Vì `memories/` là thứ bạn thêm vào, lệnh đó chưa biết tới nó — phải bổ sung, nếu không bộ nhớ của dự án cũ sẽ theo sang dự án mới và AI nói chuyện về một hệ thống không còn tồn tại:

```none
rm -rf docs memories .playwright-mcp task.md .claude/settings.local.json
```

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th>Nội dung</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Xoá</strong></td>
<td><code>docs/</code> (gồm cả bug) · <strong><code>memories/</code></strong> · <code>.playwright-mcp/</code> · <code>task.md</code> · <code>.claude/settings.local.json</code></td>
</tr>
<tr>
<td><strong>Giữ nguyên</strong></td>
<td><code>.claude/</code> (trừ <code>settings.local.json</code>) · <code>plans/</code> · <code>prompts/</code> · <code>scripts/</code> · <code>CLAUDE.md</code> · <code>README.md</code> · <code>.gitignore</code> — khung dùng lại được, không gắn với hệ thống nào</td>
</tr>
</tbody>
</table>

> ⚠️ Câu luật ở `CLAUDE.md` thì **giữ nguyên** khi chuyển dự án — chỉ xoá thư mục. Phiên đầu tiên trên dự án mới, AI đọc luật, không thấy `memories/MEMORY.md`, và đó chính là tín hiệu để tạo lại từ đầu.

## 6. `MEMORY.md` — viết sơ đồ, không viết nội dung

Đây là chỗ mô hình sống hay chết. Sơ đồ phải **đủ nhỏ để luôn đọc**: một dòng cho một file, kèm một móc câu đủ để AI quyết định có mở file đó hay không.

```none
# Bộ nhớ dự án — CRM (Perfex)

> Đọc file này TRƯỚC. Chỉ mở file bộ nhớ của module đang làm.
> Thêm file mới ⇒ thêm một dòng vào bảng dưới, cùng lượt.

| File | Mở khi nào |
|---|---|
| [_project.md](_project.md) | **Luôn đọc** — môi trường, quyền hạn của QA, quy ước mã, đầu mối |
| [login.md](login.md) | Làm module Đăng nhập / Xác thực |
| [customers.md](customers.md) | Làm module Khách hàng |

## Nhật ký
- 18-09-2026 — thêm `login.md` sau đợt bổ sung TC 4 vòng
- 18-09-2026 — tạo bộ nhớ dự án
```

<table class="rt-table">
<thead>
<tr>
<th>Luật của file sơ đồ</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Một dòng một file</strong>, không có lưu ý chi tiết trong đây</td>
<td>Nhét nội dung vào chỉ mục là tạo <strong>nguồn thứ hai</strong> — đúng cái lỗi bài trước vừa dạy cách tránh. Sáu tháng sau không ai biết bản nào đang đúng</td>
</tr>
<tr>
<td>Móc câu viết theo <strong>"mở khi nào"</strong>, không phải "file này nói về gì"</td>
<td>AI đang quyết định <em>có cần mở không</em>. <em>"Làm module Đăng nhập"</em> trả lời thẳng câu đó; <em>"ghi chú module login"</em> thì không</td>
</tr>
<tr>
<td>Có đúng <strong>một</strong> file gắn nhãn <em>"Luôn đọc"</em></td>
<td>Bối cảnh cấp dự án (môi trường dùng chung, quyền hạn QA) ảnh hưởng tới mọi việc. Nhưng chỉ một file thôi — hai ba file "luôn đọc" là quay lại bài toán nạp thừa</td>
</tr>
<tr>
<td>Có mục <strong>Nhật ký</strong> ghi ngày</td>
<td>Bộ nhớ không ghi ngày thì không ai dám tin, và cũng không biết dòng nào đã cũ</td>
</tr>
</tbody>
</table>

Dấu hiệu sơ đồ đã hỏng, nhìn là biết: file dài quá một màn hình · có đoạn văn giải thích thay vì một dòng · có lưu ý mà không file nào khác giữ · có dòng trỏ tới file đã xoá.

## 7. File bộ nhớ từng module — ghi cái gì

### 7.1. Sáu nhóm đáng nhớ của một dự án kiểm thử

Bộ kit có sẵn một bảng rất hợp làm khung: bảng *"Chốt trước khi phân tích module đầu tiên"* trong `CLAUDE.md`, liệt kê những thứ phải chốt và **ai xác định**. Đó chính là danh sách "nhớ cái gì":

<table class="rt-table">
<thead>
<tr>
<th>Nhóm</th>
<th>Ví dụ cụ thể</th>
<th>Vì sao phải nhớ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Quy ước mã</strong></td>
<td>Prefix TC ID của module, dải đã dùng, mã kế tiếp, độ hạt đang dùng</td>
<td>Đặt trùng mã là vỡ truy vết; đổi độ hạt giữa chừng là đánh lại toàn bộ TC ID</td>
</tr>
<tr>
<td><strong>Môi trường</strong></td>
<td>Dùng chung hay riêng · URL · tài khoản lưu ở biến nào trong <code>.env</code> · giờ nào không được chạy</td>
<td>Bộ kit <strong>hỏi một lần</strong> rồi bật/tắt quy tắc auto-skip theo câu trả lời. Không nhớ thì mỗi phiên phải hỏi lại, và có phiên sẽ trả lời sai</td>
</tr>
<tr>
<td><strong>Quyền hạn của QA</strong></td>
<td>Có được gọi API không · truy vấn cơ sở dữ liệu không · xem nhật ký hoạt động không</td>
<td>Đây là đầu vào của nhánh <strong>Vòng 3 — Technical</strong> ở mọi bộ TC. Kit ghi rõ: hỏi lại ở từng module là <strong>sai</strong></td>
</tr>
<tr>
<td><strong>Quyết định đã chốt</strong></td>
<td>Câu trả lời của PO cho từng điểm mờ, ngày chốt, ai chốt · điểm mờ nào <strong>còn treo</strong></td>
<td>Điểm mờ còn treo mà quên là sinh TC dựa trên giả định tạm rồi không ai rà lại</td>
</tr>
<tr>
<td><strong>Bẫy đã gặp</strong></td>
<td>Chỗ hay chấm nhầm trạng thái · dữ liệu hay đụng nhau · bước hay bị bỏ sót khi chạy tay</td>
<td>Đây là thứ đắt nhất — nó là kinh nghiệm phải trả giá mới có, và là thứ người mới vào đội không cách nào tự biết</td>
</tr>
<tr>
<td><strong>Đường đi tài liệu</strong></td>
<td>Link tới file index TC, execution gần nhất, bug đang mở của module</td>
<td>Trỏ đường, để AI không phải quét cả <code>docs/</code></td>
</tr>
</tbody>
</table>

### 7.2. Một file bộ nhớ thật

`memories/login.md` cho module Đăng nhập của CRM demo:

```none
# Bộ nhớ — Module Đăng nhập / Xác thực

**Cập nhật:** 18-09-2026

## Quy ước mã
- Prefix: `CRM_LOGIN_TC_` · đã dùng `001`→`050` · **mã kế tiếp `051`**
- Độ hạt: **GỘP** — 50 TC · 70 biến thể. Bản TÁCH 82 TC nằm ở `archive/`
- 🚫 KHÔNG đổi độ hạt: đã có execution report và bug trỏ vào TC ID hiện tại

## Điểm mờ còn treo
- `AMB-19` — chưa có câu trả lời của PO. TC dựa trên giả định tạm đang gắn
  nhãn giả định; PO trả lời xong thì phải chạy chế độ cập nhật theo tác động,
  đừng sửa tay từng TC

## Bẫy đã gặp
- 25/50 TC có dòng `Ghi chú kỹ thuật` ⇒ gắn `@TechCheck`. Những TC này
  **không chạy được** nếu tài khoản QA không có quyền xem nhật ký — kiểm
  quyền trước khi nhận chạy, đừng chấm BLOCKED hàng loạt rồi mới phát hiện
- Bug `TC018` (độ dài phần trước dấu `@`): hệ thống đang lệch chuẩn. TC được
  thiết kế để FAIL — thấy đỏ là **đúng**, không phải lỗi người chạy

## Đường đi tài liệu
- TC: `docs/testcases/login/test_cases_login.md`
- Bug đang mở: `docs/bugs/login/`
```

Để ý bốn thói quen trong file trên — chúng là thứ phân biệt một bộ nhớ dùng được với một đống ghi chú:

<table class="rt-table">
<thead>
<tr>
<th>Thói quen</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mỗi lưu ý kèm <strong>việc phải làm</strong></td>
<td><em>"Kiểm quyền trước khi nhận chạy"</em> dùng được ngay. <em>"Module này hơi khó chạy"</em> thì không</td>
</tr>
<tr>
<td>Ghi cả điều <strong>không được làm</strong></td>
<td>Dòng 🚫 về độ hạt chặn được một hành động phá truy vết mà nhìn bề ngoài rất vô hại</td>
</tr>
<tr>
<td><strong>Trỏ link</strong>, không chép nội dung</td>
<td>Chép bảng TC vào bộ nhớ là tạo bản sao sẽ lỗi thời trong một tuần</td>
</tr>
<tr>
<td>Có <strong>ngày cập nhật</strong></td>
<td>Người đọc biết dòng nào còn đáng tin. Kit quy định ngày trong tài liệu viết <code>DD-MM-YYYY</code></td>
</tr>
</tbody>
</table>

## 8. Ranh giới — `memories/`, `docs/`, `rules/` và `.env`

Bốn chỗ chứa thông tin, rất dễ lẫn. Nhầm chỗ thì hoặc mất, hoặc nhân đôi, hoặc lộ:

<table class="rt-table">
<thead>
<tr>
<th>Nơi</th>
<th>Chứa gì</th>
<th>Ai tạo</th>
<th>Dấu hiệu nhận biết</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>docs/</code></td>
<td>Tài liệu sản phẩm: REQ, Test Case, execution report, bug</td>
<td>Workflow của bộ kit sinh ra</td>
<td>Có <strong>mã truy vết</strong>, có định dạng chuẩn, đem <strong>bàn giao</strong> được</td>
</tr>
<tr>
<td><code>memories/</code></td>
<td>Lưu ý vận hành: bẫy, quyết định, quirk, mã đã dùng tới đâu</td>
<td>Bạn và AI ghi trong lúc làm</td>
<td>Là thứ bạn sẽ <strong>nói miệng</strong> cho người mới vào đội</td>
</tr>
<tr>
<td><code>.claude/rules/</code></td>
<td>Quy tắc: tài liệu phải trông thế nào</td>
<td>Bạn viết một lần, sửa hiếm</td>
<td>Câu <strong>mệnh lệnh</strong>, đúng ở mọi module, không gắn với dự án cụ thể nào</td>
</tr>
<tr>
<td><code>.env</code></td>
<td>Bí mật: mật khẩu, token, khoá API</td>
<td>Bạn, và <strong>không commit</strong></td>
<td>Lộ ra là phải đổi ngay</td>
</tr>
</tbody>
</table>

Hai câu hỏi tự kiểm khi không biết viết vào đâu:

1. **"Dự án khác có dùng lại được không?"** Có → `rules/`. Không → `memories/`.
2. **"Cái này có mã truy vết không?"** Có → nó thuộc `docs/`, bộ nhớ chỉ trỏ link tới.

> 📌 Bộ kit có một câu dễ gây hiểu nhầm ở mục cấu trúc `docs/`: *"Không có file hồ sơ dự án để điền tay — ngữ cảnh dự án nằm trong `docs/` do agent tự sinh."* Câu đó nói về **đặc tả hệ thống**: đừng ngồi điền tay một bản mô tả module song song với requirements mà workflow đã sinh. Nó không cấm ghi lưu ý vận hành — thứ mà `docs/` theo thiết kế **không** chứa. Ranh giới vẫn là: **không chép nội dung `docs/` sang `memories/`, chỉ trỏ link.**

🔒 Và một luật cứng: `memories/` được commit cho cả đội, nên **không ghi giá trị bí mật** vào đó. Bộ nhớ chỉ ghi *tên biến* — ví dụ *"tài khoản Project Manager lấy ở biến `PM_EMAIL` / `PM_PASSWORD` trong `.env`"*. Lịch sử git không xoá được bằng cách sửa file, nên lỡ ghi một lần là phải đổi mật khẩu.

## 9. Một phiên làm việc thật

Ghép bộ nhớ vào chuỗi đọc tài liệu mà bộ kit đã có, một phiên chuẩn diễn ra thế này:

<table class="rt-table">
<thead>
<tr>
<th>Bước</th>
<th>Đọc gì</th>
<th>Trả lời câu hỏi</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><code>CLAUDE.md</code> + <code>.claude/rules/</code></td>
<td>Luật của đội — tự động, không cần làm gì</td>
</tr>
<tr>
<td>2</td>
<td><code>memories/MEMORY.md</code></td>
<td>Dự án này có bộ nhớ gì, module tôi sắp làm có file riêng không</td>
</tr>
<tr>
<td>3</td>
<td><code>memories/_project.md</code> + file module</td>
<td>Môi trường ra sao, quyền hạn tới đâu, bẫy nào phải né</td>
</tr>
<tr>
<td>4</td>
<td><code>docs/requirements/README.md</code></td>
<td>Hệ thống có module nào, prefix đã chiếm, mã kế tiếp</td>
</tr>
<tr>
<td>5</td>
<td>File index của <strong>đúng</strong> module</td>
<td>Từng field, từng rule, từng thông báo</td>
</tr>
</tbody>
</table>

Bước 4–5 là **chuỗi đọc ba tầng** có sẵn của bộ kit, kèm một luật quan trọng: **không** quét toàn bộ `docs/requirements/*/` để "đọc cho chắc" — đó là cách nhanh nhất làm tràn ngữ cảnh và trả lời sai chi tiết. Bộ nhớ ở bước 2–3 phục vụ đúng mục đích đó: nó nói cho AI biết *phải mở cái gì*, để không phải mở tất.

Câu mở phiên bạn dán vào chat:

```none
Đọc memories/MEMORY.md và memories/_project.md để nắm bối cảnh dự án,
rồi đọc docs/requirements/README.md. Hôm nay làm module Đăng nhập —
mở thêm memories/login.md. Chưa cần mở file requirements của module nào.
Tóm tắt lại: môi trường, quyền hạn QA, mã TC kế tiếp, điểm mờ còn treo.
```

Và cuối phiên — phần hay bị bỏ nhất:

```none
Hôm nay có phát hiện gì đáng ghi vào bộ nhớ không? Đọc memories/MEMORY.md
trước, rồi cập nhật vào đúng file đang có. Chỉ ghi thứ phiên sau cần biết,
không chép lại nội dung đã có trong docs/.
```

> 💡 Hai câu trên nên dán vào `prompts/` của dự án để cả đội dùng chung. Bộ nhớ chỉ tốt bằng thói quen cập nhật nó — và thói quen thì cần một câu sẵn để copy, không cần ý chí.

## 10. Dự án lớn, nhiều sub-project

Ở bài **Cách thiết lập SKILL, RULE cho AI Agent trên Claude + Codex** đã hẹn sẽ nói kỹ phần này. Khi một repo chứa nhiều hệ thống con — hoặc công ty bạn gộp nhiều sản phẩm vào một repo — có ba cách chia, và chúng chồng lên nhau chứ không loại trừ nhau.

<table class="rt-table">
<thead>
<tr>
<th>Cách</th>
<th>Nạp khi nào</th>
<th>Hợp khi</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CLAUDE.md</code> <strong>ở từng thư mục con</strong></td>
<td>Nạp lúc mở phiên <strong>nếu bạn khởi động Claude từ thư mục đó</strong>; nếu khởi động từ gốc thì nạp theo nhu cầu khi Claude đọc file trong đó</td>
<td>Mỗi hệ thống con có người phụ trách riêng, và họ tự giữ quy ước của mình</td>
</tr>
<tr>
<td>Rule khai <code>paths</code> ở <code>.claude/rules/</code> gốc</td>
<td>Khi Claude làm việc với file khớp mẫu</td>
<td>Bạn muốn mọi quy ước gom một chỗ, hoặc cùng một luật áp cho nhiều đường dẫn rải rác</td>
</tr>
<tr>
<td>Thư mục <code>memories/</code> chia theo hệ thống con</td>
<td>Theo sơ đồ <code>MEMORY.md</code></td>
<td>Luôn — bối cảnh vốn đã tách theo module, chỉ cần thêm một tầng</td>
</tr>
</tbody>
</table>

Một mẹo rất hiệu quả mà tài liệu nêu thẳng: **khởi động Claude từ thư mục con** khi công việc chỉ nằm trong một hệ thống con. Khi đó Claude nạp `CLAUDE.md` của thư mục đó cộng với mọi cấp cha, và **không** có chỉ dẫn của hệ thống con khác trong ngữ cảnh.

Với repo nhiều đội mà bạn không bao giờ đụng tới phần của đội khác, có cấu hình `claudeMdExcludes` để bỏ hẳn `CLAUDE.md` và rule của những thư mục đó. Đặt vào `.claude/settings.local.json` nếu chỉ muốn áp cho riêng máy bạn. Chi tiết ở [tài liệu về repo lớn](https://code.claude.com/docs/en/large-codebases).

Cấu trúc bộ nhớ khi có nhiều hệ thống con, giữ đúng nguyên tắc "sơ đồ chỉ đường":

```none
memories/
├── MEMORY.md          ← sơ đồ chung, chia theo hệ thống
├── _project.md
├── crm/
│   ├── login.md
│   └── customers.md
└── portal/
    └── dang-ky.md
```

## 11. Nhiều dự án trên một máy

Mục 10 nói về nhiều hệ thống **trong một repo**. Mục này là chuyện thường gặp hơn với Tester: bạn chạy **nhiều dự án khác nhau** trên cùng một máy, và không muốn AI mang bối cảnh dự án A sang dự án B.

<table class="rt-table">
<thead>
<tr>
<th>Loại nội dung</th>
<th>Đặt ở đâu</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Thói quen cá nhân của bạn (ngôn ngữ báo cáo, cách trình bày)</td>
<td><code>~/.claude/CLAUDE.md</code> hoặc <code>~/.claude/rules/</code></td>
<td>Áp cho mọi dự án, không phải chép lại từng repo. Rule cá nhân nạp <strong>trước</strong> rule dự án nên dự án vẫn ưu tiên cao hơn</td>
</tr>
<tr>
<td>Chuẩn của công ty (mã TC, độ hạt, mẫu bug)</td>
<td><code>.claude/rules/</code> trong repo, commit</td>
<td>Cả đội dùng chung, đi theo repo — đúng như bài trước đã dựng</td>
</tr>
<tr>
<td>Bối cảnh riêng dự án</td>
<td><code>memories/</code> trong repo, commit</td>
<td>Chết theo dự án. Xoá thư mục là hết</td>
</tr>
<tr>
<td>Thứ chỉ đúng trên máy bạn (đường dẫn, dữ liệu test ưa dùng)</td>
<td><code>CLAUDE.local.md</code>, thêm vào <code>.gitignore</code></td>
<td>Không đẩy lên repo chung. Tài liệu chính thức khuyến nghị đúng cách này</td>
</tr>
</tbody>
</table>

Ba thứ hay theo nhầm sang dự án mới, kiểm trước khi bàn giao máy hoặc mở dự án kế tiếp:

<table class="rt-table">
<thead>
<tr>
<th>Thứ sót lại</th>
<th>Hậu quả</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>memories/</code> của dự án cũ</td>
<td>AI nói về module, mã TC, môi trường của một hệ thống không còn liên quan — và nói rất tự tin</td>
</tr>
<tr>
<td><code>.claude/settings.local.json</code></td>
<td>Chứa quyền tích luỹ theo từng máy/phiên, thường kèm <strong>đường dẫn tuyệt đối của dự án cũ</strong></td>
</tr>
<tr>
<td>Ảnh evidence trong <code>docs/executions/.../evidence/</code></td>
<td>Chụp hệ thống thật, thường có tên khách hàng, email, số tiền. 🔒 Kiểm trước khi xoá <code>docs/</code>, và <strong>đừng bao giờ commit lên repo công khai</strong></td>
</tr>
</tbody>
</table>

## 12. Giữ bộ nhớ khỏi phình to và lỗi thời

Bộ nhớ hỏng theo hai kiểu, và kiểu thứ hai nguy hiểm hơn nhiều:

<table class="rt-table">
<thead>
<tr>
<th>Kiểu hỏng</th>
<th>Biểu hiện</th>
<th>Cách chữa</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Phình to</strong></td>
<td>File module dài như một bản đặc tả; sơ đồ tràn màn hình; mọi thứ đều "quan trọng"</td>
<td>Hỏi từng dòng: <em>"phiên sau có cần cái này không?"</em> Không → xoá. Cái nào là đặc tả → chuyển sang <code>docs/</code></td>
</tr>
<tr>
<td><strong>Lỗi thời</strong></td>
<td>Bộ nhớ ghi "mã kế tiếp 051" trong khi thực tế đã tới 067; ghi một điểm mờ còn treo mà PO trả lời từ tháng trước</td>
<td>Ghi ngày cho mọi mục. Cập nhật <strong>ngay trong lượt</strong> phát sinh thay đổi, không để cuối tuần</td>
</tr>
</tbody>
</table>

Bộ nhớ lỗi thời nguy hiểm hơn bộ nhớ trống, vì AI tin nó và bạn cũng tin — không ai đi kiểm một thứ trông như đã được ghi chép cẩn thận. Đây đúng là điều mà tài liệu chính thức cảnh báo về chỉ dẫn mâu thuẫn: *nếu hai luật nói ngược nhau, Claude có thể chọn một cách tuỳ ý*.

<table class="rt-table">
<thead>
<tr>
<th>Thói quen giữ bộ nhớ sống</th>
<th>Cách làm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ghi ngay lúc phát hiện</strong></td>
<td>Vừa mất 30 phút vì một bẫy → ghi ngay câu đó vào file module, đúng lượt đó. Để tới cuối tuần là quên mất chi tiết làm nên giá trị của nó</td>
</tr>
<tr>
<td><strong>Review trong pull request</strong></td>
<td>Coi thay đổi trong <code>memories/</code> như mọi thay đổi tài liệu khác — có người đọc lại thì bộ nhớ không trôi</td>
</tr>
<tr>
<td><strong>Rà lại sau mỗi đợt lớn</strong></td>
<td>Xong một release: mở từng file, xoá mục đã hết hiệu lực, gộp mục trùng, cập nhật ngày</td>
</tr>
<tr>
<td><strong>Đừng ghi thứ suy ra được</strong></td>
<td>Cấu trúc thư mục, danh sách file, những gì <code>docs/</code> đã nói — AI tự đọc được. Ghi lại chỉ tạo thêm một bản sẽ lỗi thời</td>
</tr>
</tbody>
</table>

## 13. Nghiệm thu

### 13.1. Checklist

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
<td><code>CLAUDE.md</code> có câu luật bắt đọc <code>memories/MEMORY.md</code>, viết dạng mệnh lệnh cụ thể — không phải "nên tham khảo"</td>
</tr>
<tr>
<td>2</td>
<td>Mở phiên mới, gõ <code>/context</code>: <code>CLAUDE.md</code> có trong mục <strong>Memory files</strong></td>
</tr>
<tr>
<td>3</td>
<td>Hỏi một câu bất kỳ về module: AI <strong>tự</strong> mở <code>MEMORY.md</code> rồi mở đúng file module — không phải bạn nhắc</td>
</tr>
<tr>
<td>4</td>
<td><code>MEMORY.md</code> gọn trong một màn hình, mỗi dòng một file, <strong>không</strong> chứa lưu ý chi tiết</td>
</tr>
<tr>
<td>5</td>
<td>Mỗi file module có ngày cập nhật; mỗi lưu ý kèm việc phải làm</td>
</tr>
<tr>
<td>6</td>
<td>Không có nội dung nào của <code>docs/</code> bị chép sang <code>memories/</code> — chỉ có link</td>
</tr>
<tr>
<td>7</td>
<td>🔒 Grep toàn <code>memories/</code>: không có mật khẩu, token, cookie phiên. Chỉ có tên biến</td>
</tr>
<tr>
<td>8</td>
<td>Lệnh dọn dự án mới đã có <code>memories</code> trong danh sách xoá</td>
</tr>
<tr>
<td>9</td>
<td>Thử nghiệm reset: xoá <code>memories/</code>, mở phiên mới — AI báo chưa có bộ nhớ và đề nghị tạo, chứ không im lặng chạy tiếp</td>
</tr>
</tbody>
</table>

### 13.2. Ba lỗi hay gặp nhất

**Lỗi 1 — Sơ đồ biến thành kho.** Ban đầu `MEMORY.md` chỉ có mấy dòng trỏ đường. Vài tuần sau nó có cả lưu ý, cả bảng, cả đoạn giải thích — vì "ghi thẳng vào đây cho nhanh". Lúc đó bạn có hai nguồn cho cùng một sự thật, và cái luôn được nạp lại là cái không ai buồn cập nhật.

**Lỗi 2 — Chép `docs/` vào bộ nhớ.** Thấy bảng Test Case tiện quá nên chép một phần sang `memories/login.md` cho "khỏi phải mở file". Một tuần sau TC được cập nhật theo ticket, bản trong bộ nhớ thì không — và vì bộ nhớ được đọc *trước*, AI làm theo bản cũ.

**Lỗi 3 — Ghi bộ nhớ mà không ghi luật.** Dựng thư mục rất đẹp, viết file rất kỹ, nhưng quên câu luật trong `CLAUDE.md`. Thư mục `memories/` không được nạp tự động, nên nó nằm im ở đó; bạn thì tưởng AI đã đọc và không hiểu vì sao nó vẫn hỏi lại những thứ đã ghi rõ ràng.

## 14. Bài tập thực hành

**Bài tập 1 — Dựng bộ nhớ cho một module bạn đang làm.** Tạo `memories/`, `MEMORY.md`, `_project.md` và một file module. Thêm câu luật vào `CLAUDE.md`. Mở phiên mới, gõ `/context` kiểm file đã nạp, rồi hỏi một câu về module đó — AI phải tự mở đúng file, không cần bạn nhắc.

**Bài tập 2 — Thử phá rồi sửa.** Sửa câu luật trong `CLAUDE.md` thành *"nên tham khảo bộ nhớ nếu cần"*. Mở phiên mới, hỏi lại đúng câu ở bài tập 1. Ghi lại AI có tự đọc bộ nhớ không. Rồi đổi về câu mệnh lệnh và thử lại. Đây là bài tập cho bạn cảm giác trực tiếp về câu *"chỉ dẫn mơ hồ thì không bảo đảm được tuân thủ"*.

**Bài tập 3 — Phân loại 10 mẩu thông tin.** Lấy 10 thứ bạn đang nhớ trong đầu về dự án hiện tại và phân vào bốn cột của mục 8: `docs/` · `memories/` · `rules/` · `.env`. Dùng hai câu hỏi tự kiểm. Thứ nào bạn phân vân lâu nhất thường là thứ đang nằm sai chỗ trong dự án thật.

**Bài tập 4 — Diễn tập chuyển dự án.** Sao lưu repo, chạy lệnh dọn ở mục 5.3, mở phiên mới và hỏi về module cũ. AI phải **không** biết gì về nó. Nếu nó vẫn nói đúng tên module hay mã TC, nghĩa là còn chỗ nào đó giữ bối cảnh cũ — tìm cho ra, đó chính là chỗ sẽ gây nhầm lẫn ở dự án thật.

**Bài tập 5 — Viết câu mở phiên và câu kết phiên của riêng bạn.** Dựa trên mẫu ở mục 9, sửa cho khớp dự án của bạn và lưu vào `prompts/`. Dùng trong một tuần, rồi xem lại bộ nhớ đã dày lên được bao nhiêu — và mục nào bạn ghi vào mà chưa lần nào cần đọc lại.

## 15. Tổng kết

- **Thứ nói trong chat thì mất, thứ ghi vào file thì đọc lại được.** Mỗi phiên bắt đầu từ ngữ cảnh trống, và ngay trong một phiên dài thì chỉ dẫn chỉ nói bằng miệng cũng biến mất sau lần nén ngữ cảnh — trong khi `CLAUDE.md` ở gốc dự án được đọc lại từ đĩa.
- **Sơ đồ ba chặng:** `CLAUDE.md` → `memories/MEMORY.md` → file MD của đúng module. Luồng ghi thì ngược lại một nhịp: **đọc sơ đồ trước**, rồi mới ghi/cập nhật/thêm file.
- **Một câu luật trong `CLAUDE.md` là thứ giữ cả cơ chế sống.** Thư mục `memories/` không được nạp tự động. Câu luật phải là mệnh lệnh cụ thể — viết mơ hồ thì AI bỏ qua, vì đây là ngữ cảnh chứ không phải cấu hình cưỡng chế.
- **Sơ đồ chỉ đường, không chứa nội dung.** Một dòng một file, móc câu viết theo "mở khi nào". Nhét lưu ý vào chỉ mục là tạo nguồn thứ hai.
- **Nhớ sáu nhóm:** quy ước mã · môi trường · quyền hạn của QA · quyết định đã chốt và điểm mờ còn treo · bẫy đã gặp · đường đi tài liệu. Mỗi lưu ý kèm việc phải làm, kèm ngày.
- **Bốn chỗ chứa, đừng lẫn:** `docs/` tài liệu sản phẩm có mã truy vết · `memories/` lưu ý vận hành · `rules/` quy tắc dùng lại được · `.env` bí mật. Không chép `docs/` sang bộ nhớ, chỉ trỏ link. Không ghi mật khẩu vào file được commit.
- **Dự án lớn thì chia theo thư mục** — `CLAUDE.md` ở thư mục con nạp theo nhu cầu, khởi động Claude từ thư mục con để chỉ nạp phần liên quan, và `claudeMdExcludes` để bỏ hẳn phần của đội khác.
- **Dự án mới thì xoá `memories/` là xong** — nhớ thêm nó vào lệnh dọn, và kiểm luôn `.claude/settings.local.json` cùng ảnh evidence trước khi xoá.
- **Bộ nhớ lỗi thời nguy hiểm hơn bộ nhớ trống**, vì nó trông như đã được ghi chép cẩn thận nên không ai đi kiểm. Ghi ngày, cập nhật ngay trong lượt, rà lại sau mỗi đợt lớn.
- Bài kế tiếp: **Sử dụng MCP Server trên các nền tảng ứng dụng trong công việc** — bộ nhớ giúp AI nhớ những gì bạn đã ghi lại; MCP Server giúp nó với tay sang được các hệ thống bạn đang dùng hằng ngày.