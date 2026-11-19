# Bài 7 - [Javascript Typescript] Quản lý source code với Git và GitHub

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/405](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/405)

✅ Git và GitHub là gì: repository, commit, branch, remote  
✅ Cài Git, cấu hình một lần và viết .gitignore trước commit đầu tiên  
✅ Lưu thay đổi ở máy: status, add, commit, log, diff, restore  
✅ Đưa code lên GitHub: remote, push, pull, clone và cách đăng nhập an toàn  
✅ Branch, Pull Request và tự xử lý Merge Conflict  
✅ Dùng AI soạn lệnh Git, commit message và kiểm tra lại trước khi chạy

## ⭐ Mục tiêu bài học

Qua 6 bài, project `js-ts-for-tester` của bạn đã có 6 thư mục code, từ `bai-01-cai-dat/` tới `bai-06-ham/`. Nhưng toàn bộ chỉ nằm trên một máy: sửa hỏng một file thì không quay lại được bản cũ, ổ cứng hỏng là mất hết, làm nhóm thì không biết ai đã sửa gì. Bài này dùng **Git** để lưu lịch sử code và **GitHub** để cất code lên mạng. Học xong bạn sẽ:

- Phân biệt Git với GitHub; hiểu repository, commit, branch, remote.
- Cài Git, cấu hình tên và email một lần.
- Viết `.gitignore` trước commit đầu tiên để `.env` và `node_modules` không bao giờ lên GitHub.
- Dùng `git status`, `add`, `commit`, `log`, `diff`, `restore` ở máy; `push`, `pull`, `clone` với GitHub.
- Tạo branch, mở Pull Request và tự xử lý một merge conflict.
- Đọc và duyệt lệnh Git do AI đề xuất trước khi chạy.

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`), gõ lệnh ở Terminal của VS Code. Kết quả trong bài là kết quả chạy thật với Git 2.54.0. Mã commit (7 ký tự như `75f2b27`) và số file trên máy bạn sẽ khác. Riêng `push`, `pull`, `clone` được chạy với một remote dựng ngay trên máy soạn bài rồi thay địa chỉ bằng địa chỉ GitHub; với GitHub thật bạn thấy thêm vài dòng tiến trình.

## ✅ Phần 1: Git và GitHub là gì?

### 🔆 1. Git: lưu từng bản của code kèm ghi chú

Khi viết một báo cáo quan trọng, nhiều người lưu thành `bao-cao-v1.docx`, `bao-cao-v2-sua-ngay-12.docx`, `bao-cao-final-final.docx`. Mục đích đúng (giữ bản cũ để quay về), nhưng cách làm rối: không biết bản nào mới nhất, hai bản khác nhau chỗ nào.

**Git** là công cụ quản lý phiên bản (version control) làm việc đó cho cả thư mục code. Mỗi lần bạn bảo "lưu lại", Git ghi một **commit**: toàn bộ trạng thái code lúc đó, kèm người sửa, thời điểm và một dòng ghi chú. Git chạy trên máy bạn, không cần mạng.

Với tester làm automation: script hôm qua chạy được, hôm nay hỏng thì phải xem được ai đã sửa dòng nào.

### 🔆 2. GitHub: nơi cất repository trên mạng

Ảnh trong điện thoại muốn an toàn thì sao lưu lên kho lưu trữ trên mạng. **GitHub** là kho như vậy cho code: một trang web giữ bản sao repository của bạn, để máy hỏng không mất code và cả nhóm cùng làm việc. GitLab, Bitbucket là các dịch vụ tương tự: lệnh Git giống hệt, chỉ khác trang web.

### 🔆 3. Bốn khái niệm dùng trong cả bài

<table class="rt-table">
<thead>
<tr>
<th>Khái niệm</th>
<th>Là gì</th>
<th>Trong project của bạn</th>
</tr>
</thead>
<tbody>
<tr>
<td>Repository (repo)</td>
<td>Thư mục project được Git theo dõi, gồm code và toàn bộ lịch sử</td>
<td>Cả thư mục <code>js-ts-for-tester</code></td>
</tr>
<tr>
<td>Commit</td>
<td>Một mốc lưu: trạng thái code tại một thời điểm, kèm ghi chú</td>
<td>"Thêm ghi chú học Git"</td>
</tr>
<tr>
<td>Branch (nhánh)</td>
<td>Một dòng commit riêng để sửa code mà không đụng tới nhánh chính</td>
<td><code>main</code> là nhánh chính</td>
</tr>
<tr>
<td>Remote</td>
<td>Bản sao của repository nằm trên máy chủ</td>
<td>Repo trên GitHub, tên tắt là <code>origin</code></td>
</tr>
</tbody>
</table>

## ✅ Phần 2: Cài Git và cấu hình một lần

### 🔆 1. Cài đặt và kiểm tra

- **Windows:** tải bộ cài tại [git-scm.com](https://git-scm.com/install/windows), bấm Next với các lựa chọn mặc định. Bạn đã cài Git for Windows ở bài cài đặt thì bỏ qua bước này.
- **macOS:** chạy `xcode-select --install`, hoặc `brew install git` nếu máy có Homebrew ([hướng dẫn](https://git-scm.com/install/mac)).

Mở **terminal mới** rồi kiểm tra:

```bash
PS D:\AnhTester\js-ts-for-tester> git --version
git version 2.54.0.windows.1
```

Bản mới hơn cũng dùng được.

### 🔆 2. Khai báo tên, email và tên nhánh mặc định

Mỗi commit ghi tên và email người tạo, nên Git cần biết bạn là ai. Khai báo **một lần** cho cả máy (`--global`):

```bash
PS D:\AnhTester\js-ts-for-tester> git config --global user.name "Anh Tester"
PS D:\AnhTester\js-ts-for-tester> git config --global user.email "ban@example.com"
PS D:\AnhTester\js-ts-for-tester> git config --global init.defaultBranch main
PS D:\AnhTester\js-ts-for-tester> git config --global --list
user.name=Anh Tester
user.email=ban@example.com
init.defaultbranch=main
```

Thay bằng tên của bạn và **email đã đăng ký GitHub**. Không muốn lộ email thì dùng địa chỉ `noreply` GitHub cấp ([tài liệu](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)). `init.defaultBranch main` đặt tên nhánh đầu tiên của mọi repo mới là `main`, trùng với tên GitHub dùng.

## ✅ Phần 3: Tạo repository và file .gitignore

### 🔆 1. git init: biến thư mục project thành repository

Đứng ở **gốc project** (nhìn dấu nhắc) rồi chạy:

```bash
PS D:\AnhTester\js-ts-for-tester> git init
Initialized empty Git repository in D:/AnhTester/js-ts-for-tester/.git/
```

Git tạo thư mục ẩn `.git` để chứa lịch sử. Chỉ chạy `git init` **một lần cho một project**; xoá thư mục `.git` là mất toàn bộ lịch sử.

> ⚠️ Không chạy `git init` ở `D:\` hay thư mục người dùng. Git sẽ coi mọi thứ bên dưới là một repo khổng lồ.

### 🔆 2. git status: lệnh gõ nhiều nhất

`git status` trả lời câu hỏi "Git đang thấy gì?". Lệnh này chỉ xem, không thay đổi gì, nên gõ trước và sau mọi lệnh khác:

```bash
PS D:\AnhTester\js-ts-for-tester> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .env
        bai-01-cai-dat/
        bai-02-bien-kieu-du-lieu/
        bai-03-dieu-kien/
        bai-04-vong-lap-mang/
        bai-05-object-json/
        bai-06-ham/
        node_modules/
        package-lock.json
        package.json

