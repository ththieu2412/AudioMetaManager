import os
import csv

def bytes_to_mb(size_bytes):
    return round(size_bytes / (1024 * 1024), 2)

folders = {
    'mp3': 'samples\\.mp3',
    'ogg': 'samples\\.ogg',
    'flac': 'samples\\.flac'
}

# Mảng lưu dữ liệu để ghi vào CSV
data_rows = []

for fmt, folder_path in folders.items():
    count_files = 0
    total_size = 0
    full_path = os.path.join(os.getcwd(), folder_path)
    if not os.path.exists(full_path):
        print(f"Folder {full_path} không tồn tại!")
        continue
    for filename in os.listdir(full_path):
        if filename.lower().endswith(f'.{fmt}'):
            count_files += 1
            total_size += os.path.getsize(os.path.join(full_path, filename))
    
    if count_files > 0:
        avg_size = total_size / count_files
    else:
        avg_size = 0
    
    print(f"{fmt.upper()}: {count_files} tệp, tổng kích thước: {bytes_to_mb(total_size)} MB, kích thước trung bình: {bytes_to_mb(avg_size)} MB")

    # Thêm dữ liệu vào mảng
    data_rows.append([fmt.upper(), count_files, bytes_to_mb(total_size), bytes_to_mb(avg_size)])

# Ghi dữ liệu vào file CSV
current_folder = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(current_folder, 'audio_files_summary.csv')
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Ghi header
    writer.writerow(['Định dạng', 'Số lượng tệp', 'Tổng kích thước (MB)', 'Kích thước trung bình (MB)'])
    # Ghi các dòng dữ liệu
    writer.writerows(data_rows)

print(f"Đã lưu kết quả vào file {csv_file}")
