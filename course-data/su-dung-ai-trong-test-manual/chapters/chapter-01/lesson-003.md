# Bài 3 - Cài đặt và sử dụng Git GitHub GitLab

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/358](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/358)

✅ Cài đặt Git vào máy tính  
✅ Làm việc với GitHub/GitLab để Clone repo Claude Testing Skills và Codex Testing Skills về máy

## ✳️ Tìm hiểu tổng quan về Git

### 1. Git là gì?

***Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.***Định nghĩa ở trên mình lấy ở trang [git-scm.com](https://git-scm.com/). Hiểu nôm na Git là một phần mềm quản lý mã nguồn (source code) phân tán.  
  
[![[Selenium Java] Quản lý source code Selenium Java trên GitHub | Anh Tester](../../assets/aa0b66bfdc4c5f4ac3de.png)](https://anhtester.com/storage/photos/shares/lesson/selenium_java/git-blog-header.png)

### 2. Ưu điểm của git

- Giúp quản lý mã nguồn đơn giản, an toàn và dễ sử dụng.
- Tối ưu hóa việc quản lý source code khi làm việc theo nhóm bằng cách chia và kết hợp ra các nhánh (branch).
- Dễ dàng tích hợp CI/CD trong việc deployment với git.
- Có thể dễ dàng lấy source code ở bất kỳ đâu chỉ cần clone từ git server về máy của bạn.

### 3. Git server là gì?

- Git server là máy chủ (server) có cài đặt dịch vụ git. Source code sẽ được lưu trữ ở máy server này.
- Một số git server phổ biến: GitHub, Bitbucket, GitLab, Microsoft Azure DevOps, Amazon AWS CodeCommit ...

**Note:** Các bạn mới cần phân biệt giữa git và git server.

**Ví dụ:** GitHub là một git server. Bạn có thể tạo một respository trên github. Repository trên git server này gọi là remote repository. Bạn có thể Clone **Remote Repository** về máy bạn thành **Local Repository**[![[Selenium Java] Quản lý source code Selenium Java trên GitHub | Anh Tester](../../assets/cd7ed340e4d4735f0bc8.png)](https://files.fullstack.edu.vn/f8-prod/blog_posts/4383/62f2ece050dc5.png)

### 4. Repository là gì?

[![[Selenium Java] Quản lý source code Selenium Java trên GitHub | Anh Tester](../../assets/6b207b59ebd8a46c6253.png)](https://files.fullstack.edu.vn/f8-prod/blog_posts/4383/62f2ece81f866.png)

- Repostiory được hiểu như là một nơi lưu trữ chứa mã nguồn (source code) và tất cả thông tin liên quan đến việc sửa đổi và lịch sử của toàn bộ project (dự án).
- Dữ liệu của repository git có thể xem ở folder .git:  
    
  [![[Selenium Java] Quản lý source code Selenium Java trên GitHub | Anh Tester](../../assets/98bb34a24d84338a22ac.png)](https://anhtester.com/storage/photos/shares/lesson/selenium_java/repository_git.png)
- Respository có 2 loại:

  - **Remote Repository:** đặt ở git server và có thể chia sẻ tới nhiều người.
  - **Local Repository:** đặt ở máy local chỉ cho bản thân mình dùng. Bạn có thể Clone Remote Repository về máy bạn thành Local Repository. Và sau khi có thay đổi ở Local Repository có thể push code lên Remote Repository.

### 5. Branch là gì?

[![[Selenium Java] Quản lý source code Selenium Java trên GitHub | Anh Tester](../../assets/2b047bf3b5d8d1cb546e.png)](https://anhtester.com/storage/photos/shares/lesson/selenium_java/feature-branch-with-develop-git-workflow.png)

- **Branch** là nhánh của **repository**, hiểu đơn giản nó như một khu vực làm việc riêng (workspace). Khi tạo ra repository (kho chứa) ở git ta sẽ có 1 branch chính (master/main). Từ branch chính này ta có thể phân chia thành nhiều branch nhỏ. Branch đã phân nhánh này không ảnh hưởng đến branch chính vậy nên ta có thể tiến hành nhiều thay đổi trên cùng 1 repository. Đồng thời ta có thể merge (kết hợp) các branch với nhau.

**Ví dụ:**

- Khi ta làm một tính năng (feature) mới ta có thể tạo ra một branch riêng để code cho feature này. Sau khi feature hoàn thành ta có thể merge code vào branch chính (master).
- Hoặc trong team có nhiều team members ta có thể chia repository thành nhiều branch. Với mỗi branch cho một người. Việc chia thành các branch riêng biệt rất tiện lợi cho việc làm việc theo nhóm và tách biệt source code, cùng lúc chỉnh sửa trên 1 repository.
- Có 2 loại branch. Tương tự như repository, branch cũng có 2 loại:

  - **Remote Branch:** là branch lưu ở git server. Branch này có thể chia sẻ với người khác được.
  - **Local branch:** là branch lưu ở local máy của mình. Nó có thể liên kết với 1 remote branch hoặc không.

## ✳️ Các bước cài đặt để sử dụng được Git trên Windows

- **Bước 1**: cài đặt phần mềm **Git SCM**
- **Bước 2**: cài đặt công cụ quản lý Git là **Tortoisegit** trên **Windows** (hoặc **GitHub Desktop** cho cả **MacOS**)
- **Bước 3**: đăng ký tài khoản trên dịch vụ **GitHub** để lưu trữ source code
- **Bước 4**: tạo repository trên GitHub và kết nối với máy tính Windows

Link tải **Git SCM**: <https://git-scm.com/download/>

- Chi tiết cài đặt **Git SCM** các bạn có thể tham khảo: <https://phoenixnap.com/kb/how-to-install-git-windows>

Link tải **Tortoisegit (chỉ dành cho Window)**: <https://tortoisegit.org/download/>  
  
Link **GitHub**: <https://github.com/>

- Tạo mới một remote repository trên GiHub:

<https://docs.github.com/en/get-started/quickstart/create-a-repo>  
  
Link tải **GitHub Desktop (dành cho cả Window và MacOS)**: <https://desktop.github.com/>  
  
Link **GitLab**: <https://gitlab.com/users/sign_up>

An sẽ chỉ các bạn trên **GitHub**. Còn **GitLab** tương tự vậy luôn.

## Các lệnh Git cần thiết

Xác thực tài khoản Git lần đầu có thể lỗi này:

remote: Invalid username or token. Password authentication is not supported for Git operations.

**1. Đặt tên/email hiển thị khi commit (thiết lập danh tính Git — bước cần làm ngay sau khi cài Git)**

```none
git config --global user.name "Tên bạn muốn hiển thị"
git config --global user.email "email-cua-ban@example.com"
```

Tên và email này sẽ gắn vào mỗi lần bạn commit code, không liên quan tới việc đăng nhập GitHub/GitLab.

**Ví dụ:**

```bash
git config --local user.name "An Vo"
git config --local user.email "vothaian97@gmail.com"
```

**2. Gắn username GitHub vào lệnh clone (liên quan tới lỗi xác thực ở trên)**

```none
git clone https://tên-user-github@github.com/tên-user/tên-repo.git
```

*Dòng này copy từ Repo trên Git Server.*

Lúc này Git sẽ chỉ hỏi bạn ô password/token — bạn dán Personal Access Token vào đó là xong.

Nếu máy bạn đang lưu sẵn một username cũ (sai) khiến báo lỗi "Invalid username or token", cần xoá thông tin đăng nhập cũ đi trước:

- **Windows**: mở **Credential Manager** → **Windows Credentials** → tìm mục `git:https://github.com` → **Remove**.
- **macOS**: mở **Keychain Access**, tìm `github.com`, xoá mục đó đi.

Sau đó clone lại, Git sẽ hỏi username/token từ đầu.

Ghi nhớ

- Clone: lấy source đầu tiên về máy lần đầu (làm 1 lần)  
- Commit: thông báo có sự thay đổi cần đẩy lên Git Server (GitHub, GitLab)  
- Push: bắt đầu đẩy tất cả những Commit lên server  
- Pull: lấy source mới nhất từ trên Git Server về máy local

## ✳️ gitignore là gì?

**gitignore** là file có tên là **.gitignore** do **Git** quy định. Nhiệm vụ của nó là liệt kê những file mà mình **không mong muốn cho vào git** hoặc hiểu nôm na là Git sẽ bỏ qua những file đó đi không mang lên dịch vụ lưu trữ source code. **gitignore** hiện nay rất quan trọng trong team work, các bạn nên áp dụng ngay vào quy trình làm việc của team cụ thể là source code automation test dành cho Tester chúng ta.

## ✳️ Cách thức hoạt động của gitignore là gì?

Có thể hiểu đơn giản là git sẽ bỏ qua file hoặc một tập các file trong project của chúng ta khi commit và push lên repository. Ví dụ:

- Các file mà IDE tự sinh ra trong quá trình build project -> Tránh tốn kém tài nguyên server lưu trữ project.
- Các file cấu hình đường dẫn của máy cá nhân -> Gây ra việc không build được project khi checkout về ở các máy thành viên khác.
- Các file cần phải giữ kín nếu như repository của bạn đang để public.
- …

Git quản lý các file mà chúng ta muốn “ignore” bằng file `.gitignore` được đặt ở trong thư mục root project.

Khi add 1 file mới vào git, git sẽ kiểm tra danh sách những file sẽ bỏ qua trong file **.gitignore** và không add chúng vào git. Đó mới chỉ là điều kiện cần, **điều kiện đủ** là files không có trong **git cache** nữa thì git nó mới bỏ qua, chứ files mà nằm trong **git cache** thì **.gitignore** sẽ vô tác dụng.

## ✳️ Các kiểu format để loại bỏ trong .gitignore hay dùng

- Sử dụng dấu **#** để comment và có thể để cách dòng cho dễ đọc.
- Format cho các **file có tên cụ thể**: jdk.exe, source.zip, record.mp4,...
- Format dành cho loại bỏ cả **thư mục**: example\_folder/  
  Khi ignore thư mục **nên có dấu /** ở sau tên thư mục để nhận biết đó là thư mục, nếu không nó có thể là coi là thư mục hoặc file hay symbolic link.
- Dấu ! phía trước có ý nghĩa phủ định: **!abc/example.exe** nghĩa là không loại bỏ file cụ thể example.exe
- Sử dụng dấu **\*** để tìm các file có cùng định dạng. Ví dụ như bạn muốn ignore tất cả các file .xml trong project: \*.xml
- Trường hợp khác của **\*** nếu bạn chỉ rõ đường dẫn ví dụ: config/\*.xml thì nó chỉ có hiệu lực cho các file config/abc.xml mà không có hiệu lực cho các file config/sub/abc.xml.
- Sử dụng dấu **\*\*** để có hiệu lực cho các thư mục không cần định rõ tên. Ví dụ: **\*\*/report** nó sẽ có hiệu lực cho tất cả file hoặc thư mục có tên là report ở mọi nơi trong project.
- Hay sử dụng kiểu **folder/\*\*** để có hiệu lực cho tất cả các file bên trong thư mục.

## ✳️ Ví dụ các phần cần loại bỏ trong source code Selenium Java

**🔆 File .gitignore**

```git
bin/
out/
.idea/
.allure/
allure-results/
ExportData/
ExtentReports/
logs/
target/
test-output/
reports/
*.png
*.jpg
*.mp4
*.avi
*.zip
*.iml
```

`.gitignore` mẫu cho **Playwright TypeScript**

```log
# ==============================
# Node.js
# ==============================
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# ==============================
# Environment variables / Secrets
# ==============================
.env
.env.*
!.env.example

# ==============================
# Playwright
# ==============================
test-results/
playwright-report/
blob-report/
playwright/.cache/

# ==============================
# Screenshots / Videos / Traces
# ==============================
screenshots/
videos/
traces/

# ==============================
# Coverage
# ==============================
coverage/

# ==============================
# Build / Generated files
# ==============================
dist/
build/
out/

# ==============================
# TypeScript
# ==============================
*.tsbuildinfo

# ==============================
# IDE
# ==============================
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
.idea/
*.iml

# ==============================
# OS
# ==============================
.DS_Store
Thumbs.db

# ==============================
# Logs
# ==============================
*.log

# ==============================
# Temporary files
# ==============================
*.tmp
*.temp
```

**Lưu ý**: khi mà file hoặc folder đã lên trên server trước khi chúng ta add nó vào gitignore thì nó sẽ **KHÔNG BỊ DELETE ĐƯỢC**. Muốn **DELETE ĐƯỢC** chúng ta cần phải delete nó dưới local xong commit push lên lại thì từ đó về sau nó mới hiểu loại bỏ như trong gitignore.

## ✳️ Quy trình làm việc với Git chuẩn

***Trước khi mở code làm việc thì chúng ta nên làm theo các bước sau:***

- B1: **Pull** source về trước - Đảm bảo source dưới local mình đang mới nhất
- B2: **Commit** lên sau khi add/edit code
- B3: **Push**
- B4: Lên server check lại

Và cứ như thế lặp lại từ B1 đến B4 cho các lần mở code làm việc.  
  
Thao tác theo bước như vậy để **tránh bị** **Conflict** code (trùng lặp nội dung code trên cùng 1 file)