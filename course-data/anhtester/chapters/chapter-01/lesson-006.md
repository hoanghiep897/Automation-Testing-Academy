# Bài 6 - [Javascript Typescript] Hàm, arrow function và callback trong JavaScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/404](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/404)

✅ Vì sao cần hàm: khai báo, tham số và giá trị trả về  
✅ Tham số mặc định, truyền Object làm tham số và phạm vi của biến trong khối lệnh  
✅ Arrow function - cách viết hàm ngắn gọn  
✅ Callback và cách đọc một test Playwright viết bằng arrow function  
✅ Thực hành gói bước chuẩn bị data đăng nhập CRM thành các hàm nhỏ  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra hàm do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước, dữ liệu test đã gọn trong Object và JSON, nhưng các bước xử lý vẫn viết thẳng từ trên xuống, muốn dùng lại phải chép lại. Bài này gói các bước đó thành **hàm**, viết gọn bằng **arrow function**, hiểu **callback**, rồi đọc trọn một test Playwright. Học xong bạn sẽ:

- Khai báo, gọi hàm; phân biệt hàm in ra với hàm trả về giá trị.
- Dùng tham số mặc định và truyền Object làm tham số.
- Biết biến khai báo trong khối `{ }` nào chỉ dùng được trong khối đó.
- Đọc và viết arrow function, tránh lỗi quên `return`.
- Hiểu callback và đọc được từng phần của `test('...', async ({ page }) => { ... })`.

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật (Node.js v24.17.0), đã lược dòng đường dẫn file ở kết quả có lỗi.

## ✅ Phần 1: Hàm - viết một lần, gọi nhiều lần

### 🔆 1. Chuẩn bị thư mục cho bài học

Tạo thư mục `bai-06-ham` trong project. Mỗi ví dụ là một file trong thư mục đó:

```bash
js-ts-for-tester/
├── package.json
├── bai-05-object-json/
│   └── data/
│       └── users.json
└── bai-06-ham/
    ├── 01-pha-ca-phe.js
    ├── 02-ham-automation.js
    ├── 03-return.js
    ├── 04-tham-so-mac-dinh.js
    ├── 05-tham-so-object.js
    ├── 06-pham-vi-bien.js
    ├── 07-bien-toan-cuc.js
    ├── 08-arrow-function.js
    ├── 09-arrow-tra-object.js
    ├── 10-callback.js
    ├── 11-settimeout.js
    ├── 12-fake-test.js
    └── crm-login-helpers.js
```

### 🔆 2. Hàm là gì?

Công thức pha cà phê viết ra **một lần**, pha bao nhiêu ly cũng theo đó. Mỗi lần pha có thể đổi nguyên liệu, và thứ nhận về là một ly cà phê. **Hàm** (function) là một công thức như vậy: một đoạn code có tên, viết một lần, gọi lại nhiều lần.

Tạo file `bai-06-ham/01-pha-ca-phe.js`:

```javascript
// Công thức pha cà phê: viết MỘT lần, pha bao nhiêu ly cũng được
function phaCaPhe(loai, soThiaDuong) {
  const ly = `1 ly ${loai}, ${soThiaDuong} thìa đường`;
  return ly; // ly cà phê làm ra = giá trị trả về
}

// Gọi hàm: mỗi lần một nguyên liệu khác
const lyCuaAn = phaCaPhe('cà phê sữa', 2);
const lyCuaBinh = phaCaPhe('cà phê đen', 0);

console.log(lyCuaAn);
console.log(lyCuaBinh);
```

```bash
node bai-06-ham/01-pha-ca-phe.js
```

Kết quả:

```bash
1 ly cà phê sữa, 2 thìa đường
1 ly cà phê đen, 0 thìa đường
```

- `function phaCaPhe(loai, soThiaDuong) { ... }` là **khai báo hàm**. `loai`, `soThiaDuong` là **tham số**: nguyên liệu hàm cần.
- `return ly;` là **giá trị trả về**: thứ hàm đưa lại cho nơi gọi.
- `phaCaPhe('cà phê sữa', 2)` là **gọi hàm**: tên hàm kèm cặp ngoặc tròn. Giá trị truyền vào lúc gọi là **đối số**. Chưa gọi thì code trong hàm chưa chạy.

### 🔆 3. Hàm trong automation

Ghép URL, đổi mã HTTP thành `PASS`/`FAIL`, kiểm tra email: gói mỗi việc thành một hàm. Tạo file `bai-06-ham/02-ham-automation.js`:

```javascript
// Ghép địa chỉ trang từ địa chỉ gốc và đường dẫn
function buildUrl(baseUrl, path) {
  return `${baseUrl}${path}`;
}

// Đổi mã HTTP thành kết quả kiểm tra
function checkStatus(code) {
  if (code === 200) {
    return 'PASS';
  }
  return 'FAIL';
}

// Kiểm tra email ở mức đơn giản: có @ và không có dấu cách
function isValidEmail(email) {
  return email.includes('@') && !email.includes(' ');
}

const baseUrl = 'https://crm.anhtester.com';

console.log(buildUrl(baseUrl, '/admin/authentication'));
console.log(buildUrl(baseUrl, '/authentication/login'));
console.log(checkStatus(200), checkStatus(404));
console.log(isValidEmail('admin@example.com'), isValidEmail('admin.example.com'));
```

