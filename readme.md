# YouTube Notes Maker 🎥📝

A Python project that converts YouTube videos into structured notes using AI. It extracts video transcripts, generates notes with Google's Gemini API, and saves the results as Markdown files.

## 🚀 Features

- Accepts a YouTube video URL as input.
- Validates supported YouTube URL formats.
- Extracts the video ID from standard and shortened YouTube URLs.
- Fetches available video transcripts using `youtube-transcript-api`.
- Combines transcript snippets into a single text string.
- Generates structured notes using Google's Gemini API.
- Saves generated notes to a Markdown file (`notes.md`).

## 🛠️ Tech Stack

- **Python** — core programming language.
- **youtube-transcript-api** — retrieves YouTube transcripts.
- **Google Gen AI SDK** (`google-genai`) — connects to Google's Gemini API.
- **python-dotenv** — loads API keys from environment variables.
- **Markdown** — stores generated notes in a readable format.

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YT_notes_maker
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Install dependencies

```bash
python3 -m pip install youtube-transcript-api google-genai python-dotenv
```

### 3. Configure your Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key_here
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your `.env` file or expose your API key. Add `.env` to `.gitignore`.

### 4. Run the project

```bash
python3 main.py
```

Enter a supported YouTube video URL when prompted. The program fetches the available transcript, generates notes with Gemini, and saves them to `notes.md`.

## 🗺️ Roadmap

- [x] Accept and validate YouTube URLs.
- [x] Extract YouTube video IDs.
- [x] Fetch available video transcripts.
- [x] Combine transcript snippets into one string.
- [x] Generate structured notes using Gemini.
- [x] Save generated notes to a Markdown file.
- [ ] Create a dedicated directory for generated notes.
- [ ] Save each video's notes to a separate file.
- [ ] Improve error handling for unavailable transcripts and API failures.
- [ ] Support additional YouTube URL formats.
- [ ] Improve prompt quality and transcript accuracy.

## 📌 Project Status

**Work in progress.**

This project is being developed incrementally to practise Python, API integration, text processing, and AI application development.
