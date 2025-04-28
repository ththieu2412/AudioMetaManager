# extractor.py
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON

def extract_metadata(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        metadata = {
            'title': audio.tags.get('TIT2', 'Unknown Title').text[0] if audio.tags.get('TIT2') else 'Unknown Title',
            'artist': audio.tags.get('TPE1', 'Unknown Artist').text[0] if audio.tags.get('TPE1') else 'Unknown Artist',
            'album': audio.tags.get('TALB', 'Unknown Album').text[0] if audio.tags.get('TALB') else 'Unknown Album',
            'genre': audio.tags.get('TCON', 'Unknown Genre').text[0] if audio.tags.get('TCON') else 'Unknown Genre',
            'length': round(audio.info.length, 2)  # seconds
        }
        return metadata
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return None