```bash
node bai-06-ham/02-ham-automation.js
```

Kết quả:

```bash
https://crm.anhtester.com/admin/authentication
https://crm.anhtester.com/authentication/login
PASS FAIL
true false
```

Tên hàm bắt đầu bằng **động từ** (`build`, `check`); hàm trả `true`/`false` bắt đầu bằng `is`, để đọc lời gọi là hiểu hàm làm gì. Khi luật kiểm tra thay đổi, bạn sửa **một chỗ**. Chép đoạn code đó ra 10 file thì phải sửa 10 lần và dễ sót.

### 🔆 4. return: trả về giá trị và dừng hàm

Tạo file `bai-06-ham/03-return.js`:

```javascript
// Hàm 1: TRẢ VỀ giá trị
function tinhTong(a, b) {
  return a + b;
}

// Hàm 2: chỉ IN RA, không return
function inTong(a, b) {
  console.log('Tổng là', a + b);
}

// Hàm 3: tính xong nhưng QUÊN return
function tinhTongQuenReturn(a, b) {
  const tong = a + b;
}

const ketQua1 = tinhTong(2, 3);
const ketQua2 = inTong(2, 3);
const ketQua3 = tinhTongQuenReturn(2, 3);
console.log(ketQua1, ketQua2, ketQua3);

// return DỪNG hàm ngay: các dòng phía sau không chạy nữa
function checkStatus(code) {
  if (code >= 500) {
    return 'FAIL: lỗi phía server';
  }
  if (code !== 200) {
    return 'FAIL';
  }
  return 'PASS';
}

console.log(checkStatus(503));
console.log(checkStatus(200));
```

```bash
node bai-06-ham/03-return.js
```

Kết quả:

```bash
Tổng là 5
5 undefined undefined
FAIL: lỗi phía server
PASS
```

- **In ra khác trả về.** `inTong` in được `Tổng là 5` nhưng không đưa lại gì cho nơi gọi, nên `ketQua2` là `undefined`.
- **Thiếu `return` thì hàm trả `undefined`**, và JavaScript **không báo lỗi** (`ketQua3`).
- **`return` dừng hàm ngay.** Với `503`, hàm trả kết quả ở `if` đầu tiên, các dòng sau không chạy.

> ⚠️ Hàm tính toán, kiểm tra thì **trả về** giá trị. Hàm chỉ `console.log` thì code khác không dùng lại được kết quả.

## ✅ Phần 2: Tham số mặc định và tham số là Object

### 🔆 1. Tham số mặc định

Gọi đồ uống mà không dặn gì thì quán pha mức đường bình thường. Tham số của hàm cũng đặt sẵn được giá trị, dùng khi nơi gọi không truyền. Tạo file `bai-06-ham/04-tham-so-mac-dinh.js`:

```javascript
// baseUrl có giá trị mặc định: không truyền thì dùng CRM demo
function buildUrl(path, baseUrl = 'https://crm.anhtester.com') {
  return `${baseUrl}${path}`;
}

console.log(buildUrl('/admin/authentication'));
console.log(buildUrl('/admin/authentication', 'http://localhost:8080'));

// Sai: tham số mặc định đứng TRƯỚC tham số bắt buộc
function buildUrlSai(baseUrl = 'https://crm.anhtester.com', path) {
  return `${baseUrl}${path}`;
}

console.log(buildUrlSai('/admin/authentication'));
```

```bash
node bai-06-ham/04-tham-so-mac-dinh.js
```

Kết quả:

```bash
https://crm.anhtester.com/admin/authentication
http://localhost:8080/admin/authentication
/admin/authenticationundefined
```

Dòng thứ ba sai mà không có thông báo lỗi. Đối số được gán cho tham số **theo thứ tự từ trái sang phải**: `'/admin/authentication'` rơi vào `baseUrl`, còn `path` là `undefined`. Vì vậy tham số mặc định luôn đặt **sau** tham số bắt buộc.

### 🔆 2. Truyền Object làm tham số

Hàm nhiều tham số thì nơi gọi phải nhớ đúng thứ tự. Cách gọn hơn: nhận **một Object** và lấy nhanh ngay ở tham số, như bài trước. Tạo file `bai-06-ham/05-tham-so-object.js`:

```javascript
// Che mật khẩu trước khi đưa vào log
function maskPassword(password) {
  return password ? '***' : 'CHƯA ĐẶT';
}

// Nhận MỘT Object, lấy nhanh ngay ở tham số; role có giá trị mặc định
function describeLogin({ email, role = 'admin', password }) {
  return `[${role}] đăng nhập bằng ${email}, mật khẩu: ${maskPassword(password)}`;
}

console.log(describeLogin({ email: 'admin@example.com', password: process.env.ADMIN_PASSWORD }));

// Thứ tự key không quan trọng, vì lấy theo TÊN
console.log(describeLogin({ password: 'gia-tri-gia-de-thu', role: 'customer', email: 'customer@example.com' }));
```