nothing added to commit but untracked files present (use "git add" to track)
```

**Untracked files** là file Git nhìn thấy nhưng **chưa theo dõi**. Trong danh sách có hai thứ không được phép lên GitHub: `.env` và `node_modules/`. Phải chặn chúng **trước** khi commit.

### 🔆 3. Viết .gitignore trước commit đầu tiên

`.gitignore` là danh sách những thứ Git phải bỏ qua. Tạo file `.gitignore` (tên bắt đầu bằng dấu chấm, không có đuôi) ở gốc project:

```bash
node_modules/
.env
test-results/
playwright-report/
.DS_Store
```

<table class="rt-table">
<thead>
<tr>
<th>Dòng</th>
<th>Vì sao không đưa lên Git</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>node_modules/</code></td>
<td>Rất nặng, tạo lại được bằng <code>npm install</code></td>
</tr>
<tr>
<td><code>.env</code></td>
<td>Chứa <code>ADMIN_EMAIL</code>, <code>ADMIN_PASSWORD</code>. Lên GitHub là lộ tài khoản</td>
</tr>
<tr>
<td><code>test-results/</code>, <code>playwright-report/</code></td>
<td>Kết quả và báo cáo Playwright sinh ra mỗi lần chạy (dùng từ chương Playwright). Ảnh, video trong đó có thể chứa dữ liệu thật</td>
</tr>
<tr>
<td><code>.DS_Store</code></td>
<td>File rác macOS tự sinh trong mỗi thư mục</td>
</tr>
</tbody>
</table>

Dấu `/` ở cuối nghĩa là cả thư mục. Kiểm tra lại bằng hai lệnh:

```bash
PS D:\AnhTester\js-ts-for-tester> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        bai-01-cai-dat/
        bai-02-bien-kieu-du-lieu/
        bai-03-dieu-kien/
        bai-04-vong-lap-mang/
        bai-05-object-json/
        bai-06-ham/
        package-lock.json
        package.json

nothing added to commit but untracked files present (use "git add" to track)
PS D:\AnhTester\js-ts-for-tester> git check-ignore -v .env
.gitignore:2:.env       .env
```

`.env` và `node_modules/` đã biến mất khỏi danh sách. `git check-ignore -v` chỉ rõ: file `.env` bị bỏ qua do **dòng 2** của `.gitignore`. Bản thân `.gitignore` thì phải commit, để cả nhóm dùng chung.

### 🔆 4. Lỡ commit file .env rồi thì sao?

`.gitignore` chỉ có tác dụng với file **chưa được theo dõi**. File đã commit rồi thì thêm tên vào `.gitignore` cũng vô ích. Anh Tester dựng một repo thử riêng, trong đó `.env` (mật khẩu giả) đã lỡ nằm trong commit đầu, rồi gỡ nó ra:

```bash
PS D:\AnhTester\demo-env> git ls-files
.env
a.js
PS D:\AnhTester\demo-env> git rm --cached .env
rm '.env'
PS D:\AnhTester\demo-env> git add .gitignore
PS D:\AnhTester\demo-env> git commit -m "Ngừng theo dõi file .env"
[main befc657] Ngừng theo dõi file .env
 2 files changed, 1 insertion(+), 1 deletion(-)
 delete mode 100644 .env
 create mode 100644 .gitignore
PS D:\AnhTester\demo-env> git ls-files
.gitignore
a.js
PS D:\AnhTester\demo-env> git show HEAD~1:.env
ADMIN_PASSWORD=mat-khau-gia-de-tap
```

`git ls-files` liệt kê file Git đang theo dõi. `git rm --cached` bỏ theo dõi nhưng **giữ file trên máy**. Lệnh cuối là điều phải nhớ: `git show HEAD~1:.env` đọc file ở commit trước đó và **mật khẩu vẫn nằm trong lịch sử**.

> 🔒 Mật khẩu đã lên GitHub thì coi như đã lộ. Việc đầu tiên là **đổi mật khẩu đó**, sau mới dọn repo. GitHub cũng hướng dẫn đúng thứ tự này: [thu hồi hoặc đổi bí mật trước](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), xoá khỏi lịch sử sau.

## ✅ Phần 4: Lưu thay đổi ở máy - add, commit, log, diff, restore

### 🔆 1. git add: chọn thứ sẽ vào commit

Chụp ảnh tập thể có hai bước: gọi người vào khung hình, rồi bấm máy. Git cũng vậy: `git add` chọn thay đổi, `git commit` lưu lại. Thử chọn hai file trước:

```bash
PS D:\AnhTester\js-ts-for-tester> git add .gitignore package.json
PS D:\AnhTester\js-ts-for-tester> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   package.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        bai-01-cai-dat/
        bai-02-bien-kieu-du-lieu/
        bai-03-dieu-kien/
        bai-04-vong-lap-mang/
        bai-05-object-json/
        bai-06-ham/
        package-lock.json
