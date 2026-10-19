# YouTube Notes Maker 🎥📝

A Python project that aims to turn YouTube videos into clear, structured notes using AI.

The project currently extracts YouTube video IDs, fetches video transcripts, and combines transcript snippets into readable text. The next goal is to use AI to generate useful notes automatically.

## 🚀 Features

- Accepts a YouTube video URL as user input.
- Validates supported YouTube URL formats.
- Extracts the video ID from standard YouTube and shortened YouTube URLs.
- Fetches video transcripts using the `youtube-transcript-api` library.
- Extracts and combines transcript snippets into a single text string.

## 🛠️ Tech Stack

- **Python** — core programming language.
- **youtube-transcript-api** — retrieves available YouTube transcripts.

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YT_notes_maker
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Install dependencies

```bash
python3 -m pip install youtube-transcript-api
```

### 3. Run the project

```bash
python3 main.py
```

Enter a supported YouTube video URL when prompted.

## 🗺️ Roadmap

- [x] Accept and validate YouTube URLs.
- [x] Extract YouTube video IDs.
- [x] Fetch video transcripts.
- [x] Combine transcript snippets into a single text string.
- [ ] Generate structured notes using an AI API.
- [ ] Save generated notes to a local file.
- [ ] Improve error handling for unavailable transcripts and invalid videos.
- [ ] Add support for longer transcripts and more YouTube URL formats.

## 📌 Project Status

**Work in progress.**

This project is being developed incrementally to practise Python, API integration, text processing, and AI application development.