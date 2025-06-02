# autoshort
Program that will automatically create youtube/tiktok shorts. Uses AI to track trends on the news/world in order to bring relevant content to consumers. Success rate will be shown through view counts, likes, etc.

## Requirements
- Python 3
- FFmpeg
- gTTS
- OpenAI API Key
- Google YouTube Data API credentials

## How It Works
1. Generates a script using ChatGPT.
2. Converts script to voice using gTTS.
3. Combines voice and background video using FFmpeg.
4. (Optional) Adds subtitles.
5. Uploads the video to YouTube.

## Setup
- Fill in `config.json`
- Add your `client_secret.json` for YouTube API
- Place background videos in `assets/backgrounds`
- Run `scheduler.sh` or call Python scripts manually
