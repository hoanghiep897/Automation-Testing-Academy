# Bài 4 - Cách viết Prompt và sử dụng Token hiệu quả cho AI Agent trên Claude + Codex

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/330](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/330)

✅ Cách viết Prompt chuẩn để AI hiểu đúng yêu cầu, AI trả lời đầy đủ hơn  
✅ Cách sử dụng Token hiệu quả, cài đặt tools tối ưu Token  
✅ Thực hành viết prompt trên Claude và Codex

## 1. Prompt là gì?

**Prompt** là đoạn mô tả hoặc câu lệnh bạn gửi cho AI để yêu cầu AI thực hiện một nhiệm vụ.

Ví dụ đơn giản:

❌ Prompt kém

*`Viết test case cho login`*

AI sẽ không biết:

- Kiểm thử loại gì (Functional, UI, Edge case...)
- Test level nào (Smoke, Regression...)
- Validate ra sao
- Trình bày test case theo format nào

✅ Prompt tốt hơn

*`Viết test case cho chức năng Login`*  
  
*`Loại kiểm thử:`*  
*`- Manual functional testing`*  
*`- Web application`*  
*`- Bao gồm: Happy path, Negative case, Edge case`*

AI lúc này sẽ hiểu **bối cảnh kỹ thuật** tốt hơn, đúng ý của mình hơn, không cần hỏi lại, hạn chế trao đổi nhiều.

## 🧠 Các tiêu chí của Prompt hiệu quả

Một Prompt hiệu quả thường có các đặc trưng:

1. **Rõ ràng, đủ thông tin (Clear)**
2. **Có bối cảnh, hệ thống như nào (Context)**
3. **Nhiệm vụ cụ thể (Task)**
4. **Có ràng buộc, yêu cầu làm gì và không được làm gì (Constraints)**
5. **Chỉ định định dạng kết quả nếu muốn cụ thể theo ý (Output format)**
6. **Xác định vai trò AI (Role) - Không bắt buộc**

## 2. Cấu trúc của một Prompt chuẩn cho Claude & Codex

Áp dụng cho các tác vụ AI-assisted testing (sinh test case, viết test script, review test case, viết bug report...). Cấu trúc này dùng chung được cho cả Claude và Codex, chỉ khác đôi chút ở cách "nạp" ngữ cảnh.

```markdown
### ROLE (Vai trò)
Bạn là [vai trò cụ thể — VD: QA Manual Tester chuyên Functional Testing].

### CONTEXT (Bối cảnh)
- Dự án: [tên, loại hệ thống — VD: ERP/MES]
- Stack: [ngôn ngữ, framework, tool]
- File/tài liệu liên quan: [đường dẫn hoặc nội dung đính kèm]

### TASK (Yêu cầu cụ thể)
[Một câu mệnh lệnh rõ ràng, 1 hành động chính — tránh gộp nhiều việc vào 1 prompt]

### INPUT (Dữ liệu đầu vào)
[Requirement, user story, đoạn code, log lỗi...]

### CONSTRAINTS (Ràng buộc)
- Không được: [VD: không sửa file config gốc]
- Phải tuân theo: [coding convention, naming rule, framework version]
- Giới hạn: [số lượng test case, độ dài output...]

### OUTPUT FORMAT (Định dạng đầu ra)
[Bảng / JSON / Gherkin / code block / markdown checklist...]
```

### 🎯 1. Role – Xác định vai trò của AI

**Role** là việc yêu cầu AI **đóng vai một chuyên gia hoặc vị trí cụ thể** trước khi thực hiện nhiệm vụ.  
  
Việc chỉ định Role giúp AI:

- Chọn **góc nhìn chuyên môn phù hợp**
- Áp dụng **cách thức đúng và phù hợp nhất**
- Đưa ra **giải pháp thực tế hơn**

Ví dụ:

**Role:**  
`Bạn là Senior Manual QA Engineer với 10 năm kinh nghiệm.`

Hoặc:

**Role:**  
`Bạn là Manual Testing Expert.`

Trong Manual Testing, một số Role thường dùng:

- **QA Engineer**
- **Manual Tester**
- **Test Lead**
- **QA Analyst**

