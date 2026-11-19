# Bài 4 - [Javascript Typescript] Vòng lặp và mảng (Array) trong JavaScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/402](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/402)

✅ Vòng lặp for, break và continue  
✅ Vòng lặp while và thử lại (retry) có giới hạn số lần  
✅ Mảng (Array): chỉ số, length, push và pop  
✅ Duyệt mảng bằng for...of và forEach  
✅ map, filter, find, includes và thực hành tổng hợp kết quả thử đăng nhập CRM  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra code do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước bạn đã cho code **ra quyết định** bằng `if...else` và `switch...case`: đúng thì báo PASS, sai thì báo FAIL. Nhưng mỗi quyết định đó mới chạy cho **một** giá trị, còn tester thì luôn làm việc với số nhiều: nhiều email cần thử, nhiều mã HTTP trả về. Bài này dạy hai thứ đi cùng nhau: **mảng** để giữ cả danh sách trong một biến, và **vòng lặp** để làm lại cùng một việc cho từng phần tử. Học xong bạn sẽ:

- Đọc được vòng lặp `for`, `while`, biết `break` và `continue` làm gì, nhận ra vòng lặp vô hạn.
- Tạo mảng, lấy phần tử theo chỉ số, thêm bớt bằng `push`, `pop`.
- Duyệt mảng bằng `for...of` và đọc được `forEach`.
- Dùng `map`, `filter`, `find`, `includes` để xử lý danh sách dữ liệu test.
- Tự bắt được các lỗi vòng lặp AI hay mắc.

> 📌 Bài này làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Mọi đoạn code đều có **tên file** và **kết quả chạy thật** (Node.js v24.17.0).

## ✅ Phần 1: Vòng lặp for, break và continue

### 🔆 1. Chuẩn bị thư mục cho bài học

Trong project, tạo thư mục `bai-04-vong-lap-mang` cạnh thư mục của các bài trước. Mỗi ví dụ là một file:

```bash
js-ts-for-tester/
├── package.json
└── bai-04-vong-lap-mang/
    ├── 01-diem-danh.js
    ├── 02-break-continue.js
    ├── 03-while-goi-dien.js
    ├── 04-while-retry.js
    ├── 05-gio-di-cho.js
    ├── 06-mang-email-test.js
    ├── 07-for-of.js
    ├── 08-foreach.js
    ├── 09-for-in.js
    ├── 10-loc-rau.js
    ├── 11-xu-ly-danh-sach.js
    └── crm-login-report.js
```

Chạy từ thư mục project, ví dụ `node bai-04-vong-lap-mang/01-diem-danh.js`.

### 🔆 2. Vòng lặp for: biết trước số lần lặp

Cô giáo điểm danh lớp có 5 bạn: cùng một việc, làm 5 lần. Trong lập trình, việc lặp lại như vậy giao cho **vòng lặp**. Tạo file `bai-04-vong-lap-mang/01-diem-danh.js`:

```javascript
// Điểm danh lớp có 5 bạn: cùng một việc, làm 5 lần
for (let i = 1; i <= 5; i++) {
  console.log(`Điểm danh bạn số ${i}`);
}
console.log('Điểm danh xong');
```

Kết quả:

```bash
Điểm danh bạn số 1
Điểm danh bạn số 2
Điểm danh bạn số 3
Điểm danh bạn số 4
Điểm danh bạn số 5
Điểm danh xong
```

Trong ngoặc của `for` có 3 phần, cách nhau bằng dấu `;`:

- `let i = 1`: **khởi tạo** biến đếm, chạy đúng một lần.
- `i <= 5`: **điều kiện**, kiểm trước mỗi lượt. Còn `true` thì chạy tiếp, `false` thì thoát.
- `i++`: **bước nhảy**, chạy sau mỗi lượt, tăng `i` thêm 1.

### 🔆 3. break và continue

Chạy lần lượt 5 test case: cái đang tạm tắt thì bỏ qua, gặp lỗi chặn đường thì dừng hẳn. Đây là `if` của bài trước đặt vào trong vòng lặp. Tạo file `bai-04-vong-lap-mang/02-break-continue.js`:

```javascript
// Chạy lần lượt 5 test case, đánh số từ 1 đến 5
for (let testNumber = 1; testNumber <= 5; testNumber++) {
  if (testNumber === 2) {
    console.log(`TC${testNumber}: đang tạm tắt, bỏ qua`);
    continue; // nhảy sang lượt kế tiếp
  }
  if (testNumber === 4) {
    console.log(`TC${testNumber}: trang đăng nhập không mở được, dừng chạy`);
    break; // thoát hẳn vòng lặp
  }
  console.log(`TC${testNumber}: PASS`);
}
console.log('Kết thúc');
```

