# Bài 3 - [Javascript Typescript] Câu lệnh điều kiện if...else và switch...case trong JavaScript

Chương: 1. JavaScript TypeScript for Tester + Git

Nguồn: [https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/401](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/401)

✅ Câu lệnh if, else if, else và thứ tự điều kiện  
✅ Toán tử 3 ngôi: chọn một trong hai giá trị  
✅ Truthy, falsy và bẫy chuỗi rỗng, số 0  
✅ Giá trị mặc định với || và ??  
✅ switch...case với break và default  
✅ Dùng AI để hỏi sâu kiến thức và kiểm tra code do AI sinh ra

## ⭐ Mục tiêu bài học

Ở bài trước, file `crm-login-data.js` đã tạo ra các biến `true`/`false` như `isTitleCorrect`, nhưng mới chỉ **in** chúng ra. Bài này dạy chương trình **rẽ nhánh**: đúng thì làm việc này, sai thì làm việc khác. Học xong bạn sẽ:

- Đọc và viết được `if`, `else if`, `else`, biết vì sao thứ tự điều kiện quan trọng.
- Dùng toán tử 3 ngôi cho trường hợp chọn một trong hai giá trị.
- Hiểu truthy, falsy và hai cái bẫy: chuỗi rỗng, số 0.
- Đặt giá trị mặc định bằng `||` và `??`, biết hai toán tử khác nhau ở đâu.
- Dùng `switch...case` với `break` và `default`.
- Soi được các lỗi rẽ nhánh AI hay mắc.

> 📌 Bài làm tiếp trong project `D:\AnhTester\js-ts-for-tester` (macOS: `~/AnhTester/js-ts-for-tester`). Kết quả trong bài là kết quả chạy thật trên Node.js v24.17.0.

## ✅ Phần 1: Câu lệnh if, else if và else

### 🔆 1. Chuẩn bị thư mục cho bài học

Tạo thư mục `bai-03-dieu-kien` cạnh thư mục của bài trước. Mỗi ví dụ là một file:

```bash
js-ts-for-tester/
├── package.json
├── bai-01-cai-dat/
├── bai-02-bien-kieu-du-lieu/
└── bai-03-dieu-kien/
    ├── 01-den-giao-thong.js
    ├── 02-kiem-tra-tieu-de.js
    ├── 03-ma-http.js
    ├── 04-thu-tu-dieu-kien.js
    ├── 05-toan-tu-3-ngoi.js
    ├── 06-truthy-falsy.js
    ├── 07-email-rong.js
    ├── 08-gia-tri-mac-dinh.js
    ├── 09-cau-hinh-test.js
    ├── 10-giam-gia-thanh-vien.js
    ├── 11-quen-break.js
    ├── 12-chon-url-theo-moi-truong.js
    ├── 13-ma-http-switch.js
    └── crm-login-check.js
```

### 🔆 2. Từ đèn giao thông tới if...else if...else

Tới ngã tư, bạn nhìn đèn rồi mới quyết định: **nếu** đèn xanh thì đi, đèn vàng thì đi chậm lại, đèn đỏ thì dừng, **còn lại** (đèn hỏng) thì quan sát. Câu lệnh điều kiện làm đúng việc đó. Tạo file `bai-03-dieu-kien/01-den-giao-thong.js`:

```javascript
const mauDen = 'vàng';

if (mauDen === 'xanh') {
  console.log('Được đi');
} else if (mauDen === 'vàng') {
  console.log('Đi chậm lại, chuẩn bị dừng');
} else if (mauDen === 'đỏ') {
  console.log('Dừng lại');
} else {
  console.log(`Đèn báo màu lạ (${mauDen}): quan sát kỹ rồi mới đi`);
}

console.log('Dòng này luôn chạy, dù đèn màu gì');
```

```bash
node bai-03-dieu-kien/01-den-giao-thong.js
```

Kết quả:

```bash
Đi chậm lại, chuẩn bị dừng
Dòng này luôn chạy, dù đèn màu gì
```

Điều kiện đặt trong ngoặc tròn, khối lệnh đặt trong ngoặc nhọn. `else if` thêm bao nhiêu nhánh cũng được. `else` chạy khi **không điều kiện nào** đúng; nên có để không sót trường hợp lạ.

JavaScript xét từ trên xuống, gặp điều kiện **đầu tiên** đúng thì chạy khối đó rồi **bỏ qua mọi nhánh còn lại**. Đổi `mauDen` thành `'tím'` để thấy nhánh `else` chạy.

### 🔆 3. Automation: đúng thì báo PASS, sai thì báo FAIL kèm lý do

Dùng lại tiêu đề trang đăng nhập Admin của CRM demo ở bài trước. Tạo file `bai-03-dieu-kien/02-kiem-tra-tieu-de.js`:

```javascript
const expectedTitle = 'Perfex CRM | Anh Tester Demo - Login';
const actualTitle = 'Perfex CRM | Anh Tester Demo - Login'; // giá trị lấy từ trang

const isTitleCorrect = actualTitle === expectedTitle;

if (isTitleCorrect) {
  console.log('PASS: tiêu đề trang đăng nhập đúng');
} else {
  console.log('FAIL: tiêu đề trang đăng nhập sai');
  console.log(`  Mong đợi: "${expectedTitle}"`);
  console.log(`  Thực tế : "${actualTitle}"`);
}
```

```bash
node bai-03-dieu-kien/02-kiem-tra-tieu-de.js
```

Kết quả:

```bash
PASS: tiêu đề trang đăng nhập đúng
```

Sửa `actualTitle` thành `'Perfex CRM | Anh Tester Demo - Dashboard'` rồi chạy lại:

```bash
FAIL: tiêu đề trang đăng nhập sai
  Mong đợi: "Perfex CRM | Anh Tester Demo - Login"
  Thực tế : "Perfex CRM | Anh Tester Demo - Dashboard"
```