💡 Khi có Role, AI thường viết test case **rõ ràng và đúng chuẩn hơn**.

### 🧠 2. Context – Cung cấp bối cảnh hệ thống

AI **không biết hệ thống của bạn là gì**.

Vì vậy cần cung cấp **Context** để AI hiểu môi trường làm việc.

Context thường bao gồm:

- Loại ứng dụng
- Loại kiểm thử (Functional, Regression, Smoke...)
- Công cụ quản lý test case đang dùng (TestRail, Jira, Excel...)
- Mục tiêu kiểm thử

**Ví dụ:**

**Context:**  
*`Tôi đang viết test case cho web application.`*  
  
*`Thông tin thêm:`*  
*`- Loại hệ thống: CRM`*  
*`- Hình thức test: Manual functional testing`*  
*`- Template test case: theo mẫu bảng chuẩn của team`*

Nếu không cung cấp Context, AI có thể trả về:

- Test case quá sơ sài, thiếu bước
- Sai format bảng (thiếu cột Priority, Test Data...)
- Bỏ sót negative case / edge case

trong khi bạn cần một bộ test case **đầy đủ và đúng template chuẩn**.

### 🧪 3. Task – Mô tả nhiệm vụ cần AI thực hiện

**Task** là phần quan trọng nhất của Prompt.

Đây là nơi bạn nói rõ **AI cần làm gì**.  
  
**Ví dụ:**

**Task:**  
*`Viết test case cho chức năng Login.`*

Hoặc:

**Task:**  
`Viết 10 test case cho chức năng Upload File.`

Task nên:

- **cụ thể**
- **rõ ràng**
- **không mơ hồ**

Ví dụ tốt hơn:

**Task:**  
*`Viết test case cho chức năng Login gồm:`*  
  
*`- Login thành công`*  
*`- Login sai password`*  
*`- Login khi bỏ trống field`*

### 💼 4. Data (dữ liệu đầu vào)

Chỗ này tuỳ vào yêu cầu bạn kêu AI làm là gì thì nếu cần data đầu vào bạn cần đính kèm vào.

Có thể đính kèm các dạng data:

- Thông tin text account, url
- Screenshot
- File cụ thể (class code, logs, docs)

### ⚙️ 5. Constraints – Đặt các ràng buộc (hoặc dùng Instructions)

**Constraints** là các quy tắc hoặc giới hạn mà AI phải tuân theo.  
  
Phần này giúp:

- Tránh code **không đúng chuẩn**
- Đảm bảo **coding guideline**
- Kiểm soát **chất lượng output**

**Ví dụ:**

**Constraints:**  
*`- Mỗi step phải rõ ràng, làm theo được ngay`*  
*`- Expected Result phải cụ thể, đo lường được`*  
*`- Trình bày theo template chuẩn của team`*

Hoặc:

**Constraints:**  
*`- Ngôn ngữ rõ ràng, dễ hiểu`*  
*`- Không dùng từ ngữ mơ hồ (VD: "kiểm tra hoạt động đúng")`*  
*`- Đủ thông tin để người khác thực hiện lại được`*

Hoặc có thể dùng từ INSTRUCTIONS:  
  
`# INSTRUCTIONS`  
`- Viết rõ từng bước`  
`- Có Expected Result cụ thể`  
`- Dùng template chuẩn của team`

Trong Manual Testing, phần Constraints rất quan trọng để tránh AI viết test case **sai format, không thống nhất**.

### 📦 6. Output Format – Định dạng kết quả

Nếu không chỉ định **Output format**, AI có thể trả về:

- Code
- Giải thích
- Ví dụ
- Phân tích

→ khiến kết quả **dài và tốn token**.

Vì vậy nên yêu cầu rõ **format output**.

Ví dụ:

**Output:**  
*`Trả về test case đầy đủ gồm:`*  
  
*`- Test Case ID`*  
*`- Precondition`*  
*`- Steps & Expected Result`*

Hoặc:

**Output:**  
*`Xuất kết quả dạng bảng gồm:`*  
  
*`- Test Case ID`*  
*`- Test Scenario`*  
*`- Steps`*  
*`- Expected Result`*

