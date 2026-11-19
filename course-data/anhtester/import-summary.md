# Báo cáo nhập dữ liệu AnhTester

Kiểm tra: 2026-11-19T09:22:47.300005+07:00

## Nguồn và đích

- ZIP nguồn: `anhtester-course-export.zip`.
- SHA-256 ZIP: `82d7fd6f1a82cf1ed0085f4d907809fa7f9345d6ee389683543799c7c0f31016`.
- Repository: https://github.com/hoanghiep897/Automation-Testing-Academy.
- Nhánh chuẩn bị: `main`. Repository trống khi clone; chưa có commit trên remote.
- Đích giải nén: `course-data/anhtester/`. Đã bỏ một lớp thư mục bao ngoài `anhtester-course-export/`.
- Quyền phân phối: chủ sở hữu đã xác nhận quyền đăng lại công khai các tài liệu trong ZIP và cho phép commit/push lên `main` của repo Public.

## Thống kê đã đối chiếu với file thực tế

| Chỉ số | Kết quả |
|---|---:|
| Chương | 7 |
| Mục trong danh mục | 42 |
| Mục có nội dung, `content_status: exported` | 34 |
| Mục chỉ có metadata | 8 |
| Mục lỗi kỹ thuật chưa xử lý | 0 |
| JSON bài học | 42 |
| Markdown bài học | 42 |
| Assets duy nhất, đã kiểm tra checksum và giải mã ảnh | 126 |
| File nguyên gốc giải nén | 217 |
| Dung lượng nguyên gốc giải nén (byte) | 52,898,262 |
| Dung lượng nguyên gốc giải nén (MiB) | 50.45 |

Dung lượng trên là tổng kích thước 217 file trong ZIP sau giải nén, không tính báo cáo nhập mới hoặc các file quản trị repository.

## Kiểm tra dữ liệu

- ZIP qua kiểm tra CRC; không có đường dẫn thoát thư mục, file symlink hoặc xung đột cần ghi đè.
- Toàn bộ 217 file giải nén khớp từng byte với ZIP. Không sửa lý thuyết, code, JSON, Markdown hoặc ảnh nguồn.
- Loại riêng `chapters/.DS_Store` khỏi commit vì đây là metadata Finder của macOS, không phải nội dung khóa học. Giữ 216 file dữ liệu nguồn và thêm 3 file tài liệu/quản trị mới: tổng 219 file chuẩn bị commit.
- Đã parse manifest.json, progress.json và 42 JSON bài học; kiểm tra khớp manifest ↔ file JSON ↔ progress.
- Đã kiểm tra đủ 42 cặp JSON/Markdown và 126 ảnh; không phát hiện file lỗi hoặc thiếu so với ZIP.
- Các mục exported có nội dung HTML/blocks thật và các kiểm tra nguồn đã đạt; các mục metadata_only có content null.
- Giữ nguyên hai script crawler trong thư mục scripts/ từ ZIP để truy nguyên cách xuất dữ liệu.
- Đã quét tên file và nội dung văn bản để tìm private key, GitHub token, AWS/GCP/Stripe key, JWT/Bearer literal, session cookie và thông tin tài khoản/máy cục bộ. Không phát hiện giá trị phù hợp các mẫu này.
- Không đưa file ZIP gốc, browser profile, cookies, storage-state, log trình duyệt hoặc thông tin đăng nhập vào repository. .gitignore ngăn đưa các artifact cục bộ này vào lần sau.
- Ví dụ code và dữ liệu minh họa vốn có trong bài giảng được giữ nguyên; không tự sửa nội dung giảng dạy.
- Kiểm tra whitespace của Git có thể báo khoảng trắng cuối dòng dùng để xuống dòng Markdown và ký hiệu merge conflict minh họa trong Bài 7. Đây là nội dung gốc, đã đối chiếu ZIP và được giữ nguyên; các file README, .gitignore và báo cáo nhập mới không có lỗi whitespace.
- Tệp lớn nhất là manifest.json: 14,719,518 byte. Không có file từ 50 MiB trở lên.

## Nội dung còn thiếu ở trang nguồn

8 mục sau chỉ có tiêu đề và mô tả ngắn trên trang nguồn lúc kiểm tra. Đây là nội dung chưa có để xuất, không phải file thất lạc khi giải nén và không được tính là xuất thành công.

| Mục | Source ID | Tên bài |
|---|---|---|
| 35 | 391 | [Bài 34 - [Playwright Typescript] Chạy test song song với Parallel Execution](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/391) |
| 36 | 392 | [Bài 35 - [Playwright Typescript] API Testing với Playwright - request fixture và các method GET, POST, PUT, DELETE](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/392) |
| 37 | 393 | [Bài 36 - [Playwright Typescript] Xử lý Authentication, Param, Pagination, Multipart và cấu trúc API Framework](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/393) |
| 38 | 394 | [Bài 37 - [Playwright Typescript] Network Interception và kết hợp API với UI](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/394) |
| 39 | 395 | [Bài 38 - [Playwright Typescript] Debug lỗi với UI Mode, Trace Viewer, Screenshot và Video](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/395) |
| 40 | 396 | [Bài 39 - [Playwright Typescript] Cài đặt và sử dụng HTML Report, Allure Report](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/396) |
| 41 | 397 | [Bài 40 - [Playwright Typescript] CI/CD với GitHub Actions cho Playwright](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/397) |
| 42 | 398 | [Bài 41 - [Playwright Typescript] Xây dựng Framework Playwright hoàn chỉnh với AI](https://anhtester.com/learn/website-and-api-testing-automation-with-playwright-javascript-typescript-day-code-js-ts-tu-dau/398) |

## Đường dẫn quan trọng

| Đường dẫn | Nội dung |
|---|---|
| `course-data/anhtester/manifest.json` | Danh mục 7 chương, 42 mục và trạng thái nội dung |
| `course-data/anhtester/chapters/chapter-XX/lesson-NNN.json` | Dữ liệu có cấu trúc của từng mục |
| `course-data/anhtester/chapters/chapter-XX/lesson-NNN.md` | Nội dung đọc được bằng Markdown |
| `course-data/anhtester/assets/` | 126 file ảnh và README của assets |
| `course-data/anhtester/progress.json` | Tiến độ theo URL |
| `course-data/anhtester/export-report.md` | Báo cáo xuất và đối chiếu DOM gốc |
| `course-data/anhtester/scripts/` | Script xuất gốc, không chứa credential |
| `course-data/anhtester/import-summary.md` | Báo cáo nhập hiện tại |

## Trạng thái phát hành

Chủ sở hữu đã duyệt bản chuẩn bị dữ liệu và xác nhận quyền đăng lại công khai, cho phép commit/push lên nhánh `main`. Bản nhập chỉ bổ sung dữ liệu và tài liệu quản trị repository.

Commit message: `Add structured course data for future academy integration`.