```

Ba nhóm bạn sẽ gặp trong `git status`:

<table class="rt-table">
<thead>
<tr>
<th>Nhóm</th>
<th>Nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Untracked files</code></td>
<td>File mới, Git chưa theo dõi</td>
</tr>
<tr>
<td><code>Changes not staged for commit</code></td>
<td>File đã theo dõi, vừa bị sửa (<code>modified</code>), chưa <code>add</code></td>
</tr>
<tr>
<td><code>Changes to be committed</code></td>
<td>Đã <code>add</code>, sẽ nằm trong commit kế tiếp</td>
</tr>
</tbody>
</table>

### 🔆 2. git commit: lưu mốc đầu tiên

`git add .` chọn **mọi thay đổi** trong thư mục hiện tại. Chỉ dùng khi đã có `.gitignore`:

```bash
PS D:\AnhTester\js-ts-for-tester> git add .
PS D:\AnhTester\js-ts-for-tester> git commit -m "Khởi tạo project js-ts-for-tester: code 6 bài đầu"
[main (root-commit) 75f2b27] Khởi tạo project js-ts-for-tester: code 6 bài đầu
 15 files changed, 34 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 package-lock.json
 create mode 100644 package.json
PS D:\AnhTester\js-ts-for-tester> git status
On branch main
nothing to commit, working tree clean
```

(Đã lược các dòng `create mode` của file bài học.) `-m` là ghi chú của commit. `75f2b27` là mã commit. `working tree clean` nghĩa là mọi thứ đã được lưu.

### 🔆 3. Sửa file, xem khác biệt bằng git diff, rồi commit

Tạo thư mục `bai-07-git` và file `bai-07-git/ghi-chu.md`:

```markup
# Ghi chú học Git

- git status: xem trạng thái
```

```bash
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git commit -m "Thêm ghi chú học Git"
[main a6de119] Thêm ghi chú học Git
 1 file changed, 3 insertions(+)
 create mode 100644 bai-07-git/ghi-chu.md
```

Giờ sửa dòng cuối thành `- git status: xem trạng thái trước và sau mỗi lệnh` và thêm dòng `- git add: chọn thay đổi đưa vào commit`. Lưu file rồi xem Git thấy gì:

```bash
PS D:\AnhTester\js-ts-for-tester> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   bai-07-git/ghi-chu.md

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\AnhTester\js-ts-for-tester> git diff
diff --git a/bai-07-git/ghi-chu.md b/bai-07-git/ghi-chu.md
index 7c05e77..b122ec8 100644
--- a/bai-07-git/ghi-chu.md
+++ b/bai-07-git/ghi-chu.md
@@ -1,3 +1,4 @@
 # Ghi chú học Git

-- git status: xem trạng thái
+- git status: xem trạng thái trước và sau mỗi lệnh
+- git add: chọn thay đổi đưa vào commit
```

Cách đọc `git diff`: dòng bắt đầu bằng `-` là nội dung **cũ** bị bỏ, dòng bắt đầu bằng `+` là nội dung **mới**, dòng không có dấu là phần giữ nguyên. `git diff` chỉ hiện thay đổi **chưa add**; đã add rồi thì xem bằng `git diff --staged`.

```bash
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git commit -m "Bổ sung ghi chú về git status và git add"
[main 287cb89] Bổ sung ghi chú về git status và git add
 1 file changed, 2 insertions(+), 1 deletion(-)
PS D:\AnhTester\js-ts-for-tester> git log --oneline
287cb89 Bổ sung ghi chú về git status và git add
a6de119 Thêm ghi chú học Git
75f2b27 Khởi tạo project js-ts-for-tester: code 6 bài đầu
```

`git log --oneline` in lịch sử, mỗi commit một dòng, mới nhất ở trên.

### 🔆 4. git restore: bỏ thay đổi chưa commit

Giả sử bạn lỡ xoá hết nội dung `ghi-chu.md` và đã lưu file:

```bash
PS D:\AnhTester\js-ts-for-tester> git status --short
 M bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git restore bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git status
On branch main
nothing to commit, working tree clean
```

`git restore <file>` đưa file về đúng nội dung của commit gần nhất. Phần sửa chưa commit **mất hẳn, không lấy lại được**, nên luôn ghi rõ tên file, không gõ `git restore .` khi chưa xem `git diff`.

### 🔆 5. Commit message: viết cho người đọc sau này

<table class="rt-table">
<thead>
<tr>
<th>Không nên</th>
<th>Nên</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>update</code>, <code>fix</code>, <code>abc</code></td>
<td>Sửa locator nút Login sau khi CRM đổi giao diện</td>
<td>Đọc lịch sử là biết commit làm gì</td>
</tr>
<tr>
<td>Sửa nhiều thứ</td>
<td>Thêm data test cho vai trò Customer</td>
<td>Một commit làm <strong>một việc</strong>, dễ tìm và dễ gỡ</td>
</tr>
</tbody>
</table>

## ✅ Phần 5: Đưa code lên GitHub

### 🔆 1. Tạo repository trên GitHub

Chưa có tài khoản thì [đăng ký](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github) tại github.com. Sau đó (theo [tài liệu GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)):

1. Bấm dấu **+** ở góc trên bên phải, chọn **New repository**.
2. **Repository name:** `js-ts-for-tester`.
3. Chọn **Private**. Repo Public thì ai cũng xem được, trong khi code test thường có URL nội bộ và data test.
4. **Không** thêm README, `.gitignore` hay license: máy bạn đã có sẵn code, thêm ở đây dễ gây xung đột ngay lần push đầu.
5. Bấm **Create repository**.

### 🔆 2. Nối repo ở máy với GitHub và push

GitHub hiện địa chỉ repo dạng `https://github.com/<ten-ban>/js-ts-for-tester.git`. Khai báo nó làm remote tên `origin` rồi đẩy nhánh `main` lên:

```bash
PS D:\AnhTester\js-ts-for-tester> git remote add origin https://github.com/<ten-ban>/js-ts-for-tester.git
PS D:\AnhTester\js-ts-for-tester> git remote -v
origin  https://github.com/<ten-ban>/js-ts-for-tester.git (fetch)
origin  https://github.com/<ten-ban>/js-ts-for-tester.git (push)
PS D:\AnhTester\js-ts-for-tester> git push -u origin main
To https://github.com/<ten-ban>/js-ts-for-tester.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS D:\AnhTester\js-ts-for-tester> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

`-u` chỉ cần ở **lần push đầu** của mỗi nhánh: nó nối `main` ở máy với `main` trên `origin`. Từ đó chỉ cần gõ `git push`. Tải lại trang repo trên GitHub: code đã ở đó, và **không có** `.env`, `node_modules`.

### 🔆 3. Đăng nhập khi push

Lần push đầu tiên Git cần biết bạn là ai trên GitHub. GitHub [đã bỏ cách xác thực bằng mật khẩu tài khoản](https://docs.github.com/en/get-started/git-basics/about-remote-repositories#cloning-with-https-urls) cho Git. Hai cách đăng nhập được khuyên dùng ([tài liệu](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)):

- **Windows:** Git for Windows có sẵn **Git Credential Manager**. Nó mở một cửa sổ trình duyệt để bạn đăng nhập GitHub, rồi tự lưu lại. Các lần sau không hỏi nữa.
- **macOS (hoặc Windows):** cài [GitHub CLI](https://cli.github.com/), chạy `gh auth login`, chọn giao thức `HTTPS`.

Còn một cách nữa là [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), bài này không dùng.

> 🔒 Không dán mật khẩu hay token vào lệnh, vào địa chỉ remote, vào khung chat AI. Đăng nhập chỉ diễn ra ở cửa sổ trình duyệt của GitHub.

### 🔆 4. git clone và git pull

`git clone` tải cả repo (code và lịch sử) về một máy khác. Clone xong phải chạy `npm install` và tự tạo lại file `.env`, vì hai thứ đó không có trên GitHub:

```bash
PS D:\MayKhac> git clone https://github.com/<ten-ban>/js-ts-for-tester.git
Cloning into 'js-ts-for-tester'...
```

Từ bản clone đó, Anh Tester thêm một dòng vào `ghi-chu.md`, commit rồi push. Lúc này GitHub có commit mà máy chính chưa có. `git pull` lấy nó về:

```bash
PS D:\AnhTester\js-ts-for-tester> git pull
From https://github.com/<ten-ban>/js-ts-for-tester
   287cb89..5332052  main       -> origin/main
Updating 287cb89..5332052
Fast-forward
 bai-07-git/ghi-chu.md | 1 +
 1 file changed, 1 insertion(+)
```

Làm nhóm, hoặc học trên hai máy, thì **pull trước khi bắt đầu sửa**.

## ✅ Phần 6: Branch, Pull Request và Merge Conflict

### 🔆 1. Branch: sửa code mà không đụng tới main

Muốn thử sửa một hợp đồng, bạn photo ra một bản, sửa trên bản photo, ổn mới chép vào bản chính. **Branch** là bản photo đó. Nhánh `main` luôn giữ code chạy được; mỗi việc mới làm trên một nhánh riêng. Trước hết tạo file `bai-07-git/xung-dot.js` trên `main` và commit với ghi chú "Thêm file xung-dot.js in ra URL trang đăng nhập":

```javascript
const baseUrl = 'https://crm.anhtester.com';
const loginPath = '/admin/authentication';

console.log(`Mở trang: ${baseUrl}${loginPath}`);
```

Tạo nhánh mới và chuyển sang nó bằng `git switch -c`:

```bash
PS D:\AnhTester\js-ts-for-tester> git switch -c feature/them-timeout
Switched to a new branch 'feature/them-timeout'
PS D:\AnhTester\js-ts-for-tester> git branch
* feature/them-timeout
  main
```

Dấu `*` là nhánh đang đứng. Trên nhánh này, thêm dòng `const timeout = 30000;` dưới `loginPath` và dòng `` console.log(`Thời gian chờ tối đa: ${timeout} ms`); `` ở cuối file, rồi commit và push nhánh:

```bash
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/xung-dot.js
PS D:\AnhTester\js-ts-for-tester> git commit -m "Thêm biến timeout cho trang đăng nhập"
[feature/them-timeout b0250ff] Thêm biến timeout cho trang đăng nhập
 1 file changed, 2 insertions(+)
PS D:\AnhTester\js-ts-for-tester> git push -u origin feature/them-timeout
To https://github.com/<ten-ban>/js-ts-for-tester.git
 * [new branch]      feature/them-timeout -> feature/them-timeout
branch 'feature/them-timeout' set up to track 'origin/feature/them-timeout'.
```

Chuyển về `main`: file trở lại bản chưa có `timeout`. Gộp nhánh vào bằng `git merge`:

```bash
PS D:\AnhTester\js-ts-for-tester> git switch main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
PS D:\AnhTester\js-ts-for-tester> git merge feature/them-timeout
Updating 9dbe8f8..b0250ff
Fast-forward
 bai-07-git/xung-dot.js | 2 ++
 1 file changed, 2 insertions(+)
