# Bài 10 - [Javascript Typescript] Kiểu dữ liệu, type, interface và class trong TypeScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/408](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/408)

✅ TypeScript là gì và vì sao Automation dùng TypeScript  
✅ Chạy file .ts bằng Node.js và kiểm tra kiểu bằng npx tsc --noEmit  
✅ Chú thích kiểu cho biến, mảng, Object, hàm và khi nào tránh any  
✅ type và interface - đặt tên cho kiểu dữ liệu  
✅ class trong TypeScript với private, readonly và constructor viết gọn  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra code TypeScript do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước bạn đã tách `BasePage`, `LoginPage` ra từng file, thêm `async`/`await` và bắt lỗi bằng `try...catch`. Code đã có khuôn của một project Playwright, chỉ còn thiếu **kiểu dữ liệu**. Bài cuối của chương thêm phần đó, như bài Biến đã hẹn: **TypeScript = JavaScript + kiểu**. Học xong bạn sẽ:

- Hiểu vì sao Automation dùng TypeScript.
- Chạy file `.ts` bằng Node.js và kiểm tra kiểu bằng `npx tsc --noEmit`.
- Viết chú thích kiểu cho biến, mảng, Object, hàm; biết khi nào tránh `any`.
- Đặt tên cho kiểu dữ liệu bằng `type` và `interface`.
- Viết class có `private`, `readonly`, constructor viết gọn; tránh một lỗi mới của Playwright 1.65.

> 📌 Làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật (Node.js v24.17.0, TypeScript 7.0.2), đã lược dòng đường dẫn file và các dòng `at ...` ở kết quả có lỗi.

## ✅ Phần 1: TypeScript là gì và vì sao Automation dùng TypeScript

### 🔆 1. Từ tờ khai có ô "chỉ điền số" tới TypeScript

Tờ khai ở quầy giao dịch có ô ghi rõ "chỉ điền số". Điền chữ vào thì bị trả lại **ngay tại quầy**. Nếu ô không ghi gì, tờ khai sai vẫn được nhận, tới cuối quy trình mới bị phát hiện.

