import sqlite3

def init_db(db_path='audio_metadata.db'):
    """
    Initialize the SQLite database and create the table if it doesn't exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Artist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Genre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Album (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            release_year TEXT
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS AudioFile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL UNIQUE,
            title TEXT,
            album_id INTEGER,
            genre_id INTEGER,
            duration REAL,
            FOREIGN KEY (album_id) REFERENCES Album(id),
            FOREIGN KEY (genre_id) REFERENCES Genre(id)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS AudioArtist (
            audio_file_id INTEGER,
            artist_id INTEGER,
            PRIMARY KEY (audio_file_id, artist_id),
            FOREIGN KEY (audio_file_id) REFERENCES AudioFile(id),
            FOREIGN KEY (artist_id) REFERENCES Artist(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized and tables created if they didn't exist.")