Hoặc tối ưu token:

**Output:**  
*`- Chỉ trả về bảng test case`*  
*`- không cần giải thích`*

## 3. Ví dụ Prompt hoàn chỉnh

Dưới đây là một Prompt hoàn chỉnh áp dụng cấu trúc:

**Role – Context – Task – Constraints – Output**

```markdown
##Role:
Bạn là Senior Manual QA Engineer.

##Context:
Tôi đang viết test case cho web application, hệ thống dạng CRM.

##Phạm vi kiểm thử:
- Manual functional testing
- Web application
- Template test case dạng bảng

##Task + Data input:
Viết test case cho chức năng Login.
URL: https://crm.anhtester.com/admin/authentication
Email: admin@example.com
Password: 123456

##Constraints:
- Bao gồm Happy path, Negative case, Edge case
- Mỗi step phải rõ ràng, làm theo được ngay
- Expected Result cụ thể, đo lường được

##Output:
Trả về bảng test case gồm các cột:
- Test Case ID
- Test Scenario
- Steps
- Test Data
- Expected Result
- Priority
```

Khi Prompt có đầy đủ 5 phần, AI sẽ:

- Hiểu **vai trò**
- Hiểu **hệ thống**
- Hiểu **nhiệm vụ**
- Tuân theo **ràng buộc**
- Trả về **đúng định dạng**

## 💡 Cách nạp nội dung vào Prompt

Khi bạn viết Prompt mà cần muốn đề cập đến Test Cases, Requirements, hay generate code từ trang web / API nào đó.

- Đính kèm File vào tools AI cụ thể
- Dán nội dung vào Prompt trực tiếp
- Cung cấp Link URL thông tin của trang web và thông tin đăng nhập để AI thăm dò cấu trúc trang web đó.
- Đính kèm hình ảnh liên quan: Error, sơ đồ, cấu trúc code,...

## 💡Khi nội dung đính kèm bị dài thì làm sao?

**Paste trực tiếp** → tốt cho nội dung **ngắn và cần phân tích nhanh**

**File đính kèm** → tốt cho **tài liệu dài hoặc code lớn**

Cách hiệu quả nhất là:

***File để cung cấp context + Paste đoạn nội dung quan trọng để AI focus.***

#### ✳️ Trường hợp nên Paste trực tiếp vào prompt

- *Đoạn code ngắn*
- *Error log*
- *HTML element*
- *Requirement ngắn*

#### ✳️ Trường hợp nên dùng File đính kèm

- *Bộ test case lớn (nhiều module)*
- *Log lỗi dài*
- *Requirement document*
- *Test specification*
- *API spec*

### 📌 Ví dụ Prompt chuẩn để Generate bộ Test Case chi tiết

```markdown
# ROLE
Bạn là Senior Manual QA Engineer.

# TASK
Viết test case cho chức năng đăng nhập ứng dụng Mobile Android.

# CONTEXT
Hệ thống:
- Loại ứng dụng: Mobile Android
- Hình thức test: Manual functional testing

# INSTRUCTIONS
- Viết rõ từng step
- Có Test Data và Expected Result cụ thể
- Bao gồm Happy path, Negative case

# OUTPUT FORMAT
- Bảng Markdown test case
- Chia rõ theo từng scenario
```

Hoặc kiểu khác, chi tiết rõ ràng là ok.

```markdown
Role:
Bạn là Senior Manual QA Engineer.

Context:
Tôi đang viết test case cho web application.

Loại kiểm thử:
- Manual functional testing
- Template dạng bảng chuẩn của team

Task:
Viết test case cho chức năng:
- Add, Edit, Delete Customer

Constraints:
- Thông tin đăng nhập sử dụng lại theo tài khoản đã cấu hình sẵn trong Precondition
- Mỗi step phải rõ ràng, làm theo được ngay
- Bao gồm Happy path, Negative case, Edge case
- Sinh ra file Test Data tương ứng dùng Excel .xlsx

Output:
Trả về bảng test case gồm:
- Test Case ID
- Test Scenario
- Steps
- Test Data
- Expected Result
```