Nhánh `else` in cả giá trị mong đợi lẫn thực tế, để người đọc log biết ngay sai ở đâu mà không phải chạy lại.

### 🔆 4. Nhiều nhánh và thứ tự điều kiện

Mỗi lần test gọi tới server, server trả về một **mã HTTP** cho biết yêu cầu thành công hay lỗi ở đâu. Tạo file `bai-03-dieu-kien/03-ma-http.js`:

```javascript
const status = 404; // mã HTTP mà server trả về

if (status === 200) {
  console.log('200: thành công');
} else if (status === 401) {
  console.log('401: chưa đăng nhập hoặc phiên đã hết hạn');
} else if (status === 403) {
  console.log('403: đã đăng nhập nhưng không có quyền');
} else if (status === 404) {
  console.log('404: không tìm thấy trang hoặc dữ liệu');
} else if (status >= 500) {
  console.log(`${status}: lỗi phía server, ghi lại để báo bug`);
} else {
  console.log(`${status}: mã chưa phân loại, cần xem thêm`);
}
```

```bash
node bai-03-dieu-kien/03-ma-http.js
```

Kết quả:

```bash
404: không tìm thấy trang hoặc dữ liệu
```

Lần lượt đổi `status` thành `200`, `401`, `503`, `302` rồi chạy lại:

```bash
200: thành công
401: chưa đăng nhập hoặc phiên đã hết hạn
503: lỗi phía server, ghi lại để báo bug
302: mã chưa phân loại, cần xem thêm
```

Điều kiện `status >= 500` gom cả 500, 502, 503 vào một nhánh. Khi điều kiện là **khoảng giá trị** như vậy, thứ tự viết quyết định kết quả. Tạo file `bai-03-dieu-kien/04-thu-tu-dieu-kien.js`:

```javascript
const responseTime = 3500; // thời gian phản hồi, tính bằng mili giây

// SAI: điều kiện rộng đứng trước, nhánh "rất chậm" không bao giờ chạy tới
if (responseTime > 1000) {
  console.log('Cách 1: chậm');
} else if (responseTime > 3000) {
  console.log('Cách 1: rất chậm, báo bug hiệu năng');
} else {
  console.log('Cách 1: đạt');
}

// ĐÚNG: điều kiện hẹp (khắt khe hơn) đứng trước
if (responseTime > 3000) {
  console.log('Cách 2: rất chậm, báo bug hiệu năng');
} else if (responseTime > 1000) {
  console.log('Cách 2: chậm');
} else {
  console.log('Cách 2: đạt');
}
```

```bash
node bai-03-dieu-kien/04-thu-tu-dieu-kien.js
```

Kết quả:

```bash
Cách 1: chậm
Cách 2: rất chậm, báo bug hiệu năng
```

Ở cách 1, điều kiện `> 1000` đúng trước nên nhánh `> 3000` không bao giờ được xét. Không có lỗi nào, chỉ có kết luận sai. Quy tắc: **điều kiện hẹp đứng trước, điều kiện rộng đứng sau**.

> ⚠️ Không lồng `if` trong `if` quá 2 tầng. Code lồng sâu khó đọc và khó biết nhánh nào chưa được test. Hãy ghép điều kiện bằng `&&` hoặc tách ra biến `boolean` như bài trước.

## ✅ Phần 2: Toán tử 3 ngôi

### 🔆 1. Chọn một trong hai giá trị trên một dòng

Quầy vé hỏi tuổi: đủ 18 thì bán vé người lớn, chưa đủ thì vé trẻ em. Khi chỉ có **hai lựa chọn** và kết quả là **một giá trị**, **toán tử 3 ngôi** (ternary) viết gọn hơn `if...else`: `điều kiện ? giá trị khi đúng : giá trị khi sai`. Tạo file `bai-03-dieu-kien/05-toan-tu-3-ngoi.js`:

```javascript
// Đời thường: đủ 18 tuổi thì mua vé người lớn, chưa đủ thì vé trẻ em
const tuoi = 20;

// Cách 1: if...else, phải dùng let và mất 6 dòng
let loaiVe;
if (tuoi >= 18) {
  loaiVe = 'vé người lớn';
} else {
  loaiVe = 'vé trẻ em';
}
console.log(loaiVe);

// Cách 2: toán tử 3 ngôi, 1 dòng và dùng được const
const loaiVeGon = tuoi >= 18 ? 'vé người lớn' : 'vé trẻ em';
console.log(loaiVeGon);

// Automation: đổi true/false thành chữ để ghi log
const isTitleCorrect = false;
const result = isTitleCorrect ? 'PASS' : 'FAIL';
console.log(`Kiểm tra tiêu đề: ${result}`);
```

```bash
node bai-03-dieu-kien/05-toan-tu-3-ngoi.js
```

Kết quả:

```bash
vé người lớn
vé người lớn
Kiểm tra tiêu đề: FAIL
```

Hai cách cho cùng kết quả, và cách 2 giữ được `const`.

### 🔆 2. Chỉ dùng một tầng

> ⚠️ **Không lồng toán tử 3 ngôi vào nhau**, kiểu `a ? b : c ? d : e`. Chạy được, nhưng người đọc phải dò từng dấu `?` và `:`. Từ 3 lựa chọn trở lên thì dùng `if...else if` hoặc `switch`.

## ✅ Phần 3: Truthy và falsy

### 🔆 1. Sáu giá trị falsy cần nhớ

Hỏi "ví còn tiền không?", ví trống hay ví có 0 đồng đều là "không". JavaScript cũng vậy: giá trị nào đặt vào `if` cũng được quy về đúng/sai. Nhóm bị coi là sai gọi là **falsy**, còn lại là **truthy**. Hàm `Boolean()` cho xem kết quả quy đổi. Tạo file `bai-03-dieu-kien/06-truthy-falsy.js`:

```javascript
// Nhóm falsy: đặt vào if thì bị coi là false
console.log('false     ->', Boolean(false));
console.log('0         ->', Boolean(0));
console.log("''        ->", Boolean(''));
console.log('null      ->', Boolean(null));
console.log('undefined ->', Boolean(undefined));
console.log('NaN       ->', Boolean(NaN));

// Trông giống "rỗng" hoặc "sai" nhưng lại là truthy
console.log("'0'       ->", Boolean('0'));
console.log("'false'   ->", Boolean('false'));
console.log("' '       ->", Boolean(' '));
console.log('-1        ->', Boolean(-1));
```

```bash
node bai-03-dieu-kien/06-truthy-falsy.js
```

Kết quả:

```bash
false     -> false
0         -> false
''        -> false
null      -> false
undefined -> false
NaN       -> false
'0'       -> true
'false'   -> true
' '       -> true
-1        -> true
```

- **Falsy**: `false`, `0`, `''` (chuỗi rỗng), `null`, `undefined`, `NaN`. Mọi giá trị khác là truthy.
- Chuỗi `'0'`, `'false'` và chuỗi chỉ có dấu cách đều là **truthy** vì là chuỗi có ký tự. Biến môi trường luôn là chuỗi, nên đặt `HEADLESS=false` rồi viết `if (process.env.HEADLESS)` thì điều kiện vẫn đúng.

### 🔆 2. Kiểm tra email rỗng và hai cái bẫy

`if (!adminEmail)` đọc là "nếu **không có** email". Cách viết gọn này có hai cái bẫy. Tạo file `bai-03-dieu-kien/07-email-rong.js`:

```javascript
// 1. Thiếu biến môi trường: undefined là falsy
const adminEmail = process.env.ADMIN_EMAIL;

if (!adminEmail) {
  console.log('DỪNG: chưa đặt biến môi trường ADMIN_EMAIL');
} else {
  console.log(`Đăng nhập bằng email: ${adminEmail}`);
}

// 2. Bẫy chuỗi: ô Email chỉ có 3 dấu cách vẫn là truthy
const emailInput = '   ';

if (emailInput) {
  console.log('Chưa trim: ô Email bị coi là ĐÃ nhập');
}
if (!emailInput.trim()) {
  console.log('Đã trim  : ô Email đang rỗng');
}

// 3. Bẫy số 0: giảm giá 0 đồng là giá trị hợp lệ, nhưng 0 là falsy
const discount = 0;

if (!discount) {
  console.log('Viết !discount             : báo "chưa nhập giảm giá" (SAI)');
}
if (discount === undefined) {
  console.log('Chưa nhập giảm giá');
} else {
  console.log(`Viết discount === undefined: giảm giá là ${discount} (ĐÚNG)`);
}
```

```bash
node bai-03-dieu-kien/07-email-rong.js
```

Kết quả khi máy chưa đặt `ADMIN_EMAIL`:

```bash
DỪNG: chưa đặt biến môi trường ADMIN_EMAIL
Chưa trim: ô Email bị coi là ĐÃ nhập
Đã trim  : ô Email đang rỗng
Viết !discount             : báo "chưa nhập giảm giá" (SAI)
Viết discount === undefined: giảm giá là 0 (ĐÚNG)
```

- **Phần 1**: thiếu biến môi trường thì báo rõ, thay vì để test gõ chữ "undefined" vào ô Email. Đặt biến rồi chạy lại, dòng đầu là `Đăng nhập bằng email: admin@example.com`.
- **Bẫy chuỗi**: chuỗi 3 dấu cách là truthy, nên phải `trim()` trước khi kiểm tra rỗng.
- **Bẫy số 0**: `!discount` coi "giảm giá 0 đồng" như "chưa nhập". Khi `0` là giá trị hợp lệ, so sánh thẳng với `undefined`.

## ✅ Phần 4: Giá trị mặc định với || và ??

### 🔆 1. Có ghi thì dùng, không ghi thì lấy mặc định

Phiếu giao hàng có ô phí ship: có ghi thì thu theo số đã ghi, bỏ trống thì thu mặc định 30.000. Đơn **miễn phí ship** thì phiếu ghi rõ số `0`. Tạo file `bai-03-dieu-kien/08-gia-tri-mac-dinh.js`:

```javascript
// Phí ship: phiếu có ghi thì dùng số đã ghi, không ghi thì mặc định 30.000
const phiShipDonA = undefined; // phiếu không ghi phí ship
const phiShipDonB = 0;         // phiếu ghi rõ 0: đơn được miễn phí ship

console.log(phiShipDonA || 30000);
console.log(phiShipDonB || 30000);

console.log(phiShipDonA ?? 30000);
console.log(phiShipDonB ?? 30000);

// Ghi chú đơn hàng: khách cố ý để trống
const ghiChu = '';
console.log(`[${ghiChu || 'Không có ghi chú'}]`);
console.log(`[${ghiChu ?? 'Không có ghi chú'}]`);
```

```bash
node bai-03-dieu-kien/08-gia-tri-mac-dinh.js
```

Kết quả:

```bash
30000
30000
30000
0
[Không có ghi chú]
[]
```

<table class="rt-table">
<thead>
<tr>
<th>Giá trị của <code>a</code></th>
<th><code>a || mặc định</code></th>
<th><code>a ?? mặc định</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>undefined</code></td>
<td>Lấy mặc định</td>
<td>Lấy mặc định</td>
</tr>
<tr>
<td><code>0</code></td>
<td>⚠️ Lấy mặc định</td>
<td>Giữ <code>0</code></td>
</tr>
<tr>
<td><code>''</code></td>
<td>⚠️ Lấy mặc định</td>
<td>Giữ <code>''</code></td>
</tr>
</tbody>
</table>

- `a || b`: lấy `b` khi `a` là **falsy**, nên đơn miễn phí ship vẫn bị thu 30.000.
- `a ?? b`: chỉ lấy `b` khi `a` là `null` hoặc `undefined`, tức **thật sự không có giá trị**.

