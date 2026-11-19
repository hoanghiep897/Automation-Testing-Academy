# Automation Testing Academy

Các bộ dữ liệu khóa học được chuẩn bị cho việc tích hợp vào Automation Testing Academy sau này. Mỗi khóa có một thư mục riêng đặt theo tên khóa học.

## Danh mục dữ liệu

| Khóa học | Thư mục | Chương | Tổng mục | Có nội dung | Chỉ metadata | Ảnh |
|---|---|---:|---:|---:|---:|---:|
| Website and API Testing Automation with Playwright JavaScript TypeScript | [playwright-javascript-typescript](course-data/playwright-javascript-typescript/) | 7 | 42 | 34 | 8 | 126 |
| Sử dụng AI trong Test Manual | [su-dung-ai-trong-test-manual](course-data/su-dung-ai-trong-test-manual/) | 1 | 17 | 17 | 0 | 28 |
| AI trong Testing với Google Antigravity | [ai-trong-testing-voi-google-antigravity](course-data/ai-trong-testing-voi-google-antigravity/) | 1 | 8 | 8 | 0 | 30 |

Chỉ các mục có `content_status: exported` và nội dung HTML/blocks thật được tính là có nội dung. Khóa Playwright còn 8 mục chỉ có metadata: mục 35–42, tương ứng Bài 34–41 (source ID 391–398), chưa hiển thị nội dung bài giảng trên trang nguồn lúc kiểm tra.

Khóa Google Antigravity gồm 7 bài giảng và 1 mục liên kết tài nguyên (Bài 8). Bản repository chỉ lưu 9 URL video để xem trực tuyến; không chứa tệp video hoặc ZIP chứa video.

## Cấu trúc mỗi khóa

```text
course-data/<ten-khoa-hoc>/
├── manifest.json
├── chapters/
│   ├── chapter-01/
│   └── ...
├── assets/
├── scripts/
├── progress.json
├── export-report.md
└── import-summary.md
```

Mỗi bài có JSON và Markdown. JSON của các mục đã xuất có HTML và cấu trúc khối nội dung; ảnh nằm trong `assets/`. Markdown giữ thứ tự nội dung, bảng HTML và code block. Đường dẫn tương đối của bài và ảnh được giữ nguyên khi đổi tên thư mục khóa học.

Nội dung bài giảng, code và ảnh nguồn được giữ nguyên. Metadata xuất được điều chỉnh theo phạm vi công bố, ví dụ bỏ đường dẫn tới tệp video không đăng lên repo. Metadata hệ điều hành, browser profile, thông tin đăng nhập và log cục bộ được loại khỏi commit.

## Báo cáo

- Playwright JavaScript TypeScript: [báo cáo nhập](course-data/playwright-javascript-typescript/import-summary.md), [báo cáo xuất](course-data/playwright-javascript-typescript/export-report.md).
- Sử dụng AI trong Test Manual: [báo cáo nhập](course-data/su-dung-ai-trong-test-manual/import-summary.md), [báo cáo xuất](course-data/su-dung-ai-trong-test-manual/export-report.md).
- AI trong Testing với Google Antigravity: [báo cáo nhập](course-data/ai-trong-testing-voi-google-antigravity/import-summary.md), [báo cáo xuất](course-data/ai-trong-testing-voi-google-antigravity/export-report.md), [URL video](course-data/ai-trong-testing-voi-google-antigravity/videos.json).

## Quyền phân phối

Chủ sở hữu đã xác nhận quyền đăng lại công khai và cho phép đưa dữ liệu các khóa học lên nhánh `main` của repository Public này. URL nguồn và thông tin nguồn trong dữ liệu được giữ nguyên.
