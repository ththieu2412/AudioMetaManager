import sqlite3

def get_or_create_id(cursor, table, name, extra_fields=None):
    cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        if extra_fields:
            fields = ', '.join(['name'] + list(extra_fields.keys()))
            placeholders = ', '.join(['?'] * (1 + len(extra_fields)))
            values = [name] + list(extra_fields.values())
            cursor.execute(f"INSERT OR IGNORE INTO {table} ({fields}) VALUES ({placeholders})", values)
        else:
            cursor.execute(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (name,))
        return cursor.lastrowid

def insert_audio_file_with_metadata(metadata, database, file_path):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        # Lấy hoặc tạo album
        album_name = metadata.get("album") or "Unknown"
        release_year = metadata.get("release_year") or "Unknown"
        album_id = get_or_create_id(cursor, "Album", album_name, {"release_year": release_year})
        print(f"Album ID: {album_id}")

        # Lấy hoặc tạo thể loại
        genre_name = metadata.get("genre") or "Unknown"
        genre_id = get_or_create_id(cursor, "Genre", genre_name)

        # Thêm file âm thanh
        title = metadata.get("title") or "Unknown"
        duration = metadata.get("duration") or 0
        cursor.execute('''
            INSERT INTO AudioFile (file_path, title, duration, album_id, genre_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (file_path, title, duration, album_id, genre_id))
        audio_file_id = cursor.lastrowid

        # Thêm nghệ sĩ
        artists = metadata.get("artist", "Unknown").split(",")
        artist_ids = []
        for artist_name in artists:
            artist_id = get_or_create_id(cursor, "Artist", artist_name.strip())
            artist_ids.append(artist_id)

        # Thêm liên kết nghệ sĩ
        cursor.executemany('''
            INSERT OR IGNORE INTO AudioArtist (audio_file_id, artist_id)
            VALUES (?, ?)
        ''', [(audio_file_id, artist_id) for artist_id in artist_ids])

        conn.commit()
        print(f"✅ Đã thêm bài hát '{title}' vào cơ sở dữ liệu.")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"❌ Đã xảy ra lỗi: {e}")
    
    finally:
        conn.close()