PS D:\AnhTester\js-ts-for-tester> git branch -d feature/them-timeout
Deleted branch feature/them-timeout (was b0250ff).
PS D:\AnhTester\js-ts-for-tester> git push
To https://github.com/<ten-ban>/js-ts-for-tester.git
   5332052..b0250ff  main -> main
```

`git merge <nhánh>` gộp nhánh đó **vào nhánh đang đứng**, nên phải `switch` về `main` trước. Gộp xong thì xoá nhánh bằng `git branch -d`.

> 💡 Tài liệu cũ và AI hay viết `git checkout -b <nhánh>`, `git checkout -- <file>`. Vẫn chạy được, nhưng Git đã tách lệnh đó thành [git switch](https://git-scm.com/docs/git-switch) (đổi nhánh) và [git restore](https://git-scm.com/docs/git-restore) (khôi phục file).

### 🔆 2. Pull Request: nhờ người khác duyệt trước khi gộp

Làm nhóm thì không ai tự merge vào `main` ở máy mình. Bạn push nhánh lên rồi mở **Pull Request (PR)**: một trang trên GitHub hiện toàn bộ `diff` của nhánh, để người khác đọc, góp ý và duyệt. Các bước ([tài liệu GitHub](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)):

1. `git push -u origin <nhánh>`.
2. Mở trang repo, bấm **Compare & pull request** trên dải thông báo màu vàng.
3. Kiểm tra **base** là `main`, **compare** là nhánh của bạn. Viết tiêu đề và mô tả: sửa gì, vì sao, đã chạy thử thế nào.
4. Bấm **Create pull request**. Người duyệt đọc diff, góp ý; bạn sửa, commit, push tiếp lên cùng nhánh, PR tự cập nhật.
5. Được duyệt thì bấm **Merge pull request**. Về máy: `git switch main` rồi `git pull`.

### 🔆 3. Merge conflict: hai nhánh sửa cùng một dòng

Hai người cùng sửa một câu trong bản hợp đồng, mỗi người một ý. Git cũng vậy: hai nhánh sửa **cùng một dòng** thì Git dừng lại, gọi là **merge conflict**. Dựng lại tình huống đó: trên nhánh `feature/doi-base-url`, bạn chuyển `/admin` từ `loginPath` sang `baseUrl`:

```bash
PS D:\AnhTester\js-ts-for-tester> git switch -c feature/doi-base-url
Switched to a new branch 'feature/doi-base-url'
```

```javascript
const baseUrl = 'https://crm.anhtester.com/admin';
const loginPath = '/authentication';
```

```bash
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/xung-dot.js
PS D:\AnhTester\js-ts-for-tester> git commit -m "Đưa /admin vào baseUrl"
[feature/doi-base-url d08eddc] Đưa /admin vào baseUrl
 1 file changed, 2 insertions(+), 2 deletions(-)
PS D:\AnhTester\js-ts-for-tester> git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

Trong lúc đó, trên `main` có người (bạn đóng luôn vai này) đổi **cũng dòng đó** sang môi trường dev, `const baseUrl = 'http://localhost:8080';`, rồi commit. Giờ gộp nhánh:

```bash
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/xung-dot.js
PS D:\AnhTester\js-ts-for-tester> git commit -m "Đổi baseUrl sang môi trường dev"
[main 39d326f] Đổi baseUrl sang môi trường dev
 1 file changed, 1 insertion(+), 1 deletion(-)
PS D:\AnhTester\js-ts-for-tester> git merge feature/doi-base-url
Auto-merging bai-07-git/xung-dot.js
CONFLICT (content): Merge conflict in bai-07-git/xung-dot.js
Automatic merge failed; fix conflicts and then commit the result.
```

Conflict không làm mất code. Git đánh dấu chỗ xung đột ngay trong file `bai-07-git/xung-dot.js`:

```javascript
<<<<<<< HEAD
const baseUrl = 'http://localhost:8080';
const loginPath = '/admin/authentication';
=======
const baseUrl = 'https://crm.anhtester.com/admin';
const loginPath = '/authentication';
>>>>>>> feature/doi-base-url
const timeout = 30000;

console.log(`Mở trang: ${baseUrl}${loginPath}`);
console.log(`Thời gian chờ tối đa: ${timeout} ms`);
```

<table class="rt-table">
<thead>
<tr>
<th>Đoạn</th>
<th>Nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td>Từ <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code> tới <code>=======</code></td>
<td>Bản của nhánh đang đứng (<code>main</code>)</td>
</tr>
<tr>
<td>Từ <code>=======</code> tới <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature/doi-base-url</code></td>
<td>Bản của nhánh đang gộp vào</td>
</tr>
<tr>
<td>Các dòng bên ngoài</td>
<td>Không xung đột, Git đã tự gộp</td>
</tr>
</tbody>
</table>

### 🔆 4. Sửa conflict: quyết định nội dung, add, commit

Bạn phải **hiểu ý của cả hai bên** rồi viết lại đoạn đó. Ở đây cần cả hai: chạy trên `localhost` (ý của `main`) và `/admin` nằm trong `baseUrl` (ý của nhánh). Xoá cả ba dòng đánh dấu, sửa hai dòng đầu file thành:

```javascript
const baseUrl = 'http://localhost:8080/admin';
const loginPath = '/authentication';
```

Chạy thử file trước, rồi mới `add` và `commit` để kết thúc lần gộp:

```bash
PS D:\AnhTester\js-ts-for-tester> node bai-07-git/xung-dot.js
Mở trang: http://localhost:8080/admin/authentication
Thời gian chờ tối đa: 30000 ms
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/xung-dot.js
PS D:\AnhTester\js-ts-for-tester> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   bai-07-git/xung-dot.js

PS D:\AnhTester\js-ts-for-tester> git commit -m "Gộp feature/doi-base-url: giữ localhost, thêm /admin vào baseUrl"
[main 4e1cb03] Gộp feature/doi-base-url: giữ localhost, thêm /admin vào baseUrl
PS D:\AnhTester\js-ts-for-tester> git log --oneline --graph -5
*   4e1cb03 Gộp feature/doi-base-url: giữ localhost, thêm /admin vào baseUrl
|\
| * d08eddc Đưa /admin vào baseUrl
* | 39d326f Đổi baseUrl sang môi trường dev
|/
* b0250ff Thêm biến timeout cho trang đăng nhập
* 9dbe8f8 Thêm file xung-dot.js in ra URL trang đăng nhập
```

