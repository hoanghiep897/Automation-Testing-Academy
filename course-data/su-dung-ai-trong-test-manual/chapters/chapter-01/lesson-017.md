# Bài 17 - Xây dựng quy trình làm việc toàn diện cho Tester Manual

Chương: 1. NỘI DUNG KHOÁ HỌC

Nguồn: [https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/339](https://anhtester.com/learn/khoa-hoc-su-dung-ai-trong-test-manual/339)

✅ Work Flow: nhận task, estimate time, phân tích, viết test cases, log bug, báo cáo tổng hợp  
✅ Chia sẻ con đường ứng dụng AI vào Test Automation  
✅ Support học viên việc dùng AI để làm việc cho công ty dài lâu  
✅ Tặng bộ Testing Skills chuyên nghiệp được chuẩn hoá bởi Anh Tester dành riêng cho học viên có phí. (cập nhật dài lâu)  
🎉 KẾT THÚC KHOÁ HỌC  
📙 Làm dự án cuối khoá - cấp chứng chỉ

## 1. Từ bộ công cụ sang quy trình

Ở bài trước bạn đã cho AI tự chạy theo lịch và gửi kết quả tới đúng người. Tới đây bạn đã đi qua mười lăm bài, mỗi bài một mảnh: cài công cụ, viết prompt, thiết lập Skill và RULE, phân tích requirements, lập test plan, sinh Test Case, review, chạy, log bug, cập nhật khi requirement đổi, tuỳ biến bộ kit, bộ nhớ dự án, MCP, task theo lịch.

Biết từng mảnh chưa phải là có quy trình. Thử hình dung sáng thứ Hai bạn được giao một dự án mới. Câu hỏi đầu tiên không phải "lệnh nào sinh Test Case", mà là:

<table class="rt-table">
<thead>
<tr>
<th>Câu hỏi</th>
<th>Biết lệnh trả lời được không</th>
<th>Bài này trả lời ở</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ngày đầu tiên làm gì trước, gì sau?</strong></td>
<td>Không — mỗi bài dạy một việc, không bài nào nói việc nào phải xong trước</td>
<td>Mục 4 — dựng nền</td>
</tr>
<tr>
<td><strong>Khi nào được sang bước kế tiếp, ai cho phép?</strong></td>
<td>Một phần — lệnh có checkpoint, nhưng cổng giữa các chặng là việc của người</td>
<td>Mục 5 — dòng chảy và các cổng</td>
</tr>
<tr>
<td><strong>Dự án đang đứng ở đâu?</strong></td>
<td>Không — phải biết đọc tài liệu nào, theo thứ tự nào</td>
<td>Mục 6 — một dự án thật ở ba tốc độ</td>
</tr>
<tr>
<td><strong>Hằng ngày, hằng tuần làm gì?</strong></td>
<td>Không</td>
<td>Mục 7 — nhịp làm việc</td>
</tr>
<tr>
<td><strong>Requirement đổi, dev fix bug, có module mới thì sao?</strong></td>
<td>Có lệnh, nhưng phải nhận ra tín hiệu nào ứng với chuỗi lệnh nào</td>
<td>Mục 8 — vòng thay đổi</td>
</tr>
</tbody>
</table>

Bài này không dạy lệnh mới. Nó ghép những gì bạn đã có thành **một quy trình làm việc** — thứ bạn mang vào dự án thật, và đưa được cho người mới vào đội đọc trong một buổi.

> 📌 Bộ kit có tài liệu quy trình gốc: [AI\_FULL\_FLOW\_MANUAL.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_MANUAL.md) — 8 chặng, lệnh nào, chạy bao nhiêu lần. Bạn đã gặp nó ở bài giới thiệu bộ Testing Skills. Tài liệu đó trả lời *thứ tự lệnh*. Bài này bổ sung bốn thứ một quy trình còn thiếu: nền móng, cổng và người quyết, nhịp, và cách phản ứng khi có thay đổi.

## 2. Cả khoá học trên một trang

Trước khi ghép, nhìn lại mỗi bài đóng góp gì. Bảng dưới xếp các bài theo **lớp** của quy trình ở mục 3, không theo thứ tự đã học:

<table class="rt-table">
<thead>
<tr>
<th>Lớp</th>
<th>Bài</th>
<th>Bạn mang vào quy trình</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Nền</strong><br/>dựng một lần cho mỗi dự án</td>
<td>Cài đặt Claude Code + Codex · Git GitHub GitLab</td>
<td>Công cụ, repo, <code>.gitignore</code> chặn <code>.env</code></td>
</tr>
<tr>
<td><strong>Nền</strong></td>
<td>Viết Prompt và dùng Token hiệu quả</td>
<td>Cách giao việc cho AI khi lệnh của kit không phủ tới</td>
</tr>
<tr>
<td><strong>Nền</strong></td>
<td>Thiết lập SKILL, RULE · Bộ Testing Skills</td>
<td>Cơ chế, và bộ kit dựng sẵn 8 chặng</td>
</tr>
<tr>
<td><strong>Nền</strong></td>
<td>Chỉnh lại bộ Skills cho dự án thực tế</td>
<td>File RULE Manual của dự án: mã TC, tên cột, độ hạt, mẫu bug</td>
</tr>
<tr>
<td><strong>Nền</strong></td>
<td>Bộ nhớ Local cho từng dự án</td>
<td><code>memories/</code> + <code>MEMORY.md</code> — quyết định PO, bẫy, quyền hạn QA</td>
</tr>
<tr>
<td><strong>Nền</strong></td>
<td>MCP Server, Connectors, Plugins</td>
<td>Playwright MCP để chạy TC; Jira, Slack để kéo yêu cầu và báo cáo</td>
</tr>
<tr>
<td><strong>Dòng chảy</strong><br/>chạy cho mỗi module</td>
<td>Phân tích Requirements</td>
<td>Chặng 0–1: bản đồ module, REQ ID, điểm mờ AMB, evidence</td>
</tr>
<tr>
<td><strong>Dòng chảy</strong></td>
<td>Chuẩn hoá Requirements và tạo Test Plan</td>
<td>Cổng sẵn sàng trước khi viết TC; Master Test Plan và tiêu chí vào/ra</td>
</tr>
<tr>
<td><strong>Dòng chảy</strong></td>
<td>Tạo Test Cases từ Requirements</td>
<td>Chặng 2: FULL RBT, độ hạt, bản đồ 4 vòng</td>
</tr>
<tr>
<td><strong>Dòng chảy</strong></td>
<td>Review → Execute → Log Bug</td>
<td>Chặng 3–5: rubric, 4 trạng thái chạy, gom nhóm rồi mới log bug, retest</td>
</tr>
<tr>
<td><strong>Vòng thay đổi</strong></td>
<td>Update Requirements → Update TC → Execute → Retest</td>
<td>Chuỗi delta khi requirement đổi — không sinh lại từ đầu</td>
</tr>
<tr>
<td><strong>Nhịp</strong></td>
<td>Schedule và Notifications</td>
<td>Việc lặp lại giao cho lịch; kết quả tự tìm tới đúng người</td>
</tr>
</tbody>
</table>

## 3. Quy trình bốn lớp

Gom lại, quy trình làm việc của một Tester Manual dùng AI có bốn lớp. Mỗi lớp có tần suất riêng, và đó chính là chỗ người mới hay nhầm: làm việc của lớp này theo nhịp của lớp khác.

```none
┌─ LỚP 1 · NỀN ──────────────────────── 1 lần / dự án ───────────────┐
│  repo + kit + .env + Playwright MCP + RULE dự án + memories/        │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─ LỚP 2 · DÒNG CHẢY ────────────────── mỗi module ──────────────────┐
│  0 khám phá → 1 REQ → [cổng sẵn sàng] → 2 TC → 3 review             │
│     → [plan duyệt] → 4 chạy → 5 bug ↻ retest → 6 RTM → 7 báo cáo    │
└─────────────────────────────────────────────────────────────────────┘
        ↑                                              ↓
┌─ LỚP 4 · VÒNG THAY ĐỔI ── khi có tín hiệu ┐   ┌─ LỚP 3 · NHỊP ── ngày / tuần / đợt ─┐
│  REQ đổi · dev fix · module mới ·         │   │  task Slack · bug chờ retest ·      │
│  chuẩn công ty đổi · kit ra bản mới       │   │  báo cáo tiến độ · RTM · release    │
└───────────────────────────────────────────┘   └─────────────────────────────────────┘
```

<table class="rt-table">
<thead>
<tr>
<th>Lớp</th>
<th>Tần suất</th>
<th>Nhầm lớp thì</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Nền</strong></td>
<td>Một lần, sửa khi cần</td>
<td>Bỏ qua để "làm việc thật cho nhanh" → evidence rơi sai thư mục, mã TC mỗi người một kiểu, AI quên quyết định của PO sau mỗi phiên</td>
</tr>
<tr>
<td><strong>Dòng chảy</strong></td>
<td>Mỗi module, đi một chiều qua các cổng</td>
<td>Chạy chặng 2 khi chặng 1 còn điểm mờ 🔴 → sinh TC trên giả định, PO trả lời xong phải viết lại</td>
</tr>
<tr>
<td><strong>Nhịp</strong></td>
<td>Đều đặn, không phụ thuộc module</td>
<td>Báo cáo tiến độ "khi nào rảnh thì làm" → PM chỉ biết dự án trễ vào tuần cuối</td>
</tr>
<tr>
<td><strong>Vòng thay đổi</strong></td>
<td>Khi có tín hiệu</td>
<td>Sinh lại cả bộ TC mỗi khi có ticket → mất TC ID, đứt truy vết với execution report và bug cũ</td>
</tr>
</tbody>
</table>

## 4. Lớp 1 — Dựng nền cho một dự án mới

Ngày đầu ở dự án mới, chưa sinh một dòng requirement nào. Ngày đó dùng để dựng nền, theo đúng thứ tự dưới đây. Thứ tự này có lý do: mỗi bước là điều kiện để bước sau đúng ngay từ lần đầu.

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Việc</th>
<th>Vì sao phải xong trước việc sau</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>Repo Git</strong> + <code>.gitignore</code> chặn <code>.env</code></td>
<td>Lệnh FIX và lệnh delta của kit ghi <strong>mốc git</strong> của bản cũ vào Nhật ký thay đổi. Không có git thì không có bản đối chiếu, và <code>/update-testcases-from-impact</code> còn <strong>dừng lại</strong> nếu thấy thay đổi chưa commit</td>
</tr>
<tr>
<td>2</td>
<td><strong>Đưa bộ kit vào dự án</strong></td>
<td>Lệnh, skill, CLAUDE.md của kit phải có mặt trước phiên làm việc đầu tiên — phiên đó sẽ đọc chúng</td>
</tr>
<tr>
<td>3</td>
<td><strong><code>.env</code></strong> từ <code>.env.example</code> — tài khoản đủ vai trò</td>
<td>Chặng 0 khám phá theo quyền của tài khoản. Thiếu vai trò nào, module của vai trò đó không xuất hiện trên bản đồ</td>
</tr>
<tr>
<td>4</td>
<td><strong>Playwright MCP</strong> ở phạm vi dự án (<code>.mcp.json</code>)</td>
<td>Evidence của chặng 1 rơi đúng thư mục dự án, viewport khớp màn hình. Cài sau thì ảnh của các module đầu nằm lạc chỗ khác</td>
</tr>
<tr>
<td>5</td>
<td><strong>Điền thông tin hệ thống</strong>: môi trường có dùng chung không, <strong>năng lực kiểm thử của QA</strong></td>
<td>Hai thông tin này quyết định cách sinh <em>mọi</em> bộ TC: TC phá huỷ có bị auto-skip không, nhánh kiểm tầng tích hợp giao cho QA hay đội Dev. Chốt sau là phải sửa lại các bộ đã sinh</td>
</tr>
<tr>
<td>6</td>
<td><strong>File RULE Manual của dự án</strong> — mã TC, tên cột, độ hạt, mẫu bug</td>
<td>Bộ TC đầu tiên đã sinh thì mã và độ hạt không đổi được nữa — đổi là đánh lại toàn bộ TC ID</td>
</tr>
<tr>
<td>7</td>
<td><strong><code>memories/MEMORY.md</code></strong> + câu luật trong <code>CLAUDE.md</code></td>
<td>Từ phiên đầu tiên đã có quyết định đáng nhớ: môi trường nào, tài khoản nào thiếu quyền. Không có chỗ ghi thì chúng chỉ sống trong khung chat</td>
</tr>
<tr>
<td>8</td>
<td><strong>Connector</strong> cần dùng: Jira, Slack</td>
<td>Chỉ cài cái thật sự dùng, cấp quyền tối thiểu. Có thể để sau, không chặn dòng chảy</td>
</tr>
<tr>
<td>9</td>
<td><strong>Nghiệm thu bằng một phiên mới</strong></td>
<td>Mở phiên mới, hỏi AI: dự án dùng mã TC nào, môi trường có dùng chung không, Playwright MCP có chạy không. Trả lời sai câu nào là nền hở chỗ đó</td>
</tr>
</tbody>
</table>

Bước 5 có ví dụ thật trong danh mục requirements của CRM demo, [docs/requirements/README.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/requirements/README.md). Dòng **Năng lực kiểm thử của QA** được chốt ngày 11-09-2026: QA không gọi API trực tiếp, không truy vấn CSDL, không kiểm tầng tích hợp — ba việc đó thuộc đội Dev; QA có DevTools nên chạy được TC gắn `@TechCheck`. Dòng này ghi rõ là *dùng cho Vòng 3 của mọi bộ TC*. Nó là nền, không phải chi tiết của riêng module nào.

> 💡 **Nền không cần hoàn hảo, nhưng phải có trước.** Bước 8 để sau được. Bước 1–7 thì không: thiếu bất kỳ bước nào, chặng 0 vẫn chạy được, nhưng chạy ra kết quả bạn sẽ phải sửa lại.

## 5. Lớp 2 — Dòng chảy của một module và các cổng

Đây là phần bạn đã học kỹ nhất. Điều bài này thêm vào là **cổng**: giữa hai chặng luôn có một điều kiện phải đạt, và một người có quyền nói "được, sang chặng sau".

<table class="rt-table">
<thead>
<tr>
<th>Chặng</th>
<th>Lệnh</th>
<th>Cổng để sang chặng sau</th>
<th>Ai mở cổng</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>0</strong> Khám phá</td>
<td><code>/discover-system</code></td>
<td>Đã trả lời 3 câu ở checkpoint, nhất là <em>"có module nào AI không thấy được vì thiếu quyền"</em></td>
<td>Tester</td>
</tr>
<tr>
<td><strong>1</strong> Requirements</td>
<td><code>/generate-requirements-from-website</code></td>
<td>Mọi REQ có <code>REQ ID</code> và cột Nguồn; message lỗi nguyên văn; evidence full-page</td>
<td>Tester</td>
</tr>
<tr>
<td><strong>Cổng sẵn sàng</strong></td>
<td><code>/analyze-requirement-document</code>, <code>/update-requirements-from-ticket</code></td>
<td>Không còn AMB 🔴 chưa có câu trả lời hoặc giả định tạm được ghi lại</td>
<td><strong>PO</strong> trả lời, Tester ghi</td>
</tr>
<tr>
<td><strong>2</strong> Test Case</td>
<td><code>/generate-testcases-manual-rbt</code></td>
<td>Self-Quality Gate đạt; độ hạt đúng RULE dự án</td>
<td>Tester</td>
</tr>
<tr>
<td><strong>3</strong> Review</td>
<td><code>/review-testcases</code></td>
<td>Đã sửa theo báo cáo review (mode FIX). Muốn automate thì chạy thêm mode AUTOMATION</td>
<td>Tester / QA Lead</td>
</tr>
<tr>
<td><strong>Plan duyệt</strong> <em>(khi có plan chính thức)</em></td>
<td><code>/generate-master-test-plan</code></td>
<td>Plan đã duyệt; tiêu chí vào đạt — build, tài khoản đủ vai trò, môi trường, TC đã review</td>
<td><strong>PM</strong></td>
</tr>
<tr>
<td><strong>4</strong> Chạy</td>
<td><code>/execute-test-cases</code></td>
<td>Execution report có đủ 4 trạng thái; dữ liệu test đã dọn</td>
<td>Tester</td>
</tr>
<tr>
<td><strong>5</strong> Bug ↻ retest</td>
<td><code>/analyze-test-report</code> → <code>/create-bug-report</code> → <code>/retest-fixed-bugs</code></td>
<td>Mọi FAIL đã phân loại: bug của ứng dụng hay TC viết sai. Vòng lặp chạy tới khi hết bug cần đóng trong đợt</td>
<td>Tester; <strong>Dev</strong> fix</td>
</tr>
<tr>
<td><strong>6</strong> RTM</td>
<td><code>/generate-traceability-matrix</code></td>
<td>Đã đọc mục ⬛ trước mọi con số phần trăm</td>
<td>Tester</td>
</tr>
<tr>
<td><strong>7</strong> Báo cáo</td>
<td><code>/generate-test-summary-report</code></td>
<td>Khuyến nghị GO / GO có điều kiện / NO-GO kèm rủi ro tồn đọng</td>
<td>QA khuyến nghị, <strong>PM quyết</strong></td>
</tr>
</tbody>
</table>

### 5.1. Năm chỗ người quyết, AI không được quyết

Mọi lệnh của kit đều có thể chạy tới cuối nếu bạn gõ "tiếp tục" ở mỗi checkpoint. Quy trình tốt là quy trình biết rõ chỗ nào **không được** gõ "tiếp tục" cho nhanh:

1. **Ranh giới hệ thống ở chặng 0.** AI chỉ thấy cái tài khoản của nó thấy. Module nằm sau quyền khác hay chỉ vào được bằng URL, chỉ người biết.
2. **Câu trả lời cho điểm mờ.** AI ghi được giả định tạm, nhưng không bao giờ được viết tiêu chí chấp nhận thay PO.
3. **Duyệt plan và tiêu chí exit.** Phải chốt *trước* khi nhìn kết quả. Đặt ngưỡng sau khi thấy số là hợp thức hoá kết quả, không phải đánh giá.
4. **FAIL do ứng dụng hay do TC viết sai.** AI phân loại và đề xuất. Kết luận cuối là của người hiểu nghiệp vụ, vì một bên thành bug gửi dev, một bên thành sửa TC.
5. **Release hay không.** QA khuyến nghị, PM quyết — QA không nắm áp lực hợp đồng, thị trường, chi phí trễ hạn.

## 6. Một dự án thật ở ba tốc độ — CRM demo hôm nay

Lý thuyết về dòng chảy dễ làm người ta nghĩ cả dự án đi đều một nhịp. Thực tế không bao giờ như vậy. Mở ba file chỉ mục của CRM demo trong bộ kit — đây là ảnh chụp dự án tại thời điểm viết bài (10-2026):

<table class="rt-table">
<thead>
<tr>
<th>Module</th>
<th>Đã có</th>
<th>Đang đứng ở</th>
<th>Việc kế tiếp</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Đăng nhập</strong> <code>LOGIN</code></td>
<td>44 REQ (40 trong phạm vi) · 0 AMB treo · 51 TC, 71 biến thể · review FIX 19-09 · 2 lượt chạy · 6 bug (5 đang mở) · user guide</td>
<td>Chặng 5 — chờ dev fix để retest. <strong>Chưa có RTM</strong></td>
<td>Retest khi dev báo fix; chạy RTM trước release</td>
</tr>
<tr>
<td><strong>Khách hàng</strong> <code>CUST</code></td>
<td>84 REQ · 0 AMB treo · 129 TC, 155 biến thể · review 24-09 điểm trung bình 11,84/12</td>
<td>Giữa chặng 3 và 4 — báo cáo review còn 1 khoảng trống bảo mật, 4 lỗi tag/số liệu, đề xuất mở <code>AMB-CUST-15</code></td>
<td>Review mode FIX theo báo cáo → hỏi PO điểm mờ mới → bắt đầu chạy từ bộ Smoke</td>
</tr>
<tr>
<td><strong>Dự án</strong> <code>PRJ</code></td>
<td>104 REQ · <strong>6 AMB 🔴 treo</strong> · 0 TC</td>
<td><strong>Trước cổng sẵn sàng</strong></td>
<td>Chốt 6 điểm mờ với PO. <strong>Chưa</strong> sinh TC</td>
</tr>
<tr>
<td>20 module còn lại</td>
<td>Chỉ có prefix trên bản đồ</td>
<td>Chặng 0 xong, chưa vào chặng 1</td>
<td>Nằm ngoài phạm vi đợt Release 1.0</td>
</tr>
</tbody>
</table>

Ba module, ba chỗ đứng khác nhau, và **cả ba đều đúng quy trình**. `PRJ` đứng yên không phải vì chậm, mà vì quy trình bắt nó đứng: sinh 100 TC trên 6 điểm mờ 🔴 là sinh ra thứ phải viết lại khi PO trả lời. Một dự án lành mạnh trông đúng như bảng này — mỗi module ở một chặng, và ai nhìn vào cũng biết vì sao.

### 6.1. Đọc hiện trạng ở đâu — chỉ mục, không phải plan

Mở [Master Test Plan Release 1.0](https://github.com/anhtester/claude-testing-skills/blob/main/docs/test-plans/test_plan_release_1.0.md) (bản 17-09-2026), mục Phạm vi ghi: `CUST` — 79 REQ, **0 TC**, 4 AMB 🔴 treo. Còn [docs/testcases/README.md](https://github.com/anhtester/claude-testing-skills/blob/main/docs/testcases/README.md) hôm nay ghi `CUST` — **129 TC**, độ phủ 84/84 REQ.

Không file nào sai. Chúng làm hai việc khác nhau:

<table class="rt-table">
<thead>
<tr>
<th>Tài liệu</th>
<th>Là gì</th>
<th>Dùng để</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Master Test Plan</strong></td>
<td><strong>Cam kết</strong> lúc lập và duyệt — ảnh chụp ngày 17-09</td>
<td>So sánh: đã hứa gì, phạm vi nào, tiêu chí exit nào. Không dùng để biết hôm nay có bao nhiêu TC</td>
</tr>
<tr>
<td><strong>Ba file chỉ mục</strong> <code>requirements/README.md</code> · <code>testcases/README.md</code> · <code>bugs/README.md</code></td>
<td><strong>Hiện trạng</strong> — lệnh của kit tự cập nhật mỗi lần chạy</td>
<td>Biết module nào ở đâu, mã kế tiếp là gì, bug nào đang mở</td>
</tr>
<tr>
<td><strong>Báo cáo tiến độ</strong></td>
<td><strong>Cầu nối</strong> — đọc cả hai</td>
<td>Trả lời "hiện trạng so với cam kết thì đang sớm hay trễ"</td>
</tr>
</tbody>
</table>

> ⚠️ **Đừng sửa plan cho khớp hiện trạng.** Plan lệch hiện trạng là bình thường — đó chính là thứ báo cáo tiến độ đo. Chỉ khi *phạm vi hoặc lịch* thay đổi mới cập nhật plan, bằng cách sửa phiếu `test_plan.config.yaml` rồi gọi lại lệnh: AI tăng phiên bản, ghi lịch sử thay đổi, đưa plan về trạng thái chờ duyệt. Viết đè plan là mất dấu thứ đã được ký.

## 7. Lớp 3 — Nhịp làm việc

Dòng chảy đi theo module; nhịp đi theo lịch. Bảng dưới là nhịp đề xuất cho một Tester Manual trong một đợt kiểm thử. Cột cuối chỉ ra việc nào giao được cho task theo lịch ở bài trước:

<table class="rt-table">
<thead>
<tr>
<th>Nhịp</th>
<th>Việc</th>
<th>Lệnh / công cụ</th>
<th>Ai làm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Mỗi ngày</strong></td>
<td>Đọc task được giao, ước lượng</td>
<td>Slack connector</td>
<td>Task theo lịch 8h30 → bạn đọc</td>
</tr>
<tr>
<td><strong>Mỗi ngày</strong></td>
<td>Danh sách bug chờ retest</td>
<td>Đọc <code>docs/bugs/README.md</code></td>
<td>Task theo lịch 8h45 → bạn quyết</td>
</tr>
<tr>
<td><strong>Mỗi ngày</strong></td>
<td>Chạy TC theo kế hoạch ngày, gom nhóm FAIL, log bug</td>
<td><code>/execute-test-cases</code> → <code>/analyze-test-report</code> → <code>/create-bug-report</code></td>
<td>Bạn + AI</td>
</tr>
<tr>
<td><strong>Mỗi ngày</strong></td>
<td>Commit sau mỗi chặng xong</td>
<td>Git</td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi tuần</strong></td>
<td>Báo cáo tiến độ</td>
<td><code>/generate-test-progress-report</code></td>
<td>Task theo lịch thứ Sáu → bạn đọc, commit</td>
</tr>
<tr>
<td><strong>Mỗi tuần</strong></td>
<td>Review bộ TC mới viết trong tuần</td>
<td><code>/review-testcases</code></td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi tuần</strong></td>
<td>Rà AMB còn treo, hỏi lại PO</td>
<td>Cột AMB treo trong <code>requirements/README.md</code></td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi tuần</strong></td>
<td>Ghi quyết định mới vào bộ nhớ, dọn mục lỗi thời</td>
<td><code>memories/</code></td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi đợt</strong> release</td>
<td>Ma trận truy vết</td>
<td><code>/generate-traceability-matrix</code></td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi đợt</strong> release</td>
<td>Báo cáo tổng hợp và khuyến nghị release</td>
<td><code>/generate-test-summary-report</code></td>
<td>Bạn khuyến nghị, PM quyết</td>
</tr>
<tr>
<td><strong>Mỗi đợt</strong> release</td>
<td>Xuất Excel cho người ngoài đội</td>
<td>Web viewer của kit</td>
<td>Bạn</td>
</tr>
<tr>
<td><strong>Mỗi tháng</strong></td>
<td>Rà task theo lịch, quyền connector, bản mới của bộ kit</td>
<td>Trang Routines · Settings → Connectors · repo kit</td>
<td>Bạn</td>
</tr>
</tbody>
</table>

> 💡 **"Commit sau mỗi chặng" không phải thói quen cho đẹp.** Lệnh FIX ghi mốc git của bản cũ vào Nhật ký thay đổi; lệnh delta *dừng hẳn* khi thấy file TC có thay đổi chưa commit, vì sửa đè lên đó là mất bản đối chiếu. Commit đều tay là điều kiện để các lệnh đó chạy được.

## 8. Lớp 4 — Vòng thay đổi: tín hiệu nào, chuỗi lệnh nào

Dự án đang phát triển thì thay đổi đến hằng tuần. Kỹ năng quan trọng ở lớp này là **nhận ra tín hiệu** và chọn đúng chuỗi, thay vì phản xạ "sinh lại cho chắc":

<table class="rt-table">
<thead>
<tr>
<th>Tín hiệu</th>
<th>Chuỗi lệnh</th>
<th>Không làm</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Requirement đổi</strong> — ticket mới, PO trả lời một AMB</td>
<td><code>/update-requirements-from-ticket</code> → Impact Report → <code>/update-testcases-from-impact</code> (PLAN rồi APPLY) → chạy lại đúng phần bị ảnh hưởng → xét lại bug liên quan rồi mới retest</td>
<td>Sinh lại cả bộ TC. Dùng <code>/review-testcases</code> FIX cho TC lỗi thời — nó chấm chất lượng, không đối chiếu REQ mới</td>
</tr>
<tr>
<td><strong>Dev báo đã fix</strong></td>
<td><code>/retest-fixed-bugs</code> — Critical/Major chạy mode FULL kèm regression</td>
<td>Retest trên đúng build lúc log bug. Tạo bug mới khi lỗi cũ còn — mở lại bug cũ</td>
</tr>
<tr>
<td><strong>Phát hiện module sót</strong>, hệ thống thêm app hay API</td>
<td><code>/discover-system</code> mode ADD — chỉ xử lý phần mới, giữ prefix cũ</td>
<td>Chạy lại khám phá toàn bộ</td>
</tr>
<tr>
<td><strong>Chuẩn công ty đổi</strong> — mẫu bug, tên cột</td>
<td>Sửa RULE trước, SKILL sau; kiểm bằng phiên mới và một ca mẫu cố định</td>
<td>Sửa thẳng file TC đã sinh cho khớp chuẩn mới</td>
</tr>
<tr>
<td><strong>Bộ kit ra bản mới</strong></td>
<td>Đọc thay đổi của kit, giữ phần tuỳ biến của dự án theo cách đã học ở bài chỉnh bộ Skills</td>
<td>Chép đè cả thư mục <code>.claude/</code> — mất RULE riêng của dự án</td>
</tr>
</tbody>
</table>

> 📌 **Mắt xích cảnh báo duy nhất** cho biết TC nào đã lỗi thời là cột `TC cần xử lý` trong Nhật ký thay đổi của tài liệu requirements. Bỏ qua cột này là chạy test trên bộ TC sai mà không biết — vòng thay đổi bắt đầu từ việc đọc nó mỗi khi có lượt cập nhật REQ.

## 9. Ai làm gì — AI, Tester và những người xung quanh

Quy trình có AI không có nghĩa là AI làm hết. Bảng dưới phân vai cho những hoạt động chính:

<table class="rt-table">
<thead>
<tr>
<th>Hoạt động</th>
<th>AI</th>
<th>Tester</th>
<th>PO / PM</th>
<th>Dev</th>
</tr>
</thead>
<tbody>
<tr>
<td>Khảo sát, viết REQ</td>
<td>Mở form, đọc DOM, chụp evidence, viết nháp</td>
<td>Trả lời checkpoint, soát nguồn</td>
<td>PO trả lời AMB</td>
<td>—</td>
</tr>
<tr>
<td>Sinh và review TC</td>
<td>Sinh, tự chấm, chấm rubric</td>
<td>Duyệt danh sách sửa, quyết độ hạt</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>Lập plan</td>
<td>Đọc <code>docs/</code>, soạn plan</td>
<td>Điền phiếu, soát</td>
<td>PM duyệt</td>
<td>—</td>
</tr>
<tr>
<td>Chạy TC</td>
<td>Mở trình duyệt, thao tác, chấm, thu evidence</td>
<td>Gõ mật khẩu thật, chạy TC <code>@PersonalOnly</code>, xác nhận FAIL</td>
<td>—</td>
<td>Cung cấp build</td>
</tr>
<tr>
<td>Bug</td>
<td>Gom nhóm, soạn bug report</td>
<td>Kết luận bug hay TC sai, gửi</td>
<td>PM xếp ưu tiên</td>
<td>Fix, báo build</td>
</tr>
<tr>
<td>Báo cáo release</td>
<td>Gộp số liệu, soạn khuyến nghị</td>
<td>Soát, ký khuyến nghị</td>
<td>PM quyết release</td>
<td>—</td>
</tr>
</tbody>
</table>

Những việc ở cột "Tester" chính là phần nghề của bạn. AI làm nhanh hơn bạn mọi việc ở cột của nó; nó không thay được cột của bạn, vì mỗi việc ở đó cần một người chịu trách nhiệm.

> 🔒 Lưu ý ở dòng "Chạy TC": trong lượt chạy thật của CRM demo ngày 19-09-2026, execution report ghi rõ *mật khẩu thật do người dùng tự gõ ở các bước cần đăng nhập thật; agent không nhập mật khẩu thật*. Đây là ranh giới nên giữ trong quy trình của bạn, không chỉ trong bài học.

## 10. Làm việc nhóm trên cùng một repo

Một mình một dự án thì quy trình ở trên là đủ. Khi đội có hai, ba Tester cùng làm trên một repo, có thêm vài luật để không giẫm chân nhau:

<table class="rt-table">
<thead>
<tr>
<th>Luật</th>
<th>Vì sao</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Mỗi module một người tại một thời điểm</strong>, mỗi người một nhánh</td>
<td>Chỉ mục giữ cột <strong>Mã kế tiếp</strong> của REQ và TC. Hai người cùng sinh cho một module ở hai nhánh sẽ cùng lấy một dải mã — tới lúc merge là hai TC khác nhau trùng một ID</td>
</tr>
<tr>
<td><strong>Ba file chỉ mục là điểm va chạm</strong> — khi xung đột, giữ cả hai dòng</td>
<td>Lệnh của kit tự ghi vào <code>requirements/README.md</code>, <code>testcases/README.md</code>, <code>bugs/README.md</code>. Hai nhánh cùng sửa file đó là chuyện bình thường. Gộp bằng tay, giữ đủ dòng, <strong>không</strong> đánh lại số nào</td>
</tr>
<tr>
<td><strong>Quyết định của PO ghi một chỗ</strong></td>
<td>Câu trả lời cho AMB đi vào tài liệu requirements qua lệnh cập nhật; lý do và bối cảnh vào <code>memories/</code>. Ghi trong tin nhắn riêng là người kia không biết</td>
</tr>
<tr>
<td><strong><code>memories/</code> được commit</strong> như tài liệu</td>
<td>Bẫy một người đã gặp, người kia không phải gặp lại. Đó là toàn bộ lý do bộ nhớ nằm trong repo chứ không nằm trên máy</td>
</tr>
<tr>
<td><strong>Soát evidence trước khi push</strong> lên repo công khai</td>
<td>Ảnh chụp màn hình có thể chứa dữ liệu thật — bộ kit nhắc kiểm thư mục <code>evidence/</code> của mọi lượt chạy trước khi commit</td>
</tr>
</tbody>
</table>

## 11. Đo sức khoẻ quy trình — tám con số đọc mỗi tuần

Quy trình tốt tự cho biết nó đang hỏng ở đâu. Mỗi tuần, đọc tám con số này — phần lớn có sẵn trong chỉ mục và web viewer của kit:

<table class="rt-table">
<thead>
<tr>
<th>#</th>
<th>Con số</th>
<th>Đọc ở đâu</th>
<th>Báo động khi</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Module trong phạm vi đợt chưa khảo sát (⬛)</td>
<td>RTM, <code>requirements/README.md</code></td>
<td>Còn bất kỳ module nào — mọi tỷ lệ phần trăm khác vô nghĩa</td>
</tr>
<tr>
<td>2</td>
<td>AMB 🔴 còn treo</td>
<td>Cột AMB treo của chỉ mục</td>
<td>Treo quá một tuần, hoặc module có AMB 🔴 đã sinh TC</td>
</tr>
<tr>
<td>3</td>
<td>REQ trong phạm vi chưa có TC</td>
<td><code>testcases/README.md</code> mục độ phủ</td>
<td>Dưới 100% sát ngày bắt đầu chạy</td>
</tr>
<tr>
<td>4</td>
<td>Bộ TC chưa review</td>
<td>Nhật ký thay đổi của từng bộ</td>
<td>Có bộ đã vào chặng 4 mà chưa qua review</td>
</tr>
<tr>
<td>5</td>
<td><strong>Nợ kiểm thử</strong> — TC chưa chạy lần nào</td>
<td>Web viewer, báo cáo tiến độ</td>
<td>Nợ cũ không giảm qua hai kỳ</td>
</tr>
<tr>
<td>6</td>
<td>Tỷ lệ BLOCKED</td>
<td>Web viewer cảnh báo khi vượt 20%</td>
<td>Trên 20% — thường là tiêu chí vào chưa đạt mà vẫn chạy</td>
</tr>
<tr>
<td>7</td>
<td>Bug chờ retest</td>
<td><code>bugs/README.md</code></td>
<td>Nằm chờ quá 3 ngày làm việc</td>
</tr>
<tr>
<td>8</td>
<td>Dữ liệu test chưa dọn</td>
<td>Mục "Dữ liệu đã tạo &amp; dọn dẹp" của execution report, web viewer</td>
<td>Có bất kỳ dòng nào trên môi trường dùng chung</td>
</tr>
</tbody>
</table>

Con số 5 có ví dụ thật ở module Đăng nhập. Lượt chạy 20-08-2026 chạy 41 TC gốc. Sau đó bộ TC được bổ sung 9 TC theo bản đồ 4 vòng và 1 TC theo câu trả lời của PO — 10 TC chưa chạy lần nào. Cộng thêm 2 TC BLOCKED và 1 TC SKIP còn treo từ lượt trước, khoản nợ là 13 TC. Lượt chạy 19-09-2026 trả đúng khoản nợ đó: 13 TC, cả 13 PASS. Không đo nợ kiểm thử thì 10 TC mới sẽ nằm đó tới tận báo cáo release.

## 12. Bốn lỗi ở cấp quy trình

Các bài trước đã liệt kê lỗi hay gặp của từng lệnh. Đây là bốn lỗi chỉ lộ ra khi nhìn cả quy trình:

**Lỗi 1 — Chạy đúng lệnh, sai thứ tự.**  
Sinh TC cho `PRJ` ngay khi có 104 REQ, bỏ qua 6 AMB 🔴. Lệnh vẫn chạy, bộ TC vẫn đẹp, Self-Quality Gate vẫn đạt. Hậu quả chỉ lộ ra khi PO trả lời: một phần bộ TC dựng trên giả định sai, phải đi qua cả chuỗi delta để sửa. Cổng sẵn sàng tồn tại để ngăn đúng việc này.

**Lỗi 2 — Plan là tờ giấy ký xong cất tủ.**  
Phạm vi đổi giữa đợt mà không cập nhật plan; tới báo cáo tổng hợp, chặng 7 chấm theo bộ tiêu chí exit cũ và ra kết luận lệch. Hoặc ngược lại: thấy kết quả rồi mới hạ ngưỡng exit. Cả hai đều phá chức năng duy nhất của plan — là cam kết đo được.

**Lỗi 3 — Thay đổi đến mà không ai đọc cột `TC cần xử lý`.**  
Requirement đã cập nhật, Impact Report đã có, nhưng không ai chạy bước đồng bộ TC. Lượt chạy tuần sau chấm PASS theo hành vi cũ. Không có lỗi nào hiện ra — đó là lý do lỗi này nguy hiểm nhất.

**Lỗi 4 — Coi AI là người chạy thay, không phải người chuẩn bị.**  
Gõ "tiếp tục" ở mọi checkpoint, để AI tự kết luận FAIL là bug, để task theo lịch tự retest. Mỗi việc đều tiết kiệm được vài phút. Cộng lại, quy trình mất người chịu trách nhiệm ở đúng năm chỗ của mục 5.1.

## 13. Bài tập thực hành

Đây là bài cuối, nên bài tập là một dự án nhỏ: đưa CRM demo đi tiếp từ đúng chỗ nó đang đứng.

**Bài tập 1 — Đọc hiện trạng như người mới vào đội.** Clone bộ kit. Chỉ đọc ba file chỉ mục và thư mục `docs/executions/`, tự dựng lại bảng ở mục 6. Sau đó mở Master Test Plan Release 1.0, ghi ra mọi chỗ plan khác hiện trạng. Mỗi chỗ khác thuộc loại nào: hiện trạng đã tiến lên (bình thường), hay phạm vi đã đổi mà plan chưa cập nhật (phải xử lý)?

**Bài tập 2 — Đưa module Khách hàng sang chặng 4.** Đọc báo cáo review ngày 24-09 của bộ TC `CUST`. Chạy `/review-testcases` mode FIX cho đúng những điểm báo cáo nêu, soạn câu hỏi `AMB-CUST-15` gửi PO. Rồi chạy bộ Smoke (`part_01_web_smoke`) trên CRM demo — môi trường dùng chung, bật auto-skip, tự gõ mật khẩu. Gom nhóm FAIL trước khi log bug.

**Bài tập 3 — Giữ module Dự án ở đúng chỗ.** Đọc 6 AMB 🔴 của `PRJ`. Với mỗi cái, viết câu hỏi cho PO và một giả định tạm. Rồi trả lời: với giả định tạm đó, có được sinh TC cho phần nào của module không? Phần nào chắc chắn phải chờ? Ghi lại lý do.

**Bài tập 4 — Dựng nền cho dự án của chính bạn.** Lấy một hệ thống bạn đang test thật (hoặc một hệ thống demo khác). Làm đủ 9 bước ở mục 4, ghi lại thời gian từng bước, và nghiệm thu bằng một phiên mới. Đây là bài tập quan trọng nhất của cả khoá — mọi thứ sau đó chỉ đúng khi nền đúng.

**Bài tập 5 — Quy trình một trang cho đội.** Viết một file `QUY_TRINH.md` cho dự án của bạn, chỉ gồm ba bảng: nhịp làm việc (mục 7), năm chỗ người quyết kèm tên người cụ thể (mục 5.1), tám con số đo mỗi tuần kèm ngưỡng của đội (mục 11). Đưa cho một đồng nghiệp đọc trong 15 phút và hỏi họ còn thiếu gì.

## 14. Tổng kết

- **Biết lệnh chưa phải là có quy trình.** Tài liệu 8 chặng của kit cho thứ tự lệnh; quy trình thêm nền móng, cổng và người quyết, nhịp, và cách phản ứng khi có thay đổi.
- **Bốn lớp, bốn tần suất:** nền dựng một lần; dòng chảy chạy cho mỗi module; nhịp theo ngày, tuần, đợt; vòng thay đổi khi có tín hiệu. Làm việc của lớp này theo nhịp của lớp khác là nguồn gốc của phần lớn rắc rối.
- **Ngày đầu tiên là ngày dựng nền:** git, kit, `.env`, Playwright MCP phạm vi dự án, thông tin môi trường và năng lực QA, RULE dự án, `memories/` — đúng thứ tự, nghiệm thu bằng một phiên mới.
- **Giữa hai chặng luôn có một cổng và một người mở cổng.** Năm chỗ AI không được quyết: ranh giới hệ thống, câu trả lời cho điểm mờ, duyệt plan và tiêu chí exit, FAIL do ứng dụng hay do TC, và release.
- **Một dự án lành mạnh có nhiều tốc độ:** `LOGIN` chờ retest, `CUST` sắp chạy, `PRJ` đứng trước cổng sẵn sàng — cả ba đều đúng, và ai nhìn vào cũng biết vì sao.
- **Plan là cam kết, chỉ mục là hiện trạng, báo cáo tiến độ là cầu nối.** Đừng sửa plan cho khớp hiện trạng; chỉ cập nhật khi phạm vi hoặc lịch đổi, bằng phiếu cấu hình.
- **Thay đổi có tín hiệu riêng:** requirement đổi đi chuỗi delta, dev fix đi retest, module sót đi khám phá mode ADD. Không bao giờ "sinh lại cho chắc".
- **Làm việc nhóm:** mỗi module một người tại một thời điểm, ba file chỉ mục gộp tay giữ đủ dòng, quyết định PO ghi một chỗ, `memories/` được commit.
- **Đo tám con số mỗi tuần** — đọc mục ⬛ trước mọi tỷ lệ phần trăm, và theo dõi nợ kiểm thử để TC mới không nằm quên tới ngày release.
- **Khoá học khép lại ở đây.** Việc tiếp theo là áp quy trình này vào dự án thật của bạn, bắt đầu từ bài tập 4. Bộ TC đã review là đầu vào của flow Automation — nếu đội bạn muốn tự động hoá phần regression, [AI\_FULL\_FLOW\_AUTOMATION.md](https://github.com/anhtester/claude-testing-skills/blob/main/AI_FULL_FLOW_AUTOMATION.md) là điểm nối, và khoá **AI cho Test Automation** của Anh Tester dạy trọn phần đó.