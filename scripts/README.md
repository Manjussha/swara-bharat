# Swara-Bharat Smart Scraper

Intelligent YouTube content discovery and downloading using Qwen AI model.

## Features

- 🤖 **AI-Powered Search**: Uses Qwen model to generate smart search queries
- 📥 **Auto Download**: Downloads YouTube audio in high quality (320kbps MP3)
- ☁️ **HuggingFace Integration**: Automatically uploads to HuggingFace datasets
- 📊 **Multi-Category**: Supports news, comedy, educational, motivational content
- 🔄 **Automated**: Can run on schedule via cron
- 📝 **Detailed Logging**: Tracks all operations

## Setup

### On Raspberry Pi:

```bash
# Clone or navigate to project
cd ~/swara-bharat

# Run setup script
chmod +x scripts/setup_pi.sh
./scripts/setup_pi.sh

# Edit environment variables
nano scripts/.env
# Add your HuggingFace token: HF_TOKEN=hf_xxx

# Activate virtual environment
source venv/bin/activate
```

### On Windows/Mac:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Install ffmpeg separately:
# Windows: https://ffmpeg.org/download.html
# Mac: brew install ffmpeg

# Setup environment
cp scripts/.env.example scripts/.env
# Edit .env and add your HF_TOKEN
```

## Usage

### Manual Run:

```bash
# Activate environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Run scraper
python scripts/smart_scraper.py
```

### Automated (Raspberry Pi):

```bash
# Edit crontab
crontab -e

# Add this line to run daily at 2 AM:
0 2 * * * cd ~/swara-bharat && venv/bin/python3 scripts/smart_scraper.py >> logs/cron.log 2>&1
```

## Configuration

Edit `scripts/config.json` to customize:

```json
{
  "language": "kannada",           // Target language
  "categories": ["news", "comedy"], // Content categories
  "downloads_per_category": 5,     // Videos per category
  "audio_quality": "320",          // MP3 bitrate
  "hf_dataset_name": "your-username/dataset-name"
}
```

## How It Works

1. **Query Generation**: Qwen AI generates smart YouTube search queries
2. **Search**: Searches YouTube for relevant videos
3. **Filter**: Filters by duration, quality, upload date
4. **Download**: Downloads audio using yt-dlp
5. **Upload**: Uploads to HuggingFace dataset
6. **Log**: Saves metadata and logs

## Directory Structure

```
swara-bharat/
├── scripts/
│   ├── smart_scraper.py      # Main script
│   ├── config.json           # Configuration
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables
├── data/
│   └── raw/
│       ├── news/            # Downloaded news content
│       ├── comedy/          # Downloaded comedy content
│       └── ...
└── logs/
    └── scraper.log          # Activity logs
```

## Requirements

- Python 3.8+
- ffmpeg (for audio extraction)
- HuggingFace account and token
- Internet connection

## Troubleshooting

**yt-dlp errors:**
```bash
# Update yt-dlp
pip install --upgrade yt-dlp
```

**HuggingFace upload fails:**
```bash
# Check token in .env
# Make sure dataset name format: username/dataset-name
# Ensure dataset is created on HuggingFace
```

**Out of storage:**
```bash
# Clean old downloads
rm -rf data/raw/*
# Files are already on HuggingFace
```

## License

Apache 2.0 - See main project LICENSE
