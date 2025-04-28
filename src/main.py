# main.py
import os
from extractor import extract_metadata
from database import connect_db, create_table, insert_metadata

def main():
    samples_folder = "samples"
    audio_files = [f for f in os.listdir(samples_folder) if f.lower().endswith(".mp3")]

    if not audio_files:
        print("No audio files found in 'samples/' folder.")
        return

    conn = connect_db()
    create_table(conn)

    for file_name in audio_files:
        file_path = os.path.join(samples_folder, file_name)
        metadata = extract_metadata(file_path)
        
        if metadata:
            insert_metadata(conn, file_name, metadata)
            print(f"Inserted metadata for {file_name}")
    
    conn.close()
    print("Done extracting and saving metadata.")

if __name__ == "__main__":
    main()
