# AudioMetaManager

## 👨‍🎓 Thông tin sinh viên thực hiện

- **Họ và tên:** Trần Huỳnh Trung Hiếu
- **MSSV:** N21DCCN122
- **Lớp:** D21CQCNHT01-N
- **Khoa:** Công nghệ thông tin 2
- **Trường:** Học viện Công nghệ Bưu chính Viễn thông cơ sở thành phố Hồ Chí Minh (PTIT)
- **Email liên hệ:** n21dccn122@student.ptithcm.edu.vn

## 📌 Tên đề tài

**Trích xuất và quản lý metadata âm thanh bằng Python cho hệ cơ sở dữ liệu đa phương tiện**

## 📝 Mô tả chi tiết bài làm

Dự án **AudioMetaManager** nhằm xây dựng một hệ thống đơn giản để trích xuất và quản lý siêu dữ liệu (metadata) từ các tệp âm thanh định dạng `.mp3`, `.flac` và `.ogg`. Hệ thống hỗ trợ:
- Đọc thông tin tiêu đề, nghệ sĩ, album, thể loại,... từ tệp âm thanh.
- Lưu trữ dữ liệu vào cơ sở dữ liệu SQLite để truy xuất, phân tích hoặc tích hợp với hệ cơ sở dữ liệu đa phương tiện.
- Cấu trúc mã nguồn rõ ràng, dễ bảo trì và mở rộng.
- Hỗ trợ chạy chương trình theo folder chứa nhiều tệp âm thanh.

### Các thư viện sử dụng:
- `mutagen`: đọc metadata từ file âm thanh.
- `sqlite3`: lưu trữ và truy xuất dữ liệu trong cơ sở dữ liệu nội bộ.
- `os`: duyệt tệp và thư mục.

## 📁 Cấu trúc thư mục

```bash
AudioMetaManager/
├── docs/                   # Thư mục chứa tài liệu tham khảo
├── report/                 # Thư mục chứa bài báo cáo viết bằng LaTeX
├── samples/                # Thư mục chứa các tệp metadata audio đầu vào
├── src/                    # Thư mục chứa mã nguồn chính
│   ├── main.py             # Tệp chính để chạy chương trình
│   └── metadata_extractor.py  # Module xử lý việc đọc và ghi metadata
├── requirements.txt        # Danh sách thư viện cần cài đặt
└── README.md               # Tài liệu mô tả dự án (file hiện tại)


## 🛠️ Hướng dẫn cài đặt

### 1. Tải mã nguồn:
```bash
git clone https://github.com/yourusername/AudioMetaManager.git
cd AudioMetaManager
```

### 2. Cài đặt các thư viện cần thiết:
```bash
pip install -requirements.txt
```

## 🚀 Hướng dẫn chạy chương trình

Chạy chương trình với:

```bash
python src/app.py
```

## 📚 Tài liệu tham khảo

Thư viện Mutagen – xử lý metadata file âm thanh.

Tài liệu giảng dạy môn "Hệ cơ sở dữ liệu đa phương tiện" – PTIT.

Tài liệu chính thức SQLite Python: sqlite3 module

## 📜 Giấy phép

Dự án được phát triển với mục đích học tập, nghiên cứu và phục vụ đồ án môn học tại Học viện Công nghệ Bưu chính Viễn thông.