## 4. Một số Prompt mẫu dành cho Tester (Manual Testing)

### 🧪 1️⃣ Prompt tạo Test Case từ Requirement

Requirement có thể từ File đính kèm hoặc Copy dán trực tiếp vào Prompt luôn. Nhưng mà nên đính kèm file để nội dung của Prompt không bị dài, sẽ hiệu quả hơn.

#### 📥 Prompt Input

```markdown
# ROLE
Bạn là Senior QA Engineer với 10 năm kinh nghiệm.

# TASK
Phân tích requirement và tạo test cases.

# CONTEXT
Requirement:

User có thể đăng nhập hệ thống bằng Email và Password.

Rules:
- Email phải đúng format
- Password tối thiểu 8 ký tự
- Sai 5 lần sẽ bị khóa account
- Hiển thị message lỗi tương ứng

System type:
Web Application

# INSTRUCTIONS
- Bao gồm happy path
- Bao gồm negative case
- Bao gồm edge case

# OUTPUT FORMAT
Markdown table:
| ID | Test Scenario | Test Steps | Test Data | Expected Result | Priority |
```

#### 📤 Ví dụ Output AI

<table class="w-fit min-w-(--thread-content-width) rt-table">
<thead>
<tr>
<th class="">ID</th>
<th class="">Test Scenario</th>
<th class="">Test Steps</th>
<th class="">Test Data</th>
<th class="">Expected Result</th>
<th class="">Priority</th>
</tr>
</thead>
<tbody>
<tr>
<td>TC01</td>
<td>Login thành công</td>
<td>1. Mở trang login<br/>2. Nhập email hợp lệ<br/>3. Nhập password đúng<br/>4. Click Login</td>
<td><a class="decorated-link cursor-pointer">user@test.com</a> / 12345678</td>
<td>Login thành công và chuyển đến Dashboard</td>
<td>High</td>
</tr>
<tr>
<td>TC02</td>
<td>Sai password</td>
<td>Nhập email đúng và password sai</td>
<td><a class="decorated-link cursor-pointer">user@test.com</a> / wrong123</td>
<td>Hiển thị message "Invalid credentials"</td>
<td>High</td>
</tr>
<tr>
<td>TC03</td>
<td>Email sai format</td>
<td>Nhập email không hợp lệ</td>
<td>usertest.com</td>
<td>Hiển thị "Email format invalid"</td>
<td>Medium</td>
</tr>
<tr>
<td>TC04</td>
<td>Password &lt; 8 ký tự</td>
<td>Nhập password 6 ký tự</td>
<td>123456</td>
<td>Hiển thị "Password must be at least 8 characters"</td>
<td>Medium</td>
</tr>
<tr>
<td>TC05</td>
<td>Lock account</td>
<td>Login sai 5 lần</td>
<td>wrong password</td>
<td>Account bị khóa</td>
<td>High</td>
</tr>
</tbody>
</table>

#### 📥 Prompt Input

```markdown
# ROLE
Bạn là Senior QA Engineer với 10 năm kinh nghiệm trong Software Testing.

# TASK
Phân tích requirement và tạo bộ test case đầy đủ.

# CONTEXT
Requirement:
[PASTE REQUIREMENT HERE]

System type:
- Web / Mobile / API

# INSTRUCTIONS
- Phân tích requirement trước
- Xác định happy path
- Xác định edge case
- Xác định negative case
- Bao gồm validation dữ liệu
- Bao gồm security / permission nếu có

# OUTPUT FORMAT
Bảng Markdown với các cột:

| ID | Test Scenario | Test Steps | Test Data | Expected Result | Priority |
```

### 🧾 2️⃣ Prompt tạo Test Script chi tiết từ Test Scenario

Prompt này dùng để triển khai một Test Scenario ngắn gọn thành Test Script (các bước thực hiện chi tiết) sẵn sàng để tester khác cầm lên là chạy được ngay.  
  
Chú ý phần đính kèm File/Nội dung vào prompt cho đầy đủ.

#### 📥 Prompt Input

