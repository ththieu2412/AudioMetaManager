from mutagen.mp3 import MP3
from mutagen.id3 import ID3

def extract_metadata(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        
        # Lấy giá trị của các thẻ ID3
        title = audio.get('TIT2', None)
        artist = audio.get('TPE1', None)
        album = audio.get('TALB', None)
        genre = audio.get('TCON', None)
        
        # Chuyển đổi giá trị thành chuỗi, xử lý trường hợp danh sách
        title = title.text[0] if title and title.text else 'Unknown'
        artist = artist.text[0] if artist and artist.text else 'Unknown'
        album = album.text[0] if album and album.text else 'Unknown'
        genre = genre.text[0] if genre and genre.text else 'Unknown'
        
        # Lấy thời lượng bài hát (tính bằng giây)
        duration = int(audio.info.length)
        
        return title, artist, album, genre, duration
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return None