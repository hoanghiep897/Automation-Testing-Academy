# Bài 5 - [Javascript Typescript] Object và JSON trong JavaScript - lưu, lấy nhanh và gộp dữ liệu test

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/403](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/403)

✅ Object: tạo, đọc, thêm, sửa, xoá thuộc tính, dùng ?. và ??  
✅ Duyệt Object và mảng các Object  
✅ JSON: JSON.stringify, JSON.parse và đọc lỗi khi JSON sai  
✅ Lấy nhanh giá trị từ Object (destructuring) và vì sao test viết async ({ page })  
✅ Gộp và ghi đè Object bằng dấu ... (spread)  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra code do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước bạn đã lưu một danh sách email test vào mảng và duyệt nó bằng `for...of`, `find`, `filter`. Nhưng một tài khoản test không chỉ có email: nó còn có vai trò, trang đăng nhập. Bài này gom các thông tin đó vào **Object**, đổi Object qua lại với **JSON**, rồi **lấy nhanh** và **gộp** dữ liệu bằng hai cú pháp có trong hầu hết file test Playwright. Học xong bạn sẽ:

- Tạo Object, đọc, thêm, sửa, xoá thuộc tính; dùng `?.` và `??` khi thuộc tính có thể thiếu.
- Duyệt Object và làm việc với mảng các Object.
- Dùng `JSON.stringify`, `JSON.parse` và đọc được lỗi khi JSON sai.
- Lấy nhanh giá trị từ Object (destructuring) và hiểu vì sao test Playwright viết `async ({ page }) => {}`.
- Gộp và ghi đè Object bằng dấu `...` (spread).

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật (Node.js v24.17.0), đã lược dòng đường dẫn file ở kết quả có lỗi.

## ✅ Phần 1: Object - gom nhiều thông tin của một đối tượng

### 🔆 1. Chuẩn bị thư mục cho bài học

Tạo thư mục `bai-05-object-json` trong project. Mỗi ví dụ là một file trong thư mục đó:

```bash
js-ts-for-tester/
├── package.json
└── bai-05-object-json/
    ├── data/
    │   └── users.json
    ├── 01-the-nhan-vien.js
    ├── 02-tai-khoan-test.js
    ├── 03-them-sua-xoa.js
    ├── 04-thuoc-tinh-thieu.js
    ├── 05-duyet-object.js
    ├── 06-mang-object.js
    ├── 07-json-stringify.js
    ├── 08-json-parse.js
    ├── 09-json-loi-dau-phay.js
    ├── 10-json-loi-nhay-don.js
    ├── 11-doc-file-json.js
    ├── 12-lay-nhanh.js
    ├── 13-lay-nhanh-tham-so.js
    ├── 14-vi-sao-page.js
    ├── 15-gop-ghi-de.js
    ├── 16-gop-config.js
    ├── 17-sao-chep-nong.js
    └── crm-test-data.js
```

### 🔆 2. Object là gì?

Một thẻ nhân viên ghi nhiều thông tin của **cùng một người**: tên, tuổi, số điện thoại. Mỗi dòng có **tên mục** và **giá trị**. **Object** trong JavaScript làm đúng việc đó: gom nhiều cặp `key: value` vào một biến, đặt trong dấu `{ }`.

Tạo file `bai-05-object-json/01-the-nhan-vien.js`:

```javascript
// Thẻ nhân viên: nhiều thông tin của MỘT người gom vào một Object
const nhanVien = {
  ten: 'An',
  tuoi: 25,
  soDienThoai: '0901234567',
  daKyHopDong: true,
};

console.log(nhanVien);
console.log(nhanVien.ten);
console.log(`${nhanVien.ten} ${nhanVien.tuoi} tuổi, SĐT ${nhanVien.soDienThoai}`);
```

```bash
node bai-05-object-json/01-the-nhan-vien.js
```

Kết quả:

```bash
{ ten: 'An', tuoi: 25, soDienThoai: '0901234567', daKyHopDong: true }
An
An 25 tuổi, SĐT 0901234567
```

`ten`, `tuoi` là **key** (còn gọi là thuộc tính). Giá trị có thể là chuỗi, số, boolean, mảng, Object khác, cả hàm.

### 🔆 3. Tài khoản test là một Object

Tài khoản test của CRM demo cũng là một Object. Tạo file `bai-05-object-json/02-tai-khoan-test.js`:

```javascript
const adminUser = {
  email: process.env.ADMIN_EMAIL ?? 'admin@example.com',
  role: 'admin',
  loginPath: '/admin/authentication',
  'display-name': 'Admin Anh Tester',
};

// Cách 1: dấu chấm - dùng nhiều nhất
console.log(adminUser.email);
console.log(adminUser.role);

// Cách 2: ngoặc vuông - khi tên key có dấu gạch ngang...
console.log(adminUser['display-name']);

// ...hoặc khi tên key nằm trong một biến
const field = 'loginPath';
console.log(adminUser[field]);
```

```bash
node bai-05-object-json/02-tai-khoan-test.js
```

Kết quả:

```bash
admin@example.com
admin
Admin Anh Tester
/admin/authentication
```

