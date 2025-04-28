import os
from extractor import extract_metadata
from database import create_tables, insert_metadata

def main():
    # Tính đường dẫn thư mục samples dựa trên vị trí của main.py
    samples_folder = os.path.join(os.path.dirname(__file__), "..", "samples")
    samples_folder = os.path.abspath(samples_folder)

    try:
        audio_files = [f for f in os.listdir(samples_folder) if f.lower().endswith(".mp3")]
    except FileNotFoundError:
        print(f"Folder 'samples/' not found at {samples_folder}.")
        return

    if not audio_files:
        print("No audio files found in 'samples/' folder.")
        return

    create_tables()

    for file_name in audio_files:
        file_path = os.path.join(samples_folder, file_name)
        metadata = extract_metadata(file_path)
        
        if metadata:
            title, artist, album, genre, duration = metadata
            insert_metadata(title, artist, album, genre, duration, file_path)
            print(f"Inserted metadata for {file_name}")
    
    print("Done extracting and saving metadata.")

if __name__ == "__main__":
    main()