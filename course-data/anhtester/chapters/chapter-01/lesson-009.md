# Bài 9 - [Javascript Typescript] async/await, import/export và try...catch trong JavaScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/407](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/407)

✅ Vì sao JavaScript cần bất đồng bộ và Promise ở mức đủ dùng  
✅ async/await - cách viết bất đồng bộ dễ đọc và lỗi quên await  
✅ Chờ nhiều việc với for...of, forEach và Promise.all  
✅ Chia code thành module với export và import  
✅ Bắt lỗi với try...catch, throw new Error() và không nuốt lỗi  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra code bất đồng bộ do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước bạn đã viết `BasePage` và `LoginPage` chạy với `fakePage`, tất cả trong một file và mọi method chạy xong ngay. Project Playwright thật khác ở ba điểm: thao tác với trình duyệt **tốn thời gian** nên phải `await`; mỗi class nằm ở **một file riêng** nên phải `export`, `import`; thao tác có thể **thất bại** nên phải biết lỗi đi đâu. Học xong bạn sẽ:

- Hiểu vì sao JavaScript có bất đồng bộ, Promise là gì ở mức đủ dùng.
- Viết và đọc được `async`/`await`; nhận ra ngay chỗ **thiếu `await`**.
- Biết vì sao `forEach` không chờ `await` và khi nào dùng `Promise.all`.
- Chia code thành nhiều file bằng `export` và `import`, phân biệt named và default.
- Dùng `try...catch...finally`, `throw new Error()` và không **nuốt lỗi**.

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật (Node.js v24.17.0), đã lược các dòng `at ...` ở kết quả có lỗi; đường dẫn trong thông báo lỗi ghi theo thư mục project.

## ✅ Phần 1: Vì sao JavaScript cần bất đồng bộ - Promise

### 🔆 1. Chuẩn bị thư mục cho bài học

Tạo thư mục `bai-09-async-module` trong project. Cuối bài, thư mục sẽ như sau (file `package.json` con và hai thư mục `pages/`, `utils/` tạo ở Phần 4):

```bash
js-ts-for-tester/
├── package.json
└── bai-09-async-module/
    ├── package.json
    ├── pages/
    │   ├── BasePage.js
    │   └── LoginPage.js
    ├── utils/
    │   ├── url.js
    │   ├── delay.js
    │   ├── fakePage.js
    │   └── checkLoginPage.js
    ├── 01-goi-mon.js
    ├── 02-promise.js
    ├── 03-then-catch.js
    ├── 04-async-await.js
    ├── 05-quen-await.js
    ├── 06-await-ngoai-async.js
    ├── 07-fetch-crm.js
    ├── 08-for-of-tuan-tu.js
    ├── 09-foreach-khong-cho.js
    ├── 10-promise-all.js
    ├── 11-dung-module.js
    ├── 12-dung-class.js
    ├── 13-thieu-duoi-js.js
    ├── 14-nham-ngoac.js
    ├── 15-try-catch.js
    ├── 16-throw-error.js
    ├── 17-bat-loi-await.js
    ├── 18-nuot-loi.js
    ├── 19-thu-lai.js
    └── crm-login-flow.js
```

### 🔆 2. Gọi món ở quán: không ai đứng chặn quầy

Ở quán ăn đông khách, bạn gọi món, nhận **phiếu chờ** rồi về bàn. Bạn không đứng chặn quầy cho tới khi món ra. JavaScript làm đúng kiểu đó với việc **tốn thời gian** (mở trang web, gọi API, đọc file): giao việc đi, chạy tiếp các dòng bên dưới, có kết quả thì quay lại xử lý. Cách làm này gọi là **bất đồng bộ** (asynchronous).

Tạo file `bai-09-async-module/01-goi-mon.js`, dùng lại `setTimeout` của bài Hàm:

```javascript
console.log('1. Gọi món ở quầy, nhận phiếu chờ');

// Bếp cần 2 giây để làm món. JavaScript KHÔNG đứng chờ ở dòng này
setTimeout(() => {
  console.log('3. Món ra sau 2 giây');
}, 2000);

console.log('2. Về bàn ngồi, làm việc khác');
```

```bash
node bai-09-async-module/01-goi-mon.js
```

Kết quả:

```bash
1. Gọi món ở quầy, nhận phiếu chờ
2. Về bàn ngồi, làm việc khác
3. Món ra sau 2 giây
```

Dòng `2.` viết **sau** `setTimeout` nhưng in ra **trước** dòng `3.`. Với automation đây là chỗ nguy hiểm: lệnh mở trang chưa xong mà dòng kiểm tra tiêu đề đã chạy thì test sai.

### 🔆 3. Promise - tấm phiếu chờ

**Promise** là tấm phiếu chờ đó: một Object đại diện cho **kết quả sẽ có trong tương lai**. Hàm nào làm việc tốn thời gian thì trả về ngay một Promise, kết quả thật đến sau. Tạo file `bai-09-async-module/02-promise.js`:

```javascript
// delay(ms) trả về một Promise: sau ms mili giây thì hoàn thành
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const phieuCho = delay(1000);
console.log('Vừa gọi xong :', phieuCho);

setTimeout(() => {
  console.log('Sau 1,5 giây :', phieuCho);
}, 1500);
```

```bash
node bai-09-async-module/02-promise.js
```

Kết quả:

```bash
Vừa gọi xong : Promise { <pending> }
Sau 1,5 giây : Promise { undefined }
```

Lúc vừa gọi, phiếu ở trạng thái `<pending>` (đang chờ). Sau 1 giây, hàm `resolve` được gọi và phiếu chuyển sang hoàn thành; `undefined` là giá trị kết quả, vì `delay` không trả về gì. Một Promise luôn ở một trong ba trạng thái:

<table class="rt-table">
<thead>
<tr>
<th>Trạng thái</th>
<th>Ý nghĩa</th>
<th>Ở quán ăn</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pending</code></td>
<td>Đang chờ, chưa có kết quả</td>
<td>Cầm phiếu, bếp đang làm</td>
</tr>
<tr>
<td><code>fulfilled</code></td>
<td>Thành công, có giá trị kết quả</td>
<td>Món ra</td>
</tr>
<tr>
<td><code>rejected</code></td>
<td>Thất bại, có lỗi kèm theo</td>
<td>Bếp báo hết món</td>
</tr>
</tbody>
</table>

Bạn hiếm khi tự viết `new Promise`; việc của bạn là **dùng** Promise do Playwright và Node.js trả về. Hàm `delay` chỉ để giả lập việc tốn thời gian trong bài này.

### 🔆 4. .then và .catch - đủ để đọc code cũ

Trước khi có `await`, người ta nhận kết quả của Promise bằng `.then` (khi thành công) và `.catch` (khi thất bại), mỗi cái nhận một callback. Tạo file `bai-09-async-module/03-then-catch.js`:

```javascript
function nauMon(tenMon) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (tenMon === 'phở') {
        resolve(`${tenMon} đã xong`);            // thành công, kèm kết quả
      } else {
        reject(new Error(`Hết món ${tenMon}`));  // thất bại, kèm lỗi
      }
    }, 500);
  });
}

nauMon('phở')
  .then((ketQua) => console.log('then :', ketQua))
  .catch((error) => console.log('catch:', error.message));

nauMon('bún chả')
  .then((ketQua) => console.log('then :', ketQua))
  .catch((error) => console.log('catch:', error.message));
```