### 🔆 2. Automation: URL và cấu hình mặc định

Tạo file `bai-03-dieu-kien/09-cau-hinh-test.js`:

```javascript
// Có đặt BASE_URL thì dùng, không thì chạy trên CRM demo
const baseUrl = process.env.BASE_URL ?? 'https://crm.anhtester.com';
console.log(`Môi trường test: ${baseUrl}`);

// Cấu hình của nhóm: 0 nghĩa là KHÔNG chạy lại test lỗi
const configRetries = 0;

const retriesWrong = configRetries || 2;
const retriesRight = configRetries ?? 2;

console.log(`Dùng || : chạy lại ${retriesWrong} lần`);
console.log(`Dùng ?? : chạy lại ${retriesRight} lần`);
```

```bash
node bai-03-dieu-kien/09-cau-hinh-test.js
```

Kết quả:

```bash
Môi trường test: https://crm.anhtester.com
Dùng || : chạy lại 2 lần
Dùng ?? : chạy lại 0 lần
```

Nhóm cấu hình `0` lần chạy lại, vậy mà `||` âm thầm đổi thành 2. **Quy tắc của khoá học: đặt giá trị mặc định bằng `??`**, chỉ dùng `||` khi bạn chủ ý muốn thay cả `0` và chuỗi rỗng. Đặt biến `BASE_URL` rồi chạy lại thì URL đổi theo mà không phải sửa code:

```bash
# Windows PowerShell
$env:BASE_URL = 'https://staging.crm.example.com'
node bai-03-dieu-kien/09-cau-hinh-test.js

# macOS / Linux / Git Bash
BASE_URL=https://staging.crm.example.com node bai-03-dieu-kien/09-cau-hinh-test.js
```

Dòng đầu của kết quả (thử xong, mở Terminal mới để xoá biến vừa đặt):

```bash
Môi trường test: https://staging.crm.example.com
```

## ✅ Phần 5: Câu lệnh switch...case

### 🔆 1. Giảm giá theo hạng thành viên

Cửa hàng giảm giá theo hạng thẻ: kim cương 20%, vàng 10%, bạc 5%, còn lại không giảm. Đây là dạng **một biến so với một danh sách giá trị cố định**, hợp với `switch`. Tạo file `bai-03-dieu-kien/10-giam-gia-thanh-vien.js`:

```javascript
const hangThanhVien = 'vàng';
const giaGoc = 500000;
let phanTramGiam;

switch (hangThanhVien) {
  case 'kim cương':
    phanTramGiam = 20;
    break;
  case 'vàng':
    phanTramGiam = 10;
    break;
  case 'bạc':
    phanTramGiam = 5;
    break;
  default:
    phanTramGiam = 0;
}

const phaiTra = giaGoc * (100 - phanTramGiam) / 100;
console.log(`Hạng ${hangThanhVien}: giảm ${phanTramGiam}%, phải trả ${phaiTra}`);
```

```bash
node bai-03-dieu-kien/10-giam-gia-thanh-vien.js
```

Kết quả:

```bash
Hạng vàng: giảm 10%, phải trả 450000
```

- `switch (biến)` so biến với từng `case` bằng `===`, khớp `case` nào thì chạy từ đó tới khi gặp `break`.
- `default` chạy khi không `case` nào khớp, giống `else`. **Luôn viết `default`** để giá trị lạ không bị bỏ qua trong im lặng.

### 🔆 2. Quên break: lỗi số một của switch

Tạo file `bai-03-dieu-kien/11-quen-break.js`, giống file trên nhưng bỏ hết `break`:

```javascript
const hangThanhVien = 'vàng';
let phanTramGiam;

switch (hangThanhVien) {
  case 'kim cương':
    phanTramGiam = 20;
  case 'vàng':
    phanTramGiam = 10;
    console.log('Vào case vàng');
  case 'bạc':
    phanTramGiam = 5;
    console.log('Chạy tiếp sang case bạc');
  default:
    phanTramGiam = 0;
    console.log('Chạy tiếp sang default');
}

console.log(`Hạng ${hangThanhVien}: giảm ${phanTramGiam}%`);
```

```bash
node bai-03-dieu-kien/11-quen-break.js
```

Kết quả:

```bash
Vào case vàng
Chạy tiếp sang case bạc
Chạy tiếp sang default
Hạng vàng: giảm 0%
```

Khớp `case 'vàng'` xong, không có `break` nên JavaScript **chạy tiếp xuống các `case` bên dưới mà không so sánh nữa**. Khách hạng vàng bị tính giảm 0% mà không có thông báo lỗi nào.

### 🔆 3. Automation: chọn URL theo môi trường

Một bộ test thường chạy trên nhiều môi trường: `dev`, `staging`, `prod`. Tên môi trường truyền qua biến `ENV`, code chọn URL tương ứng. CRM demo chỉ có một địa chỉ thật, nên `dev` và `staging` dưới đây là địa chỉ ví dụ. Tạo file `bai-03-dieu-kien/12-chon-url-theo-moi-truong.js`:

```javascript
// Không đặt ENV thì chạy trên CRM demo (prod)
const env = (process.env.ENV ?? 'prod').trim().toLowerCase();
const loginPath = '/admin/authentication';
let baseUrl;

switch (env) {
  case 'dev':
    baseUrl = 'https://dev.crm.example.com';
    break;
  case 'staging':
    baseUrl = 'https://staging.crm.example.com';
    break;
  case 'prod':
    baseUrl = 'https://crm.anhtester.com';
    break;
  default:
    console.log(`ENV="${env}" không hợp lệ. Chỉ nhận: dev | staging | prod`);
}

if (baseUrl) {
  console.log(`[${env}] Mở trang: ${baseUrl}${loginPath}`);
} else {
  console.log('DỪNG: không xác định được môi trường test');
}
```

