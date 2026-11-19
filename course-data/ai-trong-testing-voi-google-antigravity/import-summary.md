# Báo cáo nhập: AI trong Testing với Google Antigravity

Cập nhật: 2026-11-19T13:27:57.025966+07:00

## Nguồn và phạm vi công bố

- Tên thư mục: `course-data/ai-trong-testing-voi-google-antigravity/`.
- Khóa học nguồn: https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-testing-voi-google-antigravity/283.
- Chủ sở hữu yêu cầu đưa dữ liệu lên main của repository Public và không đăng video.
- Giữ JSON, Markdown, ảnh, URL video xem/nhúng, báo cáo và hai script crawler nguồn.
- Không đăng 9 tệp MP4, ZIP chứa video, kế hoạch tải video, script tải video, log, browser profile hoặc dữ liệu phiên đăng nhập.
- Các video và ZIP đầy đủ vẫn được giữ nguyên trên máy; bản nhập này không xóa hoặc sửa bản xuất cục bộ.

## Thống kê đã kiểm tra

| Chỉ số | Kết quả |
|---|---:|
| Chương | 1 |
| Tổng mục | 8 |
| Mục có content_status: exported | 8 |
| Bài có nội dung bài giảng | 7 |
| Mục chỉ có liên kết tài nguyên nguồn | 1 |
| Mục chỉ có tiêu đề/mô tả metadata | 0 |
| Mục lỗi chưa xử lý | 0 |
| Cặp JSON/Markdown | 8 |
| Ảnh | 30 |
| Khối code/prompt | 81 |
| Bảng | 30 |
| URL video riêng biệt | 9 |
| Tệp video đăng lên repo | 0 |
| File dữ liệu, chưa tính báo cáo nhập này | 53 |
| Dung lượng dữ liệu, chưa tính báo cáo nhập này (byte) | 12,523,505 |
| Dung lượng dữ liệu (MiB) | 11.94 |

Bài 8 chỉ có hai liên kết Claude Testing Kit và Codex Testing Kit, không có video hoặc nội dung giảng chi tiết trong DOM nguồn. Đây là mục tài nguyên thực tế, không được mô tả thành bài lý thuyết đầy đủ.

## Kiểm tra và thay đổi metadata

- Các trường content HTML/blocks, intro, heading, mô tả, code, bảng, URL nguồn và ảnh của từng bài khớp với bản xuất cục bộ.
- Markdown giữ nguyên phần nội dung nguồn; chỉ bỏ đoạn LOCAL_VIDEO_FILES do bước tải video tự thêm, để không còn liên kết tới MP4 vắng mặt trong repo.
- Manifest và JSON từng bài chỉ giữ asset ảnh. Video vẫn giữ URL/metadata, được đánh dấu excluded_from_repository và file_included: false.
- videos.json ghi 9 URL và 0 file được bao gồm. Progress ghi video_excluded_count: 9; không coi đây là lỗi tải hoặc thiếu dữ liệu nhập.
- Kiểm tra đủ 8 JSON/Markdown, manifest, progress, 30 ảnh và toàn bộ đường dẫn tương đối. Không có file nguồn hoặc ảnh bị thiếu.
- Quét tên file và mẫu secrets trước commit; không đưa cookies, token, mật khẩu thật, dữ liệu tài khoản cục bộ hoặc thông tin phiên đăng nhập vào bản công bố.
- .gitignore được bổ sung để tránh commit nhầm video của khóa này trong tương lai.

## Đường dẫn quan trọng

| Đường dẫn | Nội dung |
|---|---|
| `course-data/ai-trong-testing-voi-google-antigravity/manifest.json` | Danh mục và trạng thái 8 mục |
| `course-data/ai-trong-testing-voi-google-antigravity/chapters/chapter-01/lesson-NNN.json` | Nội dung có cấu trúc |
| `course-data/ai-trong-testing-voi-google-antigravity/chapters/chapter-01/lesson-NNN.md` | Nội dung Markdown |
| `course-data/ai-trong-testing-voi-google-antigravity/assets/` | 30 ảnh nguồn và README |
| `course-data/ai-trong-testing-voi-google-antigravity/videos.json` | 9 URL xem/nhúng và metadata, không kèm MP4 |
| `course-data/ai-trong-testing-voi-google-antigravity/progress.json` | Trạng thái bản công bố |
| `course-data/ai-trong-testing-voi-google-antigravity/export-report.md` | Báo cáo xuất cho phạm vi không gồm video |
| `course-data/ai-trong-testing-voi-google-antigravity/import-summary.md` | Báo cáo nhập hiện tại |