Kết quả:

```bash
TC1: PASS
TC2: đang tạm tắt, bỏ qua
TC3: PASS
TC4: trang đăng nhập không mở được, dừng chạy
Kết thúc
```

`continue` bỏ phần còn lại của **lượt hiện tại** rồi lặp tiếp. `break` **thoát hẳn** vòng lặp, nên TC5 không được chạy.

## ✅ Phần 2: Vòng lặp while - lặp tới khi đạt điều kiện

### 🔆 1. Gọi điện không ai nghe máy

Gọi điện không ai nghe thì gọi lại. Bạn không biết trước phải gọi mấy lần, chỉ biết **khi nào thì dừng**: có người nghe, hoặc đã gọi đủ 3 lần. `while` dùng cho kiểu việc này. Tạo file `bai-04-vong-lap-mang/03-while-goi-dien.js`:

```javascript
// Gọi điện: chưa ai nghe máy thì gọi lại, nhiều nhất 3 lần
const maxCalls = 3;
let callCount = 0;
let isAnswered = false;

while (!isAnswered && callCount < maxCalls) {
  callCount++;
  console.log(`Gọi lần ${callCount}: không ai nghe máy`);
}
console.log(`Dừng sau ${callCount} lần gọi`);
```

Kết quả:

```bash
Gọi lần 1: không ai nghe máy
Gọi lần 2: không ai nghe máy
Gọi lần 3: không ai nghe máy
Dừng sau 3 lần gọi
```

### 🔆 2. Thử lại (retry) trong automation

Mạng chập chờn, lần đầu trang không mở được, thử lại thì được. Tạo file `bai-04-vong-lap-mang/04-while-retry.js` (chưa có Playwright nên kết quả mỗi lần thử được giả lập):

```javascript
// Thử mở trang đăng nhập, lỗi thì thử lại, tối đa 3 lần
const loginUrl = 'https://crm.anhtester.com/admin/authentication';
const maxAttempts = 3;
let attempt = 0;
let isPageOpened = false;

while (!isPageOpened && attempt < maxAttempts) {
  attempt++;
  // Giả lập: tới lần thứ 2 trang mới mở được
  isPageOpened = attempt === 2;
  console.log(`Lần ${attempt}: ${isPageOpened ? 'PASS' : 'FAIL'}`);
}

if (isPageOpened) {
  console.log(`Mở được ${loginUrl} sau ${attempt} lần thử`);
} else {
  console.log(`Không mở được trang sau ${maxAttempts} lần thử`);
}
```

Kết quả:

```bash
Lần 1: FAIL
Lần 2: PASS
Mở được https://crm.anhtester.com/admin/authentication sau 2 lần thử
```

> ⚠️ **Vòng lặp vô hạn:** nếu trong thân `while` không có dòng nào làm điều kiện tiến dần về `false` (ở đây là `attempt++`), vòng lặp chạy mãi và chương trình treo. Lỡ gặp thì bấm **Ctrl + C** để dừng. Mọi vòng `while` phải có **biến đếm và số lần tối đa**.

## ✅ Phần 3: Mảng (Array) - nhiều giá trị trong một biến

### 🔆 1. Giỏ đi chợ

Đi chợ bạn bỏ chung các món vào một cái giỏ. **Mảng** (array) là cái giỏ đó: một biến chứa nhiều giá trị xếp theo thứ tự, viết trong cặp `[]`, cách nhau bằng dấu phẩy. Tạo file `bai-04-vong-lap-mang/05-gio-di-cho.js`:

```javascript
// Giỏ đi chợ: nhiều món nằm trong một biến
const basket = ['rau cải', 'cà chua', 'trứng'];

console.log(basket.length);              // số món trong giỏ
console.log(basket[0]);                  // món đầu tiên: chỉ số 0
console.log(basket[basket.length - 1]);  // món cuối cùng
console.log(basket[3]);                  // chỉ số không tồn tại

basket.push('hành lá');                  // thêm vào cuối giỏ
console.log(basket);

const removed = basket.pop();            // lấy món cuối ra khỏi giỏ
console.log(removed);
console.log(basket);
```

Kết quả:

```bash
3
rau cải
trứng
undefined
[ 'rau cải', 'cà chua', 'trứng', 'hành lá' ]
hành lá
[ 'rau cải', 'cà chua', 'trứng' ]
```