```bash
# Windows PowerShell
node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js
$env:ENV = 'staging'; node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js
$env:ENV = 'uat'; node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js

# macOS / Linux / Git Bash
node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js
ENV=staging node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js
ENV=uat node bai-03-dieu-kien/12-chon-url-theo-moi-truong.js
```

Kết quả của ba lần chạy:

```bash
[prod] Mở trang: https://crm.anhtester.com/admin/authentication
[staging] Mở trang: https://staging.crm.example.com/admin/authentication
ENV="uat" không hợp lệ. Chỉ nhận: dev | staging | prod
DỪNG: không xác định được môi trường test
```

File này dùng lại gần hết bài: `??` đặt môi trường mặc định, `toLowerCase()` để gõ `Staging` vẫn nhận, `default` báo giá trị lạ, và `if (baseUrl)` dựa vào việc `undefined` là falsy.

### 🔆 4. Gộp nhiều case

Nhiều giá trị cùng một cách xử lý thì viết các `case` liền nhau; chỉ trường hợp này mới được bỏ `break`. Tạo file `bai-03-dieu-kien/13-ma-http-switch.js`:

```javascript
const status = 403;

switch (status) {
  case 200:
  case 201:
    console.log(`${status}: thành công`);
    break;
  case 401:
  case 403:
    console.log(`${status}: lỗi đăng nhập hoặc phân quyền`);
    break;
  case 404:
    console.log('404: không tìm thấy');
    break;
  case 500:
    console.log('500: lỗi phía server');
    break;
  default:
    console.log(`${status}: mã chưa phân loại`);
}

// switch so sánh bằng ===: chuỗi '200' không khớp với số 200
const statusText = '200';

switch (statusText) {
  case 200:
    console.log('Khớp case 200');
    break;
  default:
    console.log(`'${statusText}' là chuỗi nên rơi vào default`);
}
```

```bash
node bai-03-dieu-kien/13-ma-http-switch.js
```

Kết quả:

```bash
403: lỗi đăng nhập hoặc phân quyền
'200' là chuỗi nên rơi vào default
```

Dòng thứ hai: `switch` so sánh bằng `===`, nên giá trị dạng chuỗi phải `Number()` trước khi đưa vào `switch` có `case` là số. Còn điều kiện là **khoảng giá trị** như `status >= 500` thì không hợp với `case`: dùng `if...else if`.

## ✅ Phần 6: Thực hành - kiểm tra trang đăng nhập CRM có rẽ nhánh

Nâng cấp file `crm-login-data.js` của bài trước: chọn môi trường theo `ENV`, cho phép ghi đè bằng `BASE_URL`, rồi in `PASS` hoặc `FAIL` kèm lý do cho từng kiểm tra. Giá trị thực tế vẫn chép sẵn vào code; tới chương Playwright chúng sẽ do Playwright lấy về.

Tạo file `bai-03-dieu-kien/crm-login-check.js`:

```javascript
// ===== 1. Chọn môi trường bằng switch =====
const env = (process.env.ENV ?? 'prod').trim().toLowerCase();
let defaultBaseUrl;

switch (env) {
  case 'dev':
    defaultBaseUrl = 'https://dev.crm.example.com';
    break;
  case 'staging':
    defaultBaseUrl = 'https://staging.crm.example.com';
    break;
  default:
    defaultBaseUrl = 'https://crm.anhtester.com';
}

// ===== 2. Giá trị mặc định bằng ?? =====
const baseUrl = process.env.BASE_URL ?? defaultBaseUrl;
const loginUrl = `${baseUrl}/admin/authentication`;
const adminEmail = process.env.ADMIN_EMAIL;

// ===== 3. Giá trị thực tế (chép từ trang đăng nhập Admin, như bài trước) =====
const expectedTitle = 'Perfex CRM | Anh Tester Demo - Login';
const actualTitle = 'Perfex CRM | Anh Tester Demo - Login';
const rawHeading = '\n            Login        ';
const status = 200;

console.log(`[${env}] URL cần mở: ${loginUrl}`);

// ===== 4. Rẽ nhánh theo từng kết quả =====
if (!adminEmail) {
  console.log('SKIP: chưa đặt ADMIN_EMAIL nên chưa thể đăng nhập');
} else {
  console.log(`INFO: sẽ đăng nhập bằng ${adminEmail}`);
}

if (status === 200) {
  console.log('PASS: trang phản hồi mã 200');
} else if (status === 404) {
  console.log('FAIL: sai đường dẫn (404)');
} else if (status >= 500) {
  console.log(`FAIL: server lỗi (${status})`);
} else {
  console.log(`FAIL: mã không mong đợi (${status})`);
}

const isTitleCorrect = actualTitle === expectedTitle;
const isHeadingCorrect = rawHeading.trim() === 'Login';

if (isTitleCorrect) {
  console.log('PASS: tiêu đề tab đúng');
} else {
  console.log(`FAIL: tiêu đề tab sai. Mong đợi "${expectedTitle}", thực tế "${actualTitle}"`);
}

console.log(`${isHeadingCorrect ? 'PASS' : 'FAIL'}: tiêu đề trên trang`);

// ===== 5. Kết luận =====
const isAllPassed = status === 200 && isTitleCorrect && isHeadingCorrect;
console.log(`KẾT LUẬN: ${isAllPassed ? 'PASS' : 'FAIL'}`);
```

```bash
node bai-03-dieu-kien/crm-login-check.js
```

Kết quả khi chưa đặt biến môi trường nào:

```bash
[prod] URL cần mở: https://crm.anhtester.com/admin/authentication
SKIP: chưa đặt ADMIN_EMAIL nên chưa thể đăng nhập
PASS: trang phản hồi mã 200
PASS: tiêu đề tab đúng
PASS: tiêu đề trên trang
KẾT LUẬN: PASS
```