`--graph` vẽ hai nhánh tách ra rồi nhập lại. Ba điều cần nhớ:

- Chưa biết sửa thế nào thì `git merge --abort` để quay về trạng thái trước khi gộp.
- Còn sót dấu `<<<<<<<` mà vẫn commit thì file hỏng: Node.js dừng ngay với `SyntaxError: Unexpected token '<<'`. Soát bằng `git diff --check`, lệnh này in `leftover conflict marker` kèm số dòng còn sót.
- VS Code hiện sẵn các nút **Accept Current Change**, **Accept Incoming Change**, **Accept Both Changes** phía trên đoạn xung đột ([tài liệu VS Code](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts)). Trường hợp trên phải trộn hai bản nên vẫn cần sửa tay.

## ✅ Phần 7: Thực hành - quy trình mỗi lần ngồi vào làm bài

Từ giờ, mỗi lần thêm code vào project bạn lặp lại đúng chuỗi sau. Lần này việc cần làm là thêm dòng `- git switch -c: tạo branch mới trước khi sửa code` vào `bai-07-git/ghi-chu.md`:

```bash
PS D:\AnhTester\js-ts-for-tester> git pull
Already up to date.
PS D:\AnhTester\js-ts-for-tester> git switch -c bai-tap/ghi-chu-branch
Switched to a new branch 'bai-tap/ghi-chu-branch'
PS D:\AnhTester\js-ts-for-tester> git status --short
 M bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git diff --stat
 bai-07-git/ghi-chu.md | 1 +
 1 file changed, 1 insertion(+)
PS D:\AnhTester\js-ts-for-tester> git add bai-07-git/ghi-chu.md
PS D:\AnhTester\js-ts-for-tester> git commit -m "Ghi chú thêm lệnh git switch -c"
[bai-tap/ghi-chu-branch 7d94851] Ghi chú thêm lệnh git switch -c
 1 file changed, 1 insertion(+)
PS D:\AnhTester\js-ts-for-tester> git push -u origin bai-tap/ghi-chu-branch
To https://github.com/<ten-ban>/js-ts-for-tester.git
 * [new branch]      bai-tap/ghi-chu-branch -> bai-tap/ghi-chu-branch
branch 'bai-tap/ghi-chu-branch' set up to track 'origin/bai-tap/ghi-chu-branch'.
PS D:\AnhTester\js-ts-for-tester> git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS D:\AnhTester\js-ts-for-tester> git merge bai-tap/ghi-chu-branch
Updating 4e1cb03..7d94851
Fast-forward
 bai-07-git/ghi-chu.md | 1 +
 1 file changed, 1 insertion(+)
PS D:\AnhTester\js-ts-for-tester> git push
To https://github.com/<ten-ban>/js-ts-for-tester.git
   4e1cb03..7d94851  main -> main
```

Thứ tự: **pull → tạo nhánh → sửa → status, diff → add → commit → push → gộp**. Làm nhóm thì hai lệnh `merge`, `push` cuối được thay bằng mở Pull Request trên GitHub.

## ✅ Phần 8: Dùng Claude Code và bộ kit claude-testing-skills để soạn lệnh Git và hỏi sâu

### 🔆 1. Nguyên tắc: AI đề xuất, bạn đọc hiểu rồi mới chạy