**Dấu chấm** dùng cho hầu hết trường hợp. **Ngoặc vuông** bắt buộc khi tên key có ký tự đặc biệt như dấu `-` (viết `adminUser.display-name` thì JavaScript hiểu là phép trừ), hoặc khi tên key nằm trong một biến.

> 🔒 Object tài khoản test **không chứa mật khẩu viết thẳng**. Nếu cần thì đọc từ biến môi trường: `password: process.env.ADMIN_PASSWORD`, và không in giá trị đó ra log.

### 🔆 4. Thêm, sửa, xoá thuộc tính

Tạo file `bai-05-object-json/03-them-sua-xoa.js`:

```javascript
const adminUser = {
  email: 'admin@example.com',
  role: 'admin',
  tempNote: 'ghi chú tạm',
};

adminUser.role = 'project-manager'; // sửa thuộc tính đã có
adminUser.isActive = true;          // thêm thuộc tính mới
delete adminUser.tempNote;          // xoá thuộc tính

console.log(adminUser);

// Gán lại CẢ biến thì const không cho
adminUser = { email: 'khac@example.com' };
```

```bash
node bai-05-object-json/03-them-sua-xoa.js
```

Kết quả:

```bash
{ email: 'admin@example.com', role: 'project-manager', isActive: true }
adminUser = { email: 'khac@example.com' };
          ^

TypeError: Assignment to constant variable.
```

Giống mảng ở bài trước: `const` chỉ cấm **gán lại cả biến**, không cấm sửa bên trong.

### 🔆 5. Thuộc tính không có: undefined, ?. và ??

Tạo file `bai-05-object-json/04-thuoc-tinh-thieu.js`:

```javascript
const customerUser = {
  email: 'customer@example.com',
  role: 'customer',
};

// Đọc key không có: ra undefined, KHÔNG báo lỗi
console.log(customerUser.phone);

// ?? lấy giá trị mặc định khi thuộc tính thiếu
console.log(customerUser.phone ?? 'chưa có số');

// ?. trả undefined nếu phía trước nó không có gì
console.log(customerUser.company?.name);
console.log(customerUser.company?.name ?? 'khách lẻ');

// Không có ?. thì chương trình dừng với TypeError
console.log(customerUser.company.name);
```

```bash
node bai-05-object-json/04-thuoc-tinh-thieu.js
```

Kết quả:

```bash
undefined
chưa có số
undefined
khách lẻ
console.log(customerUser.company.name);
                                 ^

TypeError: Cannot read properties of undefined (reading 'name')
```

Đọc một key không có thì ra `undefined`, chương trình vẫn chạy. Đọc tiếp **vào bên trong** `undefined` thì dừng ngay với `TypeError`, lỗi gặp nhiều nhất với dữ liệu API. Dấu `?.` (optional chaining) chặn lỗi đó; thêm `??` của bài điều kiện để có giá trị mặc định.

> ⚠️ Không rải `?.` khắp nơi. Dữ liệu **bắt buộc phải có** (như email tài khoản test) mà thiếu thì phải để chương trình báo lỗi, test mới dừng đúng chỗ.

## ✅ Phần 2: Duyệt Object và mảng các Object

### 🔆 1. Object.keys, Object.values, Object.entries

Object không duyệt trực tiếp bằng `for...of` được. Ba hàm sau đổi Object thành **mảng** (mảng key, mảng giá trị, mảng các cặp) để duyệt như bài trước. Tạo file `bai-05-object-json/05-duyet-object.js`:

```javascript
const config = {
  baseUrl: 'https://crm.anhtester.com',
  timeout: 30000,
  headless: true,
};

console.log(Object.keys(config));
console.log(Object.values(config));
console.log(Object.entries(config));

for (const key of Object.keys(config)) {
  console.log(`${key} = ${config[key]}`);
}
```

```bash
node bai-05-object-json/05-duyet-object.js
```

Kết quả:

```bash
[ 'baseUrl', 'timeout', 'headless' ]
[ 'https://crm.anhtester.com', 30000, true ]
[
  [ 'baseUrl', 'https://crm.anhtester.com' ],
  [ 'timeout', 30000 ],
  [ 'headless', true ]
]
baseUrl = https://crm.anhtester.com
timeout = 30000
headless = true
```

### 🔆 2. Mảng các Object: danh sách tài khoản test

Danh bạ điện thoại là một danh sách, mỗi dòng là một người có tên và số. Data test cũng vậy: **mảng** giữ danh sách, mỗi phần tử là một **Object**. CRM demo có 3 vai trò. Tạo file `bai-05-object-json/06-mang-object.js`:

```javascript
const users = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
  { email: 'projectmanager@example.com', role: 'project-manager', loginPath: '/admin/authentication' },
  { email: 'customer@example.com', role: 'customer', loginPath: '/authentication/login' },
];

// Duyệt từng tài khoản
for (const user of users) {
  console.log(`${user.role} -> ${user.email}`);
}

// find: lấy MỘT tài khoản theo vai trò
const customer = users.find((user) => user.role === 'customer');
console.log(customer);

// filter: lấy CÁC tài khoản đăng nhập ở khu quản trị
const adminAreaUsers = users.filter((user) => user.loginPath === '/admin/authentication');
console.log(adminAreaUsers.length);

// find không thấy thì trả undefined
const guest = users.find((user) => user.role === 'guest');
console.log(guest?.email ?? 'không có tài khoản guest');
```

