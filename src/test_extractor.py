from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis 
from mutagen.id3 import ID3

def extract_metadata(file_path):
    try:
        # Kiểm tra định dạng MP3
        if file_path.endswith(".mp3"):
            print("MP3")
            audio_file = MP3(file_path, ID3=ID3)
            metadata = {
                'title': audio_file.get("TIT2", "Unknown").text[0] if "TIT2" in audio_file else "Unknown",
                'artist': audio_file.get("TPE1", "Unknown").text[0] if "TPE1" in audio_file else "Unknown",
                'album': audio_file.get("TALB", "Unknown").text[0] if "TALB" in audio_file else "Unknown",
                'genre': audio_file.get("TCON", "Unknown").text[0] if "TCON" in audio_file else "Unknown",
                'release_year': audio_file.get("TDRC", "Unknown").text[0] if "TDRC" in audio_file else "Unknown",
                'duration': audio_file.info.length
            }
        # Kiểm tra định dạng FLAC
        elif file_path.endswith(".flac"):
            print("FLAC")
            audio_file = FLAC(file_path)
            metadata = {
                'title': audio_file.get("title", ["Unknown"])[0],
                'artist': audio_file.get("artist", ["Unknown"])[0],
                'album': audio_file.get("album", ["Unknown"])[0],
                'genre': audio_file.get("genre", ["Unknown"])[0],
                'release_year': audio_file.get("date", ["Unknown"])[0],
                'duration': audio_file.info.length
            }
        # Kiểm tra định dạng OGG
        elif file_path.endswith(".ogg"):
            print("OGG")
            audio_file = OggVorbis(file_path)
            metadata = {
                'title': audio_file.get("title", ["Unknown"])[0],
                'artist': audio_file.get("artist", ["Unknown"])[0],
                'album': audio_file.get("album", ["Unknown"])[0],
                'genre': audio_file.get("genre", ["Unknown"])[0],
                'release_year': audio_file.get("date", ["Unknown"])[0],
                'duration': audio_file.info.length
            }
        else:
            return "Unsupported file format"
        
        return metadata

    except Exception as e:
        return f"Error extracting metadata: {e}"

# Ví dụ sử dụng
file_path = r"D:\Student\Senior_Student_2\multimedia\AudioMetaManager\samples\VuaHanVuaYeu-TrungTu-15121915.flac"# Đường dẫn tới tệp âm thanh
metadata = extract_metadata(file_path)
print(f"Metadata for {file_path}:", metadata)

# In ra metadata
if isinstance(metadata, dict):
    for key, value in metadata.items():
        print(f"{key}: {value}")
else:
    print(metadata)
