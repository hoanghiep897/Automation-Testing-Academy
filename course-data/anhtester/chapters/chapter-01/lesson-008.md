# Bài 8 - [Javascript Typescript] Class, constructor và kế thừa (extends) trong JavaScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/406](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/406)

✅ Vì sao cần class - class và object là gì  
✅ Cú pháp class, constructor và method  
✅ Kế thừa với extends và super  
✅ Đóng gói, đa hình và class field ở mức đủ dùng  
✅ Thực hành class trang đăng nhập - bước đầu của Page Object Model  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra class do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước bạn đã đưa project `js-ts-for-tester` lên GitHub, từ giờ code có lịch sử. Về JavaScript, bạn đã có **Object** để gom dữ liệu và **hàm** để gom thao tác. Nhưng dữ liệu của trang đăng nhập (đường dẫn, tên các ô nhập) nằm một nơi, các hàm thao tác với trang đó nằm nơi khác. Bài này dùng **class** để gom **cả dữ liệu lẫn thao tác của cùng một thứ** vào một chỗ, và tạo nhiều object từ cùng một khuôn. Đây là nền của Page Object Model, cách tổ chức code mà mọi project Playwright đều dùng. Học xong bạn sẽ:

- Phân biệt class và object; viết được class có `constructor`, thuộc tính và method.
- Hiểu `this` trong class và đọc được lỗi khi quên `this.`, quên `new`.
- Dùng `extends` và `super` để class con kế thừa class cha.
- Hiểu đóng gói và đa hình ở mức đủ để đọc code AI sinh ra.
- Viết một class trang đăng nhập đơn giản, bước đầu của Page Object Model.

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật (Node.js v24.17.0), đã lược dòng đường dẫn file ở kết quả có lỗi.

## ✅ Phần 1: Vì sao cần class - class và object là gì

### 🔆 1. Chuẩn bị thư mục cho bài học

Tạo thư mục `bai-08-class` trong project. Mỗi ví dụ là một file, và **mọi class của một ví dụ nằm chung trong file đó** (tách mỗi class ra một file riêng thì học ở bài import/export):

```bash
js-ts-for-tester/
├── package.json
└── bai-08-class/
    ├── 01-ban-thiet-ke.js
    ├── 02-test-user.js
    ├── 03-method.js
    ├── 04-quen-this.js
    ├── 05-quen-new.js
    ├── 06-ke-thua.js
    ├── 07-super-method.js
    ├── 08-this-truoc-super.js
    ├── 09-dong-goi.js
    ├── 10-doc-field-rieng.js
    ├── 11-da-hinh.js
    ├── 12-class-field.js
    ├── 13-field-doc-this-page.js
    └── crm-login-page.js
```

### 🔆 2. Từ bản thiết kế nhà tới class

Một khu nhà có nhiều căn giống nhau vì chúng được xây từ **cùng một bản thiết kế**. Bản thiết kế quy định căn nào cũng có chủ nhà, có số phòng; mỗi căn xây ra thì có chủ riêng, số phòng riêng. Trong lập trình, bản thiết kế là **class**, mỗi căn nhà thật là một **object**.

Tạo file `bai-08-class/01-ban-thiet-ke.js`:

```javascript
// Bản thiết kế: viết MỘT lần
class Nha {
  constructor(chuNha, soPhong) {
    this.chuNha = chuNha;
    this.soPhong = soPhong;
  }

  moTa() {
    console.log(`Nhà của ${this.chuNha} có ${this.soPhong} phòng`);
  }
}

// Căn nhà thật: xây NHIỀU lần từ cùng một bản thiết kế
const nhaAn = new Nha('An', 3);
const nhaBinh = new Nha('Bình', 5);

nhaAn.moTa();
nhaBinh.moTa();
console.log(nhaAn);
```

```bash
node bai-08-class/01-ban-thiet-ke.js
```

Kết quả:

```bash
Nhà của An có 3 phòng
Nhà của Bình có 5 phòng
Nha { chuNha: 'An', soPhong: 3 }
```

Class `Nha` viết một lần. Mỗi lần gọi `new Nha(...)` là xây thêm một căn. Dòng kết quả cuối có chữ `Nha` đứng trước dấu `{ }`: Node.js cho biết object này được tạo từ class nào.

### 🔆 3. Khi nào dùng class, khi nào dùng Object thường

<table class="rt-table">
<thead>
<tr>
<th>Điểm so sánh</th>
<th>Object viết bằng <code>{ }</code></th>
<th>Class</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dùng khi</td>
<td>Chỉ cần <strong>dữ liệu</strong>: một tài khoản test, một config</td>
<td>Cần <strong>dữ liệu kèm thao tác</strong>, và cần nhiều object cùng khuôn</td>
</tr>
<tr>
<td>Cách tạo</td>
<td>Viết thẳng <code>{ key: value }</code></td>
<td><code>new TenClass(...)</code></td>
</tr>
<tr>
<td>Trong project test</td>
<td>Data test, file JSON, config</td>
<td>Class trang (<code>LoginPage</code>), class dùng chung (<code>BasePage</code>)</td>
</tr>
</tbody>
</table>

Không cần đổi mọi Object thành class. Data test vẫn để dạng Object và JSON như bài trước.

## ✅ Phần 2: Cú pháp class, constructor và method