JavaScript là tờ khai không ghi chú: biến nào cũng nhận mọi loại giá trị, sai thì tới lúc chạy mới biết. [TypeScript](https://www.typescriptlang.org/) cho bạn ghi chú vào từng ô: biến này chỉ chứa số, hàm này nhận một chuỗi. Phần ghi chú đó gọi là **kiểu** (type). Mọi thứ còn lại vẫn là JavaScript bạn đã học trong chương này.

Phần kiểu chỉ có tác dụng **lúc viết code**. Lúc chạy, nó bị xoá đi và thứ thật sự chạy là JavaScript.

### 🔆 2. Ba lý do Automation dùng TypeScript

<table class="rt-table">
<thead>
<tr>
<th>Lý do</th>
<th>Ý nghĩa với tester</th>
</tr>
</thead>
<tbody>
<tr>
<td>Báo lỗi trước khi chạy</td>
<td>Gõ sai tên thuộc tính, truyền số vào chỗ cần chuỗi, quên <code>await</code>: VS Code gạch đỏ ngay lúc gõ, không phải chờ test chạy tới giữa mới dừng</td>
</tr>
<tr>
<td>Gợi ý code khi gõ</td>
<td>Gõ <code>page.</code> trong file test, VS Code hiện danh sách <code>goto</code>, <code>getByRole</code>, <code>getByLabel</code>... kèm tham số của từng hàm</td>
</tr>
<tr>
<td>Code tự mô tả</td>
<td>Nhìn <code><span>login(data:</span> <span>LoginData):</span> <span>Promise&lt;void&gt;</span></code> là biết hàm cần gì, trả về gì. Duyệt code AI nhanh hơn</td>
</tr>
</tbody>
</table>

Playwright được viết bằng TypeScript và lúc cài nó chọn sẵn TypeScript, nên cả khoá học viết test trong file `.ts`.

## ✅ Phần 2: Cài TypeScript, chạy và kiểm tra kiểu

### 🔆 1. Chuẩn bị thư mục và cài TypeScript

Mở Terminal tại thư mục project rồi cài hai gói: `typescript` là trình kiểm tra kiểu, `@types/node` mô tả kiểu cho những thứ có sẵn của Node.js như `process.env`.

```bash
npm install -D typescript @types/node
npx tsc -v
```

Kết quả:

```bash
Version 7.0.2
```

`-D` ghi hai gói vào mục `devDependencies` của `package.json`. `tsc` là tên lệnh của TypeScript. Từ bản 7, `tsc` được viết lại bằng ngôn ngữ Go nên kiểm tra nhanh hơn nhiều; cú pháp TypeScript không đổi (xem [bài công bố TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)).

Tạo thư mục `bai-10-typescript`. Cả bài sẽ có các file sau:

```bash
js-ts-for-tester/
├── package.json
├── tsconfig.json
└── bai-10-typescript/
    ├── package.json
    ├── 01-loi-luc-chay.js
    ├── 02-loi-truoc-khi-chay.ts
    ├── 03-kieu-co-ban.ts
    ├── 04-mang-object.ts
    ├── 05-ham.ts
    ├── 06-any.ts
    ├── 07-type-user.ts
    ├── 08-interface.ts
    ├── 09-class-co-kieu.ts
    ├── 10-constructor-gon.ts
    ├── 11-bay-field.ts
    ├── types.ts
    ├── utils/
    │   ├── url.ts
    │   └── fake-page.ts
    ├── pages/
    │   ├── BasePage.ts
    │   └── LoginPage.ts
    └── crm-login.ts
```

File `bai-10-typescript/package.json` chỉ có một dòng:

```json
{ "type": "module" }
```

Node.js chỉ cho dùng `import`/`export` khi file được coi là module, và nó xét file `.ts` theo đúng cách xét file `.js`. `package.json` ở gốc project đang là `"type": "commonjs"`; file nhỏ này đổi riêng thư mục `bai-10-typescript` sang module.

File `tsconfig.json` đặt ở **gốc project**, là cấu hình cho `tsc` và VS Code:

```json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "nodenext",
    "strict": true,
    "noEmit": true,
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "types": ["node"]
  },
  "include": ["bai-10-typescript"]
}
```

<table class="rt-table">
<thead>
<tr>
<th>Option</th>
<th>Ý nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>strict</code></td>
<td>Bật nhóm kiểm tra chặt. TypeScript 7 bật sẵn; ghi ra để nhận ra khi AI đổi thành <code>false</code></td>
</tr>
<tr>
<td><code>noEmit</code></td>
<td>Chỉ kiểm tra, không sinh file <code>.js</code> cạnh mỗi file <code>.ts</code></td>
</tr>
<tr>
<td><code>allowImportingTsExtensions</code></td>
<td>Cho viết <code>import ... from './types.ts'</code>. Node.js bắt buộc ghi đủ đuôi <code>.ts</code></td>
</tr>
<tr>
<td><code>verbatimModuleSyntax</code></td>
<td>Bắt viết <code>import type</code> khi thứ được import chỉ là kiểu (Phần 6)</td>
</tr>
<tr>
<td><code>types</code></td>
<td>Nạp gói <code>@types/node</code>. Thiếu thì <code>process.env</code> bị báo <code>TS2591: Cannot find name 'process'</code></td>
</tr>
<tr>
<td><code>include</code></td>
<td>Chỉ kiểm thư mục của bài này</td>
</tr>
</tbody>
</table>

> 📌 Lệnh `npx tsc --init` cũng tạo được `tsconfig.json`, nhưng file mẫu đó bật thêm nhiều option chưa cần. Tra nghĩa từng option tại [typescriptlang.org/tsconfig](https://www.typescriptlang.org/tsconfig/).

### 🔆 2. Cùng một lỗi: JavaScript báo lúc chạy, TypeScript báo trước khi chạy

Tạo file JavaScript `bai-10-typescript/01-loi-luc-chay.js`. Dòng thứ 5 gõ nhầm `role` thành `roel`:

```javascript
const user = { email: 'admin@example.com', role: 'admin' };

console.log('Bước 1: mở trang đăng nhập');
console.log(`Bước 2: điền email ${user.email}`);
console.log(`Bước 3: kiểm tra vai trò ${user.roel.toUpperCase()}`);
console.log('Bước 4: bấm nút Login');
```

```bash
node bai-10-typescript/01-loi-luc-chay.js
```

Kết quả:

```bash
Bước 1: mở trang đăng nhập
Bước 2: điền email admin@example.com
console.log(`Bước 3: kiểm tra vai trò ${user.roel.toUpperCase()}`);
                                                  ^

TypeError: Cannot read properties of undefined (reading 'toUpperCase')
```

Hai bước đầu chạy xong rồi chương trình mới dừng. Với test thật, đó là lúc form đã điền một nửa.

Giờ **chép nguyên nội dung** đó sang file `bai-10-typescript/02-loi-truoc-khi-chay.ts`, chỉ đổi đuôi thành `.ts`. Rồi kiểm tra kiểu:

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/02-loi-truoc-khi-chay.ts(5,46): error TS2339: Property 'roel' does not exist on type '{ email: string; role: string; }'.
```

Chưa dòng nào chạy mà lỗi đã lộ ra. Cách đọc dòng lỗi của `tsc`: `tên-file(dòng,cột)`, mã lỗi `TS2339`, rồi nội dung: thuộc tính `roel` không có trên kiểu `{ email: string; role: string; }`. Bạn chưa ghi kiểu nào, TypeScript tự suy ra từ giá trị của `user`. Trong VS Code, chỗ `roel` bị gạch đỏ ngay lúc gõ.

Nhưng nếu bạn bỏ qua và vẫn chạy file:

```bash
node bai-10-typescript/02-loi-truoc-khi-chay.ts
```

Kết quả:

```bash
Bước 1: mở trang đăng nhập
Bước 2: điền email admin@example.com
console.log(`Bước 3: kiểm tra vai trò ${user.roel.toUpperCase()}`);
                                                  ^

TypeError: Cannot read properties of undefined (reading 'toUpperCase')
```

Y hệt file JavaScript. Node.js 24 chạy thẳng được file `.ts` vì nó **xoá phần kiểu rồi chạy, không kiểm tra kiểu** ([tài liệu Node.js về TypeScript](https://nodejs.org/docs/latest-v24.x/api/typescript.html)). Sửa `roel` thành `role` rồi chạy lại: `npx tsc --noEmit` không in gì (không có lỗi kiểu), `node` in đủ bốn bước.

### 🔆 3. Hai lệnh, hai việc khác nhau

<table class="rt-table">
<thead>
<tr>
<th>Lệnh</th>
<th>Làm gì</th>
<th>Không làm gì</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>npx tsc --noEmit</code></td>
<td>Kiểm tra kiểu toàn bộ file <code>.ts</code> trong <code>include</code></td>
<td>Không chạy code</td>
</tr>
<tr>
<td><code>node tên-file.ts</code></td>
<td>Xoá phần kiểu rồi chạy</td>
<td>Không kiểm tra kiểu, không đọc <code>tsconfig.json</code></td>
</tr>
</tbody>
</table>

Thứ tự làm việc: **`npx tsc --noEmit` sạch rồi mới chạy**. Playwright cũng chạy test kể cả khi code có lỗi kiểu, nên [tài liệu Playwright](https://playwright.dev/docs/test-typescript) khuyên chạy `tsc --noEmit` song song.

> 📌 Từ đây, file ví dụ có vài dòng nằm dưới chú thích `Dòng lỗi cố ý`. Chạy `npx tsc --noEmit` xem lỗi, rồi **xoá các dòng đó** để ví dụ sau không lẫn lỗi cũ.

## ✅ Phần 3: Chú thích kiểu cho biến, mảng, Object và hàm

### 🔆 1. string, number, boolean và suy luận kiểu

Kiểu ghi sau tên biến, cách bằng dấu hai chấm. Tạo file `bai-10-typescript/03-kieu-co-ban.ts`:

```typescript
// Ghi rõ kiểu sau dấu hai chấm
const baseUrl: string = 'https://crm.anhtester.com';
let retryCount: number = 0;
let isHeadless: boolean = true;

// Suy luận kiểu: đã có giá trị ban đầu thì TypeScript tự hiểu kiểu
const loginPath = '/admin/authentication'; // string
let timeout = 30000;                       // number

retryCount = retryCount + 1;
isHeadless = false;
console.log(baseUrl + loginPath, retryCount, isHeadless, timeout);

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
timeout = '60 giây';
retryCount = true;
console.log(timeout, retryCount);
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/03-kieu-co-ban.ts(15,1): error TS2322: Type 'string' is not assignable to type 'number'.
bai-10-typescript/03-kieu-co-ban.ts(16,1): error TS2322: Type 'boolean' is not assignable to type 'number'.
```

`timeout` không ghi kiểu mà vẫn bị bắt lỗi: giá trị ban đầu là `30000` nên TypeScript tự hiểu nó là `number`. Đó là **suy luận kiểu**. Quy tắc: biến đã có giá trị ban đầu thì **không cần ghi kiểu**; chỉ ghi ở chỗ TypeScript không tự biết được, nhiều nhất là tham số của hàm.

Nếu vẫn chạy file bằng `node`, hai dòng sai kiểu chạy bình thường:

```bash
https://crm.anhtester.com/admin/authentication 1 false 30000
60 giây true
```

### 🔆 2. Mảng và Object

Tạo file `bai-10-typescript/04-mang-object.ts`:

```typescript
// Mảng: kiểu của phần tử + []
const browsers: string[] = ['chromium', 'firefox'];
const timeouts: number[] = [5000, 30000];

// Object: ghi kiểu cho từng thuộc tính, dấu ? là thuộc tính tuỳ chọn
const adminUser: { email: string; role: string; phone?: string } = {
  email: 'admin@example.com',
  role: 'admin',
};

browsers.push('webkit');
console.log(browsers, timeouts.length);
console.log(adminUser.email, adminUser.phone ?? 'chưa có số');

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
browsers.push(123);
console.log(adminUser.pasword);
const pmUser: { email: string; role: string } = { email: 'projectmanager@example.com' };
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/04-mang-object.ts(16,15): error TS2345: Argument of type 'number' is not assignable to parameter of type 'string'.
bai-10-typescript/04-mang-object.ts(17,23): error TS2339: Property 'pasword' does not exist on type '{ email: string; role: string; phone?: string | undefined; }'.
bai-10-typescript/04-mang-object.ts(18,7): error TS2741: Property 'role' is missing in type '{ email: string; }' but required in type '{ email: string; role: string; }'.
```

Mảng `string[]` không nhận số; thuộc tính gõ sai tên bị bắt; Object thiếu thuộc tính bắt buộc bị bắt. `phone?` có dấu `?` nên được phép vắng mặt. Kiểu của nó hiện trong lỗi thứ hai là `string | undefined`; dấu `|` đọc là "hoặc".

Xoá ba dòng lỗi rồi chạy `node bai-10-typescript/04-mang-object.ts`:

```bash
[ 'chromium', 'firefox', 'webkit' ] 2
admin@example.com chưa có số
```

### 🔆 3. Hàm: kiểu của tham số và của giá trị trả về

Tạo file `bai-10-typescript/05-ham.ts`:

```typescript
// Tham số có kiểu; sau ngoặc tròn là kiểu của giá trị trả về
function buildUrl(path: string, baseUrl?: string): string {
  return `${baseUrl ?? 'https://crm.anhtester.com'}${path}`;
}

// Arrow function ghi kiểu y như vậy
const isLoginTitle = (title: string): boolean => title.includes('Login');

// void: hàm không trả về gì
function logStep(message: string): void {
  console.log(`[STEP] ${message}`);
}

// Hàm async luôn trả về Promise. Promise<string>: khi xong sẽ cho ra một string
async function getTitle(): Promise<string> {
  await new Promise((resolve) => setTimeout(resolve, 200));
  return 'Perfex CRM | Anh Tester Demo - Login';
}

logStep(buildUrl('/admin/authentication'));
logStep(buildUrl('/admin/authentication', 'http://localhost:8080'));
const title = await getTitle();
console.log(title, isLoginTitle(title));

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
buildUrl(404);
buildUrl();
const title2: string = getTitle();
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/05-ham.ts(26,10): error TS2345: Argument of type 'number' is not assignable to parameter of type 'string'.
bai-10-typescript/05-ham.ts(27,1): error TS2554: Expected 1-2 arguments, but got 0.
bai-10-typescript/05-ham.ts(28,7): error TS2322: Type 'Promise<string>' is not assignable to type 'string'.
```

<table class="rt-table">
<thead>
<tr>
<th>Cách viết</th>
<th>Đọc là</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>path: string</code></td>
<td>Tham số bắt buộc, phải là chuỗi</td>
</tr>
<tr>
<td><code>baseUrl?: string</code></td>
<td>Tham số tuỳ chọn. Vì vậy lỗi thứ hai ghi "cần 1-2 tham số"</td>
</tr>
<tr>
<td><code>): string</code>, <code>): boolean</code></td>
<td>Kiểu của giá trị hàm trả về</td>
</tr>
<tr>
<td><code>): void</code></td>
<td>Hàm không trả về gì</td>
</tr>
<tr>
<td><code>): Promise&lt;string&gt;</code></td>
<td>Hàm <code>async</code>: trả về Promise, <code>await</code> xong cho ra một chuỗi. Cú pháp <code>&lt; &gt;</code> (Generics) chỉ cần đọc được</td>
</tr>
</tbody>
</table>

Lỗi thứ ba đáng giá nhất: **quên `await`**. TypeScript chỉ đúng dòng đang gán một Promise vào biến kiểu `string`. Xoá ba dòng lỗi rồi chạy `node bai-10-typescript/05-ham.ts`:

```bash
[STEP] https://crm.anhtester.com/admin/authentication
[STEP] http://localhost:8080/admin/authentication
Perfex CRM | Anh Tester Demo - Login true
```

### 🔆 4. any: tắt kiểm tra kiểu

Tạo file `bai-10-typescript/06-any.ts`, vẫn là lỗi gõ nhầm `roel` của Phần 2:

```typescript
// any = "kiểu gì cũng được": TypeScript ngừng kiểm tra mọi thứ đi qua biến này
function getRole(user: any): string {
  return user.roel.toUpperCase();
}

console.log(getRole({ email: 'admin@example.com', role: 'admin' }));
```

Chạy `npx tsc --noEmit`: **không in gì**. Chạy `node bai-10-typescript/06-any.ts`:

```bash
  return user.roel.toUpperCase();
                   ^

TypeError: Cannot read properties of undefined (reading 'toUpperCase')
```

`any` nghĩa là "kiểu gì cũng được". Mọi thứ đi qua biến kiểu `any` không được kiểm tra nữa, bạn quay về đúng tình trạng của JavaScript. Đổi `user: any` thành `user: { email: string; role: string }` rồi kiểm lại:

```bash
bai-10-typescript/06-any.ts(3,15): error TS2339: Property 'roel' does not exist on type '{ email: string; role: string; }'.
```

Bỏ hẳn phần kiểu, chỉ viết `getRole(user)`, chế độ `strict` cũng không cho qua: `error TS7006: Parameter 'user' implicitly has an 'any' type.` Sửa `roel` thành `role` để file sạch lỗi.

> ⚠️ Không dùng `any` để "cho hết đỏ": lỗi chỉ dời sang lúc chạy test. Khi thật sự chưa biết kiểu của dữ liệu, dùng `unknown`: TypeScript bắt bạn kiểm tra giá trị trước khi dùng.

## ✅ Phần 4: type và interface - đặt tên cho kiểu dữ liệu

### 🔆 1. type: đặt tên cho hình dạng của một Object

Viết lại `{ email: string; role: string }` ở mọi chỗ thì dài và dễ lệch nhau. Giống mẫu tờ khai có tên, in ra dùng nhiều lần, `type` đặt **tên** cho một kiểu. Mảng `users` 3 vai trò của bài Object và JSON giờ có kiểu `User[]`. Tạo file `bai-10-typescript/07-type-user.ts`:

```typescript
// Đặt tên User cho hình dạng của một tài khoản test
type User = {
  email: string;
  role: string;
  loginPath: string;
};

const users: User[] = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
  { email: 'projectmanager@example.com', role: 'project-manager', loginPath: '/admin/authentication' },
  { email: 'customer@example.com', role: 'customer', loginPath: '/authentication/login' },
];

// Dùng lại tên kiểu ở tham số của hàm
function describeUser(user: User): string {
  return `${user.role} -> ${user.email}`;
}

for (const user of users) {
  console.log(describeUser(user));
}

// find có thể không thấy: kiểu của customer là User | undefined
const customer = users.find((user) => user.role === 'customer');
console.log(customer?.loginPath ?? 'không có tài khoản customer');

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
users.push({ email: 'guest@example.com', role: 'guest' });
console.log(customer.loginPath);
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/07-type-user.ts(28,12): error TS2741: Property 'loginPath' is missing in type '{ email: string; role: string; }' but required in type 'User'.
bai-10-typescript/07-type-user.ts(29,13): error TS18048: 'customer' is possibly 'undefined'.
```

Lỗi đầu: tài khoản mới thiếu `loginPath`. Lỗi sau: `find` có thể không tìm thấy gì nên kiểu của `customer` là `User | undefined`, TypeScript không cho đọc thẳng `customer.loginPath`. Trước đây bạn phải tự nhớ thêm `?.`; giờ TypeScript nhắc. Xoá hai dòng lỗi rồi chạy `node bai-10-typescript/07-type-user.ts`:

```bash
admin -> admin@example.com
project-manager -> projectmanager@example.com
customer -> customer@example.com
/authentication/login
```

Tên kiểu viết **PascalCase** như tên class.

### 🔆 2. interface và thuộc tính readonly

`interface` làm cùng việc đó cho Object, không có dấu `=`. Tạo file `bai-10-typescript/08-interface.ts`:

```typescript
// interface cũng đặt tên cho hình dạng của một Object
interface LoginData {
  readonly email: string; // chỉ đọc: gán xong không được sửa
  password: string;
  rememberMe?: boolean;   // tuỳ chọn
}

const adminLogin: LoginData = {
  email: process.env.ADMIN_EMAIL ?? 'admin@example.com',
  password: process.env.ADMIN_PASSWORD ?? '',
};

function describeLogin(data: LoginData): string {
  const remember = data.rememberMe ? 'có' : 'không';
  return `Đăng nhập bằng ${data.email}, ghi nhớ: ${remember}`;
}

console.log(describeLogin(adminLogin));
console.log(describeLogin({ ...adminLogin, rememberMe: true }));

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
adminLogin.email = 'khac@example.com';
describeLogin({ email: 'customer@example.com' });
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/08-interface.ts(22,12): error TS2540: Cannot assign to 'email' because it is a read-only property.
bai-10-typescript/08-interface.ts(23,15): error TS2741: Property 'password' is missing in type '{ email: string; }' but required in type 'LoginData'.
```

`readonly` đánh dấu thuộc tính **chỉ đọc**: gán lúc tạo Object, sau đó không sửa được. Xoá hai dòng lỗi rồi chạy `node bai-10-typescript/08-interface.ts`:

```bash
Đăng nhập bằng admin@example.com, ghi nhớ: không
Đăng nhập bằng admin@example.com, ghi nhớ: có
```

> 🔒 `password` chỉ đọc từ `process.env.ADMIN_PASSWORD`: không ghi mật khẩu thật vào code, không in ra log.

### 🔆 3. Chọn type hay interface?

<table class="rt-table">
<thead>
<tr>
<th>Điểm so sánh</th>
<th>type</th>
<th>interface</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cú pháp</td>
<td><code><span>type</span> <span>User</span> <span>=</span> <span>{</span> <span>...</span> <span>};</span></code></td>
<td><code><span>interface</span> <span>User</span> <span>{</span> <span>...</span> <span>}</span></code></td>
</tr>
<tr>
<td>Đặt tên cho kiểu không phải Object</td>
<td>Được, ví dụ <code><span>type</span> <span>Role</span> <span>=</span> <span>'admin'</span> <span>|</span> <span>'customer';</span></code> (chỉ nhận một trong hai chuỗi này)</td>
<td>Không</td>
</tr>
<tr>
<td>Mở rộng kiểu có sẵn</td>
<td>Dùng dấu <code>&amp;</code></td>
<td>Dùng <code>extends</code>, giống class</td>
</tr>
</tbody>
</table>

Với Object, hai cách cho kết quả như nhau. Anh Tester khuyên **chọn một cách và dùng nhất quán**. Trong khoá học này: `interface` cho hình dạng của Object, `type` cho các trường hợp còn lại.

## ✅ Phần 5: class trong TypeScript

### 🔆 1. Kiểu cho thuộc tính, public, private và readonly

Cú pháp class giữ nguyên như bài Class. TypeScript thêm: thuộc tính phải **khai báo kèm kiểu**, và trước mỗi thuộc tính có thể đặt `public`, `private`, `readonly`. Tạo file `bai-10-typescript/09-class-co-kieu.ts`:

```typescript
class LoginPage {
  // Thuộc tính phải khai báo kèm kiểu trước khi dùng
  readonly path: string = '/admin/authentication'; // chỉ đọc
  public lastEmail: string = '';                   // public (mặc định): bên ngoài đọc, sửa được
  private attempts: number = 0;                    // private: chỉ dùng bên trong class

  login(email: string): void {
    this.attempts += 1;
    this.lastEmail = email;
    console.log(`Lần ${this.attempts}: đăng nhập ${email} tại ${this.path}`);
  }

  getAttempts(): number {
    return this.attempts;
  }
}

const loginPage = new LoginPage();
loginPage.login('admin@example.com');
loginPage.login('projectmanager@example.com');
console.log(loginPage.lastEmail, loginPage.getAttempts());

// ----- Dòng lỗi cố ý: xem lỗi xong thì xoá -----
loginPage.attempts = 99;
loginPage.path = '/authentication/login';
console.log(loginPage.getAttempts(), loginPage.path);
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/09-class-co-kieu.ts(24,11): error TS2341: Property 'attempts' is private and only accessible within class 'LoginPage'.
bai-10-typescript/09-class-co-kieu.ts(25,11): error TS2540: Cannot assign to 'path' because it is a read-only property.
```

<table class="rt-table">
<thead>
<tr>
<th>Từ khoá</th>
<th>Ý nghĩa</th>
<th>Dùng trong class trang</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>public</code></td>
<td>Bên ngoài đọc và sửa được. Là mặc định, thường không ghi</td>
<td>Method như <code>open()</code>, <code>login()</code></td>
</tr>
<tr>
<td><code>private</code></td>
<td>Chỉ dùng được bên trong class</td>
<td><code>page</code>, các giá trị nội bộ</td>
</tr>
<tr>
<td><code>protected</code></td>
<td>Như <code>private</code>, nhưng class con (<code>extends</code>) cũng dùng được</td>
<td><code>page</code> trong <code>BasePage</code></td>
</tr>
<tr>
<td><code>readonly</code></td>
<td>Gán một lần, sau đó chỉ đọc</td>
<td><code>page</code>, các locator</td>
</tr>
</tbody>
</table>

Lưu ý `private` của TypeScript chỉ được kiểm lúc viết code. Chạy file còn dòng lỗi bằng `node`, cả hai thuộc tính vẫn bị sửa:

```bash
Lần 1: đăng nhập admin@example.com tại /admin/authentication
Lần 2: đăng nhập projectmanager@example.com tại /admin/authentication
projectmanager@example.com 2
99 /authentication/login
```

Xoá các dòng lỗi trước khi sang mục sau.

### 🔆 2. Constructor viết gọn

Class trang nào cũng nhận `page` rồi cất vào thuộc tính. TypeScript có cách viết gọn cho việc đó (tên gốc: parameter properties). Tạo file `bai-10-typescript/10-constructor-gon.ts`:

```typescript
// Trang giả: chỉ cần đúng "hình dạng" mà class trang sẽ dùng
interface FakePage {
  goto(url: string): Promise<void>;
}

const fakePage: FakePage = {
  async goto(url) {
    console.log(`[fake] goto ${url}`);
  },
};

// Cách viết đầy đủ: khai báo thuộc tính, nhận tham số, gán
class LoginPageFull {
  private readonly page: FakePage;

  constructor(page: FakePage) {
    this.page = page;
  }

  async open(): Promise<void> {
    await this.page.goto('/admin/authentication');
  }
}

// Cách viết gọn: đặt private readonly ngay ở tham số, TypeScript tự khai báo và tự gán
class LoginPageShort {
  constructor(private readonly page: FakePage) {}

  async open(): Promise<void> {
    await this.page.goto('/admin/authentication');
  }
}

await new LoginPageFull(fakePage).open();
await new LoginPageShort(fakePage).open();
```

Đặt `private readonly` ngay trước tham số của constructor thì TypeScript **tự khai báo thuộc tính và tự gán**. `interface FakePage` mô tả trang giả: class chỉ cần biết `page` có method `goto`.

`npx tsc --noEmit` không báo lỗi. Nhưng chạy bằng `node`:

```bash
node bai-10-typescript/10-constructor-gon.ts
```

Kết quả:

```bash
class LoginPageShort {
  constructor(private readonly page: FakePage) {}
                               ^^^^^^^^^^^^^^

SyntaxError [ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX]: TypeScript parameter property is not supported in strip-only mode
```

Code không sai. Node.js mặc định chỉ **xoá** phần kiểu, còn cách viết gọn này cần được **đổi** thành code JavaScript (sinh thêm dòng `this.page = page`) nên Node.js từ chối. `enum` (kiểu liệt kê, bạn có thể gặp trong code AI) cũng bị từ chối vì lý do đó. Chạy được bằng cách thêm một cờ:

```bash
node --experimental-transform-types bai-10-typescript/10-constructor-gon.ts
```

Kết quả:

```bash
(node:26396) ExperimentalWarning: Transform Types is an experimental feature and might change at any time
(Use `node --trace-warnings ...` to show where the warning was created)
[fake] goto /admin/authentication
[fake] goto /admin/authentication
```

Dòng `ExperimentalWarning` báo cờ này còn thử nghiệm (con số sau `node:` mỗi lần chạy một khác). **Trong project Playwright không cần cờ nào**: Playwright tự chuyển TypeScript thành JavaScript, và constructor viết gọn rất hay gặp trong class trang.

### 🔆 3. Bẫy: field đọc this.page ngay tại chỗ khai báo

Bài Class đã cảnh báo về lỗi này. Tạo file `bai-10-typescript/11-bay-field.ts`:

```typescript
interface FakePage {
  getByRole(role: string, options: { name: string }): string;
}

const fakePage: FakePage = {
  getByRole: (role, options) => `locator ${role} "${options.name}"`,
};

class LoginPage {
  // Field đọc this.page ngay tại chỗ khai báo
  readonly loginButton = this.page.getByRole('button', { name: 'Login' });

  constructor(private readonly page: FakePage) {}
}

console.log(new LoginPage(fakePage).loginButton);
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/11-bay-field.ts(11,31): error TS2729: Property 'page' is used before its initialization.
```

Bỏ qua lỗi đó và chạy `node --experimental-transform-types bai-10-typescript/11-bay-field.ts`:

```bash
  readonly loginButton = this.page.getByRole('button', { name: 'Login' });
                                   ^

TypeError: Cannot read properties of undefined (reading 'getByRole')
```

Lý do nằm ở **thứ tự**: khi tạo object, các field chạy trước, phần gán `this.page = page` của constructor viết gọn chạy sau. Lúc đó `this.page` vẫn là `undefined`.

> ⚠️ Cách viết này có trong nhiều bài hướng dẫn cũ và code AI sinh ra. **Từ bản 1.65**, Playwright xử lý field của class giống `tsc` (theo option `useDefineForClassFields`) nên test dừng với đúng `TypeError` ở trên. Xem mục 1.65 trong [release notes của Playwright](https://playwright.dev/docs/release-notes).

Cách viết an toàn: **field chỉ khai báo kiểu, việc gán nằm trong constructor**. Sửa class trong file thành:

```typescript
class LoginPage {
  // Chỉ khai báo field kèm kiểu...
  readonly loginButton: string;

  constructor(private readonly page: FakePage) {
    // ...còn việc gán thì làm trong constructor, lúc này this.page đã có
    this.loginButton = this.page.getByRole('button', { name: 'Login' });
  }
}
```

`npx tsc --noEmit` sạch. Chạy lại lệnh ở trên, dưới hai dòng cảnh báo là:

```bash
locator button "Login"
```

## ✅ Phần 6: Thực hành - chuyển BasePage và LoginPage sang TypeScript

Viết lại class trang và hàm tiện ích của bài trước bằng TypeScript, vẫn chạy với trang giả. Khi `import` có hai điểm mới: đường dẫn ghi đuôi `.ts`, và thứ chỉ là kiểu thì dùng `import type`.

### 🔆 1. Kiểu dùng chung: types.ts

Tạo file `bai-10-typescript/types.ts`:

```typescript
// Trang giả: đúng các method mà class trang sẽ gọi, method nào cũng trả về Promise
export interface FakePage {
  goto(url: string): Promise<void>;
  fill(label: string, value: string): Promise<void>;
  click(name: string): Promise<void>;
  title(): Promise<string>;
}

// Một tài khoản test
export type User = {
  email: string;
  role: string;
  loginPath: string;
};

// Dữ liệu điền vào form đăng nhập
export interface LoginData {
  readonly email: string;
  password: string;
}
```

### 🔆 2. Hàm tiện ích: utils/url.ts và utils/fake-page.ts

Tạo file `bai-10-typescript/utils/url.ts`:

```typescript
export const BASE_URL: string = 'https://crm.anhtester.com';

export function buildUrl(path: string, baseUrl: string = BASE_URL): string {
  return `${baseUrl}${path}`;
}
```

Tạo file `bai-10-typescript/utils/fake-page.ts`:

```typescript
import type { FakePage } from '../types.ts';

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export function createFakePage(): FakePage {
  return {
    async goto(url) {
      await delay(100);
      console.log(`[fake] goto ${url}`);
    },
    async fill(label, value) {
      await delay(100);
      // Không in giá trị của ô Password ra log
      console.log(`[fake] fill "${label}" = ${label === 'Password' ? '***' : value}`);
    },
    async click(name) {
      await delay(100);
      console.log(`[fake] click "${name}"`);
    },
    async title() {
      await delay(100);
      return 'Perfex CRM | Anh Tester Demo - Login';
    },
  };
}
```

`createFakePage` khai báo trả về `FakePage`: viết thiếu một method là `tsc` báo ngay. Các tham số `url`, `label`, `value` không cần ghi kiểu vì TypeScript suy ra từ `interface FakePage`.

### 🔆 3. Class trang: pages/BasePage.ts và pages/LoginPage.ts

Tạo file `bai-10-typescript/pages/BasePage.ts`:

```typescript
import type { FakePage } from '../types.ts';
import { buildUrl } from '../utils/url.ts';

export default class BasePage {
  protected readonly page: FakePage;
  protected readonly path: string;

  constructor(page: FakePage, path: string) {
    this.page = page;
    this.path = path;
  }

  async open(): Promise<void> {
    await this.page.goto(buildUrl(this.path));
  }

  async getTitle(): Promise<string> {
    return this.page.title();
  }
}
```

Tạo file `bai-10-typescript/pages/LoginPage.ts`:

```typescript
import BasePage from './BasePage.ts';
import type { FakePage, LoginData } from '../types.ts';

export default class LoginPage extends BasePage {
  constructor(page: FakePage) {
    super(page, '/admin/authentication');
  }

  async login(data: LoginData): Promise<void> {
    await this.page.fill('Email Address', data.email);
    await this.page.fill('Password', data.password);
    await this.page.click('Login');
  }
}
```

So với bản JavaScript chỉ thêm phần kiểu: `protected readonly` cho thuộc tính (class con cần dùng `this.page` nên không dùng `private`), kiểu của tham số, kiểu trả về của method `async`. Constructor viết đầy đủ để chạy thẳng bằng `node`, không cần cờ.

### 🔆 4. File chạy: crm-login.ts

Tạo file `bai-10-typescript/crm-login.ts`:

```typescript
import LoginPage from './pages/LoginPage.ts';
import { createFakePage } from './utils/fake-page.ts';
import type { LoginData, User } from './types.ts';

const users: User[] = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
  { email: 'projectmanager@example.com', role: 'project-manager', loginPath: '/admin/authentication' },
  { email: 'customer@example.com', role: 'customer', loginPath: '/authentication/login' },
];

// find trả về User | undefined: phải xử lý trường hợp không thấy
const admin = users.find((user) => user.role === 'admin');
if (!admin) {
  throw new Error('Không có tài khoản admin trong data test');
}

const loginData: LoginData = {
  email: process.env.ADMIN_EMAIL ?? admin.email,
  password: process.env.ADMIN_PASSWORD ?? '',
};

const loginPage = new LoginPage(createFakePage());
await loginPage.open();

const title: string = await loginPage.getTitle();
console.log(`Tiêu đề: ${title}`);

await loginPage.login(loginData);
console.log('Xong');
```

```bash
npx tsc --noEmit
node bai-10-typescript/crm-login.ts
```

Kết quả (`tsc` không in gì):

```bash
[fake] goto https://crm.anhtester.com/admin/authentication
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
[fake] fill "Email Address" = admin@example.com
[fake] fill "Password" = ***
[fake] click "Login"
Xong
```

Đoạn `if (!admin) { throw ... }` là bắt buộc: loại trường hợp `undefined` xong, TypeScript mới cho đọc `admin.email`.

### 🔆 5. Cố ý gây hai lỗi kiểu

Trong `crm-login.ts`, sửa hai dòng của `loginData` thành:

```typescript
const loginData: LoginData = {
  email: process.env.ADMIN_EMAIL ?? admin.emial,
  password: 123456,
};
```

```bash
npx tsc --noEmit
```

Kết quả:

```bash
bai-10-typescript/crm-login.ts(18,43): error TS2551: Property 'emial' does not exist on type 'User'. Did you mean 'email'?
bai-10-typescript/crm-login.ts(19,3): error TS2322: Type 'number' is not assignable to type 'string'.
```

TypeScript còn gợi ý tên đúng. Nếu bỏ qua và chạy `node bai-10-typescript/crm-login.ts`, chương trình **không báo lỗi nào**:

```bash
[fake] goto https://crm.anhtester.com/admin/authentication
Tiêu đề: Perfex CRM | Anh Tester Demo - Login
[fake] fill "Email Address" = undefined
[fake] fill "Password" = ***
[fake] click "Login"
Xong
```

Ô email bị điền `undefined` mà vẫn in `Xong`. Sửa hai dòng về như cũ, chạy `npx tsc --noEmit` tới khi không còn lỗi.

### 🔆 6. Đặt cạnh class trang của Playwright thật

File dưới đây **chỉ để đọc**. Trong project Playwright, gói `@playwright/test` có sẵn hai kiểu `Page` và `Locator`:

```typescript
import type { Locator, Page } from '@playwright/test';

export class LoginPage {
  // Khai báo field kèm kiểu Locator, CHƯA gán
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;

  // Constructor viết gọn: page vừa là tham số, vừa là thuộc tính private readonly
  constructor(private readonly page: Page) {
    this.emailInput = page.getByLabel('Email Address');
    this.passwordInput = page.getByLabel('Password');
    this.loginButton = page.getByRole('button', { name: 'Login' });
  }

  async open(): Promise<void> {
    await this.page.goto('https://crm.anhtester.com/admin/authentication');
  }

  async login(email: string, password: string): Promise<void> {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
}
```

Mọi thứ trong file đều đã học: `import type`, field `readonly` chỉ khai báo kiểu, constructor viết gọn, gán locator trong constructor, method `async` trả về `Promise<void>`. Khi gọi `login`, mật khẩu chỉ lấy từ `process.env.ADMIN_PASSWORD`.

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức của bài

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills). Bản miễn phí [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/) vẫn dùng được các prompt dưới đây: chỗ có `@đường-dẫn` (cách đưa file vào câu hỏi của Claude Code, xem [tài liệu](https://code.claude.com/docs/en/common-workflows)) thì dán nội dung file vào thay. Không dán mật khẩu hay file `.env` vào khung chat.

```markdown
Chuyển file JavaScript @bai-05-object-json/crm-test-data.js sang TypeScript, lưu thành bai-10-typescript/crm-test-data.ts.
Yêu cầu:
- Đặt tên kiểu bằng interface cho từng Object (User, Config...), KHÔNG dùng any, as, @ts-ignore.
- Chỗ nào TypeScript tự suy luận được kiểu thì không ghi kiểu.
- Giữ nguyên logic và kết quả in ra.
Sau khi chuyển, giải thích TỪNG chú thích kiểu đã thêm: vì sao cần, nếu bỏ đi thì tsc báo gì.
Cuối cùng chạy npx tsc --noEmit và đưa tôi kết quả thật.
```

```markdown
Tôi mới học TypeScript. Lệnh npx tsc --noEmit báo hai lỗi sau:

bai-10-typescript/crm-login.ts(18,43): error TS2551: Property 'emial' does not exist on type 'User'. Did you mean 'email'?
bai-10-typescript/crm-login.ts(19,3): error TS2322: Type 'number' is not assignable to type 'string'.

Với từng lỗi: dịch thông báo sang tiếng Việt, giải thích các con số (18,43) và mã TSxxxx, nói nguyên nhân.
Chỉ gợi ý hướng sửa để tôi tự sửa. KHÔNG đề xuất any, as hay @ts-ignore.
```

```markdown
Rà toàn bộ file .ts trong thư mục @bai-10-typescript/ và lập bảng mọi chỗ dùng: any, ép kiểu as, // @ts-ignore, dấu ! sau tên biến.
Mỗi dòng của bảng gồm: file:dòng, đoạn code, rủi ro khi chạy, kiểu cụ thể nên thay vào.
Chỉ lập bảng, CHƯA sửa file. Tôi duyệt xong mới sửa.
```

```markdown
Giải thích cho người mới học sự khác nhau giữa hai class sau. Class thứ hai được TypeScript đổi thành code JavaScript như thế nào?
Vì sao node chạy thẳng class thứ nhất được, còn class thứ hai báo ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX? Dẫn link tài liệu nodejs.org.

class LoginPageFull {
  private readonly page: FakePage;
  constructor(page: FakePage) {
    this.page = page;
  }
}

class LoginPageShort {
  constructor(private readonly page: FakePage) {}
}
```

### 🔆 2. Bộ kit liên quan gì tới TypeScript?

<table class="rt-table">
<thead>
<tr>
<th>Chỗ trong bộ kit</th>
<th>Quy định</th>
<th>Liên hệ với bài này</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rule <a href="https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md">automation_rules.md</a>, mục 5</td>
<td>Class trang PascalCase kèm hậu tố <code>Page</code> (<code>LoginPage.ts</code>); file test <code>.spec.ts</code>; locator dạng <code><span>readonly</span> <span>loginButton</span></code></td>
<td>Đúng cách đặt tên file và field <code>readonly</code> ở Phần 6</td>
</tr>
<tr>
<td>Lệnh<br/><a href="https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/generate-automation-framework.md">/generate-automation-framework</a></td>
<td>Với Playwright + TypeScript, sinh kèm <code>tsconfig.json</code> có strict mode</td>
<td>Là option <code>strict</code> ở Phần 2</td>
</tr>
<tr>
<td>Mẫu locator trong cùng lệnh đó</td>
<td>Locator mẫu viết thành field đọc <code>this.page</code> tại chỗ khai báo</td>
<td>Đối chiếu với bẫy ở Phần 5; cần thì chuyển phần gán vào constructor</td>
</tr>
</tbody>
</table>

Lệnh [/review-automation-code](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/commands/review-automation-code.md) chấm chất lượng script nhưng **không kiểm tra kiểu**; việc đó là của `npx tsc --noEmit`. Các lệnh này dùng từ chương Playwright.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Code AI viết chạy được chưa chắc đã đúng kiểu. Rà theo bảng sau:

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
<td><code>any</code> ở tham số, biến, giá trị trả về</td>
<td>Tắt kiểm tra kiểu; lỗi dời sang lúc chạy</td>
<td>Thay bằng <code>interface</code>/<code>type</code> cụ thể; chưa biết kiểu thì <code>unknown</code></td>
</tr>
<tr>
<td><code>// @ts-ignore</code> phía trên một dòng</td>
<td>Che lỗi của dòng ngay dưới, lỗi vẫn còn nguyên</td>
<td>Xoá chú thích, đọc lỗi thật rồi sửa</td>
</tr>
<tr>
<td>Ép kiểu <code>{} as User</code>, <code>data as any</code></td>
<td><code>as</code> là lời cam đoan, TypeScript không kiểm lại: Object rỗng vẫn được coi là <code>User</code></td>
<td>Khai báo <code>const user: User = { ... }</code> để được kiểm đủ thuộc tính</td>
</tr>
<tr>
<td>Dấu <code>!</code> sau biến: <code>users.find(...)!</code></td>
<td>Cam đoan "không bao giờ <code>undefined</code>". Sai thì <code>TypeError</code> lúc chạy</td>
<td>Kiểm bằng <code>if</code> rồi <code>throw new Error</code> rõ nghĩa, hoặc dùng <code>?.</code></td>
</tr>
<tr>
<td>Field class đọc <code>this.page</code> tại chỗ khai báo, đi cùng constructor viết gọn</td>
<td><code>TS2729</code>; từ Playwright 1.65 là <code>TypeError</code> khi chạy test</td>
<td>Field chỉ khai báo kiểu, gán trong constructor</td>
</tr>
<tr>
<td><code>"strict": false</code> trong <code>tsconfig.json</code></td>
<td>Không còn báo <code>possibly 'undefined'</code>; tham số thiếu kiểu tự thành <code>any</code></td>
<td>Giữ <code>strict</code> là <code>true</code>, sửa lỗi thật</td>
</tr>
<tr>
<td>AI báo "đã chạy thành công" nhưng không chạy <code>tsc</code></td>
<td>Node.js và Playwright đều chạy mà không kiểm tra kiểu</td>
<td>Yêu cầu kết quả thật của <code>npx tsc --noEmit</code></td>
</tr>
<tr>
<td>Kiểu chung chung: <code>data: object</code>, <code>user: {}</code></td>
<td>Không đọc được thuộc tính nào, sau đó lại phải ép kiểu</td>
<td>Viết <code>interface</code> mô tả đúng hình dạng</td>
</tr>
</tbody>
</table>

## ✅ Phần 9: Bài tập thực hành

Đặt file bài tập trong thư mục `bai-10-typescript/`. Bài nào cũng phải sạch lỗi `npx tsc --noEmit` và không dùng `any`.

**Bài tập 1 - Thêm kiểu cho data test.** Tạo file `bt1-tai-khoan.ts`: khai báo `interface User` có `email`, `role`, `loginPath` và `isActive?`; tạo mảng 3 tài khoản của CRM; viết hàm `findByRole(role: string): User | undefined`; import `buildUrl` từ `utils/url.ts` để in URL đăng nhập của từng tài khoản. Với `findByRole('guest')`, in `không có tài khoản guest`.

**Bài tập 2 - Mở rộng LoginPage.** Thêm `rememberMe?: boolean` vào `interface LoginData`. Trong `LoginPage.login`, nếu `data.rememberMe` là `true` thì gọi thêm `this.page.click('Remember me')` trước khi bấm `Login`. Chạy `crm-login.ts` với cả hai trường hợp.

**Bài tập 3 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt3-duyet-code.ts`, chép vào:

```typescript
type User = { email: string; role: string; loginPath: string };

const users: any = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
];

function findUser(role: string): User {
  return users.find((user: any) => user.role === role)!;
}

// @ts-ignore
const timeout: number = '30000';
console.log(timeout + 1000);

const pmUser = {} as User;
console.log(pmUser.email.toUpperCase());

const customer = findUser('customer');
console.log(customer.loginPath);
```

`npx tsc --noEmit` không báo lỗi nào. Kết quả chạy thật bằng `node`:

```bash
300001000
console.log(pmUser.email.toUpperCase());
                         ^

TypeError: Cannot read properties of undefined (reading 'toUpperCase')
```

Có 4 chỗ AI đã tắt kiểm tra kiểu, mỗi chỗ ứng với một dòng của bảng ở Phần 8. Gỡ cả bốn, `tsc` báo 3 lỗi thật (`TS2322` hai lần, `TS2739` một lần). Sửa xong, file phải in lần lượt: `31000`, `PROJECTMANAGER@EXAMPLE.COM`, `không có tài khoản customer`.

## ✅ Phần 10: Ghi nhớ nhanh

- TypeScript = JavaScript + kiểu. Node.js và Playwright xoá kiểu rồi chạy, **không kiểm tra kiểu**.
- `npx tsc --noEmit` kiểm tra kiểu. Dòng lỗi đọc theo thứ tự: file, (dòng,cột), mã `TSxxxx`, nội dung.
- Biến có giá trị ban đầu thì để TypeScript tự suy luận; ghi kiểu cho tham số của hàm. `?` là tuỳ chọn, `|` đọc là "hoặc", `Promise<string>` là kết quả của hàm `async`.
- Không dùng `any`, `as`, `!`, `// @ts-ignore` để làm mất dấu đỏ.
- `type` và `interface` đặt tên cho kiểu; chọn một cách và dùng nhất quán.
- Class trang: `private readonly page`, field chỉ khai báo kiểu, gán trong constructor.

Chương JavaScript, TypeScript và Git kết thúc ở đây. Mỗi bài sẽ gặp lại trong code Playwright:

<table class="rt-table">
<thead>
<tr>
<th>Bài trong chương</th>
<th>Gặp lại trong code Playwright</th>
</tr>
</thead>
<tbody>
<tr>
<td>Biến, kiểu dữ liệu, toán tử</td>
<td><code>const loginButton = ...</code>, template literal, <code>===</code></td>
</tr>
<tr>
<td>Điều kiện</td>
<td>Chọn cấu hình theo <code>process.env</code></td>
</tr>
<tr>
<td>Vòng lặp và mảng</td>
<td>Chạy một test với nhiều bộ dữ liệu</td>
</tr>
<tr>
<td>Object và JSON</td>
<td><code>{ page }</code>, option <code>{ name: 'Login' }</code>, file data test, <code>playwright.config.ts</code></td>
</tr>
<tr>
<td>Hàm, arrow function, callback</td>
<td><code><span>test('...',</span> <span>async</span> <span>({</span> <span>page</span> <span>})</span> <span>=&gt;</span> <span>{</span> <span>...</span> <span>})</span></code></td>
</tr>
<tr>
<td>Git và GitHub</td>
<td>Lưu project test, chạy test tự động trên CI</td>
</tr>
<tr>
<td>Class, constructor, kế thừa</td>
<td>Page Object Model: <code>BasePage</code>, <code>LoginPage</code></td>
</tr>
<tr>
<td>async/await, import/export, try...catch</td>
<td><code>await</code> trước mọi thao tác với trang; <code><span>import</span> <span>{</span> <span>test,</span> <span>expect</span> <span>}</span> <span>from</span> <span>'@playwright/test'</span></code></td>
</tr>
<tr>
<td>TypeScript</td>
<td>File <code>.spec.ts</code>, kiểu <code>Page</code> và <code>Locator</code>, lệnh <code>npx tsc --noEmit</code></td>
</tr>
</tbody>
</table>

✅ **Kết luận:** Bạn đã có đủ nền ngôn ngữ để đọc, viết và duyệt code test. Bài kế tiếp, **Cài đặt Playwright TypeScript và chạy thử test mẫu**, thay trang giả bằng trình duyệt thật: bạn tạo project Playwright đầu tiên và chạy test mẫu.

---

## Bài tập riêng — TypeScript: type, interface, class và gỡ chỗ tắt kiểm tra kiểu

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-100](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-100)

**Mục tiêu:** khai báo kiểu cho data test và class trang, đọc hiểu lỗi của tsc và không lách kiểm tra kiểu bằng any hay @ts-ignore.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-10-typescript`

Bài nào cũng phải sạch lỗi `npx tsc --noEmit` và **không dùng** `any`.

### 📝 Đề bài

#### Bài tập 1 - Thêm kiểu cho data test

Tạo file `bt1-tai-khoan.ts`: khai báo `interface User` có `email`, `role`, `loginPath` và `isActive?`; tạo mảng 3 tài khoản của CRM; viết hàm `findByRole(role: string): User | undefined`; import `buildUrl` từ `utils/url.ts` để in URL đăng nhập của từng tài khoản. Với `findByRole('guest')`, in `không có tài khoản guest`.

#### Bài tập 2 - Mở rộng LoginPage

Thêm `rememberMe?: boolean` vào `interface LoginData`. Trong `LoginPage.login`, nếu `data.rememberMe` là `true` thì gọi thêm `this.page.click('Remember me')` trước khi bấm Login. Chạy `crm-login.ts` với cả hai trường hợp.

#### Bài tập 3 - Duyệt code AI

Tạo file `bt3-duyet-code.ts`, chép đoạn code AI viết dưới đây. `npx tsc --noEmit` không báo lỗi nào, nhưng chạy bằng node thì in `300001000` rồi dừng với TypeError. Có **4 chỗ AI đã tắt kiểm tra kiểu**, mỗi chỗ ứng với một dòng của bảng ở Phần 8. Gỡ cả bốn, tsc báo 3 lỗi thật (TS2322 hai lần, TS2739 một lần), rồi sửa cho hết lỗi.

```typescript
type User = { email: string; role: string; loginPath: string };
const users: any = [
  { email: 'admin@example.com', role: 'admin', loginPath: '/admin/authentication' },
];
function findUser(role: string): User {
  return users.find((user: any) => user.role === role)!;
}
// @ts-ignore
const timeout: number = '30000';
console.log(timeout + 1000);
const pmUser = {} as User;
console.log(pmUser.email.toUpperCase());
const customer = findUser('customer');
console.log(customer.loginPath);
```

### 📦 Cách nộp bài

1. Làm bài trong thư mục `bai-10-typescript/` của repo `js-ts-for-tester`, commit và push lên nhánh `main`.
2. Dán link thư mục bài trên GitHub vào ô **Link GitHub**, dạng `https://github.com/<ten-ban>/js-ts-for-tester/tree/main/bai-10-typescript`. Repo Private thì vào **Settings → Collaborators** thêm tài khoản GitHub của giảng viên, nếu không giảng viên không mở được.
3. Trong ô **Nội dung bài làm (Editor)**, dán **kết quả chạy thật** của từng file (mỗi file một **Đoạn code mẫu** chọn Text / Log) và phần trả lời các câu hỏi.
4. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*.
5. Trong Editor, dán thêm kết quả `npx tsc --noEmit` (không in gì là sạch lỗi) và, ở Bài tập 3, dán 3 lỗi tsc báo ra sau khi gỡ 4 chỗ tắt kiểm tra.

### ✅ Tiêu chí Đạt

- `npx tsc --noEmit` sạch lỗi cho cả thư mục; tìm `any`, `@ts-ignore`, `as User`, dấu `!` lách kiểu đều không còn.
- Bài tập 1 in 3 URL đăng nhập đúng và dòng `không có tài khoản guest`; kiểu trả về của `findByRole` là `User | undefined` và chỗ gọi có kiểm `undefined`.
- Bài tập 2: hai lần chạy cho thấy có/không có bước bấm `Remember me`; không sửa chỗ gọi cũ (thuộc tính mới là tuỳ chọn).
- Bài tập 3 sau khi sửa in lần lượt: `31000`, `PROJECTMANAGER@EXAMPLE.COM`, `không có tài khoản customer`; có ghi lại 3 lỗi TS2322, TS2322, TS2739 và cách sửa từng lỗi.
- Code đã có trên GitHub, nhánh main.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.