```markdown
# ROLE
Bạn là Senior Manual QA Engineer.

# TASK
Viết test script chi tiết từ test scenario.

# CONTEXT
Hệ thống:
- Loại ứng dụng: Web / Mobile
- Hình thức test: Manual functional testing

Test Scenario:
[PASTE TEST SCENARIO]

# INSTRUCTIONS
- Viết rõ từng bước thực hiện (Step)
- Mỗi step có Expected Result tương ứng
- Không dùng từ ngữ mơ hồ
- Ghi rõ Precondition nếu có

# OUTPUT FORMAT
Bảng Markdown với các cột:

| Step | Action | Test Data | Expected Result |
```

#### 📤 Ví dụ Output AI

**Test Script: Login thành công**

<table class="w-fit min-w-(--thread-content-width) rt-table">
<thead>
<tr>
<th class="">Step</th>
<th class="">Action</th>
<th class="">Test Data</th>
<th class="">Expected Result</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Mở trang login</td>
<td>-</td>
<td>Trang login hiển thị đầy đủ các trường Email, Password, nút Login</td>
</tr>
<tr>
<td>2</td>
<td>Nhập email hợp lệ</td>
<td>user@test.com</td>
<td>Trường Email hiển thị đúng giá trị vừa nhập</td>
</tr>
<tr>
<td>3</td>
<td>Nhập password đúng</td>
<td>12345678</td>
<td>Trường Password hiển thị dạng ẩn ký tự (••••••••)</td>
</tr>
<tr>
<td>4</td>
<td>Click nút Login</td>
<td>-</td>
<td>Đăng nhập thành công, chuyển đến trang Dashboard</td>
</tr>
</tbody>
</table>

### 🔎 3️⃣ Prompt Review Test Case

Các bạn đính kèm File test case cần review hoặc dán trực tiếp vào prompt.

#### 📥 Prompt Input

```markdown
Role:
Bạn là Senior QA Lead với nhiều kinh nghiệm review test case.

Context:
Tôi đang phát triển bộ test case manual cho web application.

Thông tin thêm:
- Hệ thống: Web application
- Template: bảng test case chuẩn của team

Test case cần review được đính kèm trong file hoặc đoạn nội dung bên dưới.

Task:
Hãy review bộ test case này dưới góc nhìn best practice của Manual Testing.

Constraints:
Phân tích các khía cạnh sau:

1. Độ bao phủ (Happy path / Negative / Edge case)
2. Tính rõ ràng của Steps
3. Expected Result có cụ thể, đo lường được không
4. Trường hợp trùng lặp / dư thừa
5. Test Data có đủ để thực thi không
6. Tính nhất quán format với template chuẩn

Output:
Trả về kết quả gồm:

1. Các vấn đề phát hiện trong test case
2. Mức độ ảnh hưởng (Low / Medium / High)
3. Đề xuất cách cải thiện
4. Ví dụ test case đã sửa nếu cần
```

### 4️⃣ Prompt mở rộng Test Case sơ sài thành Test Case chi tiết chuẩn

Bạn cần cung cấp **file test case sơ sài** đính kèm hoặc **đoạn test case** trực tiếp trong prompt luôn.