### 🔆 1. constructor và this

Ở bài Object và JSON, 3 tài khoản của CRM demo là 3 Object viết tay, mỗi Object lặp lại đủ các key. Giờ viết khuôn một lần. Tạo file `bai-08-class/02-test-user.js`:

```javascript
class TestUser {
  // constructor tự chạy mỗi lần gọi new TestUser(...)
  constructor(email, role, loginPath) {
    // this = object đang được tạo
    this.email = email;
    this.role = role;
    this.loginPath = loginPath;
    this.isLoggedIn = false; // giá trị mặc định, không cần truyền vào
  }
}

const admin = new TestUser('admin@example.com', 'admin', '/admin/authentication');
const pm = new TestUser('projectmanager@example.com', 'project-manager', '/admin/authentication');
const customer = new TestUser('customer@example.com', 'customer', '/authentication/login');

console.log(admin);
console.log(pm.role, '|', customer.loginPath);

// Mỗi object giữ dữ liệu RIÊNG: sửa admin, hai object kia không đổi
admin.isLoggedIn = true;
console.log(admin.isLoggedIn, pm.isLoggedIn, customer.isLoggedIn);
```

```bash
node bai-08-class/02-test-user.js
```

Kết quả:

```bash
TestUser {
  email: 'admin@example.com',
  role: 'admin',
  loginPath: '/admin/authentication',
  isLoggedIn: false
}
project-manager | /authentication/login
true false false
```

Ba điểm cần nắm:

- `constructor` là hàm đặc biệt, **tự chạy** mỗi lần bạn viết `new TestUser(...)`. Giá trị trong ngoặc tròn được truyền vào tham số của nó.
- `this` trong constructor là **object đang được tạo**. `this.email = email` nghĩa là: lấy giá trị của tham số `email`, lưu vào thuộc tính `email` của object mới.
- Mỗi object giữ **dữ liệu riêng**. Dòng kết quả cuối `true false false`: sửa `admin` không ảnh hưởng tới `pm` và `customer`.

Tên class viết hoa chữ đầu mỗi từ (`TestUser`, `LoginPage`); tên biến chứa object viết thường chữ đầu (`admin`, `loginPage`). Nhìn chữ hoa là biết đó là khuôn, không phải object.

### 🔆 2. Method: thao tác của object

**Method** là hàm viết trong class, không cần từ khoá `function`. Tạo file `bai-08-class/03-method.js`:

```javascript
const baseUrl = 'https://crm.anhtester.com';

class TestUser {
  constructor(email, role, loginPath) {
    this.email = email;
    this.role = role;
    this.loginPath = loginPath;
  }

  // Method TRẢ VỀ giá trị
  getLoginUrl() {
    return `${baseUrl}${this.loginPath}`;
  }

  // Method gọi method khác của chính object: this.tenMethod()
  describe() {
    console.log(`[${this.role}] ${this.email} đăng nhập tại ${this.getLoginUrl()}`);
  }
}

// Data dạng mảng các Object như ở bài Object và JSON
const rawUsers = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
  { email: 'projectmanager@example.com', role: 'project-manager', loginPath: '/admin/authentication' },
  { email: 'customer@example.com', role: 'customer', loginPath: '/authentication/login' },
];

// Đổi mỗi Object dữ liệu thành một object TestUser có sẵn method
const users = rawUsers.map((item) => new TestUser(item.email, item.role, item.loginPath));

for (const user of users) {
  user.describe();
}

const customerUrl = users[2].getLoginUrl();
console.log(customerUrl);
```

```bash
node bai-08-class/03-method.js
```

Kết quả:

```bash
[admin] admin@example.com đăng nhập tại https://crm.anhtester.com/admin/authentication
[project-manager] projectmanager@example.com đăng nhập tại https://crm.anhtester.com/admin/authentication
[customer] customer@example.com đăng nhập tại https://crm.anhtester.com/authentication/login
https://crm.anhtester.com/authentication/login
```

Trong method, `this` là **object đang gọi method đó**. Khi vòng lặp chạy `user.describe()` với tài khoản Customer, `this.email` là email của Customer. Giống hàm ở bài trước, method trả giá trị bằng `return` (`getLoginUrl`) hoặc chỉ in ra (`describe`). Muốn gọi method khác của chính object thì viết `this.getLoginUrl()`.

Dòng `rawUsers.map(...)` nối với bài trước: data vẫn là mảng các Object, khi cần thao tác thì đổi từng Object thành một object của class.

### 🔆 3. Lỗi quên this.

Tạo file `bai-08-class/04-quen-this.js`:

```javascript
class TestUser {
  constructor(email, role) {
    this.email = email;
    this.role = role;
  }

  describe() {
    // Sai: thiếu this. trước email
    console.log(`[${this.role}] ${email}`);
  }
}

const admin = new TestUser('admin@example.com', 'admin');
admin.describe();
```

```bash
node bai-08-class/04-quen-this.js
```

Kết quả:

```bash
    console.log(`[${this.role}] ${email}`);
                                  ^

ReferenceError: email is not defined
```

Viết `email` trần thì JavaScript đi tìm một **biến** tên `email`. Trong method `describe` không có biến nào như vậy: tham số `email` chỉ sống trong constructor (phạm vi biến của bài Hàm). Dữ liệu của object luôn phải đọc qua `this.`.