- **Chỉ số bắt đầu từ 0**, không phải 1. Mảng 3 phần tử có các chỉ số 0, 1, 2, nên phần tử cuối là `basket[basket.length - 1]`.
- Đọc chỉ số không tồn tại **không báo lỗi**, chỉ ra `undefined`.
- `push` thêm vào cuối, `pop` lấy phần tử cuối ra. Thao tác ở đầu mảng có `unshift` (thêm) và `shift` (lấy ra).
- `basket` khai báo bằng `const` mà vẫn `push` được: `const` giữ cố định **cái giỏ**, không khoá **đồ trong giỏ**. Chỉ khi gán lại cả giỏ (`basket = []`) mới gặp lỗi `TypeError: Assignment to constant variable.`

### 🔆 2. Danh sách email test

Tạo file `bai-04-vong-lap-mang/06-mang-email-test.js` chứa các email dùng để thử form đăng nhập Admin của CRM demo, rồi dùng `for` đi qua từng chỉ số:

```javascript
// Danh sách email dùng để thử form đăng nhập Admin của CRM demo
const testEmails = ['admin@example.com', 'pm@example.com'];
testEmails.push('customer@example.com');

console.log(`Có ${testEmails.length} email test`);

// i chạy từ 0 tới length - 1: đúng bằng các chỉ số của mảng
for (let i = 0; i < testEmails.length; i++) {
  console.log(`${i}: ${testEmails[i]}`);
}
```

Kết quả:

```bash
Có 3 email test
0: admin@example.com
1: pm@example.com
2: customer@example.com
```

Điều kiện phải là `i < testEmails.length`. Viết thành `<=` là lặp thừa một lượt và đọc ra `undefined`.

> 🔒 Mảng này chỉ chứa email. Mật khẩu không viết vào code, lúc cần thì đọc từ biến môi trường `ADMIN_PASSWORD`.

## ✅ Phần 4: Duyệt mảng bằng for...of và forEach

### 🔆 1. for...of - cách khuyên dùng

Khi chỉ cần **từng phần tử**, không cần chỉ số, `for...of` gọn hơn và không thể viết lệch chỉ số. Tạo file `bai-04-vong-lap-mang/07-for-of.js`, danh sách lần này có dòng rỗng và dòng sai định dạng:

```javascript
const testEmails = ['admin@example.com', '', 'pm.example.com', 'customer@example.com'];

for (const email of testEmails) {
  if (email === '') {
    console.log('(rỗng) -> bỏ qua');
    continue;
  }
  if (email.includes('@')) {
    console.log(`${email} -> hợp lệ, đem đi thử đăng nhập`);
  } else {
    console.log(`${email} -> sai định dạng`);
  }
}
```

Kết quả:

```bash
admin@example.com -> hợp lệ, đem đi thử đăng nhập
(rỗng) -> bỏ qua
pm.example.com -> sai định dạng
customer@example.com -> hợp lệ, đem đi thử đăng nhập
```

Đọc là "với từng `email` trong `testEmails`". `for...of` vẫn dùng được `break` và `continue`.

### 🔆 2. forEach - đủ để đọc hiểu

Code AI viết dùng `forEach` rất nhiều. Tạo file `bai-04-vong-lap-mang/08-foreach.js`:

```javascript
const browsers = ['chromium', 'firefox', 'webkit'];

browsers.forEach((browser, index) => {
  console.log(`${index + 1}. Chạy test trên ${browser}`);
});
```

Kết quả:

```bash
1. Chạy test trên chromium
2. Chạy test trên firefox
3. Chạy test trên webkit
```

Phần `(browser, index) => { ... }` là một **hàm ngắn**: mảng gọi hàm này một lần cho mỗi phần tử, đưa vào phần tử và chỉ số. Cách viết có mũi tên `=>` sẽ học kỹ ở bài về hàm, lúc này chỉ cần đọc được.

> ⚠️ `forEach` có hai giới hạn. Một: **không dùng được `break`**, viết vào là Node.js báo `SyntaxError: Illegal break statement`. Hai: **`forEach` không chờ `await`**, mà mọi thao tác Playwright đều cần `await` (bài async/await sẽ giải thích). Vì vậy khoá học mặc định dùng `for...of`.

### 🔆 3. Đừng nhầm for...in với for...of

Hai cách viết khác nhau đúng một chữ. Tạo file `bai-04-vong-lap-mang/09-for-in.js`:

```javascript
const browsers = ['chromium', 'firefox', 'webkit'];

for (const item in browsers) {
  console.log(item, typeof item, item + 1);
}
```

Kết quả:

```bash
0 string 01
1 string 11
2 string 21
```

`for...in` đưa ra **chỉ số ở dạng chuỗi** chứ không phải phần tử, nên `item + 1` thành nối chuỗi `'01'`. Với mảng, luôn dùng `for...of`.

## ✅ Phần 5: map, filter, find và includes

### 🔆 1. Lọc rau còn tươi

Mua rau về, bạn nhặt riêng những bó còn tươi. Việc "đi qua danh sách, giữ lại cái đạt điều kiện" gặp nhiều tới mức mảng có sẵn hàm làm thay vòng lặp. Tạo file `bai-04-vong-lap-mang/10-loc-rau.js`:

```javascript
// Mớ rau mua về, có bó đã héo
const vegetables = ['cải tươi', 'muống héo', 'mồng tơi tươi', 'xà lách héo'];

// filter: giữ lại các phần tử thoả điều kiện
const freshOnes = vegetables.filter(v => v.includes('tươi'));
console.log(freshOnes);

// map: đổi từng phần tử, ra mảng mới cùng số lượng
const labels = vegetables.map(v => v.toUpperCase());
console.log(labels);

// find: lấy phần tử ĐẦU TIÊN thoả điều kiện
console.log(vegetables.find(v => v.includes('héo')));
console.log(vegetables.find(v => v.includes('bắp')));

// includes: mảng có đúng giá trị này không
console.log(vegetables.includes('cải tươi'));
console.log(vegetables.includes('cải'));

// Mảng gốc không đổi
console.log(vegetables.length);
```

Kết quả:

```bash
[ 'cải tươi', 'mồng tơi tươi' ]
[ 'CẢI TƯƠI', 'MUỐNG HÉO', 'MỒNG TƠI TƯƠI', 'XÀ LÁCH HÉO' ]
muống héo
undefined
true
false
4
```

`v => v.includes('tươi')` đọc là "nhận từng phần tử `v`, trả về kết quả của biểu thức sau mũi tên".

<table class="rt-table">
<thead>
<tr>
<th>Hàm</th>
<th>Trả về</th>
<th>Dùng khi</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>filter</code></td>
<td>Mảng mới gồm các phần tử cho kết quả <code>true</code>; không có thì ra mảng rỗng</td>
<td>Lọc ra các kết quả lỗi, các dòng hợp lệ</td>
</tr>
<tr>
<td><code>map</code></td>
<td>Mảng mới <strong>cùng số phần tử</strong>, mỗi phần tử đã được biến đổi</td>
<td>Làm sạch cả danh sách text</td>
</tr>
<tr>
<td><code>find</code></td>
<td>Phần tử <strong>đầu tiên</strong> đạt điều kiện; không có thì ra <code>undefined</code></td>
<td>Lấy một tài khoản, một dòng cụ thể</td>
</tr>
<tr>
<td><code>includes</code></td>
<td><code>true</code> / <code>false</code>: mảng có phần tử <strong>bằng đúng</strong> giá trị này không</td>
<td>Kiểm một giá trị có nằm trong danh sách cho phép</td>
</tr>
</tbody>
</table>

Mảng không có phần tử nào bằng đúng `'cải'` nên ra `false`: `includes` của **chuỗi** tìm một đoạn con, còn `includes` của **mảng** so cả phần tử.

### 🔆 2. Áp dụng vào dữ liệu test

Tạo file `bai-04-vong-lap-mang/11-xu-ly-danh-sach.js` với bốn việc tester hay làm:

```javascript
// 1. Text các nhãn lấy từ trang đăng nhập: dính khoảng trắng, xuống dòng
const rawLabels = ['\n  Email Address ', ' Password\n', '  Remember me  '];
const labels = rawLabels.map(text => text.trim());
console.log(labels);

// 2. Mã HTTP của 5 request: lọc ra các mã lỗi (từ 400 trở lên)
const statusCodes = [200, 200, 404, 500, 200];
const errorCodes = statusCodes.filter(code => code >= 400);
console.log(errorCodes);
console.log(`PASS: ${statusCodes.length - errorCodes.length}, FAIL: ${errorCodes.length}`);
console.log(statusCodes.some(code => code >= 500));
console.log(statusCodes.every(code => code === 200));

// 3. Tìm email theo vai trò
const testEmails = ['admin@example.com', 'pm@example.com', 'customer@example.com'];
const pmEmail = testEmails.find(email => email.includes('pm@'));
const guestEmail = testEmails.find(email => email.includes('guest@'));
console.log(pmEmail);
console.log(guestEmail);

// 4. Trình duyệt truyền vào có nằm trong danh sách hỗ trợ không
const supportedBrowsers = ['chromium', 'firefox', 'webkit'];
const browser = process.env.BROWSER ?? 'chromium';
if (supportedBrowsers.includes(browser)) {
  console.log(`Chạy test trên ${browser}`);
} else {
  console.log(`Không hỗ trợ trình duyệt: ${browser}`);
}
```

