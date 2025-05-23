import sys
import os

import time
from database import init_db
from database_utils import insert_audio_file_with_metadata
from extractor import extract_metadata


# Khởi tạo cơ sở dữ liệu
db_path = "audio_metadata.db"
init_db(db_path)

# Đường dẫn thư mục gốc
root_folder = r"..\samples"
valid_extensions = (".mp3", ".flac", ".ogg")

# Biến đếm
total_files = 0
total_duration = 0

# Đo tổng thời gian
start_all = time.time()

for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(valid_extensions):
            file_path = os.path.join(dirpath, filename)
            print(f"\nĐang xử lý: {file_path}")
            start_time = time.time()

            metadata = extract_metadata(file_path)
            if metadata:
                insert_audio_file_with_metadata(metadata, db_path, file_path)
                end_time = time.time()
                processing_time = end_time - start_time
                print(f"Thời gian xử lý: {processing_time:.3f} giây")
                total_files += 1
                total_duration += processing_time
            else:
                print("Không thể trích xuất metadata.")

end_all = time.time()
overall_time = end_all - start_all
average_time = total_duration / total_files if total_files else 0

print(f"Số file xử lý: {total_files}")
print(f"Tổng thời gian xử lý: {overall_time:.2f} giây")
print(f"Thời gian trung bình mỗi file: {average_time:.3f} giây")
