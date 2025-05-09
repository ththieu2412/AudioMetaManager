import os
import random
from pydub import AudioSegment

def convert_audio(file_path, output_format, output_folder):
    name, _ = os.path.splitext(os.path.basename(file_path))
    output_path = os.path.join(output_folder, f"{name}.{output_format}")
    audio = AudioSegment.from_file(file_path)
    audio.export(output_path, format=output_format)
    return output_path

def convert_dataset_randomly(folder_path):
    audio_extensions = ('.mp3', '.wav', '.flac', '.ogg')
    target_formats = ['mp3', 'wav', 'flac', 'ogg']
    
    # Tạo thư mục đầu ra nếu chưa có
    output_folder = os.path.join(folder_path, "converted")
    os.makedirs(output_folder, exist_ok=True)

    # Lọc danh sách file âm thanh
    audio_files = [f for f in os.listdir(folder_path) if f.lower().endswith(audio_extensions)]
    random.shuffle(audio_files)  # Trộn ngẫu nhiên

    num_files = len(audio_files)
    num_per_format = num_files // len(target_formats)

    # Chia file ra theo format
    format_assignments = []
    for fmt in target_formats:
        format_assignments.extend([fmt] * num_per_format)
    # Gán phần dư cho các format đầu tiên
    remainder = num_files % len(target_formats)
    format_assignments.extend(target_formats[:remainder])
    random.shuffle(format_assignments)  # Trộn lần nữa để không theo thứ tự

    for filename, fmt in zip(audio_files, format_assignments):
        input_path = os.path.join(folder_path, filename)
        try:
            convert_audio(input_path, fmt, output_folder)
        except Exception as e:
            print(f"Lỗi khi xử lý '{filename}': {e}")

    print(f"Hoàn tất chuyển đổi. Các file được lưu tại: {output_folder}")

# Ví dụ sử dụng
folder = '../samples'
convert_dataset_randomly(folder)
