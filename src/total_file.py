import os

def count_audio_files(folder_path):
    audio_extensions = ('.mp3', '.wav', '.flac', '.ogg')
    count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(audio_extensions):
            count += 1
    return count

# Ví dụ sử dụng
folder = r'../samples/.ogg'  # Đường dẫn tới thư mục chứa file âm thanh
total = count_audio_files(folder)
print(f"Số lượng file âm thanh trong thư mục '{folder}': {total}")