```bash
node bai-06-ham/05-tham-so-object.js
```

Kết quả:

```bash
[admin] đăng nhập bằng admin@example.com, mật khẩu: CHƯA ĐẶT
[customer] đăng nhập bằng customer@example.com, mật khẩu: ***
```

Lời gọi ghi rõ tên từng giá trị nên không nhầm thứ tự; `role = 'admin'` dùng khi Object không có key `role`. `maskPassword` giữ cho log chỉ có `***`. Dòng đầu ra `CHƯA ĐẶT` vì máy chạy ví dụ chưa đặt biến `ADMIN_PASSWORD`.

> 🔒 Chuỗi `'gia-tri-gia-de-thu'` chỉ để thử hàm. Mật khẩu thật không viết vào code, chỉ đọc qua `process.env.ADMIN_PASSWORD`.

## ✅ Phần 3: Phạm vi của biến trong khối lệnh

### 🔆 1. Biến khai báo trong khối nào chỉ sống trong khối đó

Ghi chú trên bảng của một phòng họp thì chỉ người trong phòng đọc được. Biến khai báo bằng `let`, `const` cũng chỉ tồn tại trong cặp `{ }` chứa nó: thân hàm, `if` hay `for`. Tạo file `bai-06-ham/06-pham-vi-bien.js`:

```javascript
function buildLoginUrl() {
  const loginPath = '/admin/authentication'; // chỉ sống trong hàm này
  return `https://crm.anhtester.com${loginPath}`;
}
console.log(buildLoginUrl());

const status = 200;
if (status === 200) {
  const message = 'PASS'; // chỉ sống trong khối if
  console.log(message);
}

for (let i = 1; i <= 2; i++) {
  console.log('Lần', i); // i chỉ sống trong vòng for
}

// Ra ngoài khối { } thì biến không còn
console.log(loginPath);
```

```bash
node bai-06-ham/06-pham-vi-bien.js
```

Kết quả:

```bash
https://crm.anhtester.com/admin/authentication
PASS
Lần 1
Lần 2
console.log(loginPath);
            ^

ReferenceError: loginPath is not defined
```

Ở ngoài hàm không có biến `loginPath` nên chương trình dừng với `ReferenceError`; đọc `message` hay `i` ngoài khối của chúng cũng vậy. Chiều ngược lại thì được: code **trong** khối đọc được biến khai báo **bên ngoài** (khối `if` đọc được `status`). Muốn đưa giá trị trong hàm ra ngoài thì `return`. Nhờ luật này, hai hàm cùng đặt biến tên `user` mà không đụng nhau.

### 🔆 2. Vì sao không truyền dữ liệu giữa các hàm bằng biến toàn cục

Biến khai báo ngoài mọi khối là biến toàn cục: hàm nào cũng đọc và sửa được. Tạo file `bai-06-ham/07-bien-toan-cuc.js`:

```javascript
// KHÔNG nên: các hàm truyền dữ liệu cho nhau qua biến toàn cục
let currentRole = 'admin';

function describeUser() {
  return `Đang test với vai trò ${currentRole}`;
}

function switchToCustomer() {
  currentRole = 'customer'; // âm thầm đổi biến dùng chung
}

console.log(describeUser());
switchToCustomer();
console.log(describeUser()); // cùng một lời gọi, kết quả đã khác

// Nên: hàm cần gì thì nhận qua tham số
function describeRole(role) {
  return `Đang test với vai trò ${role}`;
}

console.log(describeRole('admin'));
console.log(describeRole('admin')); // gọi bao nhiêu lần cũng ra như nhau
```

```bash
node bai-06-ham/07-bien-toan-cuc.js
```

Kết quả:

```bash
Đang test với vai trò admin
Đang test với vai trò customer
Đang test với vai trò admin
Đang test với vai trò admin
```

Cùng lời gọi `describeUser()` mà ra hai kết quả, vì hàm khác đã sửa biến dùng chung. Trong bộ test, đây là lỗi khó tìm: test chạy riêng thì PASS, chạy chung thì FAIL vì test trước để lại giá trị. Hãy đưa dữ liệu vào hàm qua **tham số**, lấy ra qua **`return`**. Hằng số cấu hình như `baseUrl` ở đầu file thì không sao, vì không ai sửa nó.

## ✅ Phần 4: Arrow function - cách viết hàm ngắn gọn

### 🔆 1. Ba cách viết cùng một hàm

Bài vòng lặp và mảng đã dùng `v => v.includes('tươi')`. Đó là **arrow function**: hàm viết bằng mũi tên `=>`, không có từ khoá `function`. Tạo file `bai-06-ham/08-arrow-function.js`:

```javascript
// Cách 1: function thông thường
function tinhTong1(a, b) {
  return a + b;
}

// Cách 2: arrow function, thân có { } thì PHẢI viết return
const tinhTong2 = (a, b) => {
  return a + b;
};

