import os
from database import init_db
from database_utils import insert_audio_file_with_metadata
from extractor import extract_metadata

# Khởi tạo cơ sở dữ liệu
db_path = "audio_metadata.db"
init_db(db_path)

# Đường dẫn thư mục gốc
root_folder = r"..\samples"

# Các định dạng âm thanh hợp lệ
valid_extensions = (".mp3", ".flac", ".ogg")

# Duyệt tất cả các file trong thư mục và các thư mục con
for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(valid_extensions):
            file_path = os.path.join(dirpath, filename)
            print(f"\n📂 Đang xử lý: {file_path}")
            metadata = extract_metadata(file_path)
            if metadata:
                print("📄 Metadata:", metadata)
                insert_audio_file_with_metadata(metadata, db_path, file_path)
                print("✅ Đã thêm vào cơ sở dữ liệu.")
            else:
                print("❌ Không thể trích xuất metadata.")