> ⚠️ Nguy hiểm hơn là khi bên ngoài class **tình cờ có** một biến trùng tên: chương trình không báo lỗi mà lấy nhầm giá trị của biến đó. Thấy code AI đọc thuộc tính trong method mà thiếu `this.` thì sửa ngay, kể cả khi đang chạy được.

### 🔆 4. Lỗi quên new

Tạo file `bai-08-class/05-quen-new.js`:

```javascript
class TestUser {
  constructor(email) {
    this.email = email;
  }
}

// Sai: gọi class như gọi hàm, thiếu new
const admin = TestUser('admin@example.com');
console.log(admin.email);
```

```bash
node bai-08-class/05-quen-new.js
```

Kết quả:

```bash
const admin = TestUser('admin@example.com');
              ^

TypeError: Class constructor TestUser cannot be invoked without 'new'
```

Thông báo nói rõ: constructor của class `TestUser` không gọi được nếu thiếu `new`. Class là khuôn, không phải hàm để gọi thẳng.

## ✅ Phần 3: Kế thừa với extends và super

### 🔆 1. BasePage và LoginPage

Con cái thừa hưởng tài sản của cha mẹ rồi có thêm tài sản riêng. Class cũng vậy: trang nào của CRM cũng có địa chỉ, cũng mở được, cũng có tiêu đề. Phần chung đó viết **một lần** trong class cha `BasePage`; mỗi trang là một class con, **kế thừa** phần chung bằng từ khoá `extends` và chỉ viết thêm phần riêng. Tạo file `bai-08-class/06-ke-thua.js`:

```javascript
// Class cha: phần mà trang nào cũng có
class BasePage {
  constructor(path, title) {
    this.url = `https://crm.anhtester.com${path}`;
    this.title = title;
  }

  open() {
    console.log(`Mở trang ${this.url}`);
  }

  getTitle() {
    return this.title;
  }
}

// Class con: có mọi thứ của BasePage, thêm phần riêng của trang đăng nhập
class LoginPage extends BasePage {
  constructor() {
    // super(...) gọi constructor của class cha
    super('/admin/authentication', 'Perfex CRM | Anh Tester Demo - Login');
    this.emailLabel = 'Email Address';
  }

  login(email) {
    console.log(`Điền "${email}" vào ô ${this.emailLabel} rồi bấm Login`);
  }
}

const loginPage = new LoginPage();
loginPage.open();                     // method kế thừa từ BasePage
console.log(loginPage.getTitle());    // method kế thừa từ BasePage
loginPage.login('admin@example.com'); // method riêng của LoginPage
console.log(loginPage);
```

```bash
node bai-08-class/06-ke-thua.js
```

Kết quả:

```bash
Mở trang https://crm.anhtester.com/admin/authentication
Perfex CRM | Anh Tester Demo - Login
Điền "admin@example.com" vào ô Email Address rồi bấm Login
LoginPage {
  url: 'https://crm.anhtester.com/admin/authentication',
  title: 'Perfex CRM | Anh Tester Demo - Login',
  emailLabel: 'Email Address'
}
```

- `class LoginPage extends BasePage`: `LoginPage` có sẵn mọi thuộc tính và method của `BasePage`. Trong `LoginPage` không có dòng nào viết `open()` hay `getTitle()` mà vẫn gọi được.
- `super(...)` gọi **constructor của class cha**, để class cha gán `url` và `title`. Sau đó class con gán thêm thuộc tính riêng `emailLabel`.
- Object in ra có đủ 3 thuộc tính: 2 của cha, 1 của con.

Lợi ích với automation: mai thêm trang Dashboard, trang Customers thì mỗi trang chỉ viết phần riêng. Cần sửa cách mở trang thì sửa một chỗ trong `BasePage`.

### 🔆 2. Gọi lại method của class cha bằng super.method()

Class con được viết lại một method đã có ở class cha (gọi là **ghi đè**). Nếu vẫn cần phần việc của cha thì gọi `super.tenMethod()`. Tạo file `bai-08-class/07-super-method.js`:

```javascript
class BasePage {
  constructor(path) {
    this.url = `https://crm.anhtester.com${path}`;
  }

  open() {
    console.log(`Mở trang ${this.url}`);
  }
}

class LoginPage extends BasePage {
  constructor() {
    super('/admin/authentication');
  }

  // Viết lại open(): làm việc của class cha trước, rồi thêm việc riêng
  open() {
    super.open();
    console.log('Chờ ô Email Address hiển thị');
  }
}

const loginPage = new LoginPage();
loginPage.open();
```

```bash
node bai-08-class/07-super-method.js
```

Kết quả:

```bash
Mở trang https://crm.anhtester.com/admin/authentication
Chờ ô Email Address hiển thị
```

`loginPage.open()` chạy bản của `LoginPage`. Bản này gọi `super.open()` để làm phần việc của cha, rồi làm thêm việc riêng. Bỏ dòng `super.open()` thì trang không được mở nữa mà không có thông báo lỗi nào.

### 🔆 3. Lỗi dùng this trước super()

Tạo file `bai-08-class/08-this-truoc-super.js`:

```javascript
class BasePage {
  constructor(path) {
    this.url = `https://crm.anhtester.com${path}`;
  }
}

