from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
import re

def extract_year_from_string(s):
    if not s:
        return "Unknown"
    match = re.search(r'\d{4}', s)
    if match:
        return match.group(0)
    return "Unknown"

def extract_metadata(file_path):
    try:
        if file_path.endswith(".mp3"):
            print("MP3")
            audio_file = MP3(file_path, ID3=ID3)
            # Lấy tag nếu có, else None
            title = audio_file.tags.get("TIT2")
            artist = audio_file.tags.get("TPE1")
            album = audio_file.tags.get("TALB")
            genre = audio_file.tags.get("TCON")
            release_year_tag = audio_file.tags.get("TDRC") or audio_file.tags.get("TYER")

            metadata = {
                'title': title.text[0] if title else "Unknown",
                'artist': artist.text[0] if artist else "Unknown",
                'album': album.text[0] if album else "Unknown",
                'genre': genre.text[0] if genre else "Unknown",
                'release_year': extract_year_from_string(str(release_year_tag.text[0])) if release_year_tag else "Unknown",
                'duration': audio_file.info.length
            }

        elif file_path.endswith(".flac"):
            print("FLAC")
            audio_file = FLAC(file_path)
            # Có thể năm nằm trong 'date' hoặc 'year'
            year_raw = audio_file.get("date", audio_file.get("year", ["Unknown"]))[0]
            metadata = {
                'title': audio_file.get("title", ["Unknown"])[0],
                'artist': audio_file.get("artist", ["Unknown"])[0],
                'album': audio_file.get("album", ["Unknown"])[0],
                'genre': audio_file.get("genre", ["Unknown"])[0],
                'release_year': extract_year_from_string(year_raw),
                'duration': audio_file.info.length
            }

        elif file_path.endswith(".ogg"):
            print("OGG")
            audio_file = OggVorbis(file_path)
            year_raw = audio_file.get("date", audio_file.get("year", ["Unknown"]))[0]
            metadata = {
                'title': audio_file.get("title", ["Unknown"])[0],
                'artist': audio_file.get("artist", ["Unknown"])[0],
                'album': audio_file.get("album", ["Unknown"])[0],
                'genre': audio_file.get("genre", ["Unknown"])[0],
                'release_year': extract_year_from_string(year_raw),
                'duration': audio_file.info.length
            }

        else:
            return "Unsupported file format"
        
        return metadata
    
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return None
