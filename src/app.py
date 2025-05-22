from flask import Flask, render_template, send_from_directory, abort
import sqlite3
import os
from functools import lru_cache

app = Flask(__name__, static_folder="../samples", static_url_path="/samples")
DB_PATH = "audio_metadata.db"

def get_db_connection():
    """Create and return a database connection with row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@lru_cache(maxsize=1)
def get_unique_artists():
    """Cache and return sorted list of unique artist names."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM Artist ORDER BY name')
        return [row['name'] for row in cursor.fetchall()]

@app.route("/")
def index():
    """Render the main library page with audio files and artists."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # Fetch audio files with joined metadata
            cursor.execute('''
                SELECT 
                    af.id,
                    af.file_path,
                    af.title,
                    al.name AS album_name,
                    al.release_year,
                    g.name AS genre_name,
                    af.duration
                FROM AudioFile af
                LEFT JOIN Album al ON af.album_id = al.id
                LEFT JOIN Genre g ON af.genre_id = g.id
            ''')
            audio_files = cursor.fetchall()

            audio_data = []
            for row in audio_files:
                # Fetch artists for each audio file
                cursor.execute('''
                    SELECT a.name
                    FROM Artist a
                    JOIN AudioArtist aa ON a.id = aa.artist_id
                    WHERE aa.audio_file_id = ?
                ''', (row['id'],))
                artists = [artist['name'] for artist in cursor.fetchall()]
                audio_data.append({
                    'id': row['id'],
                    'file_path': row['file_path'],
                    'title': row['title'],
                    'album': row['album_name'],
                    'release_year': row['release_year'],
                    'genre': row['genre_name'],
                    'duration': row['duration'],
                    'artists': artists,
                    'artists_string': ", ".join(artists)
                })

        return render_template("index.html", audio_files=audio_data, unique_artists=get_unique_artists())
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return "Internal Server Error", 500

@app.route("/song/<int:song_id>")
def song(song_id):
    """Render the song playback page for a given song ID."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT 
                    af.id,
                    af.file_path,
                    af.title,
                    al.name AS album_name,
                    al.release_year,
                    g.name AS genre_name,
                    af.duration
                FROM AudioFile af
                LEFT JOIN Album al ON af.album_id = al.id
                LEFT JOIN Genre g ON af.genre_id = g.id
                WHERE af.id = ?
            ''', (song_id,))
            song_data = cursor.fetchone()

            if not song_data:
                abort(404)

            cursor.execute('''
                SELECT a.name
                FROM Artist a
                JOIN AudioArtist aa ON a.id = aa.artist_id
                WHERE aa.audio_file_id = ?
            ''', (song_id,))
            artists = [artist['name'] for artist in cursor.fetchall()]

            song = {
                'id': song_data['id'],
                'file_path': song_data['file_path'],
                'title': song_data['title'],
                'album': song_data['album_name'],
                'release_year': song_data['release_year'],
                'genre': song_data['genre_name'],
                'duration': song_data['duration'],
                'artists_string': ", ".join(artists)
            }

        return render_template("song.html", song=song)
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return "Internal Server Error", 500

@app.route("/samples/<path:filename>")
def serve_audio(filename):
    """Serve audio files from the samples directory."""
    try:
        return send_from_directory("../samples", filename)
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)