class LoginPage extends BasePage {
  constructor() {
    // Sai: dùng this trước khi gọi super()
    this.emailLabel = 'Email Address';
    super('/admin/authentication');
  }
}

const loginPage = new LoginPage();
console.log(loginPage.url);
```

```bash
node bai-08-class/08-this-truoc-super.js
```

Kết quả:

```bash
    this.emailLabel = 'Email Address';
    ^

ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
```

Tạm dịch: phải gọi constructor của class cha trước khi dùng `this`. Trong class con, `super(...)` luôn là **dòng đầu tiên** của constructor. Quên hẳn `super()` cũng ra đúng thông báo này (Anh Tester đã chạy thử). Nếu class con không cần thêm thuộc tính riêng thì không viết constructor, JavaScript tự gọi constructor của cha.

## ✅ Phần 4: Đóng gói và đa hình ở mức đủ dùng

### 🔆 1. Đóng gói: bên ngoài chỉ gọi method

Dùng máy ATM bạn chỉ bấm nút rút tiền, không cần biết bên trong máy đếm tiền ra sao. **Đóng gói** trong lập trình là vậy: class giữ chi tiết bên trong, bên ngoài chỉ gọi method. Với class trang, test chỉ viết `loginPage.login(email, password)`, không cần biết ô nhập được tìm bằng locator nào. Khi giao diện đổi, bạn sửa một chỗ trong class, các test giữ nguyên.

JavaScript còn cho **khoá hẳn** một thuộc tính bằng dấu `#` trước tên (field riêng). Tạo file `bai-08-class/09-dong-goi.js`:

```javascript
class TestAccount {
  // Field riêng: tên bắt đầu bằng #, phải khai báo ở đầu class
  #password;

  constructor(email) {
    this.email = email;
    this.#password = process.env.ADMIN_PASSWORD ?? '';
  }

  // Bên ngoài chỉ hỏi được "đã có mật khẩu chưa", không đọc được giá trị
  hasPassword() {
    return this.#password !== '';
  }
}

const account = new TestAccount('admin@example.com');

console.log(account);
console.log(account.hasPassword());
console.log(account.password);
```

```bash
node bai-08-class/09-dong-goi.js
```

Kết quả:

```bash
TestAccount { email: 'admin@example.com' }
false
undefined
```

In object ra không thấy `#password`. `hasPassword()` ra `false` vì máy soạn bài chưa đặt biến `ADMIN_PASSWORD`. `account.password` (không có `#`) là một thuộc tính khác, chưa tồn tại nên ra `undefined`. Còn cố đọc đúng tên `#password` từ bên ngoài, như file `bai-08-class/10-doc-field-rieng.js`:

```javascript
class TestAccount {
  #password;

  constructor(email) {
    this.email = email;
    this.#password = process.env.ADMIN_PASSWORD ?? '';
  }
}

const account = new TestAccount('admin@example.com');

// Sai: đọc field riêng từ bên ngoài class
console.log(account.#password);
```

```bash
node bai-08-class/10-doc-field-rieng.js
```

Kết quả:

```bash
console.log(account.#password);
                   ^

SyntaxError: Private field '#password' must be declared in an enclosing class
```

Đây là `SyntaxError`: Node.js từ chối chạy cả file, chưa dòng nào được thực hiện. Ở bài TypeScript bạn sẽ gặp từ khoá `private`, cách viết phổ biến hơn trong project Playwright cho cùng mục đích.

### 🔆 2. Đa hình: cùng tên method, mỗi class làm một kiểu

Cùng lệnh "mở cửa", cửa nhà thì xoay tay nắm, cửa cuốn thì bấm nút. **Đa hình** là class con viết lại method cùng tên với class cha để làm theo cách của mình. CRM demo có 2 trang đăng nhập: khu quản trị ở `/admin/authentication`, khu khách hàng ở `/authentication/login`. Tạo file `bai-08-class/11-da-hinh.js`:

```javascript
const baseUrl = 'https://crm.anhtester.com';

class LoginPage {
  getPath() {
    return '/admin/authentication';
  }

  open() {
    console.log(`Mở trang ${baseUrl}${this.getPath()}`);
  }
}

// Trang đăng nhập của Customer chỉ khác đường dẫn: viết lại đúng một method
class CustomerLoginPage extends LoginPage {
  getPath() {
    return '/authentication/login';
  }
}

const loginPages = [new LoginPage(), new CustomerLoginPage()];

// Cùng một lời gọi open(), mỗi object chạy theo cách của class mình
for (const loginPage of loginPages) {
  loginPage.open();
}
```

```bash
node bai-08-class/11-da-hinh.js
```

Kết quả:

```bash
Mở trang https://crm.anhtester.com/admin/authentication
Mở trang https://crm.anhtester.com/authentication/login
```

`CustomerLoginPage` không viết lại `open()`. Nó dùng `open()` của cha, nhưng `this.getPath()` bên trong chạy bản của **chính object đang gọi** nên ra đường dẫn của Customer. Vòng lặp không cần `if` để hỏi "đây là trang nào".

## ✅ Phần 5: Class field - thuộc tính khai báo ngoài constructor

Code AI sinh ra hay khai báo thuộc tính ngay trong thân class, không qua constructor. Cách viết này gọi là **class field**. Tạo file `bai-08-class/12-class-field.js`:

```javascript
class LoginPage {
  // Class field: khai báo thuộc tính ngay trong thân class, ngoài constructor
  path = '/admin/authentication';
  timeout = 30000;

  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }
}

const loginPage = new LoginPage('https://crm.anhtester.com');
console.log(loginPage);
```

```bash
node bai-08-class/12-class-field.js
```

Kết quả:

```bash
LoginPage {
  path: '/admin/authentication',
  timeout: 30000,
  baseUrl: 'https://crm.anhtester.com'
}
```

Kết quả giống hệt gán `this.path = ...` trong constructor. Lưu ý thứ tự: `path`, `timeout` đứng trước `baseUrl`, vì class field được gán **trước khi** thân constructor chạy. Thứ tự đó sinh ra một cái bẫy, xem file `bai-08-class/13-field-doc-this-page.js`:

```javascript
class LoginPage {
  // Sai: field chạy TRƯỚC thân constructor, lúc này this.page chưa được gán
  loginButton = this.page.getByRole('button', { name: 'Login' });

  constructor(page) {
    this.page = page;
  }
}

const fakePage = { getByRole: () => 'nút Login' };
const loginPage = new LoginPage(fakePage);
console.log(loginPage.loginButton);
```

```bash
node bai-08-class/13-field-doc-this-page.js
```

Kết quả:

```bash
  loginButton = this.page.getByRole('button', { name: 'Login' });
                          ^

TypeError: Cannot read properties of undefined (reading 'getByRole')
```

Lúc field `loginButton` được gán thì dòng `this.page = page` chưa chạy, `this.page` còn là `undefined`.

> ⚠️ Từ Playwright 1.65, class trang viết bằng TypeScript có field đọc `this.page` kiểu này cũng báo đúng lỗi trên (chi tiết ở bài TypeScript). Trong khoá học, mọi thuộc tính cần tới `page` đều **gán trong constructor**.

## ✅ Phần 6: Thực hành - class trang đăng nhập, bước đầu của Page Object Model

### 🔆 1. Viết class LoginPage chạy bằng Node.js

**Page Object Model** (POM) là cách tổ chức code test: **mỗi trang của website là một class**, class đó giữ locator và thao tác của trang; file test chỉ gọi method. Bạn chưa cài Playwright, nên bài này dùng một **trang giả** `fakePage`: Object có các method `goto`, `fill`, `click`, `title` chỉ in ra log. Hàm `fakeTest` mô phỏng hàm `test` của Playwright như ở bài Hàm. Tạo file `bai-08-class/crm-login-page.js`:

```javascript
// ===== 1. Trang giả: có các method cùng tên với page của Playwright, chỉ in ra log =====
const fakePage = {
  goto(url) {
    console.log(`  [page] goto ${url}`);
  },
  fill(label, value) {
    const shown = label === 'Password' ? '***' : value; // không in mật khẩu ra log
    console.log(`  [page] fill "${label}" = ${shown}`);
  },
  click(name) {
    console.log(`  [page] click "${name}"`);
  },
  title() {
    return 'Perfex CRM | Anh Tester Demo - Login';
  },
};

// ===== 2. Class cha: phần mà trang nào cũng có =====
class BasePage {
  constructor(page, path) {
    this.page = page;
    this.url = `https://crm.anhtester.com${path}`;
  }

  open() {
    this.page.goto(this.url);
  }

  getTitle() {
    return this.page.title();
  }
}

// ===== 3. Class trang đăng nhập: gom locator và thao tác của MỘT trang =====
class LoginPage extends BasePage {
  constructor(page) {
    super(page, '/admin/authentication');
    this.emailLabel = 'Email Address';
    this.passwordLabel = 'Password';
    this.loginButtonName = 'Login';
  }

  login(email, password) {
    this.page.fill(this.emailLabel, email);
    this.page.fill(this.passwordLabel, password);
    this.page.click(this.loginButtonName);
  }
}

// ===== 4. Hàm chạy test giả: in tên test rồi gọi callback =====
function fakeTest(name, testFn) {
  console.log(`▶ ${name}`);
  testFn({ page: fakePage });
}

// ===== 5. Test: chỉ gọi method của class trang, không còn locator nào ở đây =====
fakeTest('Mở trang đăng nhập Admin', ({ page }) => {
  const loginPage = new LoginPage(page);
  loginPage.open();

  const title = loginPage.getTitle();
  console.log(`  Tiêu đề: ${title}`);
  console.log(`  Kết quả: ${title === 'Perfex CRM | Anh Tester Demo - Login' ? 'PASS' : 'FAIL'}`);
});

fakeTest('Đăng nhập bằng tài khoản Admin', ({ page }) => {
  const loginPage = new LoginPage(page);
  loginPage.open();
  loginPage.login(process.env.ADMIN_EMAIL ?? 'admin@example.com', process.env.ADMIN_PASSWORD ?? '');
});
```

```bash
node bai-08-class/crm-login-page.js
```

Kết quả:

```bash
▶ Mở trang đăng nhập Admin
  [page] goto https://crm.anhtester.com/admin/authentication
  Tiêu đề: Perfex CRM | Anh Tester Demo - Login
  Kết quả: PASS
