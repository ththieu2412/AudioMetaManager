# database.py
import sqlite3

def connect_db(db_name="metadata.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audio_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            title TEXT,
            artist TEXT,
            album TEXT,
            genre TEXT,
            length REAL
        )
    ''')
    conn.commit()

def insert_metadata(conn, filename, metadata):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO audio_metadata (filename, title, artist, album, genre, length)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (filename, metadata['title'], metadata['artist'], metadata['album'], metadata['genre'], metadata['length']))
    conn.commit()
