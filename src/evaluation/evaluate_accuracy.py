import csv
import sqlite3
import re
from pathlib import Path

def load_ground_truth(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_extracted_from_db(format_ext, conn):
    cursor = conn.cursor()
    query = '''
        SELECT af.file_path, af.title, 
               GROUP_CONCAT(a.name, ';') AS artist,  
               (SELECT name FROM Album WHERE id = af.album_id) AS album,
               (SELECT name FROM Genre WHERE id = af.genre_id) AS genre,
               af.duration
        FROM AudioFile af
        LEFT JOIN AudioArtist aa ON af.id = aa.audio_file_id
        LEFT JOIN Artist a ON aa.artist_id = a.id
        WHERE af.file_path LIKE ?
        GROUP BY af.id
    '''
    cursor.execute(query, ('%' + format_ext, ))
    rows = cursor.fetchall()

    metadata_list = []
    for row in rows:
        metadata_list.append({
            'file_name': Path(row[0]).name,
            'title': row[1] or '',
            'artist': row[2] or '',
            'album': row[3] or '',
            'genre': row[4] or '',
            'duration': str(row[5] or '')
        })
    return metadata_list

def normalize_artist_list(artist_str):
    separators_fixed = re.sub(r'[;,]', ',', artist_str)
    return set(a.strip().lower().replace('-', ' ').replace('–', ' ') for a in separators_fixed.split(',') if a.strip())

def compare_metadata(ground_truth, extracted, duration_tolerance=1):
    fields = ['title', 'artist', 'album', 'genre', 'duration']
    correct = {field: 0 for field in fields}
    total = 0

    extracted_dict = {item['file_name'].strip().lower(): item for item in extracted}

    for gt in ground_truth:
        file_name = gt['file_name'].strip().lower()
        ex = extracted_dict.get(file_name)
        if not ex:
            continue
        total += 1
        for field in fields:
            gt_val = gt.get(field, '').strip()
            ex_val = ex.get(field, '').strip()

            if field == 'duration':
                try:
                    gt_dur = float(gt_val)
                    ex_dur = float(ex_val)
                    if abs(gt_dur - ex_dur) <= duration_tolerance:
                        correct[field] += 1
                    else:
                        print(f"[{file_name}] duration: GT={gt_dur}, EX={ex_dur}")
                except:
                    print(f"[{file_name}] duration parsing error: GT={gt_val}, EX={ex_val}")
                    continue

            elif field == 'artist':
                gt_artists = normalize_artist_list(gt_val)
                ex_artists = normalize_artist_list(ex_val)
                if gt_artists == ex_artists:
                    correct[field] += 1
                else:
                    print(f"[{file_name}] artist: GT={gt_artists}, EX={ex_artists}")

            else:
                if gt_val.lower() == ex_val.lower():
                    correct[field] += 1
                else:
                    print(f"[{file_name}] not {field}: GT={gt_val}, EX={ex_val}")

    return {field: round(correct[field] / total * 100, 1) if total else 0.0 for field in fields}

if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parent
    db_path = base_dir.parent / 'audio_metadata.db'
    ground_truth_path = base_dir / 'ground_truth.csv'
    result_path = base_dir / 'evaluation_result.csv'

    formats = ['mp3', 'ogg', 'flac']
    results = []

    conn = sqlite3.connect(db_path)

    for fmt in formats:
        gt = load_ground_truth(ground_truth_path)
        ex = load_extracted_from_db(fmt, conn)
        acc = compare_metadata(gt, ex)
        acc['format'] = fmt
        results.append(acc)

    conn.close()

    with open(result_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['format', 'title', 'artist', 'album', 'genre', 'duration'])
        writer.writeheader()
        writer.writerows(results)

    print("✅ Evaluation completed. Results with duration saved in evaluation_result.csv.")