Kết quả khi đặt `ENV` là `staging` và `ADMIN_EMAIL` là `admin@example.com`:

```bash
[staging] URL cần mở: https://staging.crm.example.com/admin/authentication
INFO: sẽ đăng nhập bằng admin@example.com
PASS: trang phản hồi mã 200
PASS: tiêu đề tab đúng
PASS: tiêu đề trên trang
KẾT LUẬN: PASS
```

Thử đổi `status` thành `503` hoặc sửa một chữ trong `actualTitle` để xem dòng nào chuyển sang `FAIL`. Lưu ý: file này dùng `default` làm nhánh `prod`, nên gõ nhầm `ENV` sẽ chạy thẳng lên `prod`. Bài tập 2 xử lý điểm này.

## ✅ Phần 7: Dùng Claude Code và bộ kit claude-testing-skills để học và hỏi sâu

### 🔆 1. Prompt hỏi sâu kiến thức

Anh Tester dùng [Claude](https://claude.ai/) và Claude Code (bản có phí) cùng bộ kit [claude-testing-skills](https://github.com/anhtester/claude-testing-skills); bản miễn phí thì chọn [ChatGPT](https://chatgpt.com/) hoặc [Gemini](https://gemini.google.com/). Prompt dưới đây dùng được cho cả ba. Trong Claude Code, `@đường-dẫn` đưa file vào câu hỏi ([tài liệu](https://code.claude.com/docs/en/common-workflows)); với ChatGPT và Gemini, bạn dán nội dung file vào thay cho `@...`.

```markdown
Tôi là tester mới học JavaScript. Giải thích truthy và falsy bằng chính các biến sau của tôi:
const adminEmail = process.env.ADMIN_EMAIL;  const emailInput = '   ';
const discount = 0;  const headless = 'false';  const errorMessage = null;
Với mỗi biến: if (biến) chạy nhánh nào, vì sao, và nên viết điều kiện thế nào cho đúng ý.
Trình bày dạng bảng. Cuối cùng cho 5 giá trị khác để tôi tự đoán, đáp án để ở cuối.
```

```markdown
Trong file @bai-03-dieu-kien/09-cau-hinh-test.js, vì sao configRetries || 2 ra 2 còn configRetries ?? 2 ra 0?
Nêu 3 tình huống trong automation test mà dùng || để đặt giá trị mặc định gây sai (timeout, retries, số lượng, chuỗi rỗng...).
Mỗi tình huống kèm code tối đa 5 dòng chạy được bằng node và kết quả in ra.
```

```markdown
Khi nào nên dùng if...else if, khi nào nên dùng switch...case trong JavaScript?
Lấy ví dụ: phân loại mã HTTP 200/401/403/404/500 và phân loại thời gian phản hồi theo khoảng.
Ví dụ nào không nên viết bằng switch, vì sao?
```

### 🔆 2. Prompt nhờ chuyển đổi và tìm bug

```markdown
Chuyển chuỗi if...else if trong file @bai-03-dieu-kien/03-ma-http.js sang switch...case.
Yêu cầu: mỗi case có break, có default, gộp 401 và 403 vào một nhánh.
Nhánh status >= 500 có viết được bằng case không? Nếu không thì giải thích và đề xuất cách xử lý.
Ghi kết quả ra file mới bai-03-dieu-kien/03-ma-http-switch-ai.js, KHÔNG sửa file gốc, rồi chạy cả hai file để so kết quả.
```

```markdown
Đoạn code sau phải giữ nguyên giá trị 0 khi người dùng cấu hình 0, nhưng luôn in ra 30000. Tìm bug và giải thích:

const configTimeout = 0;
const timeout = configTimeout || 30000;
console.log(timeout);

Chỉ ra đúng dòng sai, nêu cách sửa, và nói rõ sau khi sửa thì các giá trị 0, '', null, undefined cho kết quả gì.
```

```markdown
Rà file @bai-03-dieu-kien/crm-login-check.js theo các tiêu chí:
1. Có if lồng quá 2 tầng hoặc toán tử 3 ngôi lồng nhau không?
2. switch có đủ break và default không?
3. Có chỗ nào dùng ==, hoặc dùng || cho giá trị có thể là 0 hay chuỗi rỗng không?
4. Có điều kiện nào viết nhầm dấu = thay cho === không?
Chỉ báo cáo theo từng dòng, KHÔNG sửa file.
```

### 🔆 3. Bộ kit nói gì về rẽ nhánh?

Khi thư mục `.claude` của bộ kit nằm trong project, Claude Code nạp các file trong `.claude/rules/` ở đầu mỗi phiên ([tài liệu](https://code.claude.com/docs/en/memory)). File [automation\_rules.md](https://github.com/anhtester/claude-testing-skills/blob/main/.claude/rules/automation_rules.md), mục 3 "Chất lượng code", yêu cầu code **đơn giản, dễ đọc, dễ bảo trì**. Kit **không có** quy định riêng về `if`, `switch`, `??`: phần đó bạn tự kiểm bằng bảng ở Phần 8. Lệnh `/review-automation-code` của kit làm việc trên code Playwright, sẽ dùng từ chương Playwright.

## ✅ Phần 8: Kiểm tra code do AI sinh ra

Lỗi rẽ nhánh hiếm khi làm chương trình dừng: code vẫn chạy, chỉ đi **nhầm nhánh**. Mỗi lần nhận code, rà theo bảng:

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
<td><code>if (status = 200)</code></td>
<td>Một dấu <code>=</code> là <strong>gán</strong>: <code>status</code> bị đổi thành 200, điều kiện luôn đúng</td>
<td>Đổi thành <code>===</code></td>
</tr>
<tr>
<td><code>==</code>, <code>!=</code> trong điều kiện</td>
<td>Tự đổi kiểu: <code>'0' == 0</code> ra <code>true</code>, sai kiểu dữ liệu vẫn lọt</td>
<td>Dùng <code>===</code>, <code>!==</code>; cần thì <code>Number()</code> trước</td>
</tr>
<tr>
<td><code>if</code> lồng 3 tầng trở lên, toán tử 3 ngôi lồng nhau</td>
<td>Khó đọc, khó biết nhánh nào chưa được kiểm</td>
<td>Viết lại bằng <code>if...else if</code> phẳng hoặc <code>switch</code></td>
</tr>
<tr>
<td><code>case</code> có lệnh nhưng thiếu <code>break</code></td>
<td>Chạy tiếp xuống các <code>case</code> dưới, giá trị bị ghi đè</td>
<td>Thêm <code>break</code> cho từng <code>case</code></td>
</tr>
<tr>
<td><code>switch</code> không có <code>default</code>, chuỗi <code>else if</code> không có <code>else</code></td>
<td>Giá trị lạ bị bỏ qua trong im lặng</td>
<td>Thêm nhánh cuối báo giá trị không hợp lệ</td>
</tr>
<tr>
<td><code>timeout || 30000</code>, <code>retries || 2</code></td>
<td>Giá trị <code>0</code> và <code>''</code> hợp lệ bị thay bằng mặc định</td>
<td>Đổi sang <code>??</code></td>
</tr>
<tr>
<td><code>if (count)</code>, <code>if (!text)</code> với số hoặc chuỗi chưa <code>trim()</code></td>
<td><code>0</code> là falsy; chuỗi toàn dấu cách là truthy</td>
<td>So sánh rõ ràng: <code>count &gt; 0</code>, <code>text.trim() === ''</code></td>
</tr>
<tr>
<td>Điều kiện rộng đứng trước điều kiện hẹp</td>
<td>Nhánh phía sau không bao giờ chạy tới</td>
<td>Đảo lại: hẹp trước, rộng sau</td>
</tr>
</tbody>
</table>

Đọc xong thì **chạy thật với nhiều giá trị đầu vào**: mỗi nhánh một giá trị, thêm một giá trị lạ cho `else` hoặc `default`.

## ✅ Phần 9: Bài tập thực hành

Đặt các file bài tập trong thư mục `bai-03-dieu-kien/`.

**Bài tập 1 - Kiểm tra tiêu đề trang quên mật khẩu.** Tạo file `bt1-forgot-password.js`. Chuỗi thô lấy từ tiêu đề trang quên mật khẩu của CRM demo là `'\n Forgot Password '`. Làm sạch chuỗi, so với `'Forgot Password'` bằng `if...else`: đúng in `PASS`, sai in `FAIL` kèm giá trị mong đợi và thực tế. Viết thêm một dòng chọn chữ `PASS`/`FAIL` bằng toán tử 3 ngôi. Bỏ thử `trim()` để thấy nhánh `FAIL`.

**Bài tập 2 - Cấu hình theo môi trường.** Tạo file `bt2-cau-hinh.js`. Đọc `ENV` (mặc định `dev`), dùng `switch` chọn `timeout`: `dev` là 60000, `staging` là 30000, `prod` là 15000; giá trị khác thì báo không hợp lệ và **không** rơi vào `prod`. Khai báo `const configRetries = 0;` và đặt `retries` mặc định là 2 sao cho giá trị `0` được giữ nguyên. Chạy với `ENV=staging` phải in ra:

```bash
[staging] timeout=30000, retries=0
```

**Bài tập 3 - Duyệt code AI.** Đoạn code dưới đây do AI viết. Tạo file `bt3-duyet-code.js`, chép vào và chạy.

```javascript
let status = 404;
const retries = 0;
const env = 'staging';
const errorCount = '0';
const actualTitle = 'Perfex CRM | Anh Tester Demo - Login';

if (status = 200) {
  console.log('Trang phản hồi thành công');
}

const retryCount = retries || 3;
console.log(`Số lần chạy lại: ${retryCount}`);

let baseUrl;
switch (env) {
  case 'dev':
    baseUrl = 'https://dev.crm.example.com';
  case 'staging':
    baseUrl = 'https://staging.crm.example.com';
  case 'prod':
    baseUrl = 'https://crm.anhtester.com';
}
console.log(`Mở trang: ${baseUrl}`);

const result = errorCount == 0 ? (actualTitle.includes('Login') ? 'PASS' : 'FAIL-TITLE') : 'FAIL-ERROR';
console.log(result);
```

Kết quả chạy thật:

```bash
Trang phản hồi thành công
Số lần chạy lại: 3
Mở trang: https://crm.anhtester.com
PASS
```

Không có lỗi nào, nhưng 3 trong 4 dòng sai: mã 404 được báo "thành công", cấu hình 0 lần chạy lại thành 3, môi trường `staging` lại mở trang `prod`. Tìm đủ **5 chỗ cần sửa** theo bảng ở Phần 8 (dòng cuối ra `PASS` đúng nhưng vẫn có 2 chỗ phải viết lại). Sau khi sửa, file phải in ra:

```bash
Trang phản hồi mã 404
Số lần chạy lại: 0
Mở trang: https://staging.crm.example.com
PASS
```

## ✅ Phần 10: Ghi nhớ nhanh

- `if` xét từ trên xuống và chỉ chạy **nhánh đầu tiên** đúng. Điều kiện hẹp viết trước, điều kiện rộng viết sau, kết thúc bằng `else`.
- Toán tử 3 ngôi chỉ để chọn một trong hai giá trị, **không lồng**. `if` không lồng quá 2 tầng.
- Falsy: `false`, `0`, `''`, `null`, `undefined`, `NaN`. Chuỗi `'0'`, `'false'`, `' '` là truthy.
- Giá trị mặc định dùng `??`. `||` thay luôn cả `0` và chuỗi rỗng.
- `switch` cho một biến với danh sách giá trị cố định: mỗi `case` một `break`, luôn có `default`, so sánh bằng `===`.
- Trong điều kiện, một dấu `=` là gán; so sánh luôn là `===`. Code AI viết phải chạy thử mỗi nhánh ít nhất một lần.

✅ **Kết luận:** Chương trình đã biết rẽ nhánh, nhưng mỗi lần chạy mới kiểm được **một** giá trị: muốn thử mã 200, 404, 503 bạn phải sửa code ba lần. Bài kế tiếp, **Vòng lặp và mảng (Array) trong JavaScript**, gom nhiều giá trị vào một danh sách và chạy cùng một đoạn kiểm tra cho tất cả.

---

## Bài tập riêng — Rẽ nhánh với if else, toán tử 3 ngôi, ?? và switch case

Nguồn bài tập: [https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-93](https://anhtester.com/student-assignments?course=website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau#assignment-93)

**Mục tiêu:** viết điều kiện báo PASS/FAIL có lý do, chọn giá trị mặc định đúng và dùng switch không rơi nhánh.

**Thư mục làm bài:** `D:\AnhTester\js-ts-for-tester\bai-03-dieu-kien`

### 📝 Đề bài

#### Bài tập 1 - Kiểm tra tiêu đề trang quên mật khẩu

Tạo file `bt1-forgot-password.js`. Chuỗi thô lấy từ tiêu đề trang là `'\n Forgot Password '`. Làm sạch chuỗi, so với `Forgot Password` bằng `if...else`: đúng in `PASS`, sai in `FAIL` kèm giá trị mong đợi và thực tế. Viết thêm một dòng chọn chữ PASS/FAIL bằng **toán tử 3 ngôi**. Bỏ thử `trim()` để thấy nhánh FAIL.

#### Bài tập 2 - Cấu hình theo môi trường

Tạo file `bt2-cau-hinh.js`. Đọc `ENV` (mặc định `dev`), dùng `switch` chọn timeout: dev là 60000, staging là 30000, prod là 15000; giá trị khác thì báo không hợp lệ và **không** rơi vào prod. Khai báo `const configRetries = 0;` và đặt retries mặc định là 2 sao cho giá trị 0 được giữ nguyên. Chạy với `ENV=staging` phải in ra:

```none
[staging] timeout=30000, retries=0
```

#### Bài tập 3 - Duyệt code AI

Tạo file `bt3-duyet-code.js`, chép đoạn code AI viết dưới đây và chạy. Không có lỗi nào, nhưng 3 trong 4 dòng in ra sai. Tìm đủ **5 chỗ cần sửa** theo bảng ở Phần 8 (dòng cuối ra PASS đúng nhưng vẫn có 2 chỗ phải viết lại).

```javascript
let status = 404;
const retries = 0;
const env = 'staging';
const errorCount = '0';
const actualTitle = 'Perfex CRM | Anh Tester Demo - Login';
if (status = 200) {
  console.log('Trang phản hồi thành công');
}
const retryCount = retries || 3;
console.log(`Số lần chạy lại: ${retryCount}`);
let baseUrl;
switch (env) {
  case 'dev':
    baseUrl = 'https://dev.crm.example.com';
  case 'staging':
    baseUrl = 'https://staging.crm.example.com';
  case 'prod':
    baseUrl = 'https://crm.anhtester.com';
}
console.log(`Mở trang: ${baseUrl}`);
const result = errorCount == 0 ? (actualTitle.includes('Login') ? 'PASS' : 'FAIL-TITLE') : 'FAIL-ERROR';
console.log(result);
```

### 📦 Cách nộp bài

1. Mở ô **Nội dung bài làm (Editor)**. Với mỗi file: bấm **Đoạn code mẫu**, chọn ngôn ngữ, dán **toàn bộ** code. Dòng đầu là comment đường dẫn file, ví dụ `// bai-03-dieu-kien/bt1-....js`.
2. Ngay dưới mỗi file, chèn thêm một **Đoạn code mẫu** chọn **Text / Log** và dán **kết quả chạy thật** copy từ Terminal (không gõ lại bằng tay).
3. Với bài **Duyệt code AI**: liệt kê từng chỗ sai theo mẫu *Dòng – Lỗi – Lý do – Cách sửa*, sau đó dán file đã sửa và kết quả chạy.
4. Đã đưa project lên GitHub (học ở Bài 7) thì dán thêm link thư mục bài vào ô **Link GitHub**.
5. Bài tập 2: dán kết quả chạy với cả `ENV=staging` và một giá trị sai, ví dụ `ENV=uat`. Trên PowerShell đặt biến bằng `$env:ENV='staging'`.

### ✅ Tiêu chí Đạt

- Bài tập 1 có cả 2 kết quả: PASS khi có trim() và FAIL kèm mong đợi/thực tế khi bỏ trim(); có dòng dùng toán tử 3 ngôi (chỉ một tầng).
- Bài tập 2 in đúng `[staging] timeout=30000, retries=0`; dùng `??` chứ không dùng `||` cho retries; mỗi case có `break`; có nhánh `default` báo môi trường không hợp lệ.
- Bài tập 3 sau khi sửa in: `Trang phản hồi mã 404` · `Số lần chạy lại: 0` · `Mở trang: https://staging.crm.example.com` · `PASS`. Đủ 5 chỗ: `=` thay vì `===`, `||` thay vì `??`, thiếu `break`, `==` so chuỗi với số, toán tử 3 ngôi lồng nhau.

### 🤖 Dùng AI thế nào cho đúng

Được dùng Claude, ChatGPT hoặc Gemini để **hỏi giải thích** lỗi và khái niệm (prompt mẫu ở phần AI của bài học). Không nhờ AI làm hộ rồi dán vào: bài **Duyệt code AI** chấm chính phần *lý do* do bạn tự viết. Bài nào nộp lại vì **Cần sửa** thì sửa đúng chỗ giảng viên ghi trong feedback rồi bấm **Nộp lại**.