# Bài 3 - [AI Test Automation] Cách viết Prompt cho AI hiệu quả và tối ưu tài nguyên

Chương: 1. Nội dung khoá học

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/285](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/285)

[Video nhúng](https://www.youtube.com/embed/9tFhoKf8Wr4)

6 giờ 28 phút (2 phần)

#### 🎥 Video Bài 3 phần 1: <https://www.youtube.com/watch?v=9tFhoKf8Wr4>

#### 🎥 Video Bài 3 phần 2: <https://www.youtube.com/watch?v=MowBjWnohOk>

Sau khi đã cài đặt và làm quen với **Google Antigravity** ở bài trước, bước tiếp theo để khai thác AI hiệu quả là cần phải **viết Prompt đúng cách**.  
  
Rất nhiều Tester khi mới sử dụng AI thường gặp các vấn đề:

- AI trả lời **chung chung**
- Code AI sinh ra **không đúng framework**
- AI **tốn nhiều token**
- Phải **hỏi lại nhiều lần**

Nguyên nhân phổ biến là **Prompt chưa đủ rõ ràng**.

Một Prompt tốt không chỉ đơn giản là đặt câu hỏi, mà cần có **cấu trúc rõ ràng**.  
  
Trong bài này, chúng ta sẽ tìm hiểu cách **viết Prompt chuẩn để AI hiểu đúng yêu cầu**, đặc biệt trong **Test Automation**.

## 1. Prompt là gì?

**Prompt** là đoạn mô tả hoặc câu lệnh bạn gửi cho AI để yêu cầu AI thực hiện một nhiệm vụ.

Ví dụ đơn giản:

❌ Prompt kém

*`Viết automation test cho login`*

AI sẽ không biết:

- Dùng framework nào
- Ngôn ngữ gì
- Validate ra sao
- Structure code như thế nào

✅ Prompt tốt hơn

*`Viết automation test cho chức năng Login`*  
  
*`Tech stack:`*  
*`- Java`*  
*`- Selenium`*  
*`- TestNG`*  
*`- Page Object Model`*

AI lúc này sẽ hiểu **bối cảnh kỹ thuật** tốt hơn.

## 🧠 Các tiêu chí của Prompt hiệu quả

Một Prompt hiệu quả thường có các đặc trưng:

1. **Rõ ràng (Clear)**
2. **Có bối cảnh (Context)**
3. **Nhiệm vụ cụ thể (Task)**
4. **Có ràng buộc (Constraints)**
5. **Chỉ định định dạng kết quả (Output format)**
6. **Xác định vai trò AI (Role)**
7. **Ngắn gọn nhưng đủ thông tin**

## 2. Cấu trúc của một Prompt chuẩn

Tài liệu gốc được Google chỉ định để thiết kế prompt có thể dùng cho Gemini, trên Antigravity hoặc các AI khác.  
<https://ai.google.dev/gemini-api/docs/prompting-strategies>  
  
Sau khi ngâm cứu một thời gian dùng Prompt để AI dễ hiểu và làm đúng chuẩn yêu cầu nhất thì mình rút ra một cấu trúc Prompt hiệu quả cần có 5 thành phần như sau:

#### **`Role` `Context` `Task` `Constraints` `Output format`**

Đây là cấu trúc Prompt được sử dụng rất phổ biến khi làm việc với AI trong mảng phần mềm nói chung và Test Automation nói riêng.

### 🎯 1. Role – Xác định vai trò của AI

**Role** là việc yêu cầu AI **đóng vai một chuyên gia hoặc vị trí cụ thể** trước khi thực hiện nhiệm vụ.  
  
Việc chỉ định Role giúp AI:

- Chọn **góc nhìn chuyên môn phù hợp**
- Áp dụng **cách thức đúng và phù hợp nhất**
- Đưa ra **giải pháp thực tế hơn**

Ví dụ:

**Role:**  
`Bạn là Senior Test Automation Engineer với 10 năm kinh nghiệm.`

Hoặc:

**Role:**  
`Bạn là Selenium Automation Expert.`

Trong Test Automation, một số Role thường dùng:

- **QA Engineer**
- **Test Automation Engineer**
- **Test Architect**
- **Selenium Expert**

💡 Khi có Role, AI thường viết code **clean hơn và đúng chuẩn hơn**.

### 🧠 2. Context – Cung cấp bối cảnh hệ thống

AI **không biết hệ thống của bạn là gì**.

Vì vậy cần cung cấp **Context** để AI hiểu môi trường làm việc.

Context thường bao gồm:

- Loại ứng dụng
- Tech stack
- Framework đang dùng
- Mục tiêu automation

**Ví dụ:**

**Context:**  
*`Tôi đang viết automation test cho web application.`*  
  
*`Tech stack:`*  
*`- Java`*  
*`- Selenium`*  
*`- TestNG`*  
*`- Page Object Model`*

Nếu không cung cấp Context, AI có thể trả về:

- Python
- Cypress
- Playwright

trong khi dự án của bạn dùng **Java + Selenium**.

### 🧪 3. Task – Mô tả nhiệm vụ cần AI thực hiện

**Task** là phần quan trọng nhất của Prompt.

Đây là nơi bạn nói rõ **AI cần làm gì**.  
  
**Ví dụ:**

**Task:**  
*`Viết automation test cho chức năng Login.`*

Hoặc:

**Task:**  
`Viết 10 test case cho chức năng Upload File.`

Task nên:

- **cụ thể**
- **rõ ràng**
- **không mơ hồ**

Ví dụ tốt hơn:

**Task:**  
*`Viết automation test cho chức năng Login gồm:`*  
  
*`- Login thành công`*  
*`- Login sai password`*  
*`- Login khi bỏ trống field`*

### ⚙️ 4. Constraints – Đặt các ràng buộc (hoặc dùng Instructions)

**Constraints** là các quy tắc hoặc giới hạn mà AI phải tuân theo.  
  
Phần này giúp:

- Tránh code **không đúng chuẩn**
- Đảm bảo **coding guideline**
- Kiểm soát **chất lượng output**

**Ví dụ:**

**Constraints:**  
*`- Không dùng Thread.sleep`*  
*`- Sử dụng WebDriverWait`*  
*`- Code theo Page Object Model`*

Hoặc:

**Constraints:**  
*`- Code clean`*  
*`- Reusable`*  
*`- Tuân thủ SOLID`*

Hoặc có thể dùng từ INSTRUCTIONS:  
  
`# INSTRUCTIONS`  
`- Viết code clean`  
`- Có comment`  
`- Dùng Page Object Model`

Trong Automation, phần Constraints rất quan trọng để tránh AI viết code **sai khuôn mẫu, không thống nhất**.

### 📦 5. Output Format – Định dạng kết quả

Nếu không chỉ định **Output format**, AI có thể trả về:

- Code
- Giải thích
- Ví dụ
- Phân tích

→ khiến kết quả **dài và tốn token**.

Vì vậy nên yêu cầu rõ **format output**.

Ví dụ:

**Output:**  
*`Trả về code hoàn chỉnh gồm:`*  
  
*`- BaseTest`*  
*`- LoginPage`*  
*`- LoginTest`*

Hoặc:

**Output:**  
*`Xuất kết quả dạng bảng gồm:`*  
  
*`- Test Case ID`*  
*`- Test Scenario`*  
*`- Steps`*  
*`- Expected Result`*

Hoặc tối ưu token:

**Output:**  
*`- Chỉ trả về code`*  
*`- không cần giải thích`*

## 3. Ví dụ Prompt hoàn chỉnh

Dưới đây là một Prompt hoàn chỉnh áp dụng cấu trúc:

**Role – Context – Task – Constraints – Output**

```markdown
Role:
Bạn là Senior Test Automation Engineer.

Context:
Tôi đang viết automation test cho web application, hệ thống dạng CRM.

Tech stack:
- Java
- Selenium
- TestNG
- Page Object Model

Task:
Viết automation test cho chức năng Login.
URL: https://crm.anhtester.com/admin/authentication
Email: admin@example.com
Password: 123456

Constraints:
- Không dùng Thread.sleep
- Sử dụng WebDriverWait
- Code clean và reusable

Output:
Trả về code hoàn chỉnh gồm:
- LoginPage
- LoginTest
- BaseTest
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

- *Automation framework*
- *Class Java dài*
- *Requirement document*
- *Test specification*
- *API spec*

## 🧠 Template Prompt chuẩn theo Google Gemini gợi ý

```markdown
# ROLE
Bạn là: [vai trò chuyên gia mà AI cần đóng]

# TASK
Nhiệm vụ: [mô tả rõ ràng AI phải làm gì]

# CONTEXT
Bối cảnh:
- [thông tin nền]
- [dữ liệu liên quan]
- [đối tượng người đọc hoặc mục tiêu]

# INSTRUCTIONS
Yêu cầu chi tiết:
1. [yêu cầu cụ thể]
2. [quy tắc cần tuân thủ]
3. [các điều cần tránh]

# OUTPUT FORMAT
Định dạng kết quả:
- Format: [Markdown / JSON / Table / Code]
- Độ dài: [ngắn / chi tiết]
- Cấu trúc: [ví dụ: heading, bullet, step]

# EXAMPLES (OPTIONAL)
Ví dụ input:
[ví dụ]

Ví dụ output mong muốn:
[ví dụ output]
```

Bạn có thể bổ sung thêm phần **Examples** đầu ra để AI dễ hiểu và cho ra kết quả chắc chắn hơn theo ý mình.  
  
Còn **Instructions** chính là **Constraints**, dùng từ khoá nào cũng được.

### 📌 Ví dụ Prompt chuẩn để Generation Code Automation

```markdown
# ROLE
Bạn là Senior Java Automation Test Engineer.

# TASK
Viết code Appium Java để login vào ứng dụng Android đang được kết nối.

# CONTEXT
Framework đang dùng:
- Java
- TestNG
- Appium latest version 2.x.x

# INSTRUCTIONS
- Viết code clean
- Có comment
- Dùng Page Object Model

# OUTPUT FORMAT
- Code Java
- Chia file rõ ràng
```

Hoặc kiểu khác, chi tiết rõ ràng là ok.

```markdown
Role:
Bạn là Senior Test Automation Engineer.

Context:
Tôi đang viết automation test cho web application.

Tech stack:
- Java
- Selenium
- TestNG
- Page Object Model

Task:
Viết automation test cho chức năng:
- Add, Edit, Delete Customer

Constraints:
- Thông tin đăng nhập sử dụng lại từ class LoginPage
- Không dùng Thread.sleep
- Sử dụng WebDriverWait
- Code clean và reusable
- Sinh ra file Data Test tương ứng dùng Excel .xlsx

Output:
Trả về code gồm:
- BaseTest
- Page class
- Test class
```

## 4. Một số Prompt mẫu dành cho Tester (Manual và Automation)

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

### 🤖 2️⃣ Prompt tạo Automation Script

Prompt này có thể áp dụng cho **Selenium / Playwright / Appium**. Khi dùng các bạn chỉ định 1 món cụ thể chứ không phải khai báo tất cả thư viện nhé.  
  
Chú ý phần đính kèm File/Nội dung vào prompt cho đầy đủ.

#### 📥 Prompt Input

```markdown
# ROLE
Bạn là Senior Automation Test Engineer.

# TASK
Viết automation test script từ test scenario.

# CONTEXT
Framework:
- Language: Java
- Test Framework: TestNG
- Automation Tool: Appium / Selenium / Playwright
- Design Pattern: Page Object Model

Test Scenario:
[PASTE TEST SCENARIO]

# INSTRUCTIONS
- Viết code clean
- Tách Page Object
- Có comment rõ ràng
- Sử dụng locator ổn định
- Tránh hardcode

# OUTPUT FORMAT
Cấu trúc file:

Page Object:
[CODE]

Test Class:
[CODE]
```

#### 📤 Ví dụ Output AI

**LoginPage.java**

```java
public class LoginPage {

    private AppiumDriver driver;

    private By emailField = By.id("email");
    private By passwordField = By.id("password");
    private By loginButton = By.id("loginBtn");

    public LoginPage(AppiumDriver driver){
        this.driver = driver;
    }

    public void enterEmail(String email){
        driver.findElement(emailField).sendKeys(email);
    }

    public void enterPassword(String password){
        driver.findElement(passwordField).sendKeys(password);
    }

    public void clickLogin(){
        driver.findElement(loginButton).click();
    }
}
```

**LoginTest.java**

```java
public class LoginTest extends BaseTest {

    @Test
    public void loginSuccessfully(){

        LoginPage loginPage = new LoginPage(driver);

        loginPage.enterEmail("user@test.com");
        loginPage.enterPassword("12345678");
        loginPage.clickLogin();

        Assert.assertTrue(driver.getPageSource().contains("Dashboard"));
    }
}
```

### 🔎 3️⃣ Prompt Review Automation Code

Các bạn đính kèm File cần review hoặc dán code trực tiếp vào prompt.

#### 📥 Prompt Input

```markdown
Role:
Bạn là Senior Test Automation Architect với nhiều kinh nghiệm review automation framework.

Context:
Tôi đang phát triển automation test cho web application.

Tech stack hiện tại:
- Java
- Selenium WebDriver
- TestNG
- Page Object Model

Code cần review được đính kèm trong file hoặc đoạn code bên dưới.

Task:
Hãy review automation code này dưới góc nhìn best practice của Test Automation.

Constraints:
Phân tích các khía cạnh sau:

1. Code structure
2. Page Object Model implementation
3. Code smell
4. Maintainability
5. Reusability
6. Locator strategy
7. Synchronization (wait strategy)
8. Test stability

Output:
Trả về kết quả gồm:

1. Các vấn đề phát hiện trong code
2. Mức độ ảnh hưởng (Low / Medium / High)
3. Đề xuất cách cải thiện
4. Ví dụ code refactor nếu cần
```

### 4️⃣ Prompt tạo project code Automation Framework

Chỗ này mình lấy ví dụ cụ thể với thư viện **Selenium Java** và **Playwright Typescript**.  
  
Đối với **Selenium Java**:

```markdown
### Role
Bạn là một Senior Automation QA Engineer và Software Architect có nhiều năm kinh nghiệm trong việc thiết kế và xây dựng các hệ thống kiểm thử tự động (Automation Testing Framework) có khả năng mở rộng, độ ổn định cao và dễ bảo trì.

### Context
Tôi đang cần xây dựng một Web UI Automation Framework từ đầu (scratch) dành cho dự án của công ty. Framework này cần phải hiện đại, dễ bảo trì, dễ mở rộng và hỗ trợ chạy trên môi trường CI/CD một cách mượt mà. Công nghệ cốt lõi được lựa chọn là Java, Selenium WebDriver (v4.x) và TestNG.

### Task
Hãy thiết kế và viết code mẫu (boilerplate) cho một Automation Framework hoàn chỉnh. Đi qua từng thành phần quan trọng của framework và viết các class/file cấu hình cơ bản. Các thành phần bắt buộc phải có bao gồm:
1. Thiết kế kiến trúc thư mục dự án (Folder Structure) rõ ràng, theo chuẩn Maven.
2. Page Object Model (POM): Cấu trúc cơ bản cho BasePage và một SamplePage cụ thể.
3. Core Design: BaseTest bao gồm việc khởi tạo WebDriver an toàn (Thread-safe) bằng ThreadLocal để hỗ trợ chạy Parallel an toàn không bị conflict session.
4. Data-Driven Testing (Data Test): Cơ chế đọc dữ liệu từ file ngoài (ví dụ JSON hoặc Excel) và kết hợp với DataProvider của TestNG.
5. Configuration Management: Cơ chế đọc file config.properties (cho các biến môi trường như URL, Browser, Timeout,...).
6. Parallel Execution & Suite Configuration: File testng.xml được cấu hình để chạy test song song (parallel) ở cấp độ methods/classes.
7. Dependencies: Nội dung file pom.xml với các thư viện cần thiết nhất (Selenium, TestNG, WebDriverManager nếu cần, Log4j, ExtentReports hoặc Allure).


### Constraints
* Code phải viết bằng ngôn ngữ Java (version 11 trở lên).
* Sử dụng Selenium WebDriver 4 và TestNG.
* Áp dụng triệt để nguyên lý thiết kế Page Object Model (POM) và tuân thủ SOLID principles.
* Trình duyệt khởi tạo trong BaseTest phải được quản lý bằng ThreadLocal để bắt buộc tương thích với việc chạy Parallel của TestNG.
* Không sử dụng "Hard Sleep" (Thread.sleep()), thay vào đó tạo các hàm xử lý Smart Waits (Explicit Wait) trong BasePage hoặc WebUI utils.
* File cấu hình testng.xml phải tối ưu cho việc chạy trên hệ thống CI.
* Code sinh ra phải có comment giải thích, clean code, naming convention chuẩn Java.

** Dùng thông tin đăng nhập vào hệ thống:
https://crm.anhtester.com/admin/authentication
Email: admin@example.com
Password: 123456

### Output format
Vui lòng trình bày câu trả lời của bạn theo bố cục sau:
1. Directory Structure: Biểu diễn bằng cấu trúc cây thư mục (tree format).
2. Project dependencies: Cung cấp nội dung file pom.xml.
3. Core Components: Code cụ thể cho ConfigReader.java và DriverFactory.java (hoặc khởi tạo trong BaseTest).
4. Base Classes: Code cụ thể cho BaseTest.java (chứa Setup/Teardown) và BasePage.java (chứa các common actions & waits).
5. Implementations: Code mẫu cho LoginPage.java và LoginTest.java.
6. Test Data & Runner: Mẫu dữ liệu test, cách gọi DataProvider và nội dung file testng.xml.
7. Hướng dẫn cách chạy dự án (How to run).
```

Đối với **Playwright Typescript**:

```markdown
### Role
Bạn là một Senior Test Automation Architect chuyên gia về hệ sinh thái Node.js và Playwright. Bạn có nhiều năm kinh nghiệm trong việc xây dựng các framework kiểm thử End-to-End (E2E) hiện đại, hiệu năng cao, dễ mở rộng và tối ưu hóa cho CI/CD.

### Context
Tôi đang cần xây dựng một E2E Web UI Automation Framework từ đầu (scratch) cho dự án của công ty. Framework này cần đảm bảo tốc độ thực thi nhanh, tận dụng tối đa sức mạnh của môi trường Node.js. Các yếu tố cốt lõi bao gồm cấu trúc dự án rõ ràng, quản lý dữ liệu test tốt và dễ bảo trì. Công nghệ cốt lõi được lựa chọn là Playwright Test và ngôn ngữ TypeScript. 

### Task
Hãy thiết kế và viết code mẫu (boilerplate) cho một Playwright Automation Framework hoàn chỉnh. Đi qua từng thành phần quan trọng của framework và viết các class/file cấu hình cơ bản. Các thành phần bắt buộc phải có bao gồm:
1. Thiết kế kiến trúc thư mục dự án (Folder Structure): Hiện đại, tách biệt rõ ràng giữa configs, tests, pages, data, và utils.
2. Page Object Model (POM): Cấu trúc cơ bản cho một BasePage chứa các hàm bọc (wrapper methods) an toàn cho Playwright API và một SamplePage (ví dụ LoginPage) kế thừa từ nó.
3. Configuration Management: Cấu hình file playwright.config.ts chuẩn chỉ. Bao gồm cấu hình cho việc chạy nhiều trình duyệt (Chromium, Firefox, WebKit), cấu hình timeout, retries, workers (cho parallel execution) và reporters.
4. Environment Variables: Cách quản lý các cấu hình theo môi trường (dev, staging, prod) sử dụng .env file và thư viện dotenv.
5. Data-Driven Testing (Test Data): Cơ chế đọc dữ liệu test tĩnh (từ file .json) và cách sử dụng nó linh hoạt trong (Data-driven/Parametrized tests) của Playwright.
6. Fixtures (Playwright Fixtures): Cách tạo và sử dụng custom fixtures trong Playwright để quản lý state, khởi tạo/hủy Page Object tự động cho các test case mà không cần lặp lại code trong beforeEach.
7. Dependencies: Nội dung cơ bản của file package.json với các thư viện và script cần thiết để chạy test.

### Constraints
* Code bắt buộc phải viết bằng TypeScript và tuân thủ chặt chẽ Strict Mode.
* Sử dụng Test Runner mặc định của thư viện là @playwright/test.
* Áp dụng nguyên lý Page Object Model (POM), không viết trực tiếp locators và actions lộn xộn trong file test.
* Tận dụng tối đa điểm mạnh của Playwright là Auto-waiting, không sử dụng explicit delays (như page.waitForTimeout()) trừ khi xử lý các trường hợp siêu đặc biệt. Sử dụng Locator APIs một cách chính xác.
* Chú ý đến việc xử lý Locator hiện đại (ví dụ: getByRole, getByTestId).
* Tận dụng Playwright Fixtures để setup BasePage thay vì khởi tạo thủ công bằng từ khóa new lặp đi lặp lại.
* Code sinh ra cần có comment giải thích ngắn gọn, rõ ràng theo chuẩn Clean Code.

** Dùng thông tin đăng nhập vào hệ thống:
https://crm.anhtester.com/admin/authentication
Email: admin@example.com
Password: 123456

### Output format
Vui lòng trình bày câu trả lời của bạn theo bố cục sau:
1. Directory Structure: Biểu diễn bằng cấu trúc cây thư mục (tree format) giải thích ngắn gọn nhiệm vụ từng thư mục.
2. Setup & Dependencies: Nội dung file package.json cùng lệnh setup khởi tạo.
3. Core Configurations: Code cho playwright.config.ts và xử lý đa môi trường bằng dotenv (.env file mẫu).
4. Page Object Model (POM): Code cho BasePage.ts (các common actions) và LoginPage.ts.
5. Custom Fixtures: Code cho file fixtures.ts dùng để tự động inject Page Objects vào test (extend test).
6. Implementations & Test Data: Code định nghĩa file dữ liệu test (ví dụ .json) và file test thực tế login.spec.ts có sử dụng Data-Driven và Fixtures.
7. Hướng dẫn cách chạy dự án (How to run): Cung cấp các lệnh chạy script hữu ích (chạy UI mode, chạy parallel, xem report).
```

### 5️⃣ Prompt convert Manual Test Case sang Code Automation

Bạn cần cung cấp **file test case** đính kèm hoặc **đoạn test case** trực tiếp trong prompt luôn.

```markdown
### ROLE (Vai trò)
Bạn là một Senior Test Automation Engineer chuyên nghiệp. Bạn có nhiều năm kinh nghiệm thiết kế kiến trúc Framework độc lập, tối ưu hoá với [Playwright / Selenium / Appium] và viết code bằng ngôn ngữ [Java / TypeScript / Python]. Bạn luân tuân thủ các nguyên tắc thiết kế code sạch (Clean Code) và dễ bảo trì (Maintainability).

### CONTEXT (Ngữ cảnh)
Tôi có một bộ Test Case thủ công (Manual Test Case) đã được mô tả chi tiết các bước (Steps to reproduce), dữ liệu đầu vào (Test Data) và kết quả mong đợi (Expected Results). Tôi cần chuyển đổi tự động (Automate) Test Case này để tích hợp vào CI/CD pipeline công ty, nhằm chạy hồi quy (Regression Testing) thường xuyên.
Hệ thống mục tiêu của tôi là [Web / Mobile App] tại đường dẫn: [URL / Package name nếu có].

### TASK (Nhiệm vụ)
Hãy đọc kỹ nội dung Test Case tôi cung cấp bên dưới (hoặc trong file đính kèm) và viết toàn bộ Automation Script tương ứng. Bao gồm cả việc tạo ra các hàm tương tác tại Page Class và các Assertion (kiểm tra kết quả) tại Test Class.

---
[NỘI DUNG TEST CASE VÀ DỮ LIỆU ĐẦU VÀO DÁN VÀO ĐÂY]
Hoặc: "Dựa vào nội dung file đính kèm theo prompt này."
---

### CONSTRAINTS (Ràng buộc bắt buộc)
Để đảm bảo chất lượng code, bạn PHẢI tuân thủ nghiêm ngặt các nguyên tắc sau:
1. Design Pattern: Áp dụng triệt để Page Object Model (POM). Phân tách rõ Page objects (chứa locators & actions), Test execution (chứa assertions), và Utils/Test data.
2. Locator Strategy:
   - Locators phải ổn định, không dùng xpath/css quá dài chứa tag cha con liên tiếp.
   - TRUYỆT ĐỐI KHÔNG đoán (guess) cấu trúc DOM. Nếu không biết cấu trúc HTML, hãy tạo biến giả lập (VD: String LOGIN_BUTTON = "//ghi_chu_thay_the_locator_tai_day";) hoặc comment nhắc tôi.
3. Smart Waits (Xử lý đồng bộ):
   - KHÔNG bao giờ sử dụng Hard Sleep (như Thread.sleep hoặc waitForTimeout).
   - CHỈ sử dụng Smart Waits / Auto-waiting (như expect().toBeVisible(), WebDriverWait, v.v.).
4. Test Data (Dữ liệu ngẫu nhiên trace được):
   - Các fields yêu cầu unique (như Email, Username, ID) BẮT BUỘC phải sinh dữ liệu ngẫu nhiên nhưng có prefix để dễ truy vết (Ví dụ: test_username_17112023_101530).
5. Code Quality:
   - Code phải clean, không chứa các debug logs dư thừa (console.log() hoặc System.out.println()).
   - Giải thích code bằng các comment chuyên nghiệp, ngắn gọn bằng Tiếng Việt.

### OUTPUT FORMAT (Định dạng kết quả đầu ra)
Đầu ra của bạn cần trả về theo đúng định dạng sau:
1. Giải thích tóm tắt logic: Nêu ngắn gọn cách tiếp cận trong 2-3 câu.
2. Cấu trúc File dự kiến: Liệt kê tên các file sẽ được tạo (VD: LoginPage.java, LoginTest.java).
3. Mã nguồn (Source Code):
   - Code của <Tên Trang/Màn Hình> Page Class.
   - Code của <Tên> Test Class.
   - Code của <Tên> Data/Utils Class (nếu có dùng dữ liệu ngẫu nhiên).
4. Lưu ý / Actions required: Những vị trí nào tôi cần phải gắn locator thực tế (do bạn không thể truy cập DOM).
```

## 📚 Tổng kết

Một Prompt hiệu quả cho Test Automation cần có 5 phần:

✔ **Role** – AI đóng vai gì  
✔ **Context** – bối cảnh hệ thống  
✔ **Task** – nhiệm vụ cần thực hiện  
✔ **Constraints** – các ràng buộc  
✔ **Output** – định dạng kết quả

#### 

#### 🚀 Tham khảo bộ **Kit** do **Anh Tester** xây dựng dành riêng cho **Cộng đồng Tester Việt Nam** mình:

#### <https://github.com/anhtester/antigravity-testing-kit>

## 5. Cách sử dụng Model trên Antigravity tối ưu Quota (token)

Để tối ưu hóa thời gian sử dụng, không bị vướng giới hạn quota giữa chừng và vẫn đạt hiệu suất lập trình cao nhất, hãy áp dụng chiến thuật **"Chia Để Trị"** – dùng đúng Mode (chế độ) và đúng Model (mô hình AI) cho từng loại task.

### ✅ Phân bổ công việc theo Chế Độ (Mode)

Lưu ý quan trọng: **Planning Mode tiêu tốn số lượng Token lớn nhất**. Nó đọc rộng, suy nghĩ nhiều bước và tự động lặp lại quy trình.

- **Dùng PLANNING MODE cho Tác vụ Nền tảng (Big Tasks):**
  - Khởi tạo một Automation Framework mới (setup thư mục, Base Test, Report).
  - Xây dựng kiến trúc Page Object Model (POM) cho module chức năng hoàn toàn mới.
  - Viết một luồng End-to-End (E2E) Test phức tạp chạy qua nhiều page và thay đổi nhiều trạng thái.
- **Chuyển về FAST MODE cho Tác vụ Bảo trì (Daily Tasks):**
  - Sau khi "dựng khung" xong ở Planning, hãy lập tức tắt nó đi.
  - Dùng Fast Mode để chạy việc hàng ngày: bổ sung thêm test case, update locators bị đổi, tối ưu lại các hàm (methods) hoặc refactor code cục bộ.

### ✅ Chiến thuật lựa chọn AI Models (Theo độ khó)

Code ưu tiên Claude, nhưng hãy biết cách phân bổ cho các Model khác để bảo vệ quota.

  
⭐⭐⭐ **Claude Sonnet / Opus (Bộ óc Tinh nhuệ):**  

- - **Nhiệm vụ:** Giải quyết các logic Code khó và Fix Bug hóc búa.
  - **Automation Testing:** Dùng để xử lý các bài toán như lấy element trong Shadow DOM, tương tác iFrame lồng nhau, xử lý bất đồng bộ (Async/await), kéo thả (Drag-and-Drop) hoặc các test case đang chạy chập chờn (Flaky).
  - *Lưu ý: Token của Claude rất nhanh cạn, chỉ dùng khi thật sự "kẹt".*

  
⭐⭐ **Gemini Pro (Cỗ máy Bảo trì):**  

- - - **Nhiệm vụ:** Cán đáng công việc code "phổ thông".
    - **Automation Testing:** Sửa lỗi locator sai ID/Class, thêm một vài bước verify/assertions đơn giản, thay đổi data cứng thành biến linh hoạt. Giải quyết cực tốt các lỗi rõ ràng và đã biết nguyên nhân.

⭐ **Gemini Flash (Sát thủ Tốc độ & Tiết kiệm):**  

- - **Nhiệm vụ:** Xử lý văn bản, Data và đọc Log (nhanh, thẻ Context dài nhưng cực kỳ rẻ).
  - **Automation Testing:**
    - Phân tích cục Log CI/CD ngàn dòng để chỉ ra duy nhất 1 dòng gây lỗi `AssertionError`.
    - Đọc thẻ HTML lớn và bóc tách cấu trúc để xuất ra Table locators.
    - Sinh hàng trăm dòng Mock Data (JSON, CSV, Tài khoản giả) cho Data-Driven Testing.
    - Tạo tài liệu (Test Document), viết Git Commit messages, soạn Javadoc / Docstrings. Trình bày nội dung định dạng chuẩn SEO.

### ✅ Các Tip "Nhỏ mà Có Võ" để hạn chế tốn Token

#### 🔆 Khi gửi yêu cầu

- **Tránh đưa rác vào Context:** Thay vì copy toàn bộ thẻ `<body>` của giao diện web đổ vào chat, hãy dùng Inspect trong trình duyệt và chỉ copy đúng thẻ `<div>` biểu diễn khối thông tin (Table / Form / Dropdown) đang cần xử lý.
- **Định vị không gian làm việc:** Luôn `@mention` chỉ đúng file Test và file Page Object đang làm dở khi nhờ AI fix code (ví dụ: gõ `@LoginTest` và `@LoginPage`). Việc này ngăn AI đọc cả project mất thì giờ.
- **Mô tả yêu cầu đầy đủ ngay lần đầu:** Tránh gửi yêu cầu mơ hồ rồi bổ sung dần qua 5-6 lượt chat. Mỗi lượt hỏi thêm, AI phải đọc lại toàn bộ context trước đó — rất tốn token. Hãy cung cấp đủ: mục tiêu, tech stack, file liên quan, kết quả mong muốn ngay trong câu hỏi đầu.
- **Hạn chế gửi screenshot khi có thể dùng text:** Ảnh chụp màn hình tốn token gấp nhiều lần so với text. Nếu chỉ cần chỉ ra 1 lỗi trên UI, hãy copy text lỗi hoặc HTML element thay vì chụp ảnh.

#### 🔆 Khi debug lỗi

- **Hỏi cùng Stack Trace:** Khi Script lỗi (ví dụ: `ElementNotVisible`), đừng quăng nguyên file code lên hỏi mù. Hãy copy dòng lỗi thực tế in ra ở Terminal ghép cùng đoạn Code bị hỏng thả vào Fast Mode — AI sẽ đánh đúng trọng tâm ngay lập tức.
- **Giới hạn vòng lặp self-fix:** Nếu AI tự fix liên tục 3 lần mà test vẫn FAIL, hãy dừng lại và can thiệp thủ công — đọc log, xác định root cause rồi chỉ rõ cho AI. Để AI chạy loop vô hạn sẽ đốt token cực nhanh mà không giải quyết được gốc vấn đề.

#### 🔆 Khi quản lý conversation

- **Tách conversation nhỏ theo task:** Mỗi conversation dài tích lũy context càng dài, mỗi lượt chat tiếp theo AI càng phải đọc lại nhiều, token tăng cấp số nhân. Nên mở conversation mới cho mỗi task độc lập (ví dụ: 1 conversation cho Login Page, 1 conversation khác cho Dashboard Page).
- **Tận dụng Workflows (Slash Commands) có sẵn:** Thay vì mô tả lại quy trình dài dòng, dùng trực tiếp slash commands đã được define sẵn (ví dụ: `/generate_automation_from_testcases`). Workflow đã chứa prompt tối ưu, giúp AI hiểu đúng yêu cầu ngay lần đầu mà không cần giải thích thêm.

### 

### ✳️ Chia sẻ thêm 6 tips từ bạn **Lê Huy Đức Anh** (Admin nhóm Antigravity VN 🇻🇳)

Khá lâu trước đây, mình có viết một bài về quản lý context cho Antigravity nói riêng và các AI nói chung.  
Nhưng có vẻ chủ đề này vẫn nóng hổi như ngày đầu.   
Đặc biệt là khi các ông lớn bắt đầu bóp nghẹt user bằng chiêu giảm quota.  
Vẫn có rất nhiều người hỏi, và câu trả lời thì vẫn xoay quanh một thứ duy nhất.  
Context.  
Đúng hơn là **Context Management**.  
----------  
Hiểu đơn giản thế này.  
Mỗi lần bạn gửi tin nhắn, AI phải đọc lại toàn bộ cuộc trò chuyện từ đầu.  
Tin nhắn thứ nhất, AI đọc 1 trang.  
Tin nhắn thứ 20, AI đọc 20 trang.  
Cùng một câu hỏi, nhưng "chi phí" hoàn toàn khác nhau.  
Đó là lý do mà cùng một tác vụ, có người tốn 2% quota, có người tốn 20%.  
  
Sau vài năm dùng AI làm việc mỗi ngày, mình rút ra 6 thói quen giúp tiết kiệm quota mà chất lượng output vẫn đảm bảo.  
---------

#### 1. Làm rõ input và output trước khi bắt đầu

Nghe có vẻ hiển nhiên, nhưng đa số mọi người bỏ qua bước này.  
Trước khi gõ bất cứ thứ gì, mình luôn tự trả lời trên giấy: mình đang có gì, và mình muốn nhận lại cái gì.  
Khi bạn biết rõ điểm A và điểm B, AI sẽ giúp bạn đi con đường ngắn nhất.  
Còn khi bạn mơ hồ, AI cũng sẽ mơ hồ theo, và bạn sẽ tốn thêm 3-4 lượt chat chỉ để "căn chỉnh lại" thứ đáng ra đã rõ từ đầu.  
---------

#### 2. Edit lại câu lệnh sai, thay vì chat tiếp

Khi bạn gửi một câu lệnh sai rồi chat tiếp kiểu "ơ cái này sai rồi, làm lại thế kia đi", AI buộc phải nhớ cả phần sai lẫn phần sửa.  
Bộ nhớ phình ra, quota tốn thêm, mà kết quả chưa chắc đã tốt hơn.  
Thay vào đó, hãy bấm edit lại chính câu lệnh ban đầu.  
Context được reset, bỏ qua phần sai hoàn toàn.  
Sạch sẽ hơn, rẻ hơn, và thường ra kết quả chính xác hơn.  
---------

#### 3. Giữ cuộc trò chuyện dưới 10 lượt chat

Với kinh nghiệm cá nhân của mình, dưới 10 lượt chat, mọi thứ vẫn nhanh và chính xác.  
Qua 15-20 lượt, AI bắt đầu chậm hơn, đôi khi "quên" những gì đã thống nhất trước đó, và mỗi lượt chat tốn quota nhiều hơn hẳn.  
Lý do thì đơn giản: cuộc trò chuyện càng dài, lượng thông tin AI phải xử lý mỗi lần càng lớn.  
Nếu bạn thấy mình đang ở lượt chat thứ 15 mà vẫn chưa xong, đó là tín hiệu để dừng lại và thử cách tiếp cận khác.  
Ơ nhưng context của LLM là 1M token cơ mà.  
Đấy chỉ là quảng cáo thôi, thực tế khác xa như vậy, <100k token context và <200k token context đã cho kết quả rất khác nhau rồi.  
Mình đã thử vắt kiệt context 1M của Gemini trên Antigravity, đầu ra output là 1 mớ hỗn độn, mình sẽ gửi ở comment cho mọi người xem.  
---------

#### 4. Chủ động nén context khi đi vào bế tắc

AI có tính năng tự tóm tắt, nhưng mình thường không đợi đến lúc đó.  
Khi cuộc trò chuyện bắt đầu dài hoặc đi vào ngõ cụt, mình tự tóm tắt lại những gì đã thống nhất, rồi mở một cuộc trò chuyện mới với bản tóm tắt đó.  
Cách này vừa tiết kiệm quota, vừa giúp mình thoát khỏi bế tắc nhanh đáng kể.  
Đôi khi vấn đề nằm ở context bị "nhiễu" chứ không phải AI kém.  
Một cuộc trò chuyện mới với context sạch thường cho kết quả tốt hơn việc cố sửa trong cuộc trò chuyện cũ.  
---------

#### 5. Dàn đều phiên làm việc trong ngày

Thay vì dồn hết công việc vào một buổi rồi stuck khi hết quota, mình chia thành nhiều phiên nhỏ trong ngày.  
Sáng xử lý phần research, trưa chiều lên plan, chiều review và chỉnh sửa.  
Vừa tận dụng được quota tốt hơn, vừa có khoảng nghỉ để mình suy nghĩ lại trước khi tiếp tục.  
Nhiều khi ý tưởng tốt nhất đến trong lúc nghỉ giữa hai phiên, chứ không phải lúc đang cắm đầu chat liên tục.  
---------

#### 6. Draft nội dung trước, tạo file sau

Đây là tip mình rút ra sau khi đốt quota vào mấy lần tạo file Word/Power Point rồi sửa tới sửa lui.  
Khi bạn yêu cầu AI tạo file Word hay PowerPoint, nó phải sinh ra hàng đống ký tự liên quan đến format, căn chỉnh, màu sắc, font chữ.  
Những thứ đó không liên quan gì đến nội dung, nhưng chiếm rất nhiều token.  
Và khi bạn chỉnh sửa nội dung trong file đó, AI phải xử lý lại toàn bộ phần format kèm theo.  
Tốn gấp mấy lần so với chỉnh sửa nội dung thuần.  
Nên mình luôn làm thế này: brainstorm và chốt nội dung trước trong chat thuần.  
Ý tưởng rõ ràng rồi, logic hợp lý rồi, lúc đó mới đưa order tạo file.  
Kết quả ra ổn định hơn, đúng ý hơn, và lượng token tiêu tốn giảm đi đáng kể.  
  

Còn nếu không cần trình bày quá cầu kỳ, mình sẽ chọn tạo file Markdown (.md).

Là loại định dạng nhẹ nhất, thân thiện nhất với AI, và sau này muốn chuyển sang format khác cũng rất dễ.

---------

**6 tip này nghe có vẻ đơn giản, và đúng là đơn giản thật.**

Nhưng phần lớn việc dùng AI hiệu quả nằm ở thói quen của người dùng, từ những thứ đơn giản nhất, chứ ít khi nằm ở bản thân AI.

Có nhiều người mình gặp trả lời rằng chưa bao giờ có khoảnh khắc WoW với AI cả. Còn mình thì Wow hàng ngày :))

Cũng giống như một chiếc xe tốt, nhưng người lái cứ đạp ga rồi phanh gấp liên tục thì xăng vẫn tốn gấp đôi.

Để mở cửa cho anh em phản biện, thì mình không nói ra các case ngoại lệ :))

Quan trọng là hiểu cơ chế, rồi linh hoạt tuỳ tình huống.