// Cách 3: thân là một biểu thức, tự return
const tinhTong3 = (a, b) => a + b;

// Một tham số: bỏ được ngoặc tròn
const toUpper = text => text.toUpperCase();

// Không có tham số: giữ cặp ngoặc rỗng
const getBaseUrl = () => 'https://crm.anhtester.com';

console.log(tinhTong1(2, 3), tinhTong2(2, 3), tinhTong3(2, 3));
console.log(toUpper('admin'));
console.log(getBaseUrl());

// Lỗi hay gặp: thân có { } mà quên return
const tinhTongLoi = (a, b) => { a + b; };
console.log(tinhTongLoi(2, 3));
```

```bash
node bai-06-ham/08-arrow-function.js
```

Kết quả:

```bash
5 5 5
ADMIN
https://crm.anhtester.com
undefined
```

<table class="rt-table">
<thead>
<tr>
<th>Trường hợp</th>
<th>Cách viết</th>
<th>Luật</th>
</tr>
</thead>
<tbody>
<tr>
<td>Thân là một biểu thức</td>
<td><code>(a, b) =&gt; a + b</code></td>
<td>Tự trả về giá trị</td>
</tr>
<tr>
<td>Thân có <code>{ }</code></td>
<td><code><span>(a,</span> <span>b)</span> <span>=&gt;</span> <span>{</span> <span>return</span> <span>a</span> <span>+</span> <span>b;</span> <span>}</span></code></td>
<td><strong>Phải</strong> viết <code>return</code></td>
</tr>
<tr>
<td>Đúng một tham số</td>
<td><code><span>text</span> <span>=&gt;</span> <span>text.trim()</span></code></td>
<td>Bỏ được ngoặc tròn</td>
</tr>
<tr>
<td>Không có tham số</td>
<td><code>() =&gt; 'giá trị'</code></td>
<td>Giữ cặp ngoặc rỗng</td>
</tr>
</tbody>
</table>

Dòng cuối là lỗi gặp nhiều nhất: có `{ }` nhưng thiếu `return` nên ra `undefined`. Arrow function có khác `function` ở từ khoá `this`, nhưng code test hầu như không gặp, bạn bỏ qua được.

### 🔆 2. Trả về Object phải bọc trong ngoặc tròn

Tạo file `bai-06-ham/09-arrow-tra-object.js`:

```javascript
// Sai: JavaScript hiểu { } ngay sau => là THÂN HÀM, không phải Object
const createUserSai = (role) => { role: role };
console.log(createUserSai('admin'));

// Đúng: bọc Object trong ngoặc tròn
const createUser = (role) => ({ role: role, email: `${role}@example.com` });
console.log(createUser('admin'));
```

```bash
node bai-06-ham/09-arrow-tra-object.js
```

Kết quả:

```bash
undefined
{ role: 'admin', email: 'admin@example.com' }
```

Dấu `{` ngay sau `=>` luôn được hiểu là **mở thân hàm**. Bản sai không có `return` nên ra `undefined`, không báo lỗi. Muốn trả về Object thì bọc trong ngoặc tròn: `() => ({ ... })`.

## ✅ Phần 5: Callback và cách đọc một test Playwright

### 🔆 1. Callback: đưa một hàm cho hàm khác gọi lại

Gửi xe ở tiệm sửa, bạn để lại số điện thoại: "xong thì gọi lại cho tôi". **Callback** là một hàm bạn **truyền vào hàm khác**, để hàm kia gọi lại nó vào lúc cần. Tạo file `bai-06-ham/10-callback.js`:

```javascript
const users = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
  { email: 'projectmanager@example.com', role: 'project-manager', loginPath: '/admin/authentication' },
  { email: 'customer@example.com', role: 'customer', loginPath: '/authentication/login' },
];

// Hàm nhận MỘT HÀM KHÁC (callback), rồi gọi lại nó cho từng user
function chayVoiMoiUser(danhSach, callback) {
  for (const user of danhSach) {
    callback(user);
  }
}

// Cách 1: truyền một hàm có tên. Viết inEmail, KHÔNG viết inEmail()
function inEmail(user) {
  console.log('Email:', user.email);
}
chayVoiMoiUser(users, inEmail);

// Cách 2: viết thẳng một arrow function vào chỗ tham số
chayVoiMoiUser(users, (user) => {
  console.log(`[${user.role}] ${user.loginPath}`);
});

// map, find của mảng cũng nhận callback y như vậy
const roles = users.map((user) => user.role);
console.log(roles);

const findUserByRole = (list, role) => list.find((user) => user.role === role);
console.log(findUserByRole(users, 'customer').email);
console.log(findUserByRole(users, 'guest'));