```markdown
### ROLE (Vai trò)
Bạn là một Senior Manual QA Engineer chuyên nghiệp. Bạn có nhiều năm kinh nghiệm viết và chuẩn hóa test case theo template rõ ràng, dễ thực thi. Bạn luôn tuân thủ nguyên tắc viết test case rõ ràng, không mơ hồ và đầy đủ thông tin.

### CONTEXT (Ngữ cảnh)
Tôi có một số ý tưởng test / test case viết sơ sài (chỉ có tiêu đề hoặc mô tả ngắn, thiếu bước chi tiết, thiếu Test Data, thiếu Expected Result rõ ràng). Tôi cần chuẩn hóa lại thành test case đầy đủ để đưa vào bộ test case chính thức của dự án, phục vụ regression testing thường xuyên.
Hệ thống mục tiêu của tôi là [Web / Mobile App] tại đường dẫn: [URL / Tên màn hình nếu có].

### TASK (Nhiệm vụ)
Hãy đọc kỹ nội dung test case sơ sài tôi cung cấp bên dưới (hoặc trong file đính kèm) và viết lại thành test case chi tiết, đầy đủ, đúng chuẩn.

---
[NỘI DUNG TEST CASE SƠ SÀI DÁN VÀO ĐÂY]
Hoặc: "Dựa vào nội dung file đính kèm theo prompt này."
---

### CONSTRAINTS (Ràng buộc bắt buộc)
Để đảm bảo chất lượng test case, bạn PHẢI tuân thủ nghiêm ngặt các nguyên tắc sau:
1. Mỗi Step phải rõ ràng, làm theo được ngay, không gộp nhiều hành động vào 1 step.
2. Expected Result:
   - Phải cụ thể, đo lường được (không viết chung chung như "hoạt động đúng").
   - TUYỆT ĐỐI KHÔNG đoán (guess) hành vi hệ thống nếu không chắc chắn. Nếu thiếu thông tin, hãy để placeholder và comment nhắc tôi xác nhận lại.
3. Bổ sung độ bao phủ:
   - Bổ sung thêm Negative case và Edge case nếu test case gốc chỉ có Happy path.
4. Test Data (Dữ liệu rõ ràng, truy vết được):
   - Các giá trị test cần cụ thể (không để chung chung như "nhập dữ liệu hợp lệ").
5. Chất lượng:
   - Không viết dài dòng thừa thãi, giữ ngôn ngữ ngắn gọn, chuyên nghiệp bằng Tiếng Việt.

### OUTPUT FORMAT (Định dạng kết quả đầu ra)
Đầu ra của bạn cần trả về theo đúng định dạng sau:
1. Giải thích tóm tắt những gì đã bổ sung/chuẩn hóa: Nêu ngắn gọn trong 2-3 câu.
2. Bảng test case hoàn chỉnh gồm các cột: Test Case ID, Test Scenario, Precondition, Steps, Test Data, Expected Result, Priority.
3. Lưu ý / Actions required: Những chỗ nào tôi cần xác nhận lại thông tin (do bạn không chắc chắn hành vi hệ thống).
```

## 📚 Tổng kết

Một Prompt hiệu quả cần có 6 phần chính:

✔ **Role** – AI đóng vai gì  
✔ **Context** – bối cảnh hệ thống  
✔ **Task** – nhiệm vụ cần thực hiện  
✔ **Data** – dữ liệu đầu vào  
✔ **Constraints** – các ràng buộc  
✔ **Output** – định dạng kết quả

## ✅ Cách sử dụng hiệu quả các model Claude: Opus, Sonnet, Haiku

*Cập nhật theo docs.claude.com (8/2026). Tên/giá model đổi theo thời gian nên trước khi đưa vào course, kiểm tra lại tại <https://platform.claude.com/docs/en/about-claude/models/overview>*

---

### 1. Bảng so sánh nhanh (lineup hiện tại)

<table class="rt-table">
<thead>
<tr>
<th> </th>
<th><strong>Opus</strong> (Claude Opus 5)</th>
<th><strong>Sonnet</strong> (Claude Sonnet 5)</th>
<th><strong>Haiku</strong> (Claude Haiku 4.5)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Định vị</td>
<td>Việc agentic coding phức tạp, doanh nghiệp</td>
<td>Cân bằng tốc độ + trí tuệ — lựa chọn mặc định</td>
<td>Nhanh nhất, gần đạt trí tuệ frontier</td>
</tr>
<tr>
<td>Giá / 1M token (input / output)</td>
<td>$5 / $25</td>
<td>$2 / $10</td>
<td>$1 / $5</td>
</tr>
<tr>
<td>Context window</td>
<td>1M token</td>
<td>1M token</td>
<td>200K token</td>
</tr>
<tr>
<td>Max output</td>
<td>128K token</td>
<td>128K token</td>
<td>64K token</td>
</tr>
<tr>
<td>Tốc độ</td>
<td>Trung bình</td>
<td>Nhanh</td>
<td>Nhanh nhất</td>
</tr>
<tr>
<td>Kiểu "suy nghĩ"</td>
<td>Adaptive thinking (effort: low/med/high)</td>
<td>Adaptive thinking (effort: low/med/high)</td>
<td>Extended thinking (đặt budget_tokens thủ công)</td>
</tr>
</tbody>
</table>