```bash
node bai-09-async-module/03-then-catch.js
```

Kết quả:

```bash
then : phở đã xong
catch: Hết món bún chả
```

Gặp `.then(...)` trong code cũ, bạn đọc là "khi có kết quả thì chạy hàm này". Khoá học không viết kiểu này mà dùng `async`/`await`.

## ✅ Phần 2: async/await - đợi món ra rồi mới ăn

### 🔆 1. async function và await

`async` đặt trước hàm để báo "hàm này có việc phải đợi"; `await` đặt trước một Promise để nói "đợi phiếu này có kết quả rồi mới chạy dòng dưới". Tạo file `bai-09-async-module/04-async-await.js`:

```javascript
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Hàm giả lập việc mở trang đăng nhập, mất 1 giây
async function openLoginPage() {
  console.log('Bắt đầu mở trang...');
  await delay(1000); // đợi Promise xong rồi mới chạy dòng dưới
  console.log('Trang đã mở');
  return 'Perfex CRM | Anh Tester Demo - Login';
}

async function main() {
  const title = await openLoginPage();
  console.log('Tiêu đề:', title);
}

main();
console.log('Dòng này viết sau lời gọi main()');
```

```bash
node bai-09-async-module/04-async-await.js
```

Kết quả:

```bash
Bắt đầu mở trang...
Dòng này viết sau lời gọi main()
Trang đã mở
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
```

Ba điều rút ra từ kết quả:

- **Bên trong** hàm `async`, `await` giữ đúng thứ tự: "Trang đã mở" chỉ in sau khi đợi đủ 1 giây.
- `await` lấy luôn **giá trị** nằm trong Promise: `title` là chuỗi tiêu đề, không phải tấm phiếu.
- **Bên ngoài**, lời gọi `main()` không có `await` nên JavaScript không đợi nó: dòng cuối file in ra ngay ở vị trí thứ hai. `await` chỉ bắt **hàm đang chứa nó** đợi.

### 🔆 2. Hàm async luôn trả về Promise - lỗi quên await

Dù bạn viết `return 'chuỗi'`, hàm `async` vẫn trả về một **Promise chứa chuỗi đó**. Muốn lấy giá trị thì phải `await`. Tạo file `bai-09-async-module/05-quen-await.js`:

```javascript
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const expectedTitle = 'Perfex CRM | Anh Tester Demo - Login';

async function getTitle() {
  await delay(500);
  return 'Perfex CRM | Anh Tester Demo - Login';
}

async function main() {
  // SAI: quên await, title1 là tấm phiếu chờ chứ chưa phải tiêu đề
  const title1 = getTitle();
  console.log('Quên await:', title1);
  console.log('So sánh   :', title1 === expectedTitle);

  // ĐÚNG: có await, title2 là chuỗi tiêu đề
  const title2 = await getTitle();
  console.log('Có await  :', title2);
  console.log('So sánh   :', title2 === expectedTitle);
}

main();
```

```bash
node bai-09-async-module/05-quen-await.js
```

Kết quả:

```bash
Quên await: Promise { <pending> }
So sánh   : false
Có await  : Perfex CRM | Anh Tester Demo - Login
So sánh   : true
```

> ⚠️ Quên `await` **không báo lỗi cú pháp**, chương trình vẫn chạy. Bạn chỉ thấy hậu quả: giá trị là `Promise { <pending> }`, so sánh ra `false`, các bước chạy lộn thứ tự. Trong Playwright, `page.goto()`, `fill()`, `click()`, `page.title()`, `expect(...)` với locator đều trả về Promise, nên **thiếu một chữ `await`** là test lúc pass lúc fail. Đây là lỗi số một cần soát trong code AI viết.

### 🔆 3. await chỉ dùng được trong hàm async

Tạo file `bai-09-async-module/06-await-ngoai-async.js`:

```javascript
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// SAI: hàm thường (không có chữ async) mà dùng await
function openLoginPage() {
  await delay(1000);
  console.log('Trang đã mở');
}

openLoginPage();
```

```bash
node bai-09-async-module/06-await-ngoai-async.js
```

Kết quả:

```bash
  await delay(1000);
  ^^^^^

SyntaxError: await is only valid in async functions and the top level bodies of modules
```

Thông báo nói đúng luật: `await` chỉ hợp lệ trong hàm `async` và ở **ngoài cùng của một module** (trường hợp thứ hai bạn sẽ dùng ở Phần 4). Cách sửa: thêm `async` trước `function`. Vì vậy mọi test Playwright có chữ `async` trước `({ page }) => { ... }`.

### 🔆 4. Ví dụ thật: lấy tiêu đề trang đăng nhập CRM bằng fetch