Claude Code chạy được lệnh Git ngay trong project và tạo được cả Pull Request ([tài liệu](https://code.claude.com/docs/en/common-workflows#create-pull-requests)). Ở chế độ mặc định nó [hỏi bạn trước khi chạy](https://code.claude.com/docs/en/permissions) lệnh, trừ nhóm lệnh chỉ đọc. Đọc lệnh xong mới đồng ý. Ba lệnh **phá dữ liệu không lấy lại được**, AI đề xuất thì phải hỏi lại cho rõ: `git reset --hard` (xoá mọi thay đổi chưa commit), `git push --force` (ghi đè lịch sử trên GitHub), `git clean -fd` (xoá mọi file chưa được theo dõi).

Muốn Claude Code không bao giờ tự push, thêm luật cấm vào `.claude/settings.json` của project (ví dụ lấy từ tài liệu trên):

```json
{
  "permissions": {
    "deny": ["Bash(git push *)"]
  }
}
```

### 🔆 2. Prompt mẫu

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) dùng được cả bốn prompt dưới đây: dán kết quả lệnh vào khung chat. Trước khi dán `git diff`, đọc lại xem trong đó có mật khẩu hay nội dung `.env` không.

```markdown
Dưới đây là kết quả lệnh git diff --staged của tôi. Hãy viết 1 commit message tiếng Việt:
- dòng đầu tối đa 70 ký tự, nói rõ thay đổi gì và ở đâu, không dùng từ chung chung như "update", "fix";
- nếu diff đang làm nhiều việc không liên quan, đề xuất tách thành mấy commit và file nào vào commit nào.
Chỉ dựa vào diff, không suy đoán thêm.

[dán kết quả git diff --staged vào đây]
```

```markdown
Tôi mới học Git. Trước khi tôi chạy, hãy giải thích lệnh sau:

git reset --hard HEAD~1

1. Lệnh thay đổi gì ở: file trên máy, lịch sử commit ở máy, repo trên GitHub?
2. Có làm mất dữ liệu không lấy lại được không? Mất cái gì?
3. Tôi nên chạy lệnh nào trước để kiểm tra trạng thái hiện tại?
4. Có cách nào an toàn hơn để đạt cùng mục đích không?
Dẫn link trang git-scm.com của lệnh này.
```

```markdown
File bai-07-git/xung-dot.js của tôi bị merge conflict khi gộp nhánh feature/doi-base-url vào main:

[dán đoạn từ dòng <<<<<<< tới dòng >>>>>>> vào đây]

Tôi muốn giữ địa chỉ localhost của main, và giữ việc đưa /admin vào baseUrl của nhánh feature.
1. Giải thích mỗi bên đã sửa gì.
2. Đưa đoạn code sau khi gộp, không còn dòng đánh dấu nào.
3. Liệt kê các lệnh tôi cần chạy tiếp để kết thúc lần merge. KHÔNG tự chạy lệnh nào.
```

```markdown
Viết file .gitignore cho project Node.js dùng Playwright Test, có file .env chứa tài khoản test.
Mỗi nhóm dòng kèm 1 comment ngắn giải thích vì sao bỏ qua.
Sau đó chỉ cho tôi lệnh kiểm tra một file cụ thể có đang bị bỏ qua hay không,
và việc phải làm nếu file .env đã lỡ được commit từ trước.
```

### 🔆 3. Bộ kit quy định gì về Git?

File [CLAUDE.md](https://github.com/anhtester/claude-testing-skills/blob/main/CLAUDE.md) của bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills) có sẵn ba quy định khớp với bài này:

- Mục **Git Pull Restriction Rule**: Claude không được tự chạy lệnh Git làm thay đổi code (`git pull`, `git checkout`, `git merge`, `git rebase`, `git reset`); chỉ được dùng lệnh chỉ đọc `git status`, `git diff`, `git log`.
- File `.env` không được commit, đã nằm trong [.gitignore](https://github.com/anhtester/claude-testing-skills/blob/main/.gitignore) của kit; và "chỉ commit khi test PASS ổn định".
- Rule [reporting\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/reporting_rules.md): `.gitignore` phải có dòng `reports/`, không commit kết quả chạy test lên repo.

## ✅ Phần 9: Kiểm tra lệnh Git do AI sinh ra

Rà lệnh AI đề xuất theo bảng sau trước khi chạy:

<table class="rt-table">
<thead>
<tr>
<th>Dấu hiệu</th>
<th>Vì sao là vấn đề</th>
<th>Cách xử lý</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>git add .</code> khi chưa có <code>.gitignore</code></td>
<td>Đưa cả <code>node_modules</code> và <code>.env</code> vào commit</td>
<td>Viết <code>.gitignore</code> trước, đọc <code>git status</code> rồi mới add</td>
</tr>
<tr>
<td><code>git push --force</code> lên <code>main</code></td>
<td>Ghi đè lịch sử chung, mất commit của người khác</td>
<td>Không chạy. <code>git pull</code> trước, xử lý conflict rồi push thường</td>
</tr>
<tr>
<td><code>git reset --hard</code> để "làm sạch"</td>
<td>Mất mọi thay đổi chưa commit, không lấy lại được</td>
<td>Xem <code>git status</code>, <code>git diff</code>; bỏ từng file bằng <code>git restore</code></td>
</tr>
<tr>
<td>Commit message <code>update</code>, <code>fix</code></td>
<td>Lịch sử không cho biết đã sửa gì</td>
<td>Viết lại: sửa gì, ở đâu</td>
</tr>
<tr>
<td>Commit thẳng lên <code>main</code> khi làm nhóm</td>
<td>Code chưa ai duyệt đã vào nhánh chính</td>
<td><code>git switch -c</code> tạo nhánh, mở Pull Request</td>
</tr>
<tr>
<td>Remote dạng <code>https://user:token@github.com/...</code></td>
<td>Token nằm trong cấu hình repo và lịch sử lệnh, dễ lộ</td>
<td>Dùng địa chỉ không kèm token; đăng nhập qua Git Credential Manager hoặc <code>gh auth login</code></td>
</tr>
<tr>
<td>Dùng <code>master</code> khi repo là <code>main</code></td>
<td><code>git push -u origin master</code> dừng với <code><span>error:</span> <span>src</span> <span>refspec</span> <span>master</span> does not match any</code></td>
<td>Xem tên nhánh bằng <code>git branch</code>, sửa lại lệnh</td>
</tr>
<tr>
<td>Sửa conflict xong vẫn còn dấu <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code></td>
<td>File hỏng cú pháp, test không chạy</td>
<td><code>git diff --check</code> và chạy thử file trước khi commit</td>
</tr>
</tbody>
</table>

## ✅ Phần 10: Bài tập thực hành

**Bài tập 1 - Đưa project lên GitHub.** Làm lại Phần 2 tới Phần 5 trên máy bạn: tạo repo **Private** tên `js-ts-for-tester`, push nhánh `main`. Kết quả đúng: trang repo **không có** `.env` và `node_modules`.

**Bài tập 2 - Branch và Pull Request.** Tạo nhánh `bai-tap/lenh-git`, thêm file `bai-07-git/bt2-lenh-git.md` ghi 5 lệnh bạn dùng nhiều nhất kèm một dòng giải thích. Commit, push nhánh, mở Pull Request, đọc tab hiện diff rồi merge. Về máy `git switch main` rồi `git pull`.

**Bài tập 3 - Tự tạo và sửa conflict.** Tạo file `bai-07-git/bt3-config.js` có dòng `const timeout = 30000;` và commit trên `main`. Trên nhánh `bai-tap/timeout-60` đổi thành `60000`; quay về `main` đổi thành `45000`; commit cả hai bên rồi merge. Sửa conflict để giữ `60000`, kiểm bằng `git diff --check`.

**Bài tập 4 - Duyệt lệnh AI.** Một bạn nhờ AI đưa project lên GitHub và nhận được chuỗi lệnh dưới đây (project chưa có `.gitignore`). Có 5 chỗ cần sửa. Tìm đủ, nêu lý do theo bảng ở Phần 9 và viết lại chuỗi lệnh đúng. **Không chạy** chuỗi lệnh này.

```bash
git init
git add .
git commit -m "update"
git remote add origin https://<ten-ban>:<TOKEN_CUA_BAN>@github.com/<ten-ban>/js-ts-for-tester.git
git push -u origin master
git push --force
```

## ✅ Phần 11: Ghi nhớ nhanh

- Git lưu lịch sử code trên máy; GitHub giữ bản sao trên mạng. Một project là một repository, `git init` một lần.
- `.gitignore` phải có **trước commit đầu tiên**: `node_modules/`, `.env`, `test-results/`, `playwright-report/`. Lỡ commit `.env`: `git rm --cached .env` và **đổi mật khẩu**, vì lịch sử vẫn còn.
- Lưu thay đổi: `git add <file>` → `git commit -m "sửa gì, ở đâu"`. Luôn `git status` trước và sau. Bỏ thay đổi chưa commit: `git restore <file>`.
- Với GitHub: `git push -u origin main` lần đầu, sau đó `git push`; `git pull` trước khi sửa; `git clone` để lấy về máy khác.
- Việc mới làm trên nhánh riêng: `git switch -c <nhánh>`, xong thì Pull Request hoặc `git merge`.
- Conflict: đọc hai bản giữa `<<<<<<<`, `=======`, `>>>>>>>`, viết lại, xoá dấu, chạy thử, `add`, `commit`.
- AI đề xuất lệnh, bạn đọc hiểu rồi mới chạy. `reset --hard`, `push --force`, `clean -fd` phải hỏi kỹ.

✅ **Kết luận:** Project `js-ts-for-tester` đã có lịch sử và có bản sao trên GitHub. Từ giờ, học xong mỗi bài bạn commit và push code của bài đó. Bài kế tiếp, **Class, constructor và kế thừa (extends) trong JavaScript**, bắt đầu tổ chức code thành class, bước đầu của Page Object Model, và bạn sẽ lưu nó bằng chính quy trình ở Phần 7.

---

## Bài tập riêng — Đưa project lên GitHub, branch, Pull Request và sửa conflict

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-97](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-97)

**Mục tiêu:** tự đưa project js-ts-for-tester lên GitHub, làm việc với nhánh, Pull Request và tự sửa được merge conflict. Từ bài này trở đi, mọi bài tập đều nộp bằng link GitHub.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-07-git`

### 📝 Đề bài

#### Bài tập 1 - Đưa project lên GitHub

Làm lại Phần 2 tới Phần 5 của bài học trên máy bạn: tạo repo **Private** tên `js-ts-for-tester`, push nhánh `main`. Trang repo trên GitHub **không được có** `.env` và `node_modules`.

#### Bài tập 2 - Branch và Pull Request

Tạo nhánh `bai-tap/lenh-git`, thêm file `bai-07-git/bt2-lenh-git.md` ghi 5 lệnh Git bạn dùng nhiều nhất kèm một dòng giải thích. Commit, push nhánh, mở Pull Request, đọc tab hiện diff rồi merge. Về máy chạy:

```bash
git switch main
git pull
```

#### Bài tập 3 - Tự tạo và sửa conflict

Tạo file `bai-07-git/bt3-config.js` có dòng `const timeout = 30000;` và commit trên `main`. Trên nhánh `bai-tap/timeout-60` đổi thành 60000; quay về `main` đổi thành 45000; commit cả hai bên rồi merge. Sửa conflict để giữ **60000**, kiểm bằng `git diff --check`.

#### Bài tập 4 - Duyệt lệnh AI

Một bạn nhờ AI đưa project lên GitHub và nhận được chuỗi lệnh dưới đây (project chưa có .gitignore). Có **5 chỗ cần sửa**. Tìm đủ, nêu lý do theo bảng ở Phần 9 và viết lại chuỗi lệnh đúng. **Không chạy** chuỗi lệnh này.

```bash
git init
git add .
git commit -m "update"
git remote add origin https://<ten-ban>:<TOKEN_CUA_BAN>@github.com/<ten-ban>/js-ts-for-tester.git
git push -u origin master
git push --force
```

### 📦 Cách nộp bài

1. Làm bài trong thư mục `bai-07-git/` của repo `js-ts-for-tester`, commit và push lên nhánh `main`.
2. Dán link thư mục bài trên GitHub vào ô **Link GitHub**, dạng `https://github.com/<ten-ban>/js-ts-for-tester/tree/main/bai-07-git`. Repo Private thì vào **Settings → Collaborators** thêm tài khoản GitHub của giảng viên, nếu không giảng viên không mở được.
3. Trong ô **Nội dung bài làm (Editor)**, dán **kết quả chạy thật** của từng file (mỗi file một **Đoạn code mẫu** chọn Text / Log) và phần trả lời các câu hỏi.
4. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*.
5. Dán thêm link Pull Request của Bài tập 2 (dạng `https://github.com/<ten-ban>/js-ts-for-tester/pull/1`) vào ô **Ghi chú**.
6. Trong Editor, dán kết quả `git log --oneline --graph -10` sau khi sửa xong conflict (chọn Bash / Shell).

### ✅ Tiêu chí Đạt

- Mở được repo bằng link đã nộp (đã thêm giảng viên làm collaborator nếu repo Private); không có `.env`, `node_modules`; có `.gitignore`.
- Có Pull Request từ `bai-tap/lenh-git` đã **Merged**; file `bt2-lenh-git.md` có 5 lệnh kèm giải thích.
- `bt3-config.js` trên `main` là `const timeout = 60000;`, không còn dấu `<<<<<<<`/`=======`/`>>>>>>>`; `git log --graph` có commit merge.
- Bài tập 4 đủ 5 chỗ: thiếu `.gitignore` trước `git add .`; commit message không nói gì; lộ token trong URL remote; đẩy `master` trong khi nhánh là `main`; `--force` ghi đè lịch sử.
- Commit message của bạn mô tả rõ thay đổi (không dùng "update", "fix" trống trơn).

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.