▶ Đăng nhập bằng tài khoản Admin
  [page] goto https://crm.anhtester.com/admin/authentication
  [page] fill "Email Address" = admin@example.com
  [page] fill "Password" = ***
  [page] click "Login"
```

Đọc lại theo từng khối:

- **Khối 2:** `BasePage` nhận `page` qua constructor và giữ ở `this.page`. Mọi method sau đó thao tác qua `this.page`.
- **Khối 3:** `LoginPage` gọi `super(page, ...)` rồi khai báo tên các phần tử của trang ở **một chỗ**. Nhãn `Email Address` đổi thì chỉ sửa một dòng.
- **Khối 5:** test đọc lên như lời mô tả: mở trang, đăng nhập. Việc so sánh tiêu đề để ra `PASS`/`FAIL` nằm **trong test**, không nằm trong class trang.
- Mật khẩu chỉ đọc từ `process.env.ADMIN_PASSWORD`, và `fakePage` in `***` thay cho giá trị.

### 🔆 2. Đặt cạnh class trang của Playwright thật

Đoạn dưới đây **chỉ để đọc, chưa chạy** (cần Playwright, cài ở chương sau; phần đăng nhập CRM Anh Tester không chạy tự động khi soạn bài). Xem thêm [tài liệu Page Object Model của Playwright](https://playwright.dev/docs/pom).

```javascript
class BasePage {
  constructor(page, path) {
    this.page = page;
    this.url = `https://crm.anhtester.com${path}`;
  }

  async open() {
    await this.page.goto(this.url);
  }

  async getTitle() {
    return await this.page.title();
  }
}

class LoginPage extends BasePage {
  constructor(page) {
    super(page, '/admin/authentication');
    this.emailInput = page.getByLabel('Email Address');
    this.passwordInput = page.getByLabel('Password');
    this.loginButton = page.getByRole('button', { name: 'Login' });
  }

  async login(email, password) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
}

test('Đăng nhập bằng tài khoản Admin', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.open();
  await loginPage.login(process.env.ADMIN_EMAIL, process.env.ADMIN_PASSWORD);
});
```

Khuôn giống hệt bản bạn vừa chạy: `constructor(page)`, `super(...)`, `this.page`, `new LoginPage(page)`. Chỉ khác 2 điểm: thuộc tính giữ **locator thật** (`getByLabel`, `getByRole`) thay cho chuỗi, và có thêm `async`/`await`. Hai từ khoá đó là nội dung của bài kế tiếp.

### 🔆 3. Lưu code lên GitHub

Xong bài thì commit thư mục `bai-08-class` như đã học ở bài Git:

```bash
git add bai-08-class/
git commit -m "bai-08-class: class, constructor va ke thua"
git push
```

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức của bài

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn dùng được các prompt dưới đây: chỗ có `@đường-dẫn` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay. Không dán mật khẩu hay file `.env` vào khung chat.

```markdown
Tôi mới học class trong JavaScript, chưa học async/await và chưa học Playwright.
Đọc file @bai-08-class/crm-login-page.js và giải thích TỪNG DÒNG của class LoginPage:
1. constructor(page) nhận gì, ai truyền vào, lúc nào nó chạy?
2. super(page, '/admin/authentication') làm gì? Bỏ dòng này thì báo lỗi gì?
3. Trong method login, this là object nào?
Chỉ giải thích, KHÔNG sửa file. Chỗ nào tôi chưa học thì nói "sẽ học sau", đừng giải thích dài.
```

```markdown
Dưới đây là 3 hàm rời rạc tôi viết ở bài Hàm, cùng làm việc với trang đăng nhập CRM:

function buildLoginUrl(baseUrl, loginPath) { return `${baseUrl}${loginPath}`; }
function openLogin(baseUrl, loginPath) { console.log(`Mở ${buildLoginUrl(baseUrl, loginPath)}`); }
function describeLogin(baseUrl, loginPath, email) { console.log(`${email} đăng nhập tại ${buildLoginUrl(baseUrl, loginPath)}`); }

Hãy chuyển thành MỘT class JavaScript thuần (không TypeScript, không import/export, không static, không getter/setter).
Giải thích: tham số nào trở thành thuộc tính gán trong constructor, tham số nào vẫn là tham số của method, vì sao.
Kèm đoạn code gọi thử chạy được bằng node và kết quả in ra.
```

```markdown
Đoạn code sau chạy bằng node bị lỗi. Hãy chỉ ra TỪNG chỗ sai liên quan tới new, super và this:
dòng nào, thông báo lỗi Node.js sẽ in là gì, vì sao sai. Sau đó mới đưa bản đã sửa, không đổi tên class và method.