Giờ làm một việc tốn thời gian thật: gửi yêu cầu tới trang đăng nhập Admin của CRM demo và đọc tiêu đề. Node.js có sẵn hàm [`fetch`](https://nodejs.org/api/globals.html#fetch), hàm này trả về Promise. Tạo file `bai-09-async-module/07-fetch-crm.js`, dùng lại `baseUrl`, `loginPath` và tiêu đề đã quen từ bài Biến:

```javascript
const baseUrl = 'https://crm.anhtester.com';
const loginPath = '/admin/authentication';
const expectedTitle = 'Perfex CRM | Anh Tester Demo - Login';

async function main() {
  // 1. Gửi yêu cầu lấy trang, đợi máy chủ trả lời
  const response = await fetch(`${baseUrl}${loginPath}`);
  console.log('Status :', response.status);

  // 2. Đọc nội dung HTML của trang, cũng phải đợi
  const html = await response.text();
  console.log('Kiểu   :', typeof html);

  // 3. Cắt lấy phần chữ nằm giữa <title> và </title>
  const start = html.indexOf('<title>') + '<title>'.length;
  const end = html.indexOf('</title>');
  const title = html.slice(start, end).trim();
  console.log('Tiêu đề:', title);

  console.log('Kết quả:', title === expectedTitle ? 'PASS' : 'FAIL');
}

main();
```

```bash
node bai-09-async-module/07-fetch-crm.js
```

Kết quả:

```bash
Status : 200
Kiểu   : string
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
Kết quả: PASS
```

Có **hai** chỗ phải đợi: đợi máy chủ trả lời (`fetch`), rồi đợi đọc hết nội dung (`response.text()`). `indexOf` tìm vị trí một đoạn chữ trong chuỗi, `slice` cắt lấy phần giữa hai vị trí. Chương API sẽ gặp lại hình dạng này với `await response.json()`.

> ⚠️ Đoạn code trên chỉ **đọc** một trang công khai. Không dùng `fetch` để gửi form đăng nhập hay mật khẩu lên CRM demo.

## ✅ Phần 3: Chờ nhiều việc - for...of, forEach và Promise.all

### 🔆 1. await trong for...of: chạy tuần tự

Bài vòng lặp đã cảnh báo "`forEach` không chờ `await`" mà chưa giải thích. Giờ chạy thật để thấy. Trước hết là cách đúng, file `bai-09-async-module/08-for-of-tuan-tu.js`, với 3 vai trò của CRM:

```javascript
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const users = [
  { email: 'admin@example.com', role: 'admin' },
  { email: 'projectmanager@example.com', role: 'project-manager' },
  { email: 'customer@example.com', role: 'customer' },
];

// Giả lập kiểm tra đăng nhập cho một tài khoản, mất 0,5 giây
async function checkLogin(user) {
  console.log(`Bắt đầu kiểm ${user.role}`);
  await delay(500);
  console.log(`   Kiểm xong ${user.role}`);
}

async function main() {
  for (const user of users) {
    await checkLogin(user); // xong tài khoản này mới sang tài khoản sau
  }
  console.log('Xong tất cả');
}

main();
```

```bash
node bai-09-async-module/08-for-of-tuan-tu.js
```

Kết quả:

```bash
Bắt đầu kiểm admin
   Kiểm xong admin
Bắt đầu kiểm project-manager
   Kiểm xong project-manager
Bắt đầu kiểm customer
   Kiểm xong customer
Xong tất cả
```

### 🔆 2. forEach với async: không chờ

File `bai-09-async-module/09-foreach-khong-cho.js` giống hệt file trên, chỉ khác hàm `main`:

```javascript
async function main() {
  // SAI: forEach gọi 3 hàm async rồi đi tiếp, không chờ hàm nào
  users.forEach(async (user) => {
    await checkLogin(user);
  });
  console.log('Xong tất cả');
}

main();
```

```bash
node bai-09-async-module/09-foreach-khong-cho.js
```

Kết quả:

```bash
Bắt đầu kiểm admin
Bắt đầu kiểm project-manager
Bắt đầu kiểm customer
Xong tất cả
   Kiểm xong admin
   Kiểm xong project-manager
   Kiểm xong customer
```

"Xong tất cả" in ra khi **chưa tài khoản nào kiểm xong**. Lý do: callback `async (user) => { ... }` là một hàm `async` nên nó trả về Promise, còn `forEach` thì **bỏ qua mọi giá trị callback trả về**. Chữ `await` trong callback chỉ bắt callback đó đợi. Với Playwright, hậu quả là ba tài khoản cùng thao tác trên **một** trang một lúc, và test kết thúc khi các bước còn dang dở. Quy tắc của khoá học: **có `await` trong vòng lặp thì dùng `for...of`**.

### 🔆 3. Promise.all: chạy song song khi các việc độc lập

Ba người gọi ba món, bếp làm cùng lúc thì nhanh hơn làm lần lượt. `Promise.all` nhận một **mảng Promise** và trả về một Promise hoàn thành khi **tất cả** cùng xong. Tạo file `bai-09-async-module/10-promise-all.js`:

```javascript
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function checkLogin(role) {
  await delay(500);
  return `${role}: OK`;
}

async function main() {
  // Tuần tự: xong việc này mới bắt đầu việc kia
  let start = Date.now();
  const a = await checkLogin('admin');
  const b = await checkLogin('project-manager');
  const c = await checkLogin('customer');
  console.log([a, b, c]);
  console.log(`Tuần tự  : khoảng ${Date.now() - start} ms`);

  // Song song: bắt đầu cả 3 việc, rồi đợi tất cả cùng xong
  start = Date.now();
  const results = await Promise.all([
    checkLogin('admin'),
    checkLogin('project-manager'),
    checkLogin('customer'),
  ]);
  console.log(results);
  console.log(`Song song: khoảng ${Date.now() - start} ms`);
}

main();
```

```bash
node bai-09-async-module/10-promise-all.js
```

Kết quả (số mili giây mỗi lần chạy lệch nhau một chút):

```bash
[ 'admin: OK', 'project-manager: OK', 'customer: OK' ]
Tuần tự  : khoảng 1530 ms
[ 'admin: OK', 'project-manager: OK', 'customer: OK' ]
Song song: khoảng 505 ms
```

Trong mảng truyền cho `Promise.all`, các lời gọi **không** có `await`: bạn cần chính các tấm phiếu, rồi `await` một lần cho cả mảng. Chỉ dùng khi các việc **không phụ thuộc nhau**; các bước trên cùng một trang (điền email, điền mật khẩu, bấm nút) phải tuần tự. Code Playwright cũ và code AI viết hay dùng `Promise.all` khi chờ một tab mới hoặc file tải về, bạn sẽ gặp lại ở bài Tab/Popup.

## ✅ Phần 4: Chia code thành module với export và import

### 🔆 1. Vì sao phải tách file - và lỗi đầu tiên khi dùng import

Quán ăn chia thành quầy pha chế, bếp, thu ngân; mỗi nơi lo một việc, cần gì thì lấy từ nơi khác. Code cũng vậy. Hàm `delay` đã bị chép lại ở 7 file từ đầu bài; sửa một chỗ phải sửa đủ 7. **Module** là một file **đưa ra** (`export`) những thứ file khác được dùng, và file khác **lấy vào** (`import`) đúng thứ nó cần.

Tạo hai file dùng chung. File `bai-09-async-module/utils/url.js`:

```javascript
// Named export: đặt chữ export trước thứ muốn cho file khác dùng
export const BASE_URL = process.env.BASE_URL ?? 'https://crm.anhtester.com';
export const EXPECTED_TITLE = 'Perfex CRM | Anh Tester Demo - Login';

export function buildUrl(path) {
  return `${BASE_URL}${path}`;
}

// Không có export: chỉ dùng được bên trong file này
const note = 'ghi chú nội bộ';
```

File `bai-09-async-module/utils/delay.js`:

```javascript
export function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

Rồi tạo file dùng chúng, `bai-09-async-module/11-dung-module.js`:

```javascript
// Named import: tên trong { } phải đúng tên đã export, đường dẫn có đuôi .js
import { BASE_URL, buildUrl } from './utils/url.js';
import { delay } from './utils/delay.js';

console.log(BASE_URL);
console.log(buildUrl('/admin/authentication'));

// File là module nên dùng được await ở ngoài cùng, không cần bọc trong hàm async
await delay(500);
console.log('Đã đợi xong 0,5 giây');
```

```bash
node bai-09-async-module/11-dung-module.js
```

Kết quả:

```bash
(node:712) Warning: Failed to load the ES module: D:\AnhTester\js-ts-for-tester\bai-09-async-module\11-dung-module.js. Make sure to set "type": "module" in the nearest package.json file or use the .mjs extension.
import { BASE_URL, buildUrl } from './utils/url.js';
^^^^^^

SyntaxError: Cannot use import statement outside a module
```

Code không sai. File `package.json` của project có dòng `"type": "commonjs"`, bảo Node.js hiểu mọi file `.js` theo kiểu module cũ (CommonJS), kiểu này không có `import`. Dòng Warning đã chỉ cách sửa. Tạo file `bai-09-async-module/package.json` với đúng nội dung sau:

```json
{
  "type": "module"
}
```

Node.js đọc file `package.json` **gần nhất** tính từ file đang chạy, nên từ giờ mọi file `.js` trong `bai-09-async-module/` là module kiểu mới ([ES Modules](https://nodejs.org/api/esm.html)), các thư mục bài khác không đổi. Chạy lại lệnh trên:

```bash
https://crm.anhtester.com
https://crm.anhtester.com/admin/authentication
Đã đợi xong 0,5 giây
```

Dòng `await delay(500)` đứng ngoài mọi hàm mà vẫn chạy: trong module kiểu mới, `await` dùng được ở ngoài cùng của file (top-level await). Từ đây bài bỏ hàm `main`.

> ⚠️ Sau khi có `package.json` này, các file từ `01` đến `10` vẫn chạy ra kết quả như cũ. Riêng file `06` đổi thông báo thành `SyntaxError: Unexpected reserved word` (vẫn là lỗi đó, khác câu chữ). Và trong thư mục này không dùng được `require` nữa (lỗi `require is not defined in ES module scope`).

### 🔆 2. Default export - thứ chính của một file

Cách ở mục trên gọi là **named export**: một file đưa ra nhiều thứ, mỗi thứ có tên. Cách thứ hai là **default export**: file chỉ có **một** thứ chính, thường là một class. Tách `BasePage` của bài Class ra file `bai-09-async-module/pages/BasePage.js`, lần này method là `async`:

```javascript
import { buildUrl } from '../utils/url.js';

// Default export: thứ chính của file, mỗi file chỉ có MỘT
export default class BasePage {
  constructor(page, path) {
    this.page = page;
    this.url = buildUrl(path);
  }

  async open() {
    await this.page.goto(this.url);
  }

  async getTitle() {
    return await this.page.title();
  }
}
```

`'../utils/url.js'`: hai dấu chấm là "lùi ra một thư mục", vì file này nằm trong `pages/`. Trang giả `fakePage` cũng cần viết lại cho giống `page` thật: mỗi thao tác tốn thời gian và trả về Promise. Tạo file `bai-09-async-module/utils/fakePage.js`:

```javascript
import { delay } from './delay.js';
import { EXPECTED_TITLE } from './url.js';

// Trang giả: mỗi thao tác mất 0,3 giây và trả về Promise, giống page của Playwright
export const fakePage = {
  async goto(url) {
    await delay(300);
    console.log(`[fakePage] mở ${url}`);
  },
  async fill(label, value) {
    await delay(300);
    const shown = label === 'Password' ? '***' : value;
    console.log(`[fakePage] điền ô "${label}": ${shown}`);
  },
  async click(name) {
    await delay(300);
    console.log(`[fakePage] bấm nút "${name}"`);
  },
  async title() {
    await delay(300);
    return EXPECTED_TITLE;
  },
};
```

File chạy `bai-09-async-module/12-dung-class.js`:

```javascript
// Default import: KHÔNG có { }
import BasePage from './pages/BasePage.js';
// Named import: CÓ { }
import { fakePage } from './utils/fakePage.js';

const loginPage = new BasePage(fakePage, '/admin/authentication');

await loginPage.open();
const title = await loginPage.getTitle();
console.log('Tiêu đề:', title);
```

```bash
node bai-09-async-module/12-dung-class.js
```

Kết quả:

```bash
[fakePage] mở https://crm.anhtester.com/admin/authentication
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
```

<table class="rt-table">
<thead>
<tr>
<th>Điểm so sánh</th>
<th>Named export</th>
<th>Default export</th>
</tr>
</thead>
<tbody>
<tr>
<td>Viết ở file gốc</td>
<td><code><span>export</span> <span>function</span> <span>buildUrl</span></code>, <code><span>export</span> <span>const</span> <span>BASE_URL</span></code></td>
<td><code><span>export</span> <span>default</span> <span>class</span> <span>BasePage</span></code></td>
</tr>
<tr>
<td>Số lượng mỗi file</td>
<td>Nhiều</td>
<td>Tối đa một</td>
</tr>
<tr>
<td>Viết khi import</td>
<td><strong>Có</strong> ngoặc nhọn, đúng tên: <code><span>import</span> <span>{</span> <span>buildUrl</span> <span>}</span> <span>from</span> <span>...</span></code></td>
<td><strong>Không</strong> ngoặc nhọn, tên tự đặt: <code><span>import</span> <span>BasePage</span> <span>from</span> <span>...</span></code></td>
</tr>
<tr>
<td>Thường dùng cho</td>
<td>Nhóm hàm, hằng số dùng chung (<code>utils/</code>)</td>
<td>File chỉ chứa một class (<code>pages/</code>)</td>
</tr>
</tbody>
</table>

`pages/` chứa class trang, `utils/` chứa hàm dùng chung: đây chính là khuôn `pages/`, `utils/`, `tests/` của project Playwright sau này.

### 🔆 3. Hai lỗi import hay gặp

**Lỗi 1 - thiếu đuôi `.js`.** File `bai-09-async-module/13-thieu-duoi-js.js`:

```javascript
// SAI: thiếu đuôi .js ở cuối đường dẫn
import { buildUrl } from './utils/url';

console.log(buildUrl('/admin/authentication'));
```

```bash
node bai-09-async-module/13-thieu-duoi-js.js
```

Kết quả:

```bash
Error [ERR_MODULE_NOT_FOUND]: Cannot find module 'D:\AnhTester\js-ts-for-tester\bai-09-async-module\utils\url' imported from D:\AnhTester\js-ts-for-tester\bai-09-async-module\13-thieu-duoi-js.js
```

Với module kiểu mới, Node.js [bắt buộc ghi đủ đuôi file](https://nodejs.org/api/esm.html#mandatory-file-extensions) và đường dẫn bắt đầu bằng `./` hoặc `../`.

**Lỗi 2 - nhầm ngoặc nhọn.** File `bai-09-async-module/14-nham-ngoac.js`:

```javascript
// SAI: BasePage là default export nhưng lại import có { }
import { BasePage } from './pages/BasePage.js';

console.log(BasePage);
```

```bash
node bai-09-async-module/14-nham-ngoac.js
```

Kết quả:

```bash
import { BasePage } from './pages/BasePage.js';
         ^^^^^^^^
SyntaxError: The requested module './pages/BasePage.js' does not provide an export named 'BasePage'
```

Nhầm chiều ngược lại (`import buildUrl from './utils/url.js'`, thiếu ngoặc nhọn với named export) thì thông báo là `does not provide an export named 'default'`. Gặp một trong hai câu này, mở file gốc xem nó viết `export` hay `export default`.

> 📌 Code cũ và đôi khi code AI viết dùng `const x = require('./x')` và `module.exports = ...`. Đó là kiểu CommonJS (bạn đã gặp `require('node:fs')` ở bài Object và JSON), đọc hiểu được là đủ. Project Playwright TypeScript dùng `import`/`export`, và ở đó đường dẫn import **không** có đuôi file vì Playwright tự xử lý.

## ✅ Phần 5: Bắt lỗi với try...catch và throw new Error()

### 🔆 1. try...catch...finally

Đi làm bằng xe máy, bạn có phương án B khi xe hỏng: gửi xe, gọi xe ôm. Đi cách nào thì tới nơi vẫn phải chấm công. Trong code: `try` là việc định làm, `catch` là phương án khi có lỗi, `finally` là việc **luôn** làm. Tạo file `bai-09-async-module/15-try-catch.js`:

```javascript
// Chuỗi JSON thừa dấu phẩy cuối, giống lỗi ở bài Object và JSON
const jsonText = '{"email":"admin@example.com","role":"admin",}';

try {
  console.log('1. Bắt đầu đọc data test');
  const user = JSON.parse(jsonText); // dòng này ném lỗi
  console.log('2. Dòng này bị bỏ qua khi có lỗi', user);
} catch (error) {
  console.log('3. Vào catch:', error.name, '-', error.message);
} finally {
  console.log('4. finally luôn chạy, có lỗi hay không');
}

console.log('5. Chương trình vẫn chạy tiếp');
```

```bash
node bai-09-async-module/15-try-catch.js
```

Kết quả:

```bash
1. Bắt đầu đọc data test
3. Vào catch: SyntaxError - Expected double-quoted property name in JSON at position 44 (line 1 column 45)
4. finally luôn chạy, có lỗi hay không
5. Chương trình vẫn chạy tiếp
```

Lỗi xảy ra thì JavaScript **nhảy thẳng** vào `catch`, bỏ qua phần còn lại của `try` (dòng `2.` không in). Biến `error` là một Object có `error.name` (loại lỗi) và `error.message` (thông báo). `finally` dùng cho việc dọn dẹp, ví dụ đóng trình duyệt hay xoá data test vừa tạo.

### 🔆 2. Chủ động báo lỗi bằng throw new Error()

Có những tình huống JavaScript không coi là lỗi nhưng với bạn là sai, ví dụ `find` không thấy tài khoản thì chỉ trả `undefined`. Bạn tự **ném lỗi** bằng `throw new Error('thông báo')`. Tạo file `bai-09-async-module/16-throw-error.js`:

```javascript
const users = [
  { email: 'admin@example.com', role: 'admin' },
  { email: 'customer@example.com', role: 'customer' },
];

function getUser(role) {
  const user = users.find((item) => item.role === role);
  if (!user) {
    throw new Error(`Không có tài khoản vai trò "${role}" trong data test`);
  }
  return user;
}

// 1. Bắt lỗi và đọc thông báo
try {
  getUser('guest');
} catch (error) {
  console.log('message:', error.message);
}

// 2. SAI: ném một chuỗi thay vì new Error
try {
  throw 'Không có tài khoản';
} catch (error) {
  console.log('message:', error.message);
}

// 3. Không bắt: chương trình dừng tại đây
getUser('guest');
console.log('Dòng này không chạy tới');
```

```bash
node bai-09-async-module/16-throw-error.js
```

Kết quả:

```bash
message: Không có tài khoản vai trò "guest" trong data test
message: undefined
    throw new Error(`Không có tài khoản vai trò "${role}" trong data test`);
          ^

Error: Không có tài khoản vai trò "guest" trong data test
    at getUser (file:///D:/AnhTester/js-ts-for-tester/bai-09-async-module/16-throw-error.js:9:11)
    at file:///D:/AnhTester/js-ts-for-tester/bai-09-async-module/16-throw-error.js:29:1
```

- Thông báo lỗi viết **rõ nghĩa**: sai cái gì, giá trị nào. Nếu để `find` trả `undefined` rồi vài dòng sau mới vỡ với `TypeError: Cannot read properties of undefined`, người đọc report phải lần ngược lại mới biết nguyên nhân.
- `throw 'chuỗi'` chạy được nhưng mất `error.message` (ra `undefined`) và mất luôn các dòng `at ...` chỉ vị trí lỗi. Luôn dùng `new Error(...)`.
- Lỗi không ai bắt thì chương trình dừng. Hai dòng `at ...` cho biết lỗi ném ra ở dòng 9 trong `getUser`, do dòng 29 gọi.

### 🔆 3. try...catch với await

Promise bị `rejected` mà bạn đang `await` nó thì `await` **ném lỗi** ngay tại dòng đó, và `try...catch` bắt được như lỗi thường. Tạo file `bai-09-async-module/17-bat-loi-await.js`, gọi `fetch` tới một tên miền không tồn tại:

```javascript
// Tên miền .invalid không bao giờ tồn tại, dùng để tạo lỗi kết nối
const wrongUrl = 'https://crm-khong-ton-tai.invalid/admin/authentication';

try {
  console.log('Đang mở', wrongUrl);
  const response = await fetch(wrongUrl); // Promise bị từ chối, await ném lỗi
  console.log('Status:', response.status);
} catch (error) {
  console.log('Tên lỗi   :', error.name);
  console.log('Thông báo :', error.message);
  console.log('Nguyên do :', error.cause.code);
}
```

```bash
node bai-09-async-module/17-bat-loi-await.js
```

Kết quả:

```bash
Đang mở https://crm-khong-ton-tai.invalid/admin/authentication
Tên lỗi   : TypeError
Thông báo : fetch failed
Nguyên do : ENOTFOUND
```

Nguyên nhân gốc nằm trong `error.cause`: `ENOTFOUND` là không tìm thấy tên miền.

> ⚠️ `try...catch` chỉ bắt được lỗi của Promise khi có `await`. Viết `fetch(wrongUrl)` thiếu `await` trong `try` thì `catch` không chạy, chương trình vẫn dừng với `TypeError: fetch failed`.

### 🔆 4. Cảnh báo: nuốt lỗi làm test xanh giả

Playwright coi một test là **FAIL khi hàm test ném lỗi**, và PASS khi hàm chạy hết mà không ném gì. File `bai-09-async-module/18-nuot-loi.js` dựng một trình chạy test giả theo đúng luật đó, rồi chạy 4 cách viết khi trang đang hỏng (tiêu đề thực tế là `404 Not Found`):

```javascript
import { EXPECTED_TITLE } from './utils/url.js';

// Trình chạy test giả: hàm test KHÔNG ném lỗi thì PASS, ném lỗi thì FAIL
async function fakeTest(name, testFn) {
  try {
    await testFn();
    console.log(`PASS  ${name}`);
  } catch (error) {
    console.log(`FAIL  ${name}`);
    console.log(`      ${error.message}`);
  }
}

function checkTitle(actualTitle) {
  if (actualTitle !== EXPECTED_TITLE) {
    throw new Error(`Tiêu đề sai: mong đợi "${EXPECTED_TITLE}", thực tế "${actualTitle}"`);
  }
}

// Trang đang hỏng: tiêu đề thực tế là "404 Not Found"
await fakeTest('1. catch rỗng - nuốt lỗi', async () => {
  try {
    checkTitle('404 Not Found');
  } catch (error) {}
});

await fakeTest('2. catch chỉ console.log - vẫn nuốt lỗi', async () => {
  try {
    checkTitle('404 Not Found');
  } catch (error) {
    console.log('      Có lỗi nhưng bỏ qua');
  }
});

await fakeTest('3. không try...catch - để lỗi ném ra', async () => {
  checkTitle('404 Not Found');
});

await fakeTest('4. ghi thêm log rồi ném lại', async () => {
  try {
    checkTitle('404 Not Found');
  } catch (error) {
    console.log('      LOG: lỗi ở bước kiểm tiêu đề trang đăng nhập');
    throw error;
  }
});
```

```bash
node bai-09-async-module/18-nuot-loi.js
```

Kết quả:

```bash
PASS  1. catch rỗng - nuốt lỗi
      Có lỗi nhưng bỏ qua
PASS  2. catch chỉ console.log - vẫn nuốt lỗi
FAIL  3. không try...catch - để lỗi ném ra
      Tiêu đề sai: mong đợi "Perfex CRM | Anh Tester Demo - Login", thực tế "404 Not Found"
      LOG: lỗi ở bước kiểm tiêu đề trang đăng nhập
FAIL  4. ghi thêm log rồi ném lại
      Tiêu đề sai: mong đợi "Perfex CRM | Anh Tester Demo - Login", thực tế "404 Not Found"
```

Trang hỏng mà test 1 và 2 vẫn **PASS**: lỗi bị `catch` giữ lại, trình chạy test không hề biết. Đây là **nuốt lỗi**: report xanh trong khi sản phẩm lỗi. Quy tắc:

- Trong test Playwright, **mặc định không bọc `try...catch`** quanh thao tác và assertion. Để lỗi ném ra, test FAIL, Playwright ghi lại đầy đủ (cách 3).
- Chỉ bắt lỗi khi có **xử lý thật**, và xử lý xong mà chưa giải quyết được thì **ném lại** bằng `throw error` (cách 4).

### 🔆 5. Xử lý thật: thử lại có giới hạn

Một kiểu xử lý thật hay gặp: bước không ổn định (máy chủ bận) thì thử lại vài lần. File `bai-09-async-module/19-thu-lai.js` nối vòng `while` có biến đếm của bài vòng lặp với `try...catch`:

```javascript
import { delay } from './utils/delay.js';

// Bước giả không ổn định: 2 lần đầu lỗi, lần thứ 3 mới thành công
let callCount = 0;
async function unstableStep() {
  callCount++;
  await delay(300);
  if (callCount < 3) {
    throw new Error(`Máy chủ bận (lần gọi ${callCount})`);
  }
  return 'Mở trang thành công';
}

async function retry(stepFn, maxAttempts) {
  let attempt = 1;
  while (attempt <= maxAttempts) {
    try {
      return await stepFn();
    } catch (error) {
      console.log(`Lần ${attempt} lỗi: ${error.message}`);
      if (attempt === maxAttempts) {
        throw new Error(`Thất bại sau ${maxAttempts} lần thử: ${error.message}`);
      }
      attempt++;
    }
  }
}

console.log(await retry(unstableStep, 5));

callCount = 0;
console.log('--- Chỉ cho thử tối đa 2 lần ---');
console.log(await retry(unstableStep, 2));
```

```bash
node bai-09-async-module/19-thu-lai.js
```

Kết quả:

```bash
Lần 1 lỗi: Máy chủ bận (lần gọi 1)
Lần 2 lỗi: Máy chủ bận (lần gọi 2)
Mở trang thành công
--- Chỉ cho thử tối đa 2 lần ---
Lần 1 lỗi: Máy chủ bận (lần gọi 1)
Lần 2 lỗi: Máy chủ bận (lần gọi 2)
        throw new Error(`Thất bại sau ${maxAttempts} lần thử: ${error.message}`);
              ^

Error: Thất bại sau 2 lần thử: Máy chủ bận (lần gọi 2)
```

Đây là xử lý thật chứ không phải nuốt lỗi vì: có **số lần tối đa**, và hết lượt thì **ném lỗi ra ngoài** kèm lý do. Với Playwright bạn hiếm khi tự viết hàm này vì đã có cơ chế tự chờ và tuỳ chọn chạy lại test; nhưng code AI viết hay có, và bạn soát đúng hai điểm đó.

## ✅ Phần 6: Thực hành - luồng đăng nhập CRM với class tách file, async và bắt lỗi

Gom cả bài lại: `LoginPage` kế thừa `BasePage` ở file riêng, method đều `async`; thêm một hàm kiểm trang đăng nhập bằng `fetch` thật có ném lỗi rõ nghĩa. Tạo file `bai-09-async-module/pages/LoginPage.js`:

```javascript
import BasePage from './BasePage.js';

export default class LoginPage extends BasePage {
  constructor(page) {
    super(page, '/admin/authentication');
  }

  async login(email) {
    await this.page.fill('Email Address', email);
    await this.page.fill('Password', process.env.ADMIN_PASSWORD);
    await this.page.click('Login');
  }
}
```

File `bai-09-async-module/utils/checkLoginPage.js`:

```javascript
// Kiểm trang đăng nhập bằng fetch thật: status phải là 200 và tiêu đề phải đúng
export async function checkLoginPage(url, expectedTitle) {
  let response;
  try {
    response = await fetch(url);
  } catch (error) {
    // Có xử lý thật: thêm thông tin rõ nghĩa rồi NÉM LẠI, giữ lỗi gốc trong cause
    throw new Error(`Không kết nối được tới ${url} (${error.cause?.code ?? error.message})`, { cause: error });
  }

  if (response.status !== 200) {
    throw new Error(`Trang ${url} trả về status ${response.status}, mong đợi 200`);
  }

  const html = await response.text();
  const start = html.indexOf('<title>') + '<title>'.length;
  const title = html.slice(start, html.indexOf('</title>')).trim();

  if (title !== expectedTitle) {
    throw new Error(`Tiêu đề sai: mong đợi "${expectedTitle}", thực tế "${title}"`);
  }

  return { status: response.status, title };
}
```

File chạy chính `bai-09-async-module/crm-login-flow.js`:

```javascript
import LoginPage from './pages/LoginPage.js';
import { fakePage } from './utils/fakePage.js';
import { buildUrl, EXPECTED_TITLE } from './utils/url.js';
import { checkLoginPage } from './utils/checkLoginPage.js';

const loginUrl = buildUrl('/admin/authentication');

try {
  console.log('===== 1. Kiểm trang đăng nhập bằng fetch thật =====');
  const result = await checkLoginPage(loginUrl, EXPECTED_TITLE);
  console.log(result);

  console.log('===== 2. Chạy luồng đăng nhập với fakePage =====');
  const loginPage = new LoginPage(fakePage);
  await loginPage.open();
  await loginPage.login(process.env.ADMIN_EMAIL ?? 'admin@example.com');
  console.log('Tiêu đề:', await loginPage.getTitle());

  console.log('KẾT QUẢ: PASS');
} catch (error) {
  console.log('KẾT QUẢ: FAIL');
  console.log('Lý do  :', error.message);
  process.exitCode = 1; // báo cho terminal và CI biết lần chạy này thất bại
} finally {
  console.log('===== 3. Dọn dẹp (finally) =====');
}
```

```bash
node bai-09-async-module/crm-login-flow.js
```

Kết quả:

```bash
===== 1. Kiểm trang đăng nhập bằng fetch thật =====
{ status: 200, title: 'Perfex CRM | Anh Tester Demo - Login' }
===== 2. Chạy luồng đăng nhập với fakePage =====
[fakePage] mở https://crm.anhtester.com/admin/authentication
[fakePage] điền ô "Email Address": admin@example.com
[fakePage] điền ô "Password": ***
[fakePage] bấm nút "Login"
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
KẾT QUẢ: PASS
===== 3. Dọn dẹp (finally) =====
```

Bước 2 là trang giả: không có form nào gửi lên CRM, mật khẩu chỉ đi qua biến `ADMIN_PASSWORD` và log in `***`. Giờ chạy lần lỗi. Đặt biến môi trường `BASE_URL` là `https://crm-khong-ton-tai.invalid` rồi chạy lại:

```bash
===== 1. Kiểm trang đăng nhập bằng fetch thật =====
KẾT QUẢ: FAIL
Lý do  : Không kết nối được tới https://crm-khong-ton-tai.invalid/admin/authentication (ENOTFOUND)
===== 3. Dọn dẹp (finally) =====
```

Bước 1 ném lỗi nên bước 2 bị bỏ qua, `finally` vẫn chạy. Khối `catch` ở đây **không nuốt lỗi**: nó in FAIL kèm lý do và đặt `process.exitCode = 1`. Trong project Playwright, Playwright làm việc đó thay bạn. Bản Playwright thật của bước 1 trông như sau (chỉ để đọc, bài này chưa chạy):

```typescript
import { test, expect } from '@playwright/test';

test('mở trang đăng nhập Admin', async ({ page }) => {
  await page.goto('https://crm.anhtester.com/admin/authentication');
  await expect(page).toHaveTitle('Perfex CRM | Anh Tester Demo - Login');
});
```

Giờ bạn đọc được trọn vẹn: dòng đầu là named import; `async` đứng trước callback; mỗi thao tác một chữ `await`; không có `try...catch`, sai tiêu đề thì `expect` ném lỗi và test FAIL.

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức của bài

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn dùng được các prompt dưới đây: chỗ có `@đường-dẫn` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay. Không dán mật khẩu hay file `.env` vào khung chat.

```markdown
Đoạn test Playwright sau lúc pass lúc fail. Hãy tìm TẤT CẢ chỗ thiếu await.
Với mỗi chỗ: ghi số dòng, giải thích vì sao lời gọi đó trả về Promise (dẫn link playwright.dev),
và hậu quả nếu không await. Sau cùng mới đưa bản đã sửa. Không đổi locator, không thêm bước.

test('mở trang đăng nhập Admin', async ({ page }) => {
  page.goto('https://crm.anhtester.com/admin/authentication');
  const title = page.title();
  expect(title).toBe('Perfex CRM | Anh Tester Demo - Login');
  page.getByLabel('Email Address').fill('admin@example.com');
  expect(page.getByRole('button', { name: 'Login' })).toBeVisible();
});
```

```markdown
Đọc file @bai-09-async-module/09-foreach-khong-cho.js. Tôi mới học JavaScript.
1. Giải thích từng bước vì sao "Xong tất cả" in ra trước khi các tài khoản kiểm xong,
   dù trong callback đã có await.
2. Viết lại bằng for...of (chạy tuần tự) và bằng Promise.all + map (chạy song song).
3. Lập bảng: mỗi cách chạy theo thứ tự nào, mất khoảng bao lâu, khi nào nên dùng trong test.
Chạy cả hai bản bằng node để chứng minh, KHÔNG sửa file gốc.
```

```markdown
File dưới đây đang chứa mọi thứ trong một chỗ: hằng số URL, hàm dùng chung, class trang và phần chạy.
Hãy đề xuất cách tách thành module theo khuôn pages/ và utils/:
- Vẽ cây thư mục sau khi tách.
- Với mỗi file: export gì, named hay default, vì sao.
- Viết đủ các dòng import ở từng file (project chạy bằng Node.js, module kiểu ES, import phải có đuôi .js).
Chỉ đề xuất và giải thích, chờ tôi đồng ý rồi mới tạo file.

[dán nội dung file hoặc dùng @đường-dẫn-tới-file]
```

```markdown
Review toàn bộ try...catch trong @bai-09-async-module/ (hoặc đoạn code tôi dán bên dưới).
Với mỗi khối catch, xếp vào một trong ba loại:
(a) nuốt lỗi: catch rỗng hoặc chỉ console.log rồi chạy tiếp;
(b) xử lý thật: thử lại có giới hạn, ghi log rồi throw lại, đổi sang lỗi rõ nghĩa hơn;
(c) không cần thiết: bỏ try...catch đi thì test vẫn đúng và FAIL rõ hơn.
Ghi rõ file, số dòng, trích nguyên văn. Chỉ báo cáo, KHÔNG sửa code.
```

### 🔆 2. Bộ kit liên quan gì tới async/await, import và try...catch?

- Rule [playwright\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/playwright_rules.md) (mục 4, chiến lược chờ đợi) **cấm** `page.waitForTimeout()` và cả `await new Promise(r => setTimeout(r, N))`. Dòng thứ hai chính là hàm `delay` của bài này: `delay` chỉ để **học** Promise, test thật không dùng nó để chờ trang.
- File [CLAUDE.md](https://github.com/anhtester/claude-testing-skills/blob/main/CLAUDE.md) của kit (Definition of Done) yêu cầu tách Page class, Test class, Utils và không để import thừa.
- Lệnh [/review-automation-code](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/review-automation-code.md) soát code automation đã có (pass giả, chờ cứng, sai mô hình trang); lệnh [/run-and-fix-tests](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/run-and-fix-tests.md) chạy bộ test, phân loại lỗi và sửa nhóm sửa được. Cả hai dùng từ chương Playwright.

Các rule của kit hiện **không có dòng riêng** về thiếu `await` hay `catch` rỗng. Hai lỗi này bạn tự soát theo bảng ở phần kế tiếp.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Rà code AI viết theo bảng sau:

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
<td>Thiếu <code>await</code> trước <code>page.goto()</code>, <code>fill()</code>, <code>click()</code>, <code>expect(locator)...</code></td>
<td>Không báo lỗi cú pháp; bước sau chạy khi bước trước chưa xong, giá trị nhận về là <code>Promise { &lt;pending&gt; }</code></td>
<td>Thêm <code>await</code> trước mọi lời gọi trả về Promise</td>
</tr>
<tr>
<td><code>forEach(async ...)</code> có <code>await</code> bên trong</td>
<td><code>forEach</code> không chờ: code phía sau chạy khi các thao tác còn dang dở</td>
<td>Đổi sang <code>for...of</code>; việc độc lập thì <code>Promise.all</code></td>
</tr>
<tr>
<td><code>await</code> trong hàm không có <code>async</code></td>
<td>File không chạy: <code><span>SyntaxError:</span> <span>await</span> <span>is</span> <span>only</span> <span>valid</span> <span>in</span> <span>async</span> <span>functions...</span></code> hoặc <code>Unexpected reserved word</code></td>
<td>Thêm <code>async</code> trước hàm chứa <code>await</code></td>
</tr>
<tr>
<td><code>catch (error) {}</code> rỗng, hoặc chỉ <code>console.log</code> rồi chạy tiếp</td>
<td>Nuốt lỗi: sản phẩm lỗi mà test vẫn PASS</td>
<td>Bỏ <code>try...catch</code>, hoặc xử lý thật rồi <code>throw error</code></td>
</tr>
<tr>
<td><code>throw 'chuỗi'</code></td>
<td><code>error.message</code> ra <code>undefined</code>, mất vị trí lỗi</td>
<td>Đổi thành <code>throw new Error('...')</code> với thông báo rõ nghĩa</td>
</tr>
<tr>
<td><code>import</code> thiếu đuôi <code>.js</code> (file chạy bằng Node.js)</td>
<td><code>ERR_MODULE_NOT_FOUND</code></td>
<td>Ghi đủ <code>./đường-dẫn/file.js</code></td>
</tr>
<tr>
<td>Nhầm <code>{ }</code> giữa named và default</td>
<td><code><span>does</span> <span>not</span> <span>provide</span> <span>an</span> <span>export</span> <span>named</span> <span>...</span></code></td>
<td>Mở file gốc xem <code>export</code> hay <code>export default</code></td>
</tr>
<tr>
<td>Dùng <code>import</code> trong project <code>"type": "commonjs"</code>, hoặc trộn <code>require</code> với <code>import</code> trong một file</td>
<td><code><span>Cannot</span> <span>use</span> <span>import</span> <span>statement</span> <span>outside</span> <span>a</span> <span>module</span></code>, hoặc <code><span>require</span> <span>is</span> <span>not</span> <span>defined</span> <span>in</span> <span>ES</span> <span>module</span> <span>scope</span></code></td>
<td>Chọn một kiểu cho cả thư mục; khoá học dùng <code>import</code>/<code>export</code></td>
</tr>
<tr>
<td>Chờ cứng "cho chắc": <code>setTimeout</code>, hàm <code>delay</code>, <code>page.waitForTimeout()</code></td>
<td>Test chậm mà vẫn không ổn định; rule của kit cấm</td>
<td>Bỏ đi; dùng cơ chế tự chờ và <code>await expect(...)</code></td>
</tr>
</tbody>
</table>

## ✅ Phần 9: Bài tập thực hành

Đặt file bài tập trong thư mục `bai-09-async-module/`.

**Bài tập 1 - Kiểm tiêu đề cho 3 vai trò.** Tạo file `bt1-kiem-3-vai-tro.js`: import `fakePage` và `BasePage`, khai báo mảng `users` 3 vai trò có `loginPath` như bài Object và JSON, dùng `for...of` để với mỗi tài khoản tạo `new BasePage(fakePage, user.loginPath)` rồi `await` `open()` và `getTitle()`. Sau đó đổi sang `forEach`, chạy lại và ghi ra thứ tự in khác gì.

**Bài tập 2 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt2-duyet-code.js`, chép vào và chạy:

```javascript
import { buildUrl } from './utils/url';
import { BasePage } from './pages/BasePage.js';
import { delay } from './utils/delay.js';

async function checkRole(role) {
  await delay(300);
  if (role === 'guest') {
    throw 'Vai trò không hợp lệ';
  }
  return `${role}: OK`;
}

console.log(typeof BasePage, buildUrl('/admin/authentication'));

['admin', 'customer', 'guest'].forEach(async (role) => {
  try {
    const result = checkRole(role);
    console.log(result);
  } catch (error) {}
});

console.log('Xong tất cả');
```

Kết quả chạy thật:

```bash
Error [ERR_MODULE_NOT_FOUND]: Cannot find module 'D:\AnhTester\js-ts-for-tester\bai-09-async-module\utils\url' imported from D:\AnhTester\js-ts-for-tester\bai-09-async-module\bt2-duyet-code.js
```

Có 6 chỗ sai, mỗi chỗ ứng với một dòng của bảng ở Phần 8; sửa xong hai dòng `import` thì các chỗ còn lại mới lộ ra. Sửa xong (vai trò lỗi thì `catch` in ra `error.message`), file phải in lần lượt:

```bash
function https://crm.anhtester.com/admin/authentication
admin: OK
customer: OK
guest: FAIL - Vai trò không hợp lệ
Xong tất cả
```

## ✅ Phần 10: Ghi nhớ nhanh

- Việc tốn thời gian trả về **Promise**. `await` đợi Promise và lấy giá trị bên trong; chỉ dùng trong hàm `async` hoặc ở ngoài cùng của module. Hàm `async` luôn trả về Promise.
- Quên `await` không báo lỗi, chỉ ra `Promise { <pending> }` và chạy lộn thứ tự. Mọi thao tác Playwright đều cần `await`.
- Có `await` trong vòng lặp thì dùng `for...of`, không dùng `forEach`. Việc độc lập chạy song song bằng `await Promise.all([...])`.
- Named export: nhiều thứ mỗi file, import **có** `{ }`. Default export: một thứ mỗi file, import **không** `{ }`. Chạy bằng Node.js thì đường dẫn import có đuôi `.js`.
- `try` làm việc, `catch` xử lý lỗi, `finally` luôn chạy. Báo lỗi bằng `throw new Error('thông báo rõ nghĩa')`.
- Không nuốt lỗi. Trong test, để lỗi ném ra cho test FAIL; chỉ `catch` khi có xử lý thật rồi ném lại.

✅ **Kết luận:** Bạn đã có đủ ba mảnh mà mọi file test Playwright đều dùng: `async`/`await`, `import`/`export` và cách lỗi làm test FAIL. Nhưng JavaScript vẫn để lọt những lỗi như gõ sai tên thuộc tính hay truyền sai kiểu dữ liệu cho tới lúc chạy. Bài kế tiếp, **Kiểu dữ liệu, type, interface và class trong TypeScript**, thêm kiểu dữ liệu vào code để trình soạn thảo báo các lỗi đó ngay khi bạn gõ, và khép lại chương JavaScript TypeScript trước khi vào Playwright.

---

## Bài tập riêng — async/await, import/export và bắt lỗi với try...catch

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-99](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-99)

**Mục tiêu:** chờ đúng các thao tác bất đồng bộ, tách code thành module và bắt lỗi mà không nuốt lỗi làm test xanh giả.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-09-async-module`

Thư mục bài dùng ES module (`package.json` có `{"type":"module"}`) như bài học.

### 📝 Đề bài

#### Bài tập 1 - Kiểm tiêu đề cho 3 vai trò

Tạo file `bt1-kiem-3-vai-tro.js`: import `fakePage` và `BasePage`, khai báo mảng `users` 3 vai trò có `loginPath` như bài Object và JSON, dùng `for...of` để với mỗi tài khoản tạo `new BasePage(fakePage, user.loginPath)` rồi `await open()` và `getTitle()`. Sau đó đổi sang `forEach`, chạy lại. **Trả lời:** thứ tự in khác gì, vì sao?

#### Bài tập 2 - Duyệt code AI

Tạo file `bt2-duyet-code.js`, chép đoạn code AI viết dưới đây và chạy. Có **6 chỗ sai**, mỗi chỗ ứng với một dòng của bảng ở Phần 8; sửa xong hai dòng import thì các chỗ còn lại mới lộ ra. Vai trò lỗi thì `catch` in ra `error.message`.

```javascript
import { buildUrl } from './utils/url';
import { BasePage } from './pages/BasePage.js';
import { delay } from './utils/delay.js';
async function checkRole(role) {
  await delay(300);
  if (role === 'guest') {
    throw 'Vai trò không hợp lệ';
  }
  return `${role}: OK`;
}
console.log(typeof BasePage, buildUrl('/admin/authentication'));
['admin', 'customer', 'guest'].forEach(async (role) => {
  try {
    const result = checkRole(role);
    console.log(result);
  } catch (error) {}
});
console.log('Xong tất cả');
```

### 📦 Cách nộp bài

1. Làm bài trong thư mục `bai-09-async-module/` của repo `js-ts-for-tester`, commit và push lên nhánh `main`.
2. Dán link thư mục bài trên GitHub vào ô **Link GitHub**, dạng `https://github.com/<ten-ban>/js-ts-for-tester/tree/main/bai-09-async-module`. Repo Private thì vào **Settings → Collaborators** thêm tài khoản GitHub của giảng viên, nếu không giảng viên không mở được.
3. Trong ô **Nội dung bài làm (Editor)**, dán **kết quả chạy thật** của từng file (mỗi file một **Đoạn code mẫu** chọn Text / Log) và phần trả lời các câu hỏi.
4. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*.
5. Bài tập 1: dán cả 2 kết quả (for...of và forEach) và câu trả lời.

### ✅ Tiêu chí Đạt

- Bài tập 1: bản for...of in tuần tự từng vai trò (mở trang rồi tiêu đề, xong vai trò này mới sang vai trò sau); bản forEach in lẫn thứ tự hoặc chạy xong trước khi các trang mở; có giải thích forEach không chờ hàm async.
- Bài tập 2 sau khi sửa in lần lượt: `function https://crm.anhtester.com/admin/authentication`, `admin: OK`, `customer: OK`, `guest: FAIL - Vai trò không hợp lệ`, `Xong tất cả`.
- Nêu đủ 6 chỗ: import thiếu đuôi `.js`; import tên sai kiểu export (default/named) theo file thật; `throw` chuỗi thay vì `new Error()`; quên `await`; `forEach` với async không chờ (đổi sang `for...of`); `catch` rỗng nuốt lỗi.
- Code đã có trên GitHub, nhánh main.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.