Kết quả:

```bash
[ 'Email Address', 'Password', 'Remember me' ]
[ 404, 500 ]
PASS: 3, FAIL: 2
true
false
pm@example.com
undefined
Chạy test trên chromium
```

- Việc 1 là lý do chính phải học mảng: trong Playwright, `locator.allTextContents()` trả về **một mảng chuỗi** còn nguyên khoảng trắng, và `map` kèm `trim()` làm sạch cả danh sách.
- Việc 2: `some` hỏi "có **ít nhất một** phần tử đạt không", `every` hỏi "**tất cả** có đạt không".
- Việc 3: không có email nào chứa `guest@` nên `find` ra `undefined`. Dùng kết quả của `find` thì phải kiểm bằng `if` trước.
- Việc 4: đặt biến môi trường `BROWSER` thành `edge` rồi chạy lại, dòng cuối đổi thành `Không hỗ trợ trình duyệt: edge`.

## ✅ Phần 6: Thực hành - tổng hợp kết quả thử đăng nhập CRM

### 🔆 1. Đề bài

Bạn nhận một danh sách email chép từ file Excel để thử trang đăng nhập Admin của [CRM demo](https://crm.anhtester.com/admin/authentication):

1. Làm sạch danh sách, bỏ dòng trống và dòng sai định dạng.
2. Với từng email hợp lệ, xét mã HTTP (được **giả lập** bằng một mảng): `200` là PASS, còn lại là FAIL.
3. In tổng kết và danh sách email cần kiểm tra lại.

### 🔆 2. Code và kết quả

Tạo file `bai-04-vong-lap-mang/crm-login-report.js`:

```javascript
// ===== 1. Dữ liệu đầu vào =====
const baseUrl = 'https://crm.anhtester.com';
const loginPath = '/admin/authentication';
// Email chép từ file Excel: thừa khoảng trắng, lẫn chữ hoa, có dòng trống
const rawEmails = ['  Admin@Example.com', 'pm@example.com ', '', 'customer.example.com', 'customer@example.com'];
// Mã HTTP giả lập cho từng lần thử, theo đúng thứ tự các email hợp lệ
const statusCodes = [200, 500, 200];

// ===== 2. Làm sạch rồi lọc =====
const emails = rawEmails.map(email => email.trim().toLowerCase());
const validEmails = emails.filter(email => email.includes('@'));
const skippedCount = emails.length - validEmails.length;

// ===== 3. Duyệt, ghi kết quả từng email =====
console.log(`Trang kiểm tra: ${baseUrl}${loginPath}`);
const failedEmails = [];
for (let i = 0; i < validEmails.length; i++) {
  const email = validEmails[i];
  const code = statusCodes[i];
  if (code === 200) {
    console.log(`${i + 1}. ${email} -> ${code} PASS`);
  } else {
    console.log(`${i + 1}. ${email} -> ${code} FAIL`);
    failedEmails.push(email);
  }
}

// ===== 4. Tổng kết =====
console.log(`Bỏ qua ${skippedCount} dòng không hợp lệ`);
console.log(`PASS: ${validEmails.length - failedEmails.length}, FAIL: ${failedEmails.length}`);
console.log('Email cần kiểm tra lại:', failedEmails);
```

```bash
node bai-04-vong-lap-mang/crm-login-report.js
```

Kết quả:

```bash
Trang kiểm tra: https://crm.anhtester.com/admin/authentication
1. admin@example.com -> 200 PASS
2. pm@example.com -> 500 FAIL
3. customer@example.com -> 200 PASS
Bỏ qua 2 dòng không hợp lệ
PASS: 2, FAIL: 1
Email cần kiểm tra lại: [ 'pm@example.com' ]
```

- `map` rồi `filter`: làm sạch trước, lọc sau.
- Bước 3 dùng `for` có chỉ số vì cần `i` để lấy phần tử **cùng vị trí** ở hai mảng.
- `failedEmails` bắt đầu là mảng rỗng, mỗi lần FAIL thì `push` thêm.

Thử tự phá: đổi `i < validEmails.length` thành `<=` rồi chạy lại, bạn sẽ thấy thêm dòng `4. undefined -> undefined FAIL`.

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu về vòng lặp và mảng

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí). Bản miễn phí của [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn hỏi được y như vậy: chỗ nào prompt ghi `@đường-dẫn-file` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu Claude Code](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay.

```markdown
Dùng đúng mảng testEmails trong file @bai-04-vong-lap-mang/07-for-of.js, hãy viết lại vòng lặp theo 3 cách:
for có chỉ số, for...of, forEach. Sau đó lập bảng so sánh: cách nào dùng được break/continue,
cách nào lấy được chỉ số, cách nào dùng được với await. Chỉ giải thích, KHÔNG sửa file.
```

```markdown
Trong file @bai-04-vong-lap-mang/crm-login-report.js, hãy chỉ cho tôi cách viết lại bước 2
bằng vòng lặp for...of và push thay cho map và filter. Giải thích từng bước hai cách tương đương ra sao.
Chạy cả hai bằng node để chứng minh kết quả giống nhau, không sửa file gốc.
```

```markdown
Đọc đoạn code JavaScript dưới đây và tìm lỗi về vòng lặp: vòng lặp vô hạn, lệch chỉ số
(i <= arr.length), for...in dùng cho mảng, find không kiểm undefined.
Mỗi lỗi nêu: dòng nào, chạy thật sẽ ra gì, sửa thế nào. Chưa viết lại toàn bộ code.

[dán code vào đây]
```

```markdown
Tạo 5 bài tập JavaScript từ dễ đến khó về: for, while có giới hạn số lần, mảng, for...of,
map, filter, find, includes. Bối cảnh: tester xử lý danh sách email test và mã HTTP.
Ràng buộc: KHÔNG dùng object, hàm tự viết, async/await, reduce vì tôi chưa học.
Ghi đề bài vào file bai-04-vong-lap-mang/bai-tap-them.md, chưa đưa đáp án.
```

AI có thể ghi sai kết quả của một vòng lặp: câu trả lời nào có kết quả cụ thể thì chép code ra file, chạy bằng `node` để đối chiếu.

### 🔆 2. Bộ kit liên quan gì tới vòng lặp và mảng?

Bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills) làm việc trên code Playwright nên tới chương Playwright bạn mới dùng. Có ba chỗ nối với bài hôm nay:

