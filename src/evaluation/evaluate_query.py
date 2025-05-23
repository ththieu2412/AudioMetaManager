import sqlite3
import time
import os

# Xác định đường dẫn tuyệt đối tới file .db
current_dir = os.path.dirname(os.path.abspath(__file__))

# Thư mục cha (src/)
parent_dir = os.path.dirname(current_dir)

# Đường dẫn đến file .db
db_path = os.path.join(parent_dir, 'audio_metadata.db')

# Kiểm tra file DB có tồn tại không
if not os.path.exists(db_path):
    raise FileNotFoundError(f"Không tìm thấy file cơ sở dữ liệu tại: {db_path}")

print(f"Đang sử dụng cơ sở dữ liệu tại: {db_path}")

def measure_query_time(db_path, query, params=()):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    start = time.time()
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Lỗi khi thực hiện truy vấn: {e}")
        results = []
    end = time.time()
    conn.close()
    return end - start, results

# Danh sách truy vấn cần đo thời gian
queries = {
    "Tìm kiếm bài hát theo nghệ sĩ (ví dụ: BLACKPINK)": ("""
        SELECT AudioFile.*
        FROM AudioFile
        JOIN AudioArtist ON AudioFile.id = AudioArtist.audio_file_id
        JOIN Artist ON AudioArtist.artist_id = Artist.id
        WHERE Artist.name LIKE ?
    """, ('%BLACKPINk%',)),

    "Lọc bài hát theo tên album ('NhacCuaTui.com')": ("""
        SELECT AudioFile.*
        FROM AudioFile
        JOIN Album ON AudioFile.album_id = Album.id
        WHERE Album.name = ?
    """, ('NhacCuaTui.com',)),

    "Đếm số lượng bài hát theo thể loại": ("""
        SELECT Genre.name, COUNT(AudioFile.id)
        FROM AudioFile
        JOIN Genre ON AudioFile.genre_id = Genre.id
        GROUP BY Genre.name
    """, ()),
}

for description, (query, params) in queries.items():
    duration, results = measure_query_time(db_path, query, params)
    print(f"{description}:")
    print(f"Thời gian truy vấn: {duration:.3f} giây")
    print(f"Số dòng kết quả: {len(results)}\n")
