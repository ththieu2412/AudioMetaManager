from pydub import AudioSegment
import os

def convert_audio(input_path, output_format):
    audio = AudioSegment.from_file(input_path)
    file_name, _ = os.path.splitext(input_path)
    output_path = f"{file_name}.{output_format.lower()}"
    audio.export(output_path, format=output_format.lower())
    print(f"Đã chuyển '{input_path}' → '{output_path}'")

# Ví dụ sử dụng
convert_audio("../samples/test1.mp3", "wav")
convert_audio("../samples/test2.mp3", "flac")
convert_audio("../samples/test3.mp3", "ogg")