- Lệnh `/generate-test-data` sinh cả **bộ** dữ liệu test (giá trị hợp lệ, không hợp lệ, giá trị biên). Nhiều bộ giá trị tức là một danh sách, code dùng nó sẽ duyệt bằng vòng lặp.
- Rule [playwright\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/playwright_rules.md), mục "Chiến lược chờ đợi", **cấm tự tạo thời gian chờ cố định** vì Playwright đã tự chờ phần tử. AI viết vòng `while` để ngồi chờ một nút xuất hiện là code đi sai hướng.
- Rule [automation\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md), mục "Chất lượng code", yêu cầu **không lặp lại logic**. Năm khối code giống nhau cho năm email phải thay bằng một mảng và một vòng lặp.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Nhận code có vòng lặp hoặc mảng thì rà theo bảng:

<table class="rt-table">
<thead>
<tr>
<th>Dấu hiệu trong code</th>
<th>Vì sao là vấn đề</th>
<th>Cách xử lý</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>i &lt;= arr.length</code></td>
<td>Lặp thừa một lượt, lượt cuối đọc ra <code>undefined</code></td>
<td>Đổi thành <code>i &lt; arr.length</code>, hoặc dùng <code>for...of</code></td>
</tr>
<tr>
<td><code>for (const x in arr)</code></td>
<td>Ra chỉ số dạng chuỗi <code>'0'</code>, <code>'1'</code>, không phải phần tử</td>
<td>Đổi <code>in</code> thành <code>of</code></td>
</tr>
<tr>
<td><code>break</code> trong <code>forEach</code></td>
<td>File không chạy: <code><span>SyntaxError:</span> <span>Illegal</span> <span>break</span> <span>statement</span></code></td>
<td>Đổi sang <code>for...of</code></td>
</tr>
<tr>
<td><code>await</code> trong <code>forEach</code></td>
<td><code>forEach</code> không chờ: code phía sau chạy khi các thao tác chưa xong</td>
<td>Đổi sang <code>for...of</code></td>
</tr>
<tr>
<td><code>while</code> không có biến đếm, hoặc <code>while (true)</code></td>
<td>Điều kiện không bao giờ <code>false</code> thì test treo vô hạn</td>
<td>Thêm biến đếm và số lần tối đa vào điều kiện</td>
</tr>
<tr>
<td><code>arr.map(...)</code> mà không gán kết quả cho biến nào</td>
<td><code>map</code> sinh ra để tạo mảng mới; dùng nó để lặp làm người đọc hiểu sai ý</td>
<td>Chỉ lặp thì dùng <code>for...of</code></td>
</tr>
<tr>
<td>Dùng ngay kết quả của <code>find</code></td>
<td>Không tìm thấy thì ra <code>undefined</code>, gọi hàm trên đó là dừng với <code>TypeError</code></td>
<td>Kiểm <code>=== undefined</code> bằng <code>if</code> trước khi dùng</td>
</tr>
<tr>
<td>Thêm hoặc xoá phần tử của mảng <strong>đang được duyệt</strong></td>
<td>Chỉ số bị xô lệch: sót phần tử, hoặc lặp dài mãi</td>
<td>Dùng <code>filter</code> tạo mảng mới, hoặc <code>push</code> vào một mảng khác</td>
</tr>
</tbody>
</table>

