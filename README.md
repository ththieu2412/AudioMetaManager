# AudioMetaManager

A Python project for extracting and managing audio metadata, designed for multimedia database systems.

## 🎯 Features

- Extract metadata (title, artist, album, genre, etc.) from audio files (MP3)
- Store metadata into a local SQLite database
- Simple and clean project structure
- Easy to extend for multimedia database applications

## 🛠️ Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/AudioMetaManager.git
cd AudioMetaManager
```

Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run

Run the main program:

```bash
python src/main.py
```

You can customize the input folder in main.py to process your own audio files.

## 📦 Project Structure

AudioMetaManager/
│
├── src/
│   ├── extractor.py     # Metadata extraction module
│   ├── database.py      # Database management module
│   └── main.py          # Entry point
│
├── samples/             # Sample audio files
│
├── docs/                # Project documentation
│
├── requirements.txt     # Required Python packages
├── .gitignore           # Files/folders to ignore by Git
└── README.md            # Project overview

## 📚 References

This project was built based on academic papers and real-world Python libraries related to audio metadata extraction and multimedia database systems.

## 📜 License

This project is licensed for educational use.