```bash
node bai-05-object-json/06-mang-object.js
```

Kết quả:

```bash
admin -> admin@example.com
project-manager -> projectmanager@example.com
customer -> customer@example.com
{
  email: 'customer@example.com',
  role: 'customer',
  loginPath: '/authentication/login'
}
2
không có tài khoản guest
```

Đây là hình dạng data test của hầu hết project. Dòng cuối: `?.` hữu ích khi `find` không tìm thấy gì.

## ✅ Phần 3: JSON - đổi Object thành văn bản và ngược lại

### 🔆 1. JSON khác Object ở đâu?

Muốn gửi thông tin liên hệ của một người qua tin nhắn, bạn phải **viết nó ra thành chữ**. Object cũng vậy: muốn lưu ra file hay gửi qua mạng thì phải đổi thành văn bản. **JSON** là quy cách viết văn bản đó, giống Object nhưng luật chặt hơn:

<table class="rt-table">
<thead>
<tr>
<th>Điểm so sánh</th>
<th>Object trong code JavaScript</th>
<th>JSON</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bản chất</td>
<td>Dữ liệu trong bộ nhớ</td>
<td>Một <strong>chuỗi văn bản</strong></td>
</tr>
<tr>
<td>Tên key và chuỗi</td>
<td>Key không cần dấu nháy; chuỗi dùng nháy nào cũng được</td>
<td>Bắt buộc <strong>ngoặc kép</strong></td>
</tr>
<tr>
<td>Dấu phẩy sau phần tử cuối</td>
<td>Được phép</td>
<td>Không được phép</td>
</tr>
<tr>
<td>Comment, hàm, <code>undefined</code></td>
<td>Được phép</td>
<td>Không có</td>
</tr>
</tbody>
</table>

Bạn đã gặp JSON ở file `package.json`; sau này gặp tiếp ở file data test và dữ liệu API.

### 🔆 2. JSON.stringify: Object thành chuỗi JSON

Tạo file `bai-05-object-json/07-json-stringify.js`:

```javascript
const result = {
  testName: 'Mở trang đăng nhập Admin',
  status: 'passed',
  durationMs: 1250,
  note: undefined,
  tags: ['login', 'smoke'],
};

const jsonText = JSON.stringify(result);
console.log(typeof result);
console.log(typeof jsonText);
console.log(jsonText);

// Tham số thứ 3 là số dấu cách thụt lề: in ra dễ đọc
console.log(JSON.stringify(result, null, 2));
```

```bash
node bai-05-object-json/07-json-stringify.js
```

Kết quả:

```bash
object
string
{"testName":"Mở trang đăng nhập Admin","status":"passed","durationMs":1250,"tags":["login","smoke"]}
{
  "testName": "Mở trang đăng nhập Admin",
  "status": "passed",
  "durationMs": 1250,
  "tags": [
    "login",
    "smoke"
  ]
}
```

Thuộc tính `note` có giá trị `undefined` **biến mất** khỏi JSON. `JSON.stringify(result, null, 2)` là cách in Object ra log cho dễ đọc: số `2` là số dấu cách thụt lề.

### 🔆 3. JSON.parse: chuỗi JSON thành Object

Tạo file `bai-05-object-json/08-json-parse.js`:

```javascript
// Chuỗi JSON, ví dụ nội dung một file .json hoặc dữ liệu API trả về
const jsonText = '{"email":"admin@example.com","role":"admin","isActive":true}';

console.log(jsonText.role); // chuỗi thì không có thuộc tính role

const user = JSON.parse(jsonText);
console.log(typeof user);
console.log(user.role);
console.log(user);
```

```bash
node bai-05-object-json/08-json-parse.js
```

Kết quả:

```bash
undefined
object
admin
{ email: 'admin@example.com', role: 'admin', isActive: true }
```

Chưa `parse` thì `jsonText` chỉ là chuỗi, `jsonText.role` ra `undefined`. Ở chương API, `await response.json()` của Playwright làm sẵn bước `parse` này.

### 🔆 4. Đọc lỗi khi JSON sai

JSON sai một ký tự là `JSON.parse` dừng với `SyntaxError`. Hai lỗi gặp nhiều nhất khi sửa file `.json` bằng tay: thừa dấu phẩy cuối và dùng nháy đơn. File `bai-05-object-json/09-json-loi-dau-phay.js`:

```javascript
// Lỗi 1: thừa dấu phẩy sau thuộc tính cuối
const jsonText = '{"email":"admin@example.com","role":"admin",}';
const user = JSON.parse(jsonText);
console.log(user);
```

```bash
node bai-05-object-json/09-json-loi-dau-phay.js
```

Kết quả:

```bash
<anonymous_script>:1
{"email":"admin@example.com","role":"admin",}
                                            ^

SyntaxError: Expected double-quoted property name in JSON at position 44 (line 1 column 45)
    at JSON.parse (<anonymous>)
```

File `bai-05-object-json/10-json-loi-nhay-don.js`:

```javascript
// Lỗi 2: dùng nháy đơn thay cho ngoặc kép
const jsonText = "{'email':'admin@example.com'}";
const user = JSON.parse(jsonText);
console.log(user);
```

```bash
node bai-05-object-json/10-json-loi-nhay-don.js
```

Kết quả:

```bash
<anonymous_script>:1
{'email':'admin@example.com'}
 ^

SyntaxError: Expected property name or '}' in JSON at position 1 (line 1 column 2)
    at JSON.parse (<anonymous>)
```

Dấu `^` và cụm `line ... column ...` chỉ đúng ký tự làm hỏng JSON: dấu `}` ngay sau dấu phẩy, và nháy đơn ở cột 2.

### 🔆 5. Đọc data test từ file .json

Tạo file data `bai-05-object-json/data/users.json`:

```json
[
  {
    "email": "admin@example.com",
    "role": "admin",
    "loginPath": "/admin/authentication"
  },
  {
    "email": "projectmanager@example.com",
    "role": "project-manager",
    "loginPath": "/admin/authentication"
  },
  {
    "email": "customer@example.com",
    "role": "customer",
    "loginPath": "/authentication/login"
  }
]
```

Rồi tạo file `bai-05-object-json/11-doc-file-json.js`:

```javascript
const fs = require('node:fs');

// Đường dẫn tính từ thư mục project, nơi bạn gõ lệnh node
const jsonText = fs.readFileSync('bai-05-object-json/data/users.json', 'utf8');
console.log(typeof jsonText);

const users = JSON.parse(jsonText);
console.log(users.length);

const pm = users.find((user) => user.role === 'project-manager');
console.log(pm.email);
```

```bash
node bai-05-object-json/11-doc-file-json.js
```

Kết quả:

```bash
string
3
projectmanager@example.com
```

`require('node:fs')` lấy bộ công cụ đọc ghi file của Node.js (cú pháp `import` học ở bài async/await, import/export). `readFileSync` trả về **chuỗi**, `JSON.parse` đổi nó thành mảng các Object.

> 🔒 File `.json` được đưa lên Git cùng code nên **không ghi mật khẩu vào đó**; mật khẩu chỉ đọc qua `process.env.ADMIN_PASSWORD`.

## ✅ Phần 4: Lấy nhanh giá trị từ Object (destructuring)

### 🔆 1. Lấy nhanh, đổi tên, giá trị mặc định

Thay vì lặp lại `user.email`, `user.role`, JavaScript có cú pháp lấy nhanh (**destructuring**). Tạo file `bai-05-object-json/12-lay-nhanh.js`:

```javascript
const user = {
  email: 'admin@example.com',
  role: 'admin',
  loginPath: '/admin/authentication',
};

// Cách cũ: mỗi thuộc tính một dòng
const email1 = user.email;
const role1 = user.role;
console.log(email1, role1);

// Lấy nhanh: tên biến trùng tên key
const { email, role } = user;
console.log(email, role);

// Đổi tên biến: lấy key loginPath, đặt vào biến adminLoginPath
const { loginPath: adminLoginPath } = user;
console.log(adminLoginPath);

// Giá trị mặc định khi key không có
const { timeout = 30000 } = user;
console.log(timeout);
```

```bash
node bai-05-object-json/12-lay-nhanh.js
```

Kết quả:

```bash
admin@example.com admin
admin@example.com admin
/admin/authentication
30000
```

Dấu `{ }` nằm **bên trái** dấu `=` không tạo Object. Nó nghĩa là: "lấy trong Object bên phải các key có tên này, đặt vào biến cùng tên". Trong `{ loginPath: adminLoginPath }`, bên trái dấu hai chấm là tên key, bên phải là tên biến mới.

### 🔆 2. Lấy nhanh ngay ở tham số của hàm

Tạo file `bai-05-object-json/13-lay-nhanh-tham-so.js` (hàm học kỹ ở bài kế tiếp, ở đây chỉ cần nhìn phần trong ngoặc tròn):

```javascript
const baseUrl = 'https://crm.anhtester.com';

// Cách 1: nhận cả Object, bên trong đọc bằng dấu chấm
function describeLogin1(user) {
  console.log(`[${user.role}] mở ${baseUrl}${user.loginPath}`);
}

// Cách 2: lấy nhanh ngay ở chỗ nhận tham số
function describeLogin2({ role, loginPath }) {
  console.log(`[${role}] mở ${baseUrl}${loginPath}`);
}

const customer = {
  email: 'customer@example.com',
  role: 'customer',
  loginPath: '/authentication/login',
};

describeLogin1(customer);
describeLogin2(customer);
```

```bash
node bai-05-object-json/13-lay-nhanh-tham-so.js
```

Kết quả:

```bash
[customer] mở https://crm.anhtester.com/authentication/login
[customer] mở https://crm.anhtester.com/authentication/login
```

Với cách 2, nhìn dòng đầu của hàm là biết nó cần đúng `role` và `loginPath`.

### 🔆 3. Vì sao test Playwright viết async ({ page }) => {}

Mọi test Playwright đều có dạng sau:

```typescript
test('mở trang đăng nhập', async ({ page }) => {
  await page.goto('https://crm.anhtester.com/admin/authentication');
});
```

Khi chạy test, Playwright chuẩn bị [**một Object**](https://playwright.dev/docs/test-fixtures#built-in-fixtures) chứa `page`, `context`, `browser`, `request`, `browserName`... rồi truyền cả Object đó vào hàm của bạn. `{ page }` chính là lấy nhanh ở tham số như mục trên. File `bai-05-object-json/14-vi-sao-page.js` mô phỏng cơ chế đó bằng một hàm giả, không cần Playwright:

```javascript
// Hàm giả, mô phỏng cách Playwright chạy một test
function fakeRunTest(testFn) {
  // Playwright chuẩn bị sẵn MỘT Object chứa nhiều thứ...
  const fixtures = {
    page: 'trang giả',
    context: 'context giả',
    browserName: 'chromium',
  };
  // ...rồi truyền cả Object đó vào hàm test của bạn
  testFn(fixtures);
}

// Viết đúng: dấu { } lấy nhanh page ra khỏi Object
fakeRunTest(({ page }) => {
  console.log('Có ngoặc nhọn   :', page);
});

// Lấy nhiều thứ cùng lúc
fakeRunTest(({ page, browserName }) => {
  console.log('Lấy hai giá trị :', page, '|', browserName);
});

// Viết sai: thiếu { } nên "page" là CẢ Object
fakeRunTest((page) => {
  console.log('Thiếu ngoặc nhọn:', page);
});
```

```bash
node bai-05-object-json/14-vi-sao-page.js
```

Kết quả:

```bash
Có ngoặc nhọn   : trang giả
Lấy hai giá trị : trang giả | chromium
Thiếu ngoặc nhọn: { page: 'trang giả', context: 'context giả', browserName: 'chromium' }
```

Dòng cuối là lỗi hay gặp: viết `(page)` thiếu ngoặc nhọn thì biến `page` là **cả Object**, không phải trang. Với Playwright thật, test viết như vậy không chạy được: Playwright dừng ngay và báo lỗi `First argument must use the object destructuring pattern` (tạm dịch: tham số đầu tiên phải dùng cách lấy nhanh giá trị từ Object).

## ✅ Phần 5: Gộp và ghi đè Object bằng dấu ... (spread)

### 🔆 1. Chép Object mẫu rồi sửa vài chỗ

Tờ khai mẫu đã điền sẵn hầu hết các ô, mỗi người chỉ sửa vài ô. Dấu `...` đặt trước một Object (**spread**) nghĩa là "trải toàn bộ thuộc tính của nó vào đây". Tạo file `bai-05-object-json/15-gop-ghi-de.js`:

```javascript
// Tờ khai mẫu: điền sẵn các giá trị hay dùng
const defaultUser = {
  email: 'admin@example.com',
  role: 'admin',
  loginPath: '/admin/authentication',
  isActive: true,
};

// Chép toàn bộ defaultUser, chỉ sửa 2 ô
const pmUser = {
  ...defaultUser,
  email: 'projectmanager@example.com',
  role: 'project-manager',
};

console.log(pmUser);
console.log(defaultUser.role); // tờ khai mẫu không bị đổi

// Sai thứ tự: giá trị mặc định đè lại giá trị mới
const wrongUser = {
  email: 'projectmanager@example.com',
  ...defaultUser,
};
console.log(wrongUser.email);
```

```bash
node bai-05-object-json/15-gop-ghi-de.js
```

Kết quả:

```bash
{
  email: 'projectmanager@example.com',
  role: 'project-manager',
  loginPath: '/admin/authentication',
  isActive: true
}
admin
admin@example.com
```

Luật duy nhất: **key viết sau ghi đè key viết trước**. Vì vậy `...defaultUser` phải đứng **đầu**. Đảo thứ tự như `wrongUser` thì email mới bị giá trị mặc định đè mất mà không có thông báo lỗi nào.

### 🔆 2. Gộp config mặc định với config theo môi trường

Tạo file `bai-05-object-json/16-gop-config.js`:

```javascript
const baseConfig = {
  baseUrl: 'https://crm.anhtester.com',
  timeout: 30000,
  headless: true,
};

// Phần khác biệt của từng môi trường
const envConfigs = {
  dev: { baseUrl: 'http://localhost:8080', headless: false },
  staging: { timeout: 60000 },
};

const env = process.env.ENV ?? 'staging';
const envConfig = envConfigs[env] ?? {};

const config = { ...baseConfig, ...envConfig };

console.log(`Môi trường: ${env}`);
console.log(config);
```

```bash
node bai-05-object-json/16-gop-config.js
```

Kết quả:

```bash
Môi trường: staging
{
  baseUrl: 'https://crm.anhtester.com',
  timeout: 60000,
  headless: true
}
```

`staging` chỉ khai báo phần khác biệt; phần còn lại lấy từ `baseConfig`. Bài điều kiện chọn theo `ENV` bằng `switch`; ở đây `envConfigs[env]` làm việc đó bằng cách tra key. Đặt biến môi trường `ENV` là `dev` rồi chạy lại:

```bash
Môi trường: dev
{ baseUrl: 'http://localhost:8080', timeout: 30000, headless: false }
```

Bạn sẽ gặp đúng cú pháp này trong file `playwright.config.ts` ở chương cấu hình Playwright: `devices['Desktop Chrome']` là một Object có sẵn, được trải vào `use`.

```typescript
projects: [
  {
    name: 'chromium',
    use: { ...devices['Desktop Chrome'] },
  },
],
```

### 🔆 3. Cảnh báo: dấu ... chỉ sao chép một tầng

Tạo file `bai-05-object-json/17-sao-chep-nong.js`:

```javascript
const baseConfig = {
  baseUrl: 'https://crm.anhtester.com',
  viewport: { width: 1280, height: 720 },
};

const mobileConfig = { ...baseConfig };

// Thuộc tính tầng ngoài: sửa bản sao, bản gốc giữ nguyên
mobileConfig.baseUrl = 'https://m.crm.anhtester.com';
console.log(baseConfig.baseUrl);

// Object lồng bên trong: hai bản vẫn dùng CHUNG
mobileConfig.viewport.width = 390;
console.log(baseConfig.viewport.width);

// Cách đúng: tạo Object mới cho cả phần lồng
const tabletConfig = {
  ...baseConfig,
  viewport: { ...baseConfig.viewport, width: 768 },
};
console.log(tabletConfig.viewport.width, baseConfig.viewport.width);

// Dấu ... cũng gộp được mảng
const browsers = [...['chromium', 'firefox'], ...['webkit']];
console.log(browsers);
```

```bash
node bai-05-object-json/17-sao-chep-nong.js
```

Kết quả:

```bash
https://crm.anhtester.com
390
768 390
[ 'chromium', 'firefox', 'webkit' ]
```

Dòng kết quả thứ hai là chỗ nguy hiểm: sửa `viewport` của bản sao mà bản gốc cũng thành `390`. Dấu `...` chỉ chép **tầng ngoài cùng** (shallow copy); Object lồng bên trong vẫn dùng chung, nên test này sửa config có thể làm hỏng test khác. Cách xử lý: trải thêm cho phần lồng như `tabletConfig`, hoặc dùng `structuredClone(obj)` để sao chép mọi tầng.

## ✅ Phần 6: Thực hành - chuẩn bị data test cho trang đăng nhập CRM

Gom cả bài vào một file: đọc `data/users.json`, chọn tài khoản Admin, gộp config, lấy nhanh giá trị, in kết quả dạng JSON. Tạo file `bai-05-object-json/crm-test-data.js`:

```javascript
const fs = require('node:fs');

// ===== 1. Đọc data test từ file JSON =====
const users = JSON.parse(fs.readFileSync('bai-05-object-json/data/users.json', 'utf8'));

// ===== 2. Chọn tài khoản theo vai trò =====
const user = users.find((item) => item.role === 'admin');

// ===== 3. Gộp config mặc định với config theo môi trường =====
const baseConfig = { baseUrl: 'https://crm.anhtester.com', timeout: 30000, headless: true };
const envConfigs = { staging: { timeout: 60000 } };
const env = process.env.ENV ?? 'staging';
const config = { ...baseConfig, ...(envConfigs[env] ?? {}) };

// ===== 4. Lấy nhanh các giá trị cần dùng =====
const { baseUrl, timeout } = config;
const { email, role, loginPath } = user;

// ===== 5. Ghi lại kết quả chuẩn bị dưới dạng JSON =====
const result = {
  env,
  role,
  loginUrl: `${baseUrl}${loginPath}`,
  email,
  password: process.env.ADMIN_PASSWORD ? '***' : 'CHƯA ĐẶT BIẾN ADMIN_PASSWORD',
  timeout,
};

console.log(JSON.stringify(result, null, 2));
```

```bash
node bai-05-object-json/crm-test-data.js
```

Kết quả:

```bash
{
  "env": "staging",
  "role": "admin",
  "loginUrl": "https://crm.anhtester.com/admin/authentication",
  "email": "admin@example.com",
  "password": "CHƯA ĐẶT BIẾN ADMIN_PASSWORD",
  "timeout": 60000
}
```

Thuộc tính `password` không chứa mật khẩu thật: đã đặt `ADMIN_PASSWORD` thì log chỉ in `***`. Thử tự phá: đổi `'admin'` ở bước 2 thành `'guest'` rồi chạy lại, `find` trả `undefined` và bước 4 dừng với `TypeError`.

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức của bài

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn dùng được các prompt dưới đây: chỗ có `@đường-dẫn` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay. Không dán mật khẩu hay file `.env` vào khung chat.

```markdown
Tôi mới học JavaScript, chưa học Playwright. Giải thích giúp tôi phần ({ page }) trong đoạn test sau:

test('mở trang đăng nhập', async ({ page }) => {
  await page.goto('https://crm.anhtester.com/admin/authentication');
});

1. Dấu { } ở đây có phải là tạo Object không?
2. Ngoài page, tôi còn lấy ra được những gì? Dẫn link tài liệu playwright.dev.
3. Nếu viết (page) thiếu ngoặc nhọn thì chuyện gì xảy ra?
Viết thêm một ví dụ JavaScript thuần chạy được bằng node, không cần Playwright, để mô phỏng cơ chế này.
```

```markdown
File JSON sau bị lỗi khi JSON.parse. Hãy chỉ ra TỪNG chỗ sai (dòng nào, ký tự nào, vi phạm luật gì của JSON),
sau đó mới đưa bản đã sửa. Không thêm, không bớt dữ liệu.

{
  // tài khoản quản trị
  'email': "admin@example.com",
  "role": "admin",
  "isActive": True,
}
```

```markdown
Chuyển Object JavaScript trong file @bai-05-object-json/06-mang-object.js (biến users) thành JSON hợp lệ,
thụt lề 2 dấu cách, để tôi lưu vào file data/users.json.
Nếu có thuộc tính nào JSON không biểu diễn được (hàm, undefined) thì liệt kê ra, đừng tự ý bỏ.
```

```markdown
Đọc file @bai-05-object-json/17-sao-chep-nong.js. Giải thích vì sao tôi sửa mobileConfig.viewport.width
mà baseConfig.viewport.width cũng đổi, trong khi sửa mobileConfig.baseUrl thì bản gốc giữ nguyên.
Vẽ sơ đồ bằng chữ cho thấy biến nào đang trỏ tới Object nào. Chỉ giải thích, KHÔNG sửa file.
```

### 🔆 2. Bộ kit liên quan gì tới Object và JSON?

Rule [automation\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md) (mục 1) yêu cầu **tách test data khỏi code**, ví dụ ra file JSON. Lệnh [/generate-test-data](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/generate-test-data.md) sinh data test với định dạng mặc định là **JSON**. Lệnh này dùng từ chương Playwright.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Rà code và data AI viết theo bảng sau:

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
<td>Mật khẩu thật nằm trong Object hoặc file <code>.json</code></td>
<td>Lộ thông tin đăng nhập khi đưa code lên Git</td>
<td>Xoá khỏi data; đọc từ <code>process.env.ADMIN_PASSWORD</code></td>
</tr>
<tr>
<td>File <code>.json</code> có comment, nháy đơn, dấu phẩy sau phần tử cuối</td>
<td><code>JSON.parse</code> dừng với <code>SyntaxError</code></td>
<td>Sửa theo vị trí lỗi báo</td>
</tr>
<tr>
<td><code>JSON.parse(user)</code> khi <code>user</code> đã là Object</td>
<td>Lỗi <code><span>"[object</span> <span>Object]"</span> <span>is</span> <span>not</span> <span>valid</span> <span>JSON</span></code></td>
<td>Bỏ <code>JSON.parse</code></td>
</tr>
<tr>
<td><code>actual === expected</code> với hai Object</td>
<td>So xem có <strong>cùng một Object</strong> không, không so nội dung: <code>{ a: 1 } === { a: 1 }</code> ra <code>false</code></td>
<td>So từng thuộc tính</td>
</tr>
<tr>
<td><code><span>{</span> <span>email:</span> <span>'...',</span> <span>...defaultUser</span> <span>}</span></code></td>
<td>Giá trị mặc định viết sau nên đè mất giá trị mới</td>
<td>Đưa <code>...defaultUser</code> lên đầu</td>
</tr>
<tr>
<td>Sao chép bằng <code>{ ...config }</code> rồi sửa Object lồng</td>
<td>Bản gốc đổi theo, test này làm hỏng test khác</td>
<td>Trải thêm phần lồng, hoặc <code>structuredClone</code></td>
</tr>
<tr>
<td><code>data.user.profile.name</code> với dữ liệu có thể thiếu</td>
<td><code><span>TypeError:</span> Cannot read properties of undefined</code></td>
<td>Thêm <code>?.</code> ở chỗ có thể thiếu</td>
</tr>
<tr>
<td><code>async (page) =&gt; {}</code> trong test Playwright</td>
<td>Thiếu ngoặc nhọn: <code>page</code> không phải là trang</td>
<td>Sửa thành <code>async ({ page }) =&gt; {}</code></td>
</tr>
</tbody>
</table>

## ✅ Phần 9: Bài tập thực hành

Đặt file bài tập trong thư mục `bai-05-object-json/`.

**Bài tập 1 - Thêm tài khoản và lọc.** Thêm vào `data/users.json` thuộc tính `"isActive"` cho cả 3 tài khoản (Customer là `false`). Tạo file `bt1-loc-tai-khoan.js`: đọc file, `filter` tài khoản đang hoạt động, dùng `for...of` và lấy nhanh `{ email, role }` để in mỗi tài khoản một dòng (kết quả đúng có 2 dòng).

**Bài tập 2 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt2-duyet-code.js`, chép vào và chạy:

```javascript
const defaultUser = { email: 'admin@example.com', role: 'admin', profile: { language: 'en' } };

const customer = { role: 'customer', ...defaultUser };
console.log(customer.role);

const copy = { ...defaultUser };
copy.profile.language = 'vi';
console.log(defaultUser.profile.language);

const sameData = { role: 'admin' };
console.log(sameData === { role: 'admin' });

console.log(defaultUser.company.name);

const user = JSON.parse(defaultUser);
console.log(user.email);
```

Kết quả chạy thật:

```bash
admin
vi
false
console.log(defaultUser.company.name);
                                ^

TypeError: Cannot read properties of undefined (reading 'name')
```

Có 5 chỗ sai, mỗi chỗ ứng với một dòng của bảng ở Phần 8; chỗ thứ năm chỉ lộ ra sau khi sửa chỗ thứ tư. Sửa xong, file phải in lần lượt: `customer`, `en`, `true`, `chưa có công ty`, `admin@example.com`.

## ✅ Phần 10: Ghi nhớ nhanh

- Object gom nhiều cặp `key: value` của một đối tượng; data test thường là **mảng các Object**. Đọc bằng dấu chấm; dùng ngoặc vuông khi key có ký tự đặc biệt hoặc nằm trong biến.
- Key không có thì ra `undefined`; đọc sâu hơn là `TypeError`, chặn bằng `?.` và `??`.
- JSON là **chuỗi**: ngoặc kép, không comment, không dấu phẩy cuối. `JSON.parse` đổi chuỗi thành Object, `JSON.stringify(obj, null, 2)` đổi ngược lại.
- `const { email, role } = user` là lấy nhanh giá trị. `async ({ page }) => {}` lấy nhanh `page` từ Object Playwright truyền vào.
- `{ ...macDinh, key: giaTriMoi }`: key viết sau ghi đè key viết trước. Dấu `...` chỉ sao chép một tầng.
- Mật khẩu không nằm trong Object hay file JSON, chỉ có tên biến môi trường.

✅ **Kết luận:** Bạn đã có dữ liệu test gọn trong Object và JSON. Nhưng các bước xử lý vẫn viết thẳng từ trên xuống, muốn dùng lại phải chép lại. Bài kế tiếp, **Hàm, arrow function và callback trong JavaScript**, gói các bước đó thành hàm để gọi lại, và giải thích nốt `async ({ page }) => {}`: bản thân nó là một arrow function.

---

## Bài tập riêng — Object, JSON, destructuring và spread cho data test

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-95](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-95)

**Mục tiêu:** đọc data test từ file JSON, lọc và lấy nhanh thuộc tính, gộp Object mà không làm hỏng dữ liệu gốc.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-05-object-json`

### 📝 Đề bài

#### Bài tập 1 - Thêm thuộc tính và lọc tài khoản

Thêm vào `data/users.json` của bài học thuộc tính `"isActive"` cho cả 3 tài khoản (Customer là `false`). Tạo file `bt1-loc-tai-khoan.js`: đọc file, `filter` tài khoản đang hoạt động, dùng `for...of` và lấy nhanh `{ email, role }` để in mỗi tài khoản một dòng.

#### Bài tập 2 - Duyệt code AI

Tạo file `bt2-duyet-code.js`, chép đoạn code AI viết dưới đây và chạy. Có **5 chỗ sai**, mỗi chỗ ứng với một dòng của bảng ở Phần 8; chỗ thứ năm chỉ lộ ra sau khi sửa chỗ thứ tư.

```javascript
const defaultUser = { email: 'admin@example.com', role: 'admin', profile: { language: 'en' } };
const customer = { role: 'customer', ...defaultUser };
console.log(customer.role);
const copy = { ...defaultUser };
copy.profile.language = 'vi';
console.log(defaultUser.profile.language);
const sameData = { role: 'admin' };
console.log(sameData === { role: 'admin' });
console.log(defaultUser.company.name);
const user = JSON.parse(defaultUser);
console.log(user.email);
```

### 📦 Cách nộp bài

1. Mở ô **Nội dung bài làm (Editor)**. Với mỗi file: bấm **Đoạn code mẫu**, chọn ngôn ngữ, dán **toàn bộ** code. Dòng đầu là comment đường dẫn file, ví dụ `// bai-05-object-json/bt1-....js`.
2. Ngay dưới mỗi file, chèn thêm một **Đoạn code mẫu** chọn **Text / Log** và dán **kết quả chạy thật** copy từ Terminal (không gõ lại bằng tay).
3. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*, sau đó dán file đã sửa và kết quả chạy.
4. Đã đưa project lên GitHub (học ở Bài 7) thì dán thêm link thư mục bài vào ô **Link GitHub**.
5. Bài tập 1: dán cả nội dung `data/users.json` sau khi sửa (chọn ngôn ngữ JSON). **Không** dán mật khẩu thật, file chỉ ghi email và tên biến môi trường như bài học.

### ✅ Tiêu chí Đạt

- `users.json` hợp lệ (chạy `JSON.parse` không lỗi), đủ 3 tài khoản có `isActive`; Bài tập 1 in đúng 2 dòng (Admin và Project Manager), có dùng destructuring trong vòng `for...of`.
- Bài tập 2 sau khi sửa in lần lượt: `customer`, `en`, `true`, `chưa có công ty`, `admin@example.com`.
- Nêu đúng 5 lý do: spread đặt trước nên bị ghi đè; spread chỉ sao chép một tầng; `===` so địa chỉ chứ không so nội dung; truy cập thuộc tính của `undefined` (dùng `?.` và `??`); `JSON.parse` nhận chuỗi chứ không nhận Object.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.