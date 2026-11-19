# Automation Testing Academy

Dữ liệu khóa học được chuẩn bị cho việc tích hợp vào Automation Testing Academy sau này.

## Dữ liệu AnhTester

Thư mục: [`course-data/anhtester/`](course-data/anhtester/).

| Chỉ số | Số lượng |
|---|---:|
| Chương | 7 |
| Mục trong danh mục | 42 |
| Mục có `content_status: exported` | 34 |
| Mục chỉ có metadata | 8 |
| Mục lỗi kỹ thuật chưa xử lý | 0 |
| Bài tập riêng có nội dung | 33 |
| Ảnh đã kiểm tra | 126 |

Mục 35–42, tương ứng Bài 34–41 (source ID 391–398), chỉ hiển thị tiêu đề và mô tả ngắn trên trang nguồn lúc xuất. Các mục này có trạng thái `metadata_only` và không được tính là đã xuất nội dung thành công.

## Cấu trúc

```text
course-data/anhtester/
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

Mỗi bài có JSON và Markdown. JSON của các mục đã xuất có HTML và cấu trúc khối nội dung; hình ảnh nằm trong `assets/`. Bản Markdown giữ thứ tự nội dung, bảng HTML và code block. Các file dữ liệu nguyên gốc từ ZIP được giữ nguyên từng byte; metadata hệ điều hành `.DS_Store` được loại khỏi commit.

Xem [báo cáo nhập dữ liệu](course-data/anhtester/import-summary.md) và [báo cáo xuất từ nguồn](course-data/anhtester/export-report.md).

## Quyền phân phối

Chủ sở hữu đã xác nhận quyền đăng lại công khai các tài liệu trong ZIP và cho phép commit/push dữ liệu lên nhánh `main` của repository Public này.