Đọc xong thì **chạy thật**. Nghi vòng lặp chạy sai số lượt thì thêm tạm dòng `console.log(i, arr[i])` trong vòng lặp, kiểm xong thì xoá.

## ✅ Phần 9: Bài tập thực hành

Đặt các file bài tập trong thư mục `bai-04-vong-lap-mang/`.

**Bài tập 1 - Làm sạch danh sách.** Tạo file `bt1-danh-sach-menu.js` với mảng `[' Dashboard', 'Customers ', '', ' Projects ', 'Tasks\n']`. Làm sạch bằng `map`; bỏ phần tử rỗng bằng `filter`; in từng tên kèm số thứ tự từ 1 bằng `for`; kiểm danh sách có `'Projects'` không bằng `includes`. Kết quả đúng: 4 tên, dòng cuối in `true`.

**Bài tập 2 - Thử lại có giới hạn.** Tạo file `bt2-retry.js` dựa trên `04-while-retry.js`: cho phép tối đa 5 lần, giả lập tới lần thứ 4 mới PASS. Sau đó hạ số lần tối đa xuống 3 rồi chạy lại. Hai kết quả khác nhau thế nào, vì sao?

**Bài tập 3 - Duyệt code AI.** Đoạn code dưới đây do AI viết để đếm request lỗi. Tạo file `bt3-duyet-code.js`, chép vào và chạy.

```javascript
const statusCodes = [200, 404, 200, 500];
let failCount = 0;

for (let i = 0; i <= statusCodes.length; i++) {
  if (statusCodes[i] !== 200) {
    failCount++;
  }
}
console.log(`FAIL: ${failCount}`);

for (const i in statusCodes) {
  console.log(`Request ${i + 1}: ${statusCodes[i]}`);
}

const firstError = statusCodes.find(code => code >= 600);
console.log(firstError.toString());
```

Kết quả chạy thật:

```bash
FAIL: 3
Request 01: 200
Request 11: 404
Request 21: 200
Request 31: 500
D:\AnhTester\js-ts-for-tester\bai-04-vong-lap-mang\bt3-duyet-code.js:16
console.log(firstError.toString());
                       ^

TypeError: Cannot read properties of undefined (reading 'toString')
```

Mảng chỉ có 2 mã khác 200 mà code đếm ra 3. Có 3 chỗ cần sửa, tìm đủ và nêu lý do theo bảng ở Phần 8. Sửa đúng thì file in ra `FAIL: 2`, bốn dòng từ `Request 1: 200` tới `Request 4: 500`, và một dòng báo không tìm thấy thay cho `TypeError`.

## ✅ Phần 10: Ghi nhớ nhanh

- `for` có 3 phần: khởi tạo; điều kiện; bước nhảy. `continue` bỏ qua lượt hiện tại, `break` thoát hẳn vòng lặp.
- `while` lặp tới khi điều kiện hết đúng. Luôn có biến đếm và số lần tối đa, nếu không sẽ lặp vô hạn.
- Mảng viết trong `[]`, chỉ số bắt đầu từ 0, phần tử cuối là `arr[arr.length - 1]`. Đọc quá chỉ số ra `undefined`, không báo lỗi.
- `push` thêm vào cuối, `pop` lấy phần tử cuối ra, kể cả khi mảng khai báo bằng `const`.
- Duyệt mảng: mặc định `for...of`. `forEach` không `break` được và không chờ `await`. Không dùng `for...in` cho mảng.
- `map` đổi từng phần tử, `filter` lọc, `find` lấy phần tử đầu tiên (có thể ra `undefined`), `includes` kiểm có hay không. Cả bốn không làm đổi mảng gốc.