> Lưu ý: bên trên còn có tier **Fable/Mythos** (cao hơn Opus, dùng cho các tác vụ cần năng lực cao nhất/agent chạy dài) — course có thể nhắc qua nhưng không cần đi sâu vì phần lớn học viên sẽ làm việc ở 3 tier Opus/Sonnet/Haiku.

---

### 2. Nguyên tắc chọn model: "85% dùng Sonnet"

- **Sonnet = mặc định.** Dùng cho phần lớn công việc hàng ngày — đủ thông minh, đủ nhanh, giá vừa phải.
- **Nâng lên Opus khi:**
  - Task đòi hỏi suy luận nhiều bước, phức tạp (thiết kế kiến trúc, refactor lớn, debug lỗi khó)
  - Sai sót có chi phí cao (task ảnh hưởng nhiều người, nhiều file, quyết định khó đảo ngược)
  - Đã thử Sonnet với prompt tốt mà kết quả vẫn không đạt
- **Hạ xuống Haiku khi:**
  - Task đơn giản, rõ ràng, đầu ra dễ kiểm tra
  - Cần chạy khối lượng lớn / tốc độ cao (xử lý hàng loạt, real-time)
  - Sai sót nhỏ chấp nhận được hoặc dễ sửa

---

### 3. Áp dụng vào công việc QA / Manual Testing (theo đúng domain của bạn)

<table class="rt-table">
<thead>
<tr>
<th>Việc</th>
<th>Model phù hợp</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sinh nhanh test data giả, format lại test case sang bảng, viết tóm tắt ngắn cho Slack</td>
<td><strong>Haiku</strong></td>
<td>Task đơn giản, cần nhanh, khối lượng có thể lớn</td>
</tr>
<tr>
<td>Sinh test case từ requirement, viết test script chi tiết, review test case, viết bug report</td>
<td><strong>Sonnet</strong></td>
<td>Việc hàng ngày, cần chất lượng ổn định — đây là phần lớn công việc</td>
</tr>
<tr>
<td>Thiết kế chiến lược test cho hệ thống lớn (luồng ERP ↔ MES), thiết kế test plan/test strategy đầy đủ, phân tích root cause phức tạp qua nhiều log/module, review bộ test case lớn</td>
<td><strong>Opus</strong></td>
<td>Cần suy luận sâu, nhiều bước, sai thì tốn thời gian sửa lại toàn bộ</td>
</tr>
</tbody>
</table>

**Mẹo kết hợp nhiều tier trong 1 quy trình** (rất hợp để dạy trong course): dùng Opus để *lập kế hoạch/thiết kế* (VD: vạch chiến lược test cho 1 module mới), sau đó giao Sonnet hoặc Haiku *triển khai chi tiết* theo kế hoạch đó — vừa tiết kiệm chi phí vừa giữ chất lượng.

---

### 4. Mẹo dùng hiệu quả, tránh lãng phí

1. **Bắt đầu ở Sonnet**, chỉ chuyển sang Opus khi có bằng chứng Sonnet không đủ (đừng nâng "phòng hờ").
2. Trên **Claude API / Claude Code**, có thể chỉnh tham số `effort` (low/med/high) để tăng/giảm độ sâu suy luận của Opus/Sonnet mà **không cần đổi hẳn model** — rẻ hơn nhiều so với nhảy tier.
3. Theo dõi chi phí: Opus đắt gấp 5 lần Haiku ở cả input lẫn output — nếu chạy hàng loạt (VD: sinh test case cho hàng trăm requirement), nên thử Sonnet/Haiku trước.
4. Trên **claude.ai**, chọn model qua dropdown ở giao diện chat; trên **API/Claude Code**, chọn qua model ID (VD: `claude-sonnet-5`, `claude-haiku-4-5`).
5. Prompt tốt (xem template ở file trước) quan trọng hơn việc chọn tier cao — nhiều trường hợp Sonnet + prompt rõ ràng cho kết quả tốt hơn Opus + prompt mơ hồ.