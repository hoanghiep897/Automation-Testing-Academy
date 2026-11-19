# Bài 1 - [AI Test Automation] Con đường ứng dụng AI trong Test Automation hiện nay

Chương: 1. Nội dung khoá học

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/283](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/283)

[Video nhúng](https://www.youtube.com/embed/k8nEibYZwis)

4 giờ 36 phút

Trong bài học đầu tiên này, chúng ta sẽ cùng nhìn tổng quan về **con đường ứng dụng AI trong Test Automation hiện nay** và định hướng **Career Path mới cho Tester trong kỷ nguyên AI**.  

1. ***Sự tiến hóa của Software Testing***
2. ***Các con đường ứng dụng AI trong Testing hiện nay***
3. ***Những khó khăn của Test Automation trước khi có AI***
4. ***AI đang thay đổi Test Automation như thế nào***
5. ***Career Path mới cho Tester***
6. ***Vì sao AI Agent là bước tiến quan trọng***  
   ***Vì sao khóa học này sử dụng Google Antigravity***
7. **Tester có cần phải biết code và kiến thức Automation khi ứng dụng AI hay không?**
8. ***Mục tiêu hướng đi của khóa học này***

## 🤖 Bối cảnh AI trong Software Testing năm **2026**

**AI** đang tạo ra một sự thay đổi rất lớn trong ngành **Software Testing**. Nếu trước đây Tester chủ yếu làm Manual Testing hoặc Automation Testing theo cách truyền thống, thì từ khoảng **2024 – 2026**, AI bắt đầu trở thành một phần quan trọng trong quy trình kiểm thử.  
  
AI có thể hỗ trợ Tester trong rất nhiều công việc như:

- ***Phân tích requirement***
- ***Tạo test case***
- ***Sinh test data***
- ***Viết test automation***
- ***Debug test fail***
- ***Tạo report  
  ...***

**Điều này dẫn đến một thay đổi quan trọng:**

👉 Tester không còn chỉ là người viết test nữa, mà dần trở thành **người điều khiển AI để thực hiện Testing**.

---

## 1. Sự tiến hóa của Software Testing

Software Testing đã trải qua nhiều giai đoạn phát triển khác nhau.

<table class="w-fit min-w-(--thread-content-width) rt-table">
<thead>
<tr>
<th class="">Giai đoạn</th>
<th class="">Đặc điểm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Manual Testing</td>
<td>Tester thực hiện test thủ công</td>
</tr>
<tr>
<td>Automation Testing</td>
<td>Viết script để tự động hóa test</td>
</tr>
<tr>
<td>CI/CD Testing</td>
<td>Test được chạy tự động trong pipeline</td>
</tr>
<tr>
<td>AI-Assisted Testing</td>
<td>AI hỗ trợ viết test và phân tích lỗi</td>
</tr>
</tbody>
</table>

Trước đây, Tester phải làm gần như tất cả các công việc:

- Đọc requirement
- Viết test case
- Viết automation script
- Chạy test
- Debug lỗi  
  ...

Tuy nhiên với sự xuất hiện của AI, nhiều công việc trong số đó đã có thể được **tự động hóa hoặc hỗ trợ bởi AI**.

---

## 

## 2. Các con đường ứng dụng AI trong Testing hiện nay

Hiện nay AI trong Testing thường được chia thành **3 hướng chính, cả Manual và Automation.**

### ✳️ Chat AI hỗ trợ Tester (AI Assistant)

Ví dụ:

- ChatGPT
- Gemini
- Claude
- Copilot
- Grok

AI giúp:

- Phân tích requirements
- Tạo test case
- Viết code
- Debug lỗi

Tuy nhiên Tester vẫn phải:

- Copy code
- Paste vào project
- Chỉnh sửa
- Chạy test

### ✳️ AI Agent tự động hóa workflow

Đây là bước tiến lớn hơn.

AI có thể:

- Đọc source code
- Hiểu framework automation
- Viết test automation
- Chạy test
- Sửa test khi bị fail

AI lúc này giống như **một thành viên trong team**.

### ✳️ Autonomous Testing (Agentic AI)

Đây là hướng phát triển trong tương lai đang được xây dựng và hướng đến.

AI có thể:

- Đọc requirement
- Tạo test case
- Viết automation
- Chạy test
- Tạo report bug

Tester sẽ đóng vai trò **thiết kế hệ thống testing**. (***AI Test Architect***)

  

---

## 

## 3. Những khó khăn của Test Automation trước khi có AI

Mặc dù Automation Testing giúp tăng hiệu quả kiểm thử, nhưng vẫn tồn tại nhiều vấn đề.

### ⚠️ Viết automation mất nhiều thời gian

Ví dụ một thao tác đơn giản:

`driver.findElement(By.xpath("//button[text()='Login']")).click();`

Chỉ riêng việc tìm locator đôi khi cũng đã tốn khá nhiều thời gian.

### ⚠️ Locator dễ bị gãy

Khi UI thay đổi, locator thường bị ảnh hưởng. Điều này dẫn đến:

- test fail hàng loạt
- phải sửa lại locator
- chạy lại test

Đây chính là nguyên nhân của rất nhiều **flaky test** trong automation.

### ⚠️ Viết test case tốn nhiều công sức

Tester cần:

1. đọc requirement
2. phân tích user story
3. viết test case > test automation từ script auto

Đối với các dự án lớn, quá trình này có thể mất rất nhiều thời gian.

### ⚠️ Tạo test data phức tạp

Một số hệ thống yêu cầu:

- nhiều data
- data hợp lệ
- data edge case

Việc tạo test data thủ công đôi khi rất tốn công sức.

### ⚠️ Debug automation khó khăn

Một test fail có thể đến từ nhiều nguyên nhân:

- Locator sai
- Element chưa load ổn định
- Timing issue
- Environment lỗi
- Bug thật của hệ thống

Tester phải đọc log và phân tích khá nhiều thông tin để tìm ra nguyên nhân.

## 

---

## 

## 4. AI đang thay đổi Test Automation như thế nào

AI đang giúp Tester giải quyết rất nhiều vấn đề trong Automation Testing.

### ✅ AI có thể viết test automation

Ví dụ prompt:

```log
Write Playwright login test:
- Open login page
- Enter email
- Enter password
- Click login
- Verify dashboard page
```

AI có thể sinh ra code automation được và thậm chí là hoàn chỉnh khi mô tả càng chi tiết hơn.

### ✅ AI hỗ trợ tìm locator tốt hơn

AI có thể phân tích DOM và đề xuất locator ổn định hơn.

Ví dụ:

`get_by_role("button", name="Login")`

So với XPath phức tạp, các locator này thường **ổn định hơn và ít bị gãy hơn**.

### ✅ AI tạo test case từ requirement

Ví dụ requirement:

`User can login with email and password`

AI có thể tạo nhiều test case như:

- Login thành công
- Email sai format
- Password sai
- Bỏ trống input
- Security case  
  ...

### ✅ AI sinh test data

AI có thể tạo nhiều loại test data như:

- name
- email
- phone
- address
- zipcode

Chỉ với một prompt đơn giản mà kết quả lại đáp ứng cho đủ các tets cases đã được sinh ra trước đó hoặc đang tồn tại.

### ✅ AI hỗ trợ debug test fail

AI có thể đọc:

- Error log
- Stack trace
- Screenshot

Sau đó phân tích nguyên nhân test fail và đề xuất cách sửa.

## 

---

## 

## 5. Career Path mới cho Tester từ năm 2026

Sự xuất hiện của AI đang tạo ra một career path mới cho Tester.

### 

### 🔆 Career path truyền thống

```log
Manual Tester
↓
Automation Tester
↓
Senior Automation Engineer
```

### 🚀 Career path trong kỷ nguyên AI

```log
Tester
↓
Automation Tester
↓
AI-assisted Tester
↓
AI Test Engineer
↓
AI Test Architect
```

Tester trong tương lai cần nhiều kỹ năng mới như:

- Prompt Engineering
- AI Workflow Design
- AI Agent Configuration
- Automation Framework Knowledge
- CI/CD Integration
- AI Tool Integration

### 

### 🎯 Vai trò mới của Tester

Trong kỷ nguyên AI, Tester không chỉ là người thực hiện Testing.

Tester sẽ trở thành người:

- Thiết kế hệ thống Testing
- Thiết kế workflow cho AI
- Cấu hình AI Agent
- Giám sát hoạt động của AI

Nói cách khác Tester trong tương lai sẽ giống như **người quản lý một AI Tester trong team**.

Điều quan trọng là:

👉Tester cần biết cách **điều khiển AI để làm Testing hiệu quả hơn**.

  
Trong tương lai, Tester giỏi không phải là người viết nhiều test nhất,  
mà là người **biết cách sử dụng AI để Testing hiệu quả nhất**.  
  

## 

## 6. Vì sao AI Agent là bước tiến quan trọng

Hiện nay nhiều người đang sử dụng AI trong Testing theo cách rất phổ biến: **hỏi AI và copy code**.

Ví dụ workflow quen thuộc:

`Tester → hỏi AI → copy code → paste vào project → sửa lại → chạy test`

Cách này có một số hạn chế lớn:

- AI không hiểu cấu trúc project
- AI không biết framework automation đang dùng
- AI không thể chạy automation
- AI không thể debug lỗi
- AI không thể tương tác trực tiếp với hệ thống

AI lúc này chỉ đóng vai trò **AI Assistant (trợ lý)**.

Đây chính là lý do xuất hiện khái niệm **AI Agent**.

### 🤖 AI Agent là gì?

**AI Agent** là một hệ thống AI có khả năng **tự thực hiện hành động để hoàn thành một mục tiêu**, thay vì chỉ trả lời câu hỏi.

Nói đơn giản:

**AI Agent** = AI + khả năng hành động + khả năng sử dụng tool

Một AI Agent thường có các khả năng sau:

- Hiểu mục tiêu được giao
- Lập kế hoạch để đạt mục tiêu
- Sử dụng các tool hoặc API
- Thực hiện các bước hành động
- Quan sát kết quả và điều chỉnh

Workflow của **AI Agent** thường sẽ như sau:  
  
`Mục tiêu → Kế hoạch → Hành động → Quan sát → Điều chỉnh`

Ví dụ trong **Test Automation**, AI Agent có thể:

- Đọc source code của project
- Hiểu framework automation
- Tạo test case
- Viết test automation
- Chạy test
- Đọc log khi test fail
- Tự sửa lại test script

Lúc này AI không chỉ trả lời nữa, mà **thực sự làm việc trong project**.

#### 🧑‍💻 AI Agent trong Test Automation

Ví dụ một AI Agent trong test automation có thể thực hiện workflow như sau:

```log
Requirement
   ↓
AI tạo Test Case
   ↓
AI viết Automation Script
   ↓
AI chạy Test
   ↓
AI phân tích Log
   ↓
AI sửa Test Script
```

Tester lúc này không còn phải làm từng bước nhỏ nữa. Thay vào đó Tester sẽ:

- Thiết kế workflow cho AI
- Định nghĩa rule cho automation
- Cấu hình skill cho AI
- Giám sát kết quả

### 

### 🔍 So sánh AI Assistant và AI Agent

<table class="w-fit min-w-(--thread-content-width) rt-table">
<thead>
<tr>
<th class="">Tiêu chí</th>
<th class="">AI Assistant</th>
<th class="">AI Agent</th>
</tr>
</thead>
<tbody>
<tr>
<td>Trả lời câu hỏi</td>
<td>✔</td>
<td>✔</td>
</tr>
<tr>
<td>Viết code</td>
<td>✔</td>
<td>✔</td>
</tr>
<tr>
<td>Hiểu project</td>
<td>❌</td>
<td>✔</td>
</tr>
<tr>
<td>Chạy automation</td>
<td>❌</td>
<td>✔</td>
</tr>
<tr>
<td>Debug lỗi</td>
<td>❌</td>
<td>✔</td>
</tr>
<tr>
<td>Sử dụng tool</td>
<td>❌</td>
<td>✔</td>
</tr>
<tr>
<td>Tự thực hiện workflow</td>
<td>❌</td>
<td>✔</td>
</tr>
</tbody>
</table>

**AI Assistant** chỉ **giúp bạn làm việc**.

**AI Agent** có thể **thực hiện công việc thay bạn**.

### 🧠 Agentic AI là gì?

**Agentic AI** là khái niệm rộng hơn của **AI Agent**.

Agentic AI mô tả **một kiểu hệ thống AI có khả năng tự chủ (autonomous) để hoàn thành nhiệm vụ**.

Thay vì chỉ phản hồi theo prompt, Agentic AI có thể:

- Tự quyết định bước tiếp theo
- Tự lập kế hoạch hành động
- Tự sử dụng tool
- Tự cải thiện kết quả

Agentic AI thường có các đặc điểm:

1️⃣ Goal-driven  
AI hoạt động dựa trên mục tiêu.

2️⃣ Planning  
AI có thể lập kế hoạch các bước thực hiện.

3️⃣ Tool usage  
AI có thể gọi tool hoặc API.

4️⃣ Iteration  
AI có thể thử lại và cải thiện kết quả.

### 💥Vì sao khóa học này sử dụng Google Antigravity

Trong khóa học này chúng ta sẽ sử dụng **Google Antigravity** để xây dựng **AI Agent** cho **Test Automation**.

🔆 **Antigravity** cho phép:

- Tạo AI Agent
- Thiết kế skill cho AI
- Xây dựng workflow automation
- Kết nối MCP server để AI sử dụng tool

Nhờ đó AI có thể:

- Hiểu project
- Viết automation
- Chạy test
- Debug test
- Tạo report

  

---

## 

## 7. Tester có cần phải biết code và kiến thức Automation khi ứng dụng AI hay không?

Khi AI ngày càng mạnh và có thể viết code automation, nhiều người bắt đầu đặt câu hỏi:

***Nếu AI có thể viết test automation thì Tester có còn cần biết code nữa không?***

👉 Câu trả lời ngắn gọn là: **Có. Và vẫn rất quan trọng.**

AI có thể giúp viết code nhanh hơn, nhưng để **ứng dụng AI vào Testing hiệu quả**, Tester vẫn cần hiểu những kiến thức nền tảng về Automation Testing.

### 🔍 AI có thể viết code, nhưng không hiểu toàn bộ hệ thống

AI có thể tạo ra automation script chỉ từ một prompt, ví dụ:

*`Use Selenium Java to wirte test automation for login page...`*

AI có thể sinh ra một đoạn code chạy được. Tuy nhiên AI thường **không hiểu đầy đủ bối cảnh của project**, ví dụ:

- Cấu trúc framework automation
- Cách tổ chức Page Object Model
- Naming convention của project
- Cách quản lý test data
- Chiến lược retry khi test fail

***Nếu Tester không hiểu code, sẽ rất khó để:***

- Kiểm tra code AI sinh ra
- Sửa lỗi automation
- Tối ưu framework
- Và thậm chí là không có kiến thức để viết Prompt đầy đủ cụ thể cho từng thư viện automation mong muốn

### 🧪 Tester cần hiểu cách automation framework hoạt động

Dù AI có thể viết code, Tester vẫn cần hiểu:

- Cấu trúc automation framework
- Cách tổ chức test case
- Cách quản lý locator
- Cách quản lý test data
- Cách thiết kế Page Object Model

Ví dụ một framework automation thường bao gồm:

`tests/`  
`pages/`  
`utils/`  
`config/`  
`report/`

Nếu Tester không hiểu cấu trúc này, việc sử dụng AI để viết test sẽ dễ dẫn đến:

- Code không đồng bộ
- Khó maintain
- Khó mở rộng project

### ⚙️ AI cần người định hướng đúng cách

AI hoạt động tốt nhất khi được **hướng dẫn rõ ràng**.

Ví dụ một prompt tốt hơn:

*`Generate Playwright login test using Page Object Model`*  
*`with get_by_role locator and add assertion for dashboard page`*

Để viết được prompt như vậy, Tester cần hiểu:

- Framework đang dùng là gì
- Design pattern của automation
- Cách viết test script tốt hơn

Nói cách khác, **AI không thay thế kiến thức của Tester**, mà chỉ giúp **tăng tốc độ làm việc**.

### 🤖 Vai trò của Tester khi sử dụng AI trong Test Automation

Khi áp dụng AI vào Testing nói chung và Test Automation nói riêng, vai trò của Tester sẽ thay đổi.

Tester không còn chỉ viết test script nữa, mà sẽ:

- Thiết kế automation framework
- Định nghĩa quy tắc viết test
- Thiết kế workflow cho AI
- Kiểm tra và tối ưu code do AI tạo ra

AI giống như **một automation engineer trong team**, nhưng vẫn cần một người hiểu hệ thống để **định hướng và kiểm soát**.

### 🎯 Kết luận

AI giúp việc viết automation trở nên nhanh hơn và dễ tiếp cận hơn, nhưng điều đó **không có nghĩa là Tester không cần biết code**.  
  
Ngược lại, Tester càng phải hiểu:

- Lập trình
- Automation framework
- Kiến trúc hệ thống test

thì càng có thể **tận dụng AI hiệu quả hơn**.

*Trong kỷ nguyên AI, lợi thế không thuộc về người viết nhiều code nhất,*  
*mà thuộc về người **biết sử dụng AI để làm Automation hiệu quả nhất**.*

## 8. Mục tiêu của khóa học

Sau khóa học này, bạn sẽ có thể:

- Sử dụng AI để viết automation nhanh hơn
- Thiết lập AI Agent cho project testing cả Manual và Automation
- Xây dựng workflow cho AI trong automation
- Tích hợp AI vào framework automation
- Chạy test automation bằng CI/CD
- Xuất report tự động

Quan trọng hơn hết, bạn sẽ biết cách:

**👉 Biến AI thành một Tester trong team của mình.**