✅ **Kết luận:** Mảng giữ được cả một danh sách, nhưng mỗi phần tử trong bài mới chỉ là **một** giá trị: một email, một mã HTTP. Một tài khoản test thì có nhiều thông tin đi cùng nhau: email, vai trò, tên hiển thị. Bài kế tiếp, **Object và JSON trong JavaScript - lưu, lấy nhanh và gộp dữ liệu test**, dạy cách gom các thông tin đó vào một chỗ, rồi đặt nhiều object vào chính mảng bạn vừa học.

---

## Bài tập riêng — Vòng lặp, retry có giới hạn và xử lý mảng

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-94](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-94)

**Mục tiêu:** dùng for, while, for...of và các hàm map, filter, find, includes để xử lý danh sách dữ liệu test.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-04-vong-lap-mang`

### 📝 Đề bài

#### Bài tập 1 - Làm sạch danh sách menu

Tạo file `bt1-danh-sach-menu.js` với mảng dưới đây. Làm sạch bằng `map`; bỏ phần tử rỗng bằng `filter`; in từng tên kèm số thứ tự từ 1 bằng `for`; kiểm danh sách có `Projects` không bằng `includes`.

```javascript
const menu = ['  Dashboard', 'Customers ', '', ' Projects  ', 'Tasks\n'];
```

#### Bài tập 2 - Thử lại có giới hạn

Tạo file `bt2-retry.js` dựa trên `04-while-retry.js` của bài học: cho phép tối đa 5 lần, giả lập tới lần thứ 4 mới PASS. Sau đó hạ số lần tối đa xuống 3 rồi chạy lại. **Trả lời:** hai kết quả khác nhau thế nào, vì sao?

#### Bài tập 3 - Duyệt code AI

Đoạn code dưới đây do AI viết để đếm request lỗi. Tạo file `bt3-duyet-code.js`, chép vào và chạy. Mảng chỉ có 2 mã khác 200 mà code đếm ra 3. Có **3 chỗ cần sửa**, tìm đủ và nêu lý do theo bảng ở Phần 8.

```javascript
const statusCodes = [200, 404, 200, 500];
let failCount = 0;
for (let i = 0; i <= statusCodes.length; i++) {
  if (statusCodes[i] !== 200) {
    failCount++;
  }
}
console.log(`FAIL: ${failCount}`);
for (const i in statusCodes) {
  console.log(`Request ${i + 1}: ${statusCodes[i]}`);
}
const firstError = statusCodes.find(code => code >= 600);
console.log(firstError.toString());
```

### 📦 Cách nộp bài

1. Mở ô **Nội dung bài làm (Editor)**. Với mỗi file: bấm **Đoạn code mẫu**, chọn ngôn ngữ, dán **toàn bộ** code. Dòng đầu là comment đường dẫn file, ví dụ `// bai-04-vong-lap-mang/bt1-....js`.
2. Ngay dưới mỗi file, chèn thêm một **Đoạn code mẫu** chọn **Text / Log** và dán **kết quả chạy thật** copy từ Terminal (không gõ lại bằng tay).
3. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*, sau đó dán file đã sửa và kết quả chạy.
4. Đã đưa project lên GitHub (học ở Bài 7) thì dán thêm link thư mục bài vào ô **Link GitHub**.
5. Bài tập 2: dán cả 2 kết quả (tối đa 5 lần và tối đa 3 lần) và câu trả lời.

### ✅ Tiêu chí Đạt

- Bài tập 1 in đúng 4 tên đã sạch, đánh số 1 tới 4, dòng cuối in `true`.
- Bài tập 2: tối đa 5 lần thì PASS ở lần 4; tối đa 3 lần thì dừng sau lần 3 và báo FAIL. Vòng while có điều kiện dừng theo số lần, không lặp vô hạn.
- Bài tập 3 sau khi sửa in `FAIL: 2`, bốn dòng từ `Request 1: 200` tới `Request 4: 500`, và một dòng báo không tìm thấy thay cho TypeError. Đủ 3 chỗ: `<=` chạy quá cuối mảng, `for...in` trả về chỉ số dạng chuỗi, không kiểm `undefined` sau `find`.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.