[dán code của bạn vào đây]
```

```markdown
Đọc file @bai-08-class/11-da-hinh.js. Vẽ sơ đồ kế thừa bằng chữ (dạng cây) cho các class trong file:
mỗi class có thuộc tính gì, method gì, method nào kế thừa từ cha, method nào được viết lại.
Sau đó giải thích vì sao CustomerLoginPage không viết open() mà vẫn mở đúng trang /authentication/login.
```

### 🔆 2. Bộ kit liên quan gì tới class?

Rule [automation\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md) của bộ kit **bắt buộc dùng Page Object Model** (mục 1): Page class khai báo locator và method tương tác với giao diện; **assertion chỉ đặt ở phần test, không đặt trong Page class**. Mục 5 của rule quy định tên Page class viết kiểu PascalCase kèm hậu tố `Page`, ví dụ `LoginPage.ts`. Lệnh [/generate-automation-framework](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/generate-automation-framework.md) ở bước 3 sinh sẵn một Base Page chứa các method dùng chung, bước 4 sinh một `LoginPage` mẫu. Đó chính là cặp `BasePage` và `LoginPage` của bài này. Lệnh dùng từ chương Playwright.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Rà class AI viết theo bảng sau:

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
<td>Trong method đọc thuộc tính mà thiếu <code>this.</code></td>
<td><code>ReferenceError</code>, hoặc lấy nhầm một biến trùng tên ở ngoài class</td>
<td>Thêm <code>this.</code> trước tên thuộc tính</td>
</tr>
<tr>
<td><code>const p = LoginPage(page)</code></td>
<td><code><span>TypeError:</span> <span>Class</span> <span>constructor</span> <span>LoginPage</span> <span>cannot</span> <span>be</span> <span>invoked</span> <span>without</span> <span>'new'</span></code></td>
<td>Thêm <code>new</code></td>
</tr>
<tr>
<td>Class con có constructor nhưng thiếu <code>super()</code>, hoặc dùng <code>this</code> trước <code>super()</code></td>
<td><code><span>ReferenceError:</span> <span>Must</span> <span>call</span> <span>super</span> <span>constructor...</span></code></td>
<td>Đưa <code>super(...)</code> lên dòng đầu constructor</td>
</tr>
<tr>
<td>Một class chứa locator và thao tác của mọi trang</td>
<td>File dài hàng trăm dòng, sửa một trang dễ làm hỏng trang khác</td>
<td>Tách mỗi trang một class</td>
</tr>
<tr>
<td>Class trang tự so sánh kết quả, tự in <code>PASS</code>/<code>FAIL</code> hoặc chứa <code>expect(...)</code></td>
<td>Trái rule của bộ kit: assertion chỉ đặt ở test. Đọc test không biết nó kiểm tra gì</td>
<td>Method của class trang chỉ thao tác hoặc trả giá trị; việc kiểm tra chuyển về test</td>
</tr>
<tr>
<td>Kế thừa 3, 4 tầng (<code>A extends B extends C...</code>) cho vài trang</td>
<td>Muốn hiểu một method phải lần qua nhiều file</td>
<td>Giữ một tầng: <code>BasePage</code> rồi tới các trang</td>
</tr>
<tr>
<td>Locator trong class trang viết bằng CSS selector</td>
<td>Khoá học quy ước chỉ dùng <code>getBy...</code> và XPath; ở chương Playwright bạn sẽ ghi quy ước này thành rule của project</td>
<td>Yêu cầu AI đổi sang <code>getBy...</code>, không được thì XPath</td>
</tr>
<tr>
<td>Class field đọc <code>this.page</code> trong khi <code>page</code> được gán ở constructor</td>
<td><code><span>TypeError:</span> <span>Cannot</span> <span>read</span> <span>properties</span> <span>of</span> <span>undefined</span></code></td>
<td>Chuyển phép gán đó vào trong constructor</td>
</tr>
</tbody>
</table>

## ✅ Phần 9: Bài tập thực hành

Đặt file bài tập trong thư mục `bai-08-class/`, làm xong thì commit và push.

**Bài tập 1 - Class TestCase.** Tạo file `bt1-test-case.js`: class `TestCase` có thuộc tính `id`, `title`, `status` (mặc định `'not-run'`), method `markPassed()`, `markFailed()` đổi `status` và method `summary()` trả về chuỗi dạng `[passed] TC01 - Mở trang đăng nhập`. Tạo 3 object, đánh dấu 2 passed, 1 failed, in `summary()` của từng object bằng `for...of`.

**Bài tập 2 - Thêm một trang.** Chép `crm-login-page.js` thành `bt2-forgot-password-page.js`. Thêm class `ForgotPasswordPage extends BasePage` với đường dẫn `/admin/authentication/forgot_password` và method `requestReset(email)` điền ô `Email Address` rồi bấm nút `Confirm`. Thêm một `fakeTest` gọi class mới. Không sửa `BasePage`.

**Bài tập 3 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt3-duyet-code.js`, chép vào và chạy:

```javascript
class BasePage {
  constructor(path) {
    this.url = `https://crm.anhtester.com${path}`;
  }

  open() {
    console.log(`Mở trang ${this.url}`);
  }
}

class LoginPage extends BasePage {
  constructor() {
    this.emailLabel = 'Email Address';
    super('/admin/authentication');
  }

  login(email) {
    console.log(`Điền "${email}" vào ô ${emailLabel}`);
    console.log(email.includes('@') ? 'PASS' : 'FAIL');
  }
}

const loginPage = LoginPage();
loginPage.open();
loginPage.login('admin@example.com');
```

Kết quả chạy thật:

```bash
const loginPage = LoginPage();
                  ^

TypeError: Class constructor LoginPage cannot be invoked without 'new'
```

Có 4 chỗ sai theo bảng ở Phần 8: 3 chỗ làm chương trình dừng (sửa xong chỗ này mới lộ ra chỗ sau) và 1 chỗ sai về cách tổ chức. Sửa xong, file phải in đúng 2 dòng: `Mở trang https://crm.anhtester.com/admin/authentication` và `Điền "admin@example.com" vào ô Email Address`.

