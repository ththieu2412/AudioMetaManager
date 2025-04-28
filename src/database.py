import sqlite3

def connect_db():
    return sqlite3.connect('audio_metadata.db')

def create_tables():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                artist_id INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists(id)
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist_id INTEGER,
                album_id INTEGER,
                genre TEXT,
                duration INTEGER,
                file_path TEXT NOT NULL,
                FOREIGN KEY (artist_id) REFERENCES artists(id),
                FOREIGN KEY (album_id) REFERENCES albums(id)
            );
        ''')
        conn.commit()

def insert_metadata(title, artist, album, genre, duration, file_path):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            
            # Kiểm tra xem artist đã tồn tại chưa
            cursor.execute('SELECT id FROM artists WHERE name = ?', (artist,))
            artist_row = cursor.fetchone()
            if artist_row:
                artist_id = artist_row[0]
            else:
                cursor.execute('INSERT INTO artists (name) VALUES (?)', (artist,))
                artist_id = cursor.lastrowid

            # Kiểm tra xem album đã tồn tại chưa
            cursor.execute('SELECT id FROM albums WHERE name = ? AND artist_id = ?', (album, artist_id))
            album_row = cursor.fetchone()
            if album_row:
                album_id = album_row[0]
            else:
                cursor.execute('INSERT INTO albums (name, artist_id) VALUES (?, ?)', (album, artist_id))
                album_id = cursor.lastrowid

            # Chèn track
            cursor.execute('''
                INSERT INTO tracks (title, artist_id, album_id, genre, duration, file_path)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, artist_id, album_id, genre, duration, file_path))

            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def update_metadata(track_id, new_title, new_artist, new_album, new_genre):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            
            # Lấy artist_id và album_id từ track
            cursor.execute('SELECT artist_id, album_id FROM tracks WHERE id = ?', (track_id,))
            track = cursor.fetchone()
            if not track:
                print(f"Track with ID {track_id} not found.")
                return
            
            artist_id, album_id = track

            # Cập nhật track
            cursor.execute('UPDATE tracks SET title = ?, genre = ? WHERE id = ?', 
                         (new_title, new_genre, track_id))
            
            # Cập nhật artist
            cursor.execute('UPDATE artists SET name = ? WHERE id = ?', (new_artist, artist_id))
            
            # Cập nhật album
            cursor.execute('UPDATE albums SET name = ? WHERE id = ?', (new_album, album_id))

            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")