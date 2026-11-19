# Bài 7 - [AI Test Automation] Hoàn thiện project Test Automation xuất Report và chạy CI với GitHub Actions

Chương: 1. Nội dung khoá học

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/289](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/289)

[Video nhúng](https://www.youtube.com/embed/P-NU-XK8KbY)

3 giờ 49 phút

Sau khi đã “trao tay chân” cho AI bằng MCP Server ở bài trước, bước tiếp theo để biến project thành một hệ thống Test Automation hoàn chỉnh chính là:

- Xuất report đẹp để đọc kết quả test
- Tự động chạy test trên CI/CD
- AI có thể tự debug khi pipeline fail
- Và cuối cùng: chỉ cần prompt → AI tự làm gần như toàn bộ workflow 😄

Nếu ở bài 6 chúng ta giúp AI “nhìn thấy” hệ thống thật thông qua MCP Server, thì bài này sẽ giúp AI:

👉 biết cách vận hành project như một Automation Engineer thực thụ.

Tham khảo bài trước tại [[AI Test Automation] Bài 6 - Thiết lập cho AI sử dụng MCP Server trên Antigravity](https://anhtester.com/lesson/ai-test-automation-bai-6-thiet-lap-cho-ai-su-dung-mcp-server-tren-antigravity?utm_source=chatgpt.com)

## 🎯 Mục tiêu bài này

Sau bài học này, bạn sẽ có thể:

- Tích hợp Allure Report cho framework automation
- Dùng AI generate report config
- Push project lên GitHub
- Tạo GitHub Actions tự chạy test
- Tự động upload report sau mỗi lần run
- Prompt để AI tự fix pipeline khi CI fail

Nghe thì nhiều bước…

Nhưng thật ra phần lớn chúng ta chỉ cần:

> “ra lệnh đúng cho AI” 😄

---

## 

## 🧠 Tư duy mới: Tester không còn chỉ viết code

Trước đây quy trình thường là:

```text
Viết script → Chạy local → Fix → Push → Chạy CI → Fix tiếp 😭
```

Còn hiện tại với AI + MCP:

```text
Prompt → AI code → AI chạy → AI đọc log → AI sửa → PASS ✅
```

Điểm khác biệt rất lớn là:

👉 AI giờ không chỉ “sinh code”.

Mà AI có thể:

- đọc project structure
- tạo YAML CI
- generate report config
- debug pipeline
- đọc screenshot khi fail
- tự retry

Đây mới là thứ làm AI Test Automation thực sự đáng giá.

---

## 

## 📦 Phần 1 - Tích hợp Allure Report

### 🔆 Vì sao cần report?

Một framework automation không có report…

thì giống như chạy test xong rồi “tin bằng niềm tin” 😅

Report giúp:

- Biết testcase nào fail
- Screenshot lỗi ở đâu
- Thời gian chạy test
- Log từng step
- Video execution
- Phân tích flaky test

Trong các loại report hiện nay:

<table class="rt-table">
<thead>
<tr>
<th>Report</th>
<th>Ưu điểm</th>
<th>Nhược điểm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Extent Report</td>
<td>Dễ dùng</td>
<td>UI cũ</td>
</tr>
<tr>
<td>HTML Report</td>
<td>Nhẹ</td>
<td>Ít tính năng</td>
</tr>
<tr>
<td>Allure Report</td>
<td>Đẹp + mạnh + phổ biến</td>
<td>Setup nhiều hơn</td>
</tr>
</tbody>
</table>

👉 Mình khuyến nghị **Allure** cho AI Test Automation.

Vì AI đọc structure của Allure rất tốt.

---

## 

## ⚙️ Cài đặt Allure với Playwright

### Cài package

```bash
npm install -D allure-playwright
```

### Update playwright.config.ts

```ts
reporter: [
  ['list'],
  ['allure-playwright']
]
```

### Chạy test

```bash
npx playwright test
```

### Generate report

```bash
allure generate allure-results --clean
allure open
```

---

## 

## 🤖 Prompt cho AI tự tích hợp Allure

Đây là kiểu prompt mình đang dùng với Antigravity:

```text

```

```markdown
Phân tích project Playwright hiện tại [playwright-typescript-framework] và: 

1. Tích hợp Allure Report
2. Cài package cần thiết
3. Update playwright.config.ts
4. Tự động attach screenshot khi fail
5. Attach video execution
6. Generate command scripts trong package.json
7. Verify report chạy thành công

Yêu cầu:
- Không phá existing config
- Giữ tương thích GitHub Actions
- Nếu thiếu dependency thì tự cài
- Ghi log các step trong Test Body của Allure report với câu mô tả tiếng anh rõ ràng hơn
- Đối với những test cases passed thì đính kèm ảnh chụp màn hình vào bước cuối cùng
- Có nhiều bước trung gian automation trong code bị dư thừa khi hiển thị lên Test Body nên bạn lọc bớt giúp tôi, chỉ giữ lại các bước automation chính theo test cases.
- Thêm các bước chi tiết automation con bên trong cho bước cha bên ngoài. Các step name detail trong các class page và class test như bạn đã custom cho step cha, dùng tiếng anh rõ ràng.
- Gắn giá trị locator và giá trị của tham số vào các step cho tôi luôn.
- Thêm/Cập nhật .github/workflows/playwright.yml để thêm thư viện Allure Report vào project và setup để tạo report xem trực tiếp trên GitHub Actions.
```

```text

```

Điểm hay là:

AI sẽ:

- tự scan project
- hiểu framework đang dùng
- update config phù hợp
- và tự test lại sau khi sửa

Đây là chỗ MCP cực kỳ mạnh.

---

## 

## 📁 Cấu trúc project sau khi hoàn thiện

Ví dụ:

```text
project-root/
│
├── tests/
├── pages/
├── utils/
├── playwright.config.ts
├── package.json
│
├── allure-results/
├── allure-report/
│
└── .github/
    └── workflows/
        └── regression.yml
```

---

## 

## 🚀 Phần 2 - Đưa project lên GitHub

### 🔆 Vì sao cần GitHub?

Nhiều bạn nghĩ GitHub chỉ đơn giản là nơi để “đẩy source code lên”.

Nhưng với Test Automation hiện đại, GitHub chính là trung tâm vận hành của cả project.

Bởi vì từ đây chúng ta mới có thể:

- quản lý version source code
- làm việc team
- review code automation
- trigger CI/CD
- lưu artifact và report
- tracking lịch sử execution
- và quan trọng nhất:  
  👉 để AI có môi trường làm việc hoàn chỉnh

---

Khi project chỉ chạy ở local:

```none
PASS máy mình ≠ PASS môi trường thật
```

Rất nhiều case:

- local chạy PASS
- lên CI fail
- browser khác fail
- Linux fail
- timeout fail

Đó là lý do project automation chuyên nghiệp luôn cần CI/CD.

Và GitHub Actions hiện tại là lựa chọn quá phù hợp:

- miễn phí cho project nhỏ
- setup nhanh
- AI support rất tốt
- ecosystem mạnh

---

Điểm mình thấy thú vị nhất là:

Khi project đã đưa lên GitHub,  
AI bắt đầu có thể tham gia sâu hơn vào workflow automation.

Ví dụ:

- AI đọc pipeline log
- AI đọc error trên CI
- AI phân tích artifact
- AI sửa YAML
- AI fix flaky locator
- AI rerun pipeline

Cái này bạn có thể copy từng cái gửi cho AI còn muốn tự động thì dùng GitHub MCP. Nhưng mình nghĩ nên làm thủ công chỗ này sẽ an toàn hơn và kĩ hơn, có con người can thiệp phần nào. Vì việc mình là kiểm thử cho chắc chắn.  
  
Và lúc này AI không còn chỉ là “tool generate code”.

Mà gần giống:  
👉 một Automation Engineer hỗ trợ vận hành project cùng chúng ta 😄

---

### 

### ⚙️ Cài đặt Git trên Windows và MacOS

#### 1. Tải Git

Truy cập trang chính thức của [Git SCM](https://git-scm.com/?utm_source=chatgpt.com)

#### 2. Cài đặt

- Window thì chạy file **exe**  
- MacOS thì chạy lệnh: cài [Homebrew](https://brew.sh/) trước, lệnh cài **Git** sau thông qua Brew

#### 3. Kiểm tra cài đặt

Mở:

- CMD
- PowerShell
- Git Bash

Chạy:

```none
git --version
```

#### 4. Cấu hình thông tin Git

```none
git config --global user.name "Anh Tester"git config --global user.email "email@example.com"
```

Kiểm tra:

```none
git config --list
```

### ⚙️ Khởi tạo Git repository

```bash
git init
git add .
git commit -m "initial automation framework"
```

### 

### Tạo GitHub repo

Ví dụ:

```bash
https://github.com/yourname/ai-test-framework
```

Sau đó:

```bash
git remote add origin <repo-url>
git push -u origin main
```

---

# 

### 🤖 Prompt để AI setup GitHub project

```text
Hãy chuẩn hóa project để push lên GitHub:

1. Tạo .gitignore phù hợp Playwright
2. Loại bỏ file không cần commit
3. Tạo README.md chuyên nghiệp
4. Thêm scripts cần thiết vào package.json
5. Verify project clean trước khi push
```

AI thường làm khá sạch phần này 😄

---

## 

## ⚙️ Phần 3 - Tạo GitHub Actions chạy automation

Đây mới là phần “nâng cấp” project thành hệ thống thật sự.

### 🔆 GitHub Actions là gì?

Hiểu đơn giản:

Mỗi lần:

- push code
- tạo pull request
- merge branch

👉 GitHub sẽ tự chạy test cho bạn.

Không cần mở máy local.

---

## 

### 📄 Tạo workflow đầu tiên

File:

```text
.github/workflows/regression.yml
```

Nội dung:

```yaml
name: Regression Test

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Setup NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install packages
        run: npm install

      - name: Install Playwright Browsers
        run: npx playwright install --with-deps

      - name: Run automation test
        run: npx playwright test

      - name: Upload Allure Results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: allure-results
          path: allure-results/
```

---

# 

### 🔥 Điểm cực mạnh khi dùng AI

Ngày xưa:

Viết YAML CI là ác mộng 😭

Sai indent 1 dấu cách:

- pipeline fail
- debug 2 tiếng

Giờ thì:

👉 AI viết YAML rất nhanh.

Thậm chí còn:

- optimize cache
- parallel execution
- retry flaky test
- split job
- matrix browser

---

## 

### 🤖 Prompt cho AI tự build GitHub Actions

```text
Hãy tạo GitHub Actions cho project Playwright này:

Yêu cầu:
- Chạy trên Ubuntu latest
- NodeJS 20
- Install browser dependencies
- Run toàn bộ regression test
- Upload Allure Results
- Nếu fail vẫn upload artifact
- Tối ưu tốc độ CI bằng cache
- Chia rõ step để dễ debug
```

---

# 

## 📊 Phần 4 - Upload Allure Report lên GitHub Pages

Đây là bước nhiều bạn rất thích 😄

Sau mỗi lần CI chạy:

👉 report sẽ có URL online riêng.

Ví dụ:

```text
https://yourname.github.io/automation-report
```

Team:

- Dev
- QA
- Manager

đều xem được.

---

## 

## ⚙️ Workflow publish report

AI thường generate thêm:

```yaml
- name: Generate Allure Report
  run: |
    npm install -g allure-commandline
    allure generate allure-results --clean -o allure-report

- name: Deploy Report
  uses: peaceiris/actions-gh-pages@v3
```

---

## 

## 🤯 Kịch bản thực tế rất mạnh

Sau khi setup xong:

Bạn chỉ cần prompt:

```text
Run toàn bộ regression test.
Nếu testcase fail:
- đọc log
- đọc screenshot
- tìm nguyên nhân
- tự fix locator
- rerun đến khi pass
- update lại source code
```

Và AI thực sự làm được phần lớn workflow này.

Đó là lý do mình nói:

👉 AI Test Automation hiện tại không còn là “AI viết code”.

Mà là:

- AI Engineer Assistant
- AI Debugger
- AI CI Operator

---

## 

## 🔁 Self-Healing thật sự bắt đầu từ CI

Nhiều người nghĩ self-healing chỉ là:

```text
Locator fail → AI sửa locator
```

Không.

Self-healing thật sự là:

```text
CI fail
→ AI đọc pipeline
→ đọc artifact
→ đọc screenshot
→ sửa code
→ commit lại
→ rerun
→ PASS
```

Đây mới là level automation tiếp theo.

---

# 

## 📌 Best Practices khi chạy CI cho AI Automation

### 1. Always Headless

CI không cần UI.

```bash
npx playwright test --headed
```

❌ Không nên trên CI

Nên dùng:

```bash
npx playwright test
```

---

## 

### 2. Luôn attach screenshot khi fail

Ví dụ config:

```ts
use: {
  screenshot: 'only-on-failure',
  video: 'retain-on-failure'
}
```

AI debug screenshot rất hiệu quả.

---

## 

### 3. Không hardcode timeout

CI thường chậm hơn local.

Ví dụ:

```ts
timeout: 60000
```

---

## 

### 4. Retry trên CI

```ts
retries: process.env.CI ? 2 : 0
```

---

## 

### 5. Tách smoke và regression

Đừng chạy full regression mỗi commit 😄

Ví dụ:

<table class="rt-table">
<thead>
<tr>
<th>Trigger</th>
<th>Suite</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pull Request</td>
<td>Smoke</td>
</tr>
<tr>
<td>Nightly</td>
<td>Regression</td>
</tr>
<tr>
<td>Release</td>
<td>Full E2E</td>
</tr>
</tbody>
</table>

---

# 

## 💡 Một mindset rất quan trọng

Nhiều tester hiện tại vẫn nghĩ:

> “Muốn làm automation thì phải code rất giỏi.”

Thật ra trong kỷ nguyên AI:

Điều quan trọng hơn là:

- Cần biết code ngôn ngữ lập trình nền tảng

- Biết cần dùng thư viện gì hiệu quả cho từng loại automation
- biết architecture
- biết workflow
- biết review AI output
- biết prompt đúng
- biết debug đúng hướng

AI sẽ hỗ trợ phần coding rất nhiều.

Còn tư duy testing…  
vẫn là thứ con người quyết định 😄

---

# 

## 🏁 Kết luận

Sau 7 bài vừa qua, chúng ta đã đi từ:

- AI generate testcase
- AI generate automation script
- AI dùng MCP thao tác browser thật, mobile thật
- AI vận hành cả pipeline automation hoàn chỉnh

Và đây mới chỉ là khởi đầu.

Giai đoạn tiếp theo sẽ còn thú vị hơn:

- AI tự phân tích flaky test
- AI visual testing
- AI API contract testing
- AI mobile testing với Appium MCP
- AI tự optimize execution strategy

Quan trọng nhất:

👉 Đừng cố “đấu lại AI”.

Hãy học cách:

- điều khiển AI
- review AI
- và biến AI thành teammate mạnh nhất của mình 😄

## 

## 📚 Tham khảo

- [Anh Tester](https://anhtester.com/)
- [Playwright](https://playwright.dev/)
- [GitHub Actions](https://github.com/features/actions)
- [Allure Report](https://allurereport.org/)
- [Model Context Protocol](https://modelcontextprotocol.io/?utm_source=chatgpt.com)