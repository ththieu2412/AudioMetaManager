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
├── docs/                                 # Thư mục chứa tài liệu tham khảo
├── report/                               # Thư mục chứa bài báo cáo viết bằng LaTeX
├── samples/                              # Thư mục chứa các tệp metadata audio đầu vào
├── src/                                  # Thư mục chứa mã nguồn chính
│   ├── evaluation/                       # Thư mục chứa các code đánh giá kết quả
│   |   ├── evaluate_accuracy.py          # Tệp kiểm tra độ chính xác khi trích xuất dữ liệu
│   |   ├── evaluate_query.py             # Tệp đánh giá hiệu suất truy vấn trong cơ sở dữ liệu
│   |   ├── evaluation_result.csv         # Kết quả đánh giá độ chính xác khi trích xuất dữ liệu
│   |   ├── ground_truth.py               # Tập dữ liệu metadata thực tế dùng để kiểm tra tính chính xác
│   ├── templates
│   ├── app.py                            # Tệp chính để chạy giao diện chương trình chương trình
│   ├── create_db.py                      # Tạo database lưu metadata
│   ├── database_util.py                  # Hỗ trợ tương tác cơ sở dữ liệu
│   ├── database.py                       # Định nghĩa cấu trúc cơ sở dữ liệu
│   ├── extractor.py                      # Trích xuất metadata từ audio
├── requirements.txt                      # Danh sách thư viện cần cài đặt
└── README.md                             # Tài liệu mô tả dự án
```

## 🛠️ Hướng dẫn cài đặt

### 1. Tải mã nguồn:

```bash
git clone https://github.com/ththieu2412/AudioMetaManager.git
cd AudioMetaManager
```

### 2. Cài đặt các thư viện cần thiết:

```bash
pip install -requirements.txt
```

## 🧪 Ví dụ chạy chương trình

### 🎧 Đầu vào (Input)

Các tệp âm thanh cần được trích xuất metadata, đặt trong thư mục samples/.

Ví dụ tệp đầu vào:

```bash
samples/.flac/sample1.flac
samples/.mp3/sample2.mp3
samples/.ogg/sample3.ogg
```

### 📤 Đầu ra (Output)

Một tệp cơ sở dữ liệu audio_metadata.db được tạo tự động trong thư mục src/.

Cơ sở dữ liệu lưu trữ metadata được trích xuất từ các tệp âm thanh, bao gồm các thông tin sau:

| Thông tin   | Mô tả                         |
| ----------- | ----------------------------- |
| `title`     | Tên bài hát                   |
| `artist`    | Nghệ sĩ                       |
| `album`     | Tên album                     |
| `genre`     | Thể loại âm nhạc              |
| `duration`  | Thời lượng bài hát (giây)     |
| `file_path` | Đường dẫn gốc của tệp đầu vào |

## 🚀 Hướng dẫn chạy chương trình

**⚠️ Lưu ý: Các tệp .py trong thư mục src/ có sử dụng đường dẫn tương đối, vì vậy phải di chuyển vào thư mục src trước khi chạy để đảm bảo chương trình hoạt động đúng.**

### 1. Tạo database và trích xuất metadata lưu vào database:

```bash
cd src
python create_db.py
```

### 2. Chạy giao diện web:

```bash
cd src
python app.py
```

Sau khi chạy, giao diện sẽ được phục vụ tại địa chỉ:

```bash
http://127.0.0.1:5000
```

## 📊 Đánh giá (Evaluation)

Các chức năng đánh giá nằm trong thư mục src/evaluation/.
**⚠️ Cần chuyển thư mục làm việc vào src/evaluation trước khi chạy, vì các script sử dụng đường dẫn tương đối.**

### 🔍 1. Kiểm tra độ chính xác khi trích xuất metadata

```bash
cd src/evaluation
python evaluate_accuracy.py

```

| 📌 Tệp này sẽ so sánh metadata trích xuất được với dữ liệu thực tế trong ground_truth.py và xuất kết quả ra evaluation_result.csv.

### ⚡ 2. Đánh giá hiệu suất truy vấn

```bash
cd src/evaluation
python evaluate_query.py
```

| 📌 Tệp này đo thời gian thực thi các truy vấn thường dùng trên database metadata đã tạo.

## 📚 Tài liệu tham khảo

Thư viện Mutagen – xử lý metadata file âm thanh.

Tài liệu chính thức SQLite Python: sqlite3 module

## 📜 Giấy phép

Dự án được phát triển với mục đích học tập, nghiên cứu và phục vụ đồ án môn học tại Học viện Công nghệ Bưu chính Viễn thông.