// Sai: baoXong() là GỌI hàm ngay, rồi truyền KẾT QUẢ của nó (undefined) vào
function baoXong() {
  console.log('Đã xử lý xong');
}
chayVoiMoiUser(users, baoXong());
```

```bash
node bai-06-ham/10-callback.js
```

Kết quả:

```bash
Email: admin@example.com
Email: projectmanager@example.com
Email: customer@example.com
[admin] /admin/authentication
[project-manager] /admin/authentication
[customer] /authentication/login
[ 'admin', 'project-manager', 'customer' ]
customer@example.com
undefined
Đã xử lý xong
    callback(user);
    ^

TypeError: callback is not a function
```

- `chayVoiMoiUser` lo việc lặp; **làm gì với từng user** do callback quyết định.
- `forEach`, `map`, `filter`, `find` của mảng hoạt động đúng như vậy: `(user) => user.role` là arrow function truyền làm callback, mảng gọi lại nó cho từng phần tử.
- `findUserByRole` trả `undefined` khi không thấy; nơi gọi phải kiểm tra trước khi đọc `.email`.
- Lỗi ở cuối: `baoXong()` có ngoặc nên hàm **chạy ngay**, rồi kết quả của nó (`undefined`) mới được truyền vào. Truyền callback thì viết **tên hàm, không ngoặc**: `baoXong`.

### 🔆 2. setTimeout: callback được gọi lại sau

Tạo file `bai-06-ham/11-settimeout.js`:

```javascript
console.log('1. Bắt đầu');

// Hẹn: 1000 mili giây nữa thì gọi lại hàm này
setTimeout(() => {
  console.log('3. Đã chờ xong 1 giây');
}, 1000);

console.log('2. Dòng này chạy ngay, không chờ');
```

```bash
node bai-06-ham/11-settimeout.js
```

Kết quả:

```bash
1. Bắt đầu
2. Dòng này chạy ngay, không chờ
3. Đã chờ xong 1 giây
```

Dòng 2 in trước dòng 3 dù viết sau. [`setTimeout`](https://nodejs.org/api/timers.html#settimeoutcallback-delay-args) chỉ **hẹn giờ** rồi cho chương trình chạy tiếp; hết 1000 mili giây callback mới được gọi. Mở trang, bấm nút cũng là việc phải chờ; cách chờ cho đúng học ở bài async/await.

### 🔆 3. Đọc một test Playwright

Đoạn dưới là code Playwright thật, **chỉ để đọc**, chưa chạy được trong project này (Playwright cài ở chương sau):

```typescript
test('mở trang đăng nhập', async ({ page }) => {
  await page.goto('https://crm.anhtester.com/admin/authentication');
});
```

<table class="rt-table">
<thead>
<tr>
<th>Phần code</th>
<th>Là gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>test(...)</code></td>
<td>Gọi hàm <a href="https://playwright.dev/docs/api/class-test#test-call"><code>test</code></a> của Playwright với 2 đối số</td>
</tr>
<tr>
<td><code>'mở trang đăng nhập'</code></td>
<td>Đối số 1: tên test, một chuỗi</td>
</tr>
<tr>
<td><code>async (...) =&gt; { ... }</code></td>
<td>Đối số 2: <strong>arrow function truyền làm callback</strong>. Playwright gọi lại nó khi tới lượt test chạy</td>
</tr>
<tr>
<td><code>({ page })</code></td>
<td>Tham số của callback: lấy nhanh <code>page</code> từ Object Playwright truyền vào (bài trước)</td>
</tr>
<tr>
<td><code>page.goto(...)</code></td>
<td>Gọi hàm <code>goto</code> nằm trong Object <code>page</code></td>
</tr>
<tr>
<td><code>async</code>, <code>await</code></td>
<td>Chờ một việc làm xong, học ở bài async/await</td>
</tr>
</tbody>
</table>

File `14-vi-sao-page.js` của bài trước có hàm giả `fakeRunTest(testFn)`. Thêm tham số tên test là thành bản mô phỏng của `test`, không cần Playwright. Tạo file `bai-06-ham/12-fake-test.js`:

```javascript
// Hàm giả, mô phỏng hàm test() của Playwright
function fakeTest(name, fn) {
  console.log(`▶ ${name}`);

  // "Playwright" chuẩn bị sẵn một Object...
  const fixtures = {
    page: {
      goto: (url) => console.log(`  (giả) mở trang ${url}`),
    },
    browserName: 'chromium',
  };

  // ...rồi GỌI LẠI hàm của bạn, đưa Object đó vào
  fn(fixtures);
  console.log(`✔ xong: ${name}`);
}

fakeTest('mở trang đăng nhập', ({ page }) => {
  page.goto('https://crm.anhtester.com/admin/authentication');
});

fakeTest('in tên trình duyệt', ({ browserName }) => {
  console.log(`  đang chạy trên ${browserName}`);
});
```

```bash
node bai-06-ham/12-fake-test.js
```

Kết quả:

```bash
▶ mở trang đăng nhập
  (giả) mở trang https://crm.anhtester.com/admin/authentication
✔ xong: mở trang đăng nhập
▶ in tên trình duyệt
  đang chạy trên chromium