## ✅ Phần 10: Ghi nhớ nhanh

- Class là khuôn, object là sản phẩm tạo từ khuôn bằng `new`. Class gom dữ liệu (thuộc tính) và thao tác (method) của cùng một thứ.
- `constructor` tự chạy khi `new`. `this` là object đang được tạo hoặc đang gọi method; đọc thuộc tính và gọi method khác đều qua `this.`.
- `class Con extends Cha`: con có mọi thứ của cha. `super(...)` là dòng đầu constructor của con; `super.method()` gọi lại bản của cha.
- Đóng gói: bên ngoài chỉ gọi method. Đa hình: class con viết lại method cùng tên.
- Thuộc tính cần tới `page` thì gán trong constructor, không viết thành class field.
- Page Object Model: mỗi trang một class giữ locator và thao tác; việc kiểm tra kết quả nằm ở test.

✅ **Kết luận:** Bạn đã có class trang đầu tiên, nhưng nó mới chạy với trang giả. Với Playwright thật, mọi method của class trang đều có `async` và phải gọi kèm `await`; mỗi class nằm ở một file riêng nên cần cách lấy class từ file này sang file khác. Bài kế tiếp, **async/await, import/export và try...catch trong JavaScript**, giải quyết cả hai việc đó.

---

## Bài tập riêng — Class, constructor, kế thừa và bước đầu Page Object Model

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-98](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-98)

**Mục tiêu:** viết class có constructor và method, kế thừa BasePage để thêm một trang mới mà không sửa class cha.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-08-class`

Làm xong thì commit và push.

### 📝 Đề bài

#### Bài tập 1 - Class TestCase

Tạo file `bt1-test-case.js`: class `TestCase` có thuộc tính `id`, `title`, `status` (mặc định `not-run`), method `markPassed()`, `markFailed()` đổi status và method `summary()` trả về chuỗi dạng `[passed] TC01 - Mở trang đăng nhập`. Tạo 3 object, đánh dấu 2 passed, 1 failed, in `summary()` của từng object bằng `for...of`.

#### Bài tập 2 - Thêm một trang

Chép `crm-login-page.js` của bài học thành `bt2-forgot-password-page.js`. Thêm `class ForgotPasswordPage extends BasePage` với đường dẫn `/admin/authentication/forgot_password` và method `requestReset(email)` điền ô **Email Address** rồi bấm nút **Confirm**. Thêm một `fakeTest` gọi class mới. **Không sửa** `BasePage`.

#### Bài tập 3 - Duyệt code AI

Tạo file `bt3-duyet-code.js`, chép đoạn code AI viết dưới đây và chạy. Có **4 chỗ sai** theo bảng ở Phần 8: 3 chỗ làm chương trình dừng (sửa xong chỗ này mới lộ ra chỗ sau) và 1 chỗ sai về cách tổ chức.

```javascript
class BasePage {
  constructor(path) {
    this.url = `https://crm.anhtester.com${path}`;
  }
  open() {
    console.log(`Mở trang ${this.url}`);
  }
}
class LoginPage extends BasePage {
  constructor() {
    this.emailLabel = 'Email Address';
    super('/admin/authentication');
  }
  login(email) {
    console.log(`Điền "${email}" vào ô ${emailLabel}`);
    console.log(email.includes('@') ? 'PASS' : 'FAIL');
  }
}
const loginPage = LoginPage();
loginPage.open();
loginPage.login('admin@example.com');
```

### 📦 Cách nộp bài

1. Làm bài trong thư mục `bai-08-class/` của repo `js-ts-for-tester`, commit và push lên nhánh `main`.
2. Dán link thư mục bài trên GitHub vào ô **Link GitHub**, dạng `https://github.com/<ten-ban>/js-ts-for-tester/tree/main/bai-08-class`. Repo Private thì vào **Settings → Collaborators** thêm tài khoản GitHub của giảng viên, nếu không giảng viên không mở được.
3. Trong ô **Nội dung bài làm (Editor)**, dán **kết quả chạy thật** của từng file (mỗi file một **Đoạn code mẫu** chọn Text / Log) và phần trả lời các câu hỏi.
4. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*.

### ✅ Tiêu chí Đạt

- Bài tập 1 in đúng 3 dòng `[passed] ...`, `[passed] ...`, `[failed] ...`; status đổi qua method, bên ngoài không gán trực tiếp `tc.status = ...`.
- Bài tập 2: `ForgotPasswordPage` gọi `super(...)` với đúng đường dẫn, dùng lại `open()` của BasePage; git diff cho thấy BasePage không đổi; fakeTest chạy ra đủ các bước mở trang, điền email, bấm Confirm.
- Bài tập 3 sau khi sửa in đúng 2 dòng: `Mở trang https://crm.anhtester.com/admin/authentication` và `Điền "admin@example.com" vào ô Email Address`. Đủ 4 chỗ: thiếu `new`; dùng `this` trước `super()`; thiếu `this.` trước `emailLabel`; method của trang không nên tự kết luận PASS/FAIL (việc kiểm tra để ở test).
- Code đã có trên GitHub, nhánh main.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.