✔ xong: in tên trình duyệt
```

`fakeTest` in tên test, chuẩn bị Object, rồi gọi lại callback của bạn. Playwright thật cũng theo trình tự đó, chỉ khác là `page` điều khiển trình duyệt thật.

## ✅ Phần 6: Thực hành - gói bước chuẩn bị data đăng nhập CRM thành hàm

File `crm-test-data.js` của bài trước chuẩn bị data cho **một** vai trò, viết thẳng từ trên xuống. Giờ tách thành các hàm nhỏ rồi chạy cho cả 3 vai trò, vẫn đọc file `bai-05-object-json/data/users.json`. Tạo file `bai-06-ham/crm-login-helpers.js`:

```javascript
const fs = require('node:fs');

// Tên biến môi trường chứa mật khẩu của từng vai trò (chỉ là TÊN biến)
const passwordEnvNames = {
  admin: 'ADMIN_PASSWORD',
  'project-manager': 'PM_PASSWORD',
  customer: 'CUSTOMER_PASSWORD',
};

// ===== Các hàm nhỏ, mỗi hàm một việc =====
function loadUsers(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

const findUserByRole = (users, role) => users.find((user) => user.role === role);

function buildUrl(path, baseUrl = 'https://crm.anhtester.com') {
  return `${baseUrl}${path}`;
}

const isValidEmail = (email) => email.includes('@') && !email.includes(' ');

const maskPassword = (password) => (password ? '***' : 'CHƯA ĐẶT');

// ===== Hàm ghép: gọi các hàm nhỏ ở trên =====
function prepareLoginData(users, role) {
  const user = findUserByRole(users, role);
  if (!user) {
    return { status: 'FAIL', note: 'không có tài khoản cho vai trò này' };
  }

  const { email, loginPath } = user;
  const envName = passwordEnvNames[role];

  return {
    status: isValidEmail(email) ? 'PASS' : 'FAIL',
    loginUrl: buildUrl(loginPath),
    email,
    password: `${envName} = ${maskPassword(process.env[envName])}`,
  };
}

// ===== Chạy với 3 vai trò =====
const users = loadUsers('bai-05-object-json/data/users.json');

for (const role of ['admin', 'project-manager', 'customer']) {
  const result = prepareLoginData(users, role);
  console.log(role, result);
}
```

```bash
node bai-06-ham/crm-login-helpers.js
```

Kết quả:

```bash
admin {
  status: 'PASS',
  loginUrl: 'https://crm.anhtester.com/admin/authentication',
  email: 'admin@example.com',
  password: 'ADMIN_PASSWORD = CHƯA ĐẶT'
}
project-manager {
  status: 'PASS',
  loginUrl: 'https://crm.anhtester.com/admin/authentication',
  email: 'projectmanager@example.com',
  password: 'PM_PASSWORD = CHƯA ĐẶT'
}
customer {
  status: 'PASS',
  loginUrl: 'https://crm.anhtester.com/authentication/login',
  email: 'customer@example.com',
  password: 'CUSTOMER_PASSWORD = CHƯA ĐẶT'
}
```

Năm hàm nhỏ, mỗi hàm một việc; `prepareLoginData` ghép chúng lại và `return` sớm khi không thấy tài khoản. Vòng `for...of` gọi cùng một hàm cho 3 vai trò, không chép lại dòng nào. Log chỉ có **tên biến** môi trường; đặt `ADMIN_PASSWORD` rồi chạy lại thì thành `ADMIN_PASSWORD = ***`. Thử thêm `'guest'` vào mảng vai trò, kết quả có thêm dòng:

```bash
guest { status: 'FAIL', note: 'không có tài khoản cho vai trò này' }
```

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức của bài

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn dùng được các prompt dưới đây: chỗ có `@đường-dẫn` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay. Không dán mật khẩu hay file `.env` vào khung chat.

```markdown
Đọc file @bai-05-object-json/crm-test-data.js. Code đang viết thẳng từ trên xuống.
Hãy tách thành các hàm nhỏ, mỗi hàm chỉ làm một việc. Với TỪNG hàm, giải thích:
1. Vì sao đặt tên như vậy.
2. Hàm nhận tham số gì, tham số nào nên có giá trị mặc định.
3. Hàm return gì, và nơi gọi dùng giá trị đó vào việc gì.
Ràng buộc: JavaScript thuần chạy bằng node, không dùng class, không dùng async/await vì tôi chưa học.
Không in mật khẩu ra log.
```

```markdown
Đổi các hàm sau từ function sang arrow function, rồi đổi ngược lại.
Với mỗi hàm, chỉ ra chỗ dễ viết sai khi đổi (quên return khi thân có { },
trả về Object thiếu ngoặc tròn) và cho thấy kết quả sai trông như thế nào khi chạy bằng node.

function createUser(role) {
  return { role: role, email: role + '@example.com' };
}

function isAdmin(user) {
  return user.role === 'admin';
}
```

```markdown
Tôi mới học JavaScript tới phần hàm và callback, chưa học Playwright, chưa học async/await.
Giải thích TỪNG phần của đoạn test sau theo thứ tự: test là gì, có mấy đối số,
đối số nào là callback, ai gọi callback đó và gọi lúc nào, ({ page }) là gì.
Riêng async/await chỉ nói một câu, tôi sẽ học sau.

test('mở trang đăng nhập', async ({ page }) => {
  await page.goto('https://crm.anhtester.com/admin/authentication');
});

Sau đó viết một hàm fakeTest(name, fn) bằng JavaScript thuần để mô phỏng, chạy được bằng node.
```

```markdown
Đoạn code sau chạy không báo lỗi nhưng in ra undefined. Chưa sửa vội.
Hãy chỉ ra từng hàm bị thiếu return, giải thích vì sao JavaScript không báo lỗi,
sau đó mới đưa bản đã sửa và kết quả chạy đúng.

const getEmails = (users) => { users.map((user) => user.email); };
const createResult = (status) => { status: status };

console.log(getEmails([{ email: 'admin@example.com' }]));
console.log(createResult('PASS'));
```

### 🔆 2. Bộ kit liên quan gì tới hàm?

Rule [automation\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md) (mục 3) yêu cầu **không để logic trùng lặp**: hành động lặp lại thì tạo hàm dùng chung (helper), và xoá `console.log` dùng lúc debug trước khi giao code. Mục 5 quy định tên file chứa hàm dùng chung, ví dụ `data-generator.ts`. Lệnh rà code [/review-automation-code](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/review-automation-code.md) dùng từ chương Playwright.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Rà hàm AI viết theo bảng sau:

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
<td>Hàm không <code>return</code>, nhất là arrow function có <code>{ }</code></td>
<td>Hàm trả <code>undefined</code>, không báo lỗi</td>
<td>Thêm <code>return</code>, hoặc bỏ <code>{ }</code></td>
</tr>
<tr>
<td><code>(role) =&gt; { role: role }</code></td>
<td><code>{ }</code> bị hiểu là thân hàm, kết quả <code>undefined</code></td>
<td>Bọc ngoặc tròn: <code>() =&gt; ({ ... })</code></td>
</tr>
<tr>
<td><code>console.log(getRole)</code> thiếu <code>()</code></td>
<td>Không gọi hàm, in ra <code>[Function: getRole]</code></td>
<td>Thêm ngoặc: <code>getRole()</code></td>
</tr>
<tr>
<td>Truyền <code>done()</code> làm callback</td>
<td>Hàm chạy ngay, thứ được truyền là kết quả</td>
<td>Truyền tên hàm <code>done</code>, hoặc <code>() =&gt; done()</code></td>
</tr>
<tr>
<td>Hàm đọc, sửa biến toàn cục thay vì nhận tham số</td>
<td>Test này làm hỏng test khác</td>
<td>Vào qua tham số, ra qua <code>return</code></td>
</tr>
<tr>
<td>Tham số mặc định đứng trước tham số bắt buộc</td>
<td>Đối số gán lệch, tham số sau thành <code>undefined</code></td>
<td>Đưa tham số mặc định xuống cuối</td>
</tr>
<tr>
<td>Một hàm dài làm nhiều việc</td>
<td>Khó đọc, không dùng lại được từng phần</td>
<td>Tách thành hàm nhỏ, mỗi hàm một việc</td>
</tr>
<tr>
<td><code>async (page) =&gt; {}</code> trong test Playwright</td>
<td>Thiếu ngoặc nhọn, test không chạy</td>
<td>Sửa thành <code>async ({ page }) =&gt; {}</code></td>
</tr>
</tbody>
</table>

## ✅ Phần 9: Bài tập thực hành

Đặt file bài tập trong thư mục `bai-06-ham/`.

**Bài tập 1 - Viết hàm và truyền callback.** Tạo file `bt1-format-result.js`. Viết arrow function `formatResult({ name, status, durationMs = 0 })` trả về một chuỗi, và hàm `printAll(list, formatter)` in kết quả của `formatter` cho từng phần tử. Gọi `printAll(results, formatResult)` với mảng 3 kết quả test, kết quả thứ ba không có `durationMs`. Kết quả đúng:

```bash
PASS | Mở trang đăng nhập Admin | 1250 ms
FAIL | Đăng nhập sai mật khẩu | 980 ms
PASS | Mở trang đăng nhập Customer | 0 ms
```

**Bài tập 2 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt2-duyet-code.js`, chép vào và chạy:

```javascript
const users = [
  { email: 'admin@example.com', role: 'admin' },
  { email: 'customer@example.com', role: 'customer' },
];

const getEmails = (list) => { list.map((user) => user.email); };
console.log(getEmails(users));

const createResult = (status) => { status: status };
console.log(createResult('PASS'));

function buildUrl(baseUrl = 'https://crm.anhtester.com', path) {
  return `${baseUrl}${path}`;
}
console.log(buildUrl('/admin/authentication'));

function getRole() {
  return users[0].role;
}
console.log(getRole);

function done() {
  console.log('xong');
}
setTimeout(done(), 100);
```

Kết quả chạy thật:

```bash
undefined
undefined
/admin/authenticationundefined
[Function: getRole]
xong
TypeError [ERR_INVALID_ARG_TYPE]: The "callback" argument must be of type function. Received undefined
```

Có 5 chỗ sai, mỗi chỗ ứng với một dòng của bảng ở Phần 8. Sửa xong, file phải in lần lượt:

```bash
[ 'admin@example.com', 'customer@example.com' ]
{ status: 'PASS' }
https://crm.anhtester.com/admin/authentication
admin
xong
```

## ✅ Phần 10: Ghi nhớ nhanh

- Hàm viết một lần, gọi nhiều lần. Dữ liệu vào qua **tham số**, kết quả ra qua **`return`**; thiếu `return` thì hàm trả `undefined`.
- Tham số mặc định đặt cuối. Hàm nhiều tham số thì nhận một Object: `function f({ email, role = 'admin' })`.
- Biến `let`, `const` chỉ sống trong cặp `{ }` chứa nó. Không truyền dữ liệu giữa các hàm bằng biến toàn cục.
- Arrow function: `(a, b) => a + b` tự trả về; thân có `{ }` phải viết `return`; trả Object phải bọc `({ ... })`.
- Callback là hàm truyền vào hàm khác để được gọi lại. Truyền `fn`, không truyền `fn()`.
- `test('tên', async ({ page }) => { ... })`: gọi hàm `test` với một chuỗi và một callback.

✅ **Kết luận:** Qua 6 bài, thư mục `js-ts-for-tester` đã có khá nhiều code, nhưng code mới chỉ nằm trên máy bạn: lỡ sửa hỏng là không quay lại được bản cũ. Bài kế tiếp, **Quản lý source code với Git và GitHub**, lưu lịch sử thay đổi của code bằng Git và đưa project lên GitHub.

---

## Bài tập riêng — Hàm, arrow function, tham số mặc định và callback

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-96](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-96)

**Mục tiêu:** viết hàm nhận Object làm tham số, trả về giá trị đúng cách và truyền hàm làm callback.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-06-ham`

### 📝 Đề bài

#### Bài tập 1 - Viết hàm và truyền callback

Tạo file `bt1-format-result.js`. Viết arrow function `formatResult({ name, status, durationMs = 0 })` trả về một chuỗi, và hàm `printAll(list, formatter)` in kết quả của `formatter` cho từng phần tử. Gọi `printAll(results, formatResult)` với mảng 3 kết quả test, kết quả thứ ba **không có** `durationMs`. Kết quả đúng:

```none
PASS | Mở trang đăng nhập Admin | 1250 ms
FAIL | Đăng nhập sai mật khẩu | 980 ms
PASS | Mở trang đăng nhập Customer | 0 ms
```

#### Bài tập 2 - Duyệt code AI

Tạo file `bt2-duyet-code.js`, chép đoạn code AI viết dưới đây và chạy. Có **5 chỗ sai**, mỗi chỗ ứng với một dòng của bảng ở Phần 8.

```javascript
const users = [
  { email: 'admin@example.com', role: 'admin' },
  { email: 'customer@example.com', role: 'customer' },
];
const getEmails = (list) => { list.map((user) => user.email); };
console.log(getEmails(users));
const createResult = (status) => { status: status };
console.log(createResult('PASS'));
function buildUrl(baseUrl = 'https://crm.anhtester.com', path) {
  return `${baseUrl}${path}`;
}
console.log(buildUrl('/admin/authentication'));
function getRole() {
  return users[0].role;
}
console.log(getRole);
function done() {
  console.log('xong');
}
setTimeout(done(), 100);
```

### 📦 Cách nộp bài

1. Mở ô **Nội dung bài làm (Editor)**. Với mỗi file: bấm **Đoạn code mẫu**, chọn ngôn ngữ, dán **toàn bộ** code. Dòng đầu là comment đường dẫn file, ví dụ `// bai-06-ham/bt1-....js`.
2. Ngay dưới mỗi file, chèn thêm một **Đoạn code mẫu** chọn **Text / Log** và dán **kết quả chạy thật** copy từ Terminal (không gõ lại bằng tay).
3. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*, sau đó dán file đã sửa và kết quả chạy.
4. Đã đưa project lên GitHub (học ở Bài 7) thì dán thêm link thư mục bài vào ô **Link GitHub**.

### ✅ Tiêu chí Đạt

- Bài tập 1 in đúng 3 dòng như đề; `printAll` không biết gì về định dạng (chỉ gọi `formatter`); giá trị mặc định nằm ở tham số, không dùng `if` để gán 0.
- Bài tập 2 sau khi sửa in lần lượt: `[ 'admin@example.com', 'customer@example.com' ]`, `{ status: 'PASS' }`, `https://crm.anhtester.com/admin/authentication`, `admin`, `xong`.
- Nêu đúng 5 lý do: arrow có ngoặc nhọn thì phải `return`; trả về Object phải bọc ngoặc tròn; tham số mặc định đặt trước tham số bắt buộc; in tên hàm thay vì gọi hàm; truyền kết quả `done()` thay vì truyền hàm `done` làm callback.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.