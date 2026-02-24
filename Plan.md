# Swara-Bharat: Complete Implementation Plan
## Open-Source Emotional Voice AI Platform for Indian Languages

**Vision:** Build India's first open-source alternative to Sarvam AI with emotional voice capabilities

**Creator:** Manju (@manjussha)  
**Timeline:** 12 months to full platform  
**Investment:** ₹10,000-15,000 first year  
**Daily Effort:** 1-2 hours  

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technical Stack](#technical-stack)
3. [Phase-wise Roadmap](#phase-wise-roadmap)
4. [Setup Guide](#setup-guide)
5. [Development Workflow](#development-workflow)
6. [Data Collection Strategy](#data-collection-strategy)
7. [Model Training](#model-training)
8. [Dashboard Development](#dashboard-development)
9. [API & Integration](#api--integration)
10. [Community & Growth](#community--growth)
11. [Cost Breakdown](#cost-breakdown)
12. [Success Metrics](#success-metrics)

---

## Project Overview

### Mission
Create free, open-source emotional voice AI for Indian languages that anyone can use, contribute to, and build upon.

### What Makes Swara-Bharat Unique

**vs Sarvam AI:**
- ✅ Completely free and open-source
- ✅ Emotional voice expressions (comedy, empathy, sarcasm)
- ✅ Deep dialect support (Bangalore, Mysore, Dharwad Kannada, etc.)
- ✅ Community-driven improvements
- ✅ Transparent development

**vs AI4Bharat:**
- ✅ Focus on emotional, natural-sounding voices
- ✅ Modern architecture (XTTS, latest models)
- ✅ Better voice quality
- ✅ User-friendly platform (not just research)

**vs ElevenLabs:**
- ✅ Indian language native support
- ✅ Dialect variations
- ✅ Free for all
- ✅ Cultural context awareness

### Core Capabilities

**Phase 1 (v0.1 - Months 1-3):**
- Text → Emotional Voice (TTS)
- Kannada language
- 5 dialects (Bangalore, Mysore, Dharwad, Coastal, North Karnataka)
- 5 emotions (Neutral, Happy, Empathetic, Sarcastic, Excited)

**Phase 2 (v0.5 - Months 4-6):**
- Voice → Text (STT)
- Text ↔ Voice workflow
- 3 languages (Kannada, Tamil, Hindi)
- Script management

**Phase 3 (v0.8 - Months 7-9):**
- Conversational AI (LLM integration)
- Voice → Understanding → Voice response
- Multi-turn conversations
- 5 languages

**Phase 4 (v1.0 - Months 10-12):**
- Complete platform (Sarvam alternative)
- API service
- Business dashboard
- 7+ languages
- Voice cloning

---

## Technical Stack

### Hardware

**Development:**
- MacBook Pro 2019 (programming, testing)
- Raspberry Pi 4 2GB (24/7 automation)
- External drive 1TB (data storage)

**Training:**
- Kaggle free GPU (30 hrs/week, P100)
- Google Colab backup (12-15 hrs/week, T4)

**Production:**
- HuggingFace Spaces (hosting)
- HuggingFace Hub (model storage)

### Software Stack

**Core ML:**
```
TTS (Text-to-Speech):
├── Coqui XTTS v2 (primary)
├── YourTTS (alternative)
└── Custom fine-tuning with emotion conditioning

STT (Speech-to-Text):
├── OpenAI Whisper (medium/large)
└── Fine-tuned for Indian accents

LLM (Language Model):
├── Qwen2.5 (7B/14B for Indic languages)
├── Llama 3.2 (3B for lightweight)
└── Claude API (premium option)

Emotion Detection:
├── Wav2Vec2 (emotion classifier)
├── pyannote.audio (speaker diarization)
└── Custom emotion models
```

**Development:**
```
Languages:
├── Python 3.10+ (primary)
├── JavaScript/React (dashboard frontend)
└── Node.js (API server)

Frameworks:
├── PyTorch (ML training)
├── Transformers (HuggingFace)
├── FastAPI (Python API)
├── Express.js (Node API alternative)
└── React + Tailwind (dashboard)

Tools:
├── Claude Code (AI-assisted development)
├── Git/GitHub (version control)
├── Docker (containerization)
└── Jupyter/Kaggle Notebooks (experimentation)
```

**Data Processing:**
```
Collection:
├── yt-dlp (YouTube downloading)
├── Custom scraper scripts

Processing:
├── FFmpeg (audio conversion)
├── pydub (audio manipulation)
├── librosa (audio analysis)
└── soundfile (audio I/O)

Labeling:
├── Whisper (transcription)
├── Qwen2-Audio (emotion detection)
├── Gradio (manual labeling UI)
└── Custom annotation tools
```

**Deployment:**
```
Hosting:
├── HuggingFace Spaces (demo + inference)
├── Render/Railway (API server free tier)
└── Vercel (dashboard frontend)

Storage:
├── HuggingFace Hub (models + datasets)
├── GitHub (code)
└── Local (development data)

Monitoring:
├── HuggingFace analytics
├── Google Analytics (website)
└── Custom usage tracking
```

### Network Architecture
```
┌──────────────────────────────────────────────┐
│ User Interface Layer                         │
├──────────────────────────────────────────────┤
│                                              │
│  Web Dashboard (React)                       │
│  ├── Text-to-Audio converter                │
│  ├── Audio-to-Text converter                │
│  ├── Script manager                          │
│  ├── Voice library                           │
│  └── Project history                         │
│                                              │
│  Mobile App (Flutter - future)               │
│  API Playground (HuggingFace)                │
│                                              │
└──────────────┬───────────────────────────────┘
               ↓
┌──────────────────────────────────────────────┐
│ API Layer (FastAPI/Node.js)                  │
├──────────────────────────────────────────────┤
│                                              │
│  /tts          - Text to Speech              │
│  /stt          - Speech to Text              │
│  /chat         - Conversational AI           │
│  /voices       - List available voices       │
│  /clone        - Voice cloning               │
│                                              │
└──────────────┬───────────────────────────────┘
               ↓
┌──────────────────────────────────────────────┐
│ AI Processing Layer                          │
├──────────────────────────────────────────────┤
│                                              │
│  ┌─────────────┐  ┌──────────────┐          │
│  │ TTS Engine  │  │ STT Engine   │          │
│  │ (XTTS)      │  │ (Whisper)    │          │
│  └─────────────┘  └──────────────┘          │
│                                              │
│  ┌─────────────┐  ┌──────────────┐          │
│  │ LLM Engine  │  │ Emotion AI   │          │
│  │ (Qwen/Llama)│  │ (Custom)     │          │
│  └─────────────┘  └──────────────┘          │
│                                              │
└──────────────┬───────────────────────────────┘
               ↓
┌──────────────────────────────────────────────┐
│ Storage Layer                                │
├──────────────────────────────────────────────┤
│                                              │
│  HuggingFace Hub (Models + Datasets)         │
│  User Data (Projects, History)               │
│  Cache Layer (Fast responses)                │
│                                              │
└──────────────────────────────────────────────┘
```

---

## Phase-wise Roadmap

### Phase 1: Foundation (Months 1-3) - v0.1

**Goal:** Kannada emotional TTS with 5 dialects

#### Month 1: Setup + Data Collection

**Week 1: Environment Setup**
- Day 1: Mac setup (Python, tools, accounts)
  - Install Homebrew, Python, Git, FFmpeg
  - Create GitHub, HuggingFace, Kaggle accounts
  - Setup project structure
  - Test basic functionality
  - **Time:** 8-10 hours

- Day 2-7: Pi automation setup
  - Install Raspberry Pi OS
  - Configure yt-dlp scraping
  - Setup external drive
  - Create auto-download scripts (Claude Code)
  - Test with 5 videos
  - **Time:** 1-2 hours daily

**Week 2-3: Data Collection - Bangalore Kannada**
- Identify 10 YouTube channels (news, comedy, educational)
- Download 30-40 videos (5-10 min each)
- Target: 5 hours raw audio
- Organize by source
- **Automation:** Pi runs overnight

**Week 4: Data Processing Pipeline**
- Build processing scripts (Claude Code)
  - Audio standardization (16kHz WAV)
  - Speaker separation (pyannote.audio)
  - Transcription (Whisper)
  - Quality filtering
- Process collected data
- Target: 3 hours clean segments

**Deliverables:**
- ✅ 3 hours Bangalore Kannada audio
- ✅ Processing pipeline working
- ✅ GitHub repo created
- ✅ Documentation started

#### Month 2: More Data + Emotion Labeling

**Week 1-2: Expand Data Collection**
- Download 50 more videos
- Cover all 5 dialects:
  - Bangalore: 4 hours
  - Mysore: 2 hours
  - Dharwad: 2 hours
  - Coastal: 1 hour
  - North Karnataka: 1 hour
- Total target: 10 hours

**Week 3: Emotion Labeling**
- Build Gradio labeling tool (Claude Code)
- Manual labeling workflow:
  - Listen to clips
  - Tag emotion (Neutral, Happy, Empathetic, Sarcastic, Excited)
  - Mark dialect
  - Rate quality
- Recruit 2-3 volunteers to help
- Target distribution:
  - Neutral: 4 hours
  - Happy: 2 hours
  - Empathetic: 2 hours
  - Sarcastic: 1 hour
  - Excited: 1 hour

**Week 4: Dataset Preparation**
- Organize final dataset structure
- Create metadata files
- Split train/validation/test (80/10/10)
- Upload to HuggingFace Datasets
- Document data sources (transparency)

**Deliverables:**
- ✅ 10 hours labeled Kannada data
- ✅ 5 dialects covered
- ✅ 5 emotions tagged
- ✅ Dataset on HuggingFace
- ✅ Data documentation complete

#### Month 3: Training + Release

**Week 1: Training Setup**
- Setup Kaggle training environment
- Configure XTTS for Kannada
- Add emotion conditioning
- Test with small dataset
- Debug issues

**Week 2: Full Training**
- Upload full dataset to Kaggle
- Run training (12-24 hours GPU time)
- Monitor checkpoints
- Generate test samples
- Iterate if quality poor

**Week 3: Testing + Refinement**
- Test all emotion/dialect combinations
- Get feedback from native speakers
- Retrain if needed
- Optimize model (quantization)
- Create model card documentation

**Week 4: v0.1 Release**
- Upload model to HuggingFace Hub
- Create demo (Gradio/Streamlit)
- Deploy to HuggingFace Spaces
- Write comprehensive README
- Announcement posts (Reddit, LinkedIn, Twitter)
- Gather initial feedback

**Deliverables:**
- ✅ Working Kannada emotional TTS
- ✅ 5 dialects supported
- ✅ 5 emotions working
- ✅ Public demo live
- ✅ v0.1 released on GitHub/HuggingFace
- ✅ 50+ GitHub stars (goal)
- ✅ 10+ community members

---

### Phase 2: Expansion (Months 4-6) - v0.5

**Goal:** Multi-language + STT + Dashboard

#### Month 4: Add Languages

**Week 1-2: Tamil Language**
- Collect 10 hours Tamil data (similar process)
- Focus on Chennai/Madurai dialects
- Label emotions
- Train Tamil model

**Week 3-4: Hindi Language**
- Collect 10 hours Hindi data
- Delhi/Mumbai/UP variations
- Label emotions
- Train Hindi model

**Deliverables:**
- ✅ Tamil emotional TTS
- ✅ Hindi emotional TTS
- ✅ 3 languages total

#### Month 5: Speech-to-Text Integration

**Week 1: Whisper Fine-tuning**
- Fine-tune Whisper on Kannada data
- Improve accent recognition
- Test accuracy

**Week 2: STT API Integration**
- Build STT endpoint
- Audio upload → Transcription
- Support all 3 languages
- Emotion detection in input

**Week 3-4: Bidirectional Workflow**
- Text → Voice (existing)
- Voice → Text (new)
- Voice → Text → Edit → Voice (workflow)
- Test complete pipeline

**Deliverables:**
- ✅ STT working for 3 languages
- ✅ Bidirectional conversion
- ✅ Emotion detection in speech

#### Month 6: Dashboard Development

**Week 1-2: Frontend (React)**
- Design UI/UX (Claude Code assistance)
- Build components:
  - Text-to-Audio converter
  - Audio-to-Text converter
  - Script editor
  - Voice selector (language/dialect/emotion)
  - Audio player
  - Project manager
- Responsive design (mobile-friendly)

**Week 3: Backend API**
- FastAPI or Node.js
- Endpoints for all features
- User authentication (optional)
- Usage tracking
- Rate limiting

**Week 4: Deploy + Test**
- Deploy frontend (Vercel/Netlify)
- Deploy backend (Render/Railway)
- Connect to HuggingFace models
- End-to-end testing
- Bug fixes

**Deliverables:**
- ✅ Professional dashboard live
- ✅ TTS + STT integrated
- ✅ 3 languages accessible
- ✅ User-friendly interface
- ✅ v0.5 release

---

### Phase 3: Intelligence (Months 7-9) - v0.8

**Goal:** Conversational AI capabilities

#### Month 7: LLM Integration

**Week 1: LLM Selection + Setup**
- Choose LLM: Qwen2.5-7B (recommended)
- Setup on Kaggle/HuggingFace
- Test Kannada/Hindi/Tamil understanding
- Benchmark performance

**Week 2: Fine-tuning for Indian Context**
- Collect conversational data (Indian context)
- Fine-tune Qwen on Indian scenarios
- Test cultural understanding
- Improve responses

**Week 3-4: Integration**
- Connect LLM to TTS pipeline
- User question → LLM answer → Voice output
- Build conversation manager
- Handle multi-turn dialogs

**Deliverables:**
- ✅ LLM understanding Indian languages
- ✅ Text Q&A working
- ✅ Voice responses working

#### Month 8: Complete Voice Pipeline

**Week 1-2: Voice-to-Voice**
- Full pipeline:
  - User speaks (any language)
  - Whisper transcribes
  - LLM understands + generates answer
  - Swara-Bharat speaks response
- Test latency (optimize for <5 sec)
- Handle interruptions

**Week 3: Multi-turn Conversations**
- Conversation memory
- Context awareness
- Natural dialog flow
- Emotion-aware responses (empathetic, excited, etc.)

**Week 4: Domain Specialization**
- Customer service scripts
- Educational content
- Healthcare scenarios
- Comedy/entertainment

**Deliverables:**
- ✅ Voice-in, voice-out working
- ✅ Multi-turn conversations
- ✅ Emotion-aware responses
- ✅ Domain templates

#### Month 9: Quality + Performance

**Week 1-2: Optimization**
- Reduce latency
- Model quantization
- Caching strategies
- Load balancing

**Week 3: Testing at Scale**
- Stress testing
- Bug fixes
- User feedback integration
- A/B testing different approaches

**Week 4: Documentation + Examples**
- API documentation
- Usage tutorials
- Video demos
- Case studies

**Deliverables:**
- ✅ Production-ready performance
- ✅ Comprehensive documentation
- ✅ v0.8 release

---

### Phase 4: Platform (Months 10-12) - v1.0

**Goal:** Complete Sarvam alternative

#### Month 10: More Languages + Features

**Week 1-2: Add Languages**
- Telugu (10 hours data + training)
- Malayalam (10 hours data + training)
- Total: 5 major Indian languages

**Week 3-4: Advanced Features**
- Voice cloning (user uploads 2 min, get their voice)
- Speed/pitch control
- Background noise removal
- Multi-speaker support

**Deliverables:**
- ✅ 5 languages total
- ✅ Voice cloning working
- ✅ Advanced audio controls

#### Month 11: Business Features

**Week 1: API Platform**
- Public API with authentication
- API keys management
- Rate limiting (free tier)
- Usage analytics
- Documentation

**Week 2: Business Dashboard**
- Team management
- Batch processing
- Analytics dashboard
- Export options (MP3, WAV, etc.)
- Webhook integrations

**Week 3: Integrations**
- Zapier integration
- WordPress plugin
- Chrome extension
- Discord bot
- Telegram bot

**Week 4: Premium Features (Optional)**
- Priority processing
- Higher rate limits
- Custom voice training
- Dedicated support

**Deliverables:**
- ✅ API platform live
- ✅ Business dashboard
- ✅ Integration ecosystem
- ✅ Freemium model defined

#### Month 12: Polish + Launch

**Week 1-2: Quality Assurance**
- Security audit
- Performance optimization
- Bug bash
- User testing (beta program)

**Week 3: Marketing Materials**
- Professional website
- Demo videos
- Case studies
- Press kit
- Blog posts

**Week 4: v1.0 Launch**
- ProductHunt launch
- HackerNews post
- Press releases
- Conference talks (submit proposals)
- Academic paper (optional)

**Deliverables:**
- ✅ v1.0 production release
- ✅ 1000+ GitHub stars (goal)
- ✅ 100+ active users
- ✅ Media coverage
- ✅ Sustainable project

---

## Setup Guide

### Day 1: Complete Mac Setup (8-10 hours)

#### Part 1: System Tools (2 hours)

**Step 1: Install Homebrew**
```bash
# Install Homebrew (package manager)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verify installation
brew --version
```

**Step 2: Install Core Tools**
```bash
# Git (version control)
brew install git
git --version

# Python 3.10+
brew install python@3.10
python3 --version

# FFmpeg (audio processing)
brew install ffmpeg
ffmpeg -version

# Check installations
which python3
which git
which ffmpeg
```

**Step 3: Configure Git**
```bash
git config --global user.name "Manju"
git config --global user.email "your-email@example.com"
git config --list
```

#### Part 2: Python Environment (2 hours)

**Step 1: Create Project Structure**
```bash
# Create main directory
mkdir ~/swara-bharat
cd ~/swara-bharat

# Create subdirectories
mkdir -p {scripts,training,data/{raw,processed,segments},models,docs,demos}

# Verify structure
tree -L 2  # If tree not installed: brew install tree
```

**Step 2: Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv

# Activate (you'll do this every time you work)
source venv/bin/activate

# Your prompt should now show (venv)

# Upgrade pip
pip install --upgrade pip
```

**Step 3: Install Python Packages**
```bash
# Core ML packages
pip install torch torchvision torchaudio
pip install transformers
pip install datasets
pip install accelerate

# TTS and audio
pip install TTS
pip install openai-whisper
pip install pydub
pip install librosa
pip install soundfile
pip install pyannote.audio

# Data collection
pip install yt-dlp
pip install beautifulsoup4
pip install requests

# UI and API
pip install gradio
pip install streamlit
pip install fastapi
pip install uvicorn

# Utilities
pip install python-dotenv
pip install tqdm
pip install pandas
pip install numpy

# Save requirements
pip freeze > requirements.txt
```

**Step 4: Test Installations**
```bash
# Test PyTorch
python3 -c "import torch; print(f'PyTorch: {torch.__version__}')"

# Test Transformers
python3 -c "import transformers; print(f'Transformers: {transformers.__version__}')"

# Test Whisper
python3 -c "import whisper; print('Whisper: OK')"

# Test TTS
python3 -c "from TTS.api import TTS; print('TTS: OK')"

# Test yt-dlp
yt-dlp --version
```

#### Part 3: Create Accounts (1 hour)

**GitHub**
1. Go to https://github.com/join
2. Username: manjussha
3. Email: your-email@example.com
4. Verify email
5. Create personal access token:
   - Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select: repo, workflow, write:packages
   - Save token securely

**HuggingFace**
1. Go to https://huggingface.co/join
2. Sign up
3. Verify email
4. Create access token:
   - Settings → Access Tokens
   - New token → Write access
   - Save token securely

**Kaggle**
1. Go to https://www.kaggle.com
2. Sign up with Google/email
3. Phone verification
4. Accept terms
5. Download API token:
   - Account → API → Create New API Token
   - Downloads kaggle.json
   - Move to: ~/.kaggle/kaggle.json
   - Set permissions: chmod 600 ~/.kaggle/kaggle.json

#### Part 4: GitHub Repository Setup (1 hour)

**Create Repository**
```bash
cd ~/swara-bharat

# Initialize git
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/

# Data (too large for git)
data/raw/
data/processed/
models/*.pth
models/*.pt
*.wav
*.mp3
*.mp4

# Environment
.env
.DS_Store

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
EOF

# Create initial README
cat > README.md << 'EOF'
# 🎙️ Swara-Bharat (ಸ್ವರ-ಭಾರತ)

Open-source emotional voice AI for Indian languages

## Status
🚧 Under Development - v0.1 in progress

## Vision
Build India's first open-source alternative to Sarvam AI with emotional voice capabilities.

## Features (Planned)
- Emotional TTS (Text-to-Speech)
- Multiple Indian languages
- Dialect support
- Free and open-source

## Progress
- [x] Project setup
- [ ] Data collection
- [ ] Model training
- [ ] Demo release

## License
Apache 2.0

## Contact
GitHub: @manjussha
EOF

# Add Apache 2.0 License
curl -o LICENSE https://www.apache.org/licenses/LICENSE-2.0.txt

# Initial commit
git add .
git commit -m "Initial commit: Project structure"

# Create GitHub repo (do this on GitHub.com first)
# Then connect:
git remote add origin https://github.com/manjussha/swara-bharat.git
git branch -M main
git push -u origin main
```

#### Part 5: Test Download (1 hour)

**Create test script**
```bash
cd ~/swara-bharat/scripts

# Create test_download.py using Claude Code
# Prompt for Claude Code: "Write a Python script to download 
# one YouTube video audio in MP3 format using yt-dlp, 
# with error handling and progress bar"
```

**Test download**
```bash
# Find a test video (Kannada news clip)
python3 test_download.py "https://www.youtube.com/watch?v=[TEST_VIDEO_ID]"

# Should download to data/raw/
# Verify file exists
ls -lh data/raw/
```

#### Part 6: HuggingFace Setup (1 hour)

**Login to HuggingFace**
```bash
# Install huggingface-cli
pip install huggingface_hub

# Login
huggingface-cli login
# Paste your HF token

# Test upload
cat > test.txt << 'EOF'
This is a test file for Swara-Bharat
EOF

huggingface-cli upload manjussha/swara-bharat-test test.txt test.txt --repo-type model

# Verify on HuggingFace website
```

**Create repositories**
1. Go to https://huggingface.co/new
2. Create model repo: swara-bharat-kannada
3. Create dataset repo: swara-bharat-kannada-data
4. Set both to public

#### Part 7: Kaggle Setup (1 hour)

**Test Kaggle**
```bash
# Verify kaggle.json exists
cat ~/.kaggle/kaggle.json

# Test Kaggle API
kaggle datasets list

# Create test notebook
# Go to https://www.kaggle.com/code
# Click "New Notebook"
# Select GPU
# Run: !nvidia-smi
# Should show GPU info
# Save as "swara-bharat-test"
```

---

### Raspberry Pi Setup (3-4 hours)

#### Part 1: OS Installation (1 hour)

**Download and Flash OS**
1. Download Raspberry Pi Imager: https://www.raspberrypi.com/software/
2. Insert SD card (32GB minimum)
3. Choose OS: Raspberry Pi OS Lite (64-bit)
4. Configure settings:
   - Set hostname: swara-scraper
   - Enable SSH
   - Set username/password
   - Configure WiFi (or use ethernet)
5. Flash to SD card
6. Insert in Pi and power on
7. Wait 2-3 minutes for first boot

**Find Pi on network**
```bash
# From Mac, find Pi IP
ping swara-scraper.local

# Or scan network
nmap -sn 192.168.1.0/24
```

**SSH into Pi**
```bash
ssh pi@swara-scraper.local
# Enter password

# Update system
sudo apt update
sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip git ffmpeg
```

#### Part 2: External Drive Setup (30 mins)

**Connect and mount drive**
```bash
# Find drive
sudo fdisk -l

# Create mount point
sudo mkdir /mnt/downloads

# Get drive UUID
sudo blkid
# Note the UUID of your external drive

# Auto-mount on boot
sudo nano /etc/fstab
# Add line (replace UUID):
# UUID=your-drive-uuid /mnt/downloads ext4 defaults,auto,users,rw,nofail 0 0

# Mount now
sudo mount -a

# Verify
df -h | grep downloads

# Set permissions
sudo chmod 777 /mnt/downloads
```

#### Part 3: Install Python Tools (30 mins)
```bash
# Install yt-dlp
sudo pip3 install yt-dlp

# Install other tools
sudo pip3 install requests beautifulsoup4 tqdm

# Test
yt-dlp --version
python3 --version
```

#### Part 4: Create Scraper Script (1 hour)

**Create project directory**
```bash
mkdir ~/swara-scraper
cd ~/swara-scraper

# Create directories
mkdir -p scripts logs
```

**Create download script** (use Claude Code on Mac, then transfer)
```python
# On Mac, create scripts/auto_scraper.py
# Prompt for Claude Code: "Create a robust YouTube downloader 
# that reads URLs from urls.txt, downloads audio as 320kbps MP3, 
# saves to /mnt/downloads, logs progress, handles errors, 
# and runs continuously checking for new URLs every hour"

# Transfer to Pi
scp scripts/auto_scraper.py pi@swara-scraper.local:~/swara-scraper/scripts/
```

**Create systemd service for auto-start**
```bash
# On Pi
sudo nano /etc/systemd/system/swara-scraper.service

# Add:
[Unit]
Description=Swara-Bharat YouTube Scraper
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/swara-scraper
ExecStart=/usr/bin/python3 /home/pi/swara-scraper/scripts/auto_scraper.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

# Save and exit (Ctrl+X, Y, Enter)

# Enable and start
sudo systemctl enable swara-scraper
sudo systemctl start swara-scraper

# Check status
sudo systemctl status swara-scraper

# View logs
journalctl -u swara-scraper -f
```

#### Part 5: File Transfer Setup (30 mins)

**Setup SSH keys for passwordless access**
```bash
# On Mac
ssh-keygen -t rsa
# Press enter for all prompts

# Copy to Pi
ssh-copy-id pi@swara-scraper.local

# Test passwordless login
ssh pi@swara-scraper.local
# Should login without password
```

**Create sync script on Mac**
```bash
cd ~/swara-bharat/scripts

# Create sync_from_pi.sh
cat > sync_from_pi.sh << 'EOF'
#!/bin/bash
# Sync downloaded files from Pi to Mac

PI_HOST="pi@swara-scraper.local"
PI_DIR="/mnt/downloads/"
LOCAL_DIR="$HOME/swara-bharat/data/raw/"

echo "Syncing from Pi..."
rsync -avz --progress $PI_HOST:$PI_DIR $LOCAL_DIR

echo "Sync complete!"
echo "Files in: $LOCAL_DIR"
ls -lh $LOCAL_DIR | tail -10
EOF

# Make executable
chmod +x sync_from_pi.sh

# Test
./sync_from_pi.sh
```

---

## Development Workflow

### Daily Workflow (1-2 hours)

**Morning Routine (10 mins)**
```bash
# 1. Check Pi status from Mac
ssh pi@swara-scraper.local "df -h /mnt/downloads && tail -20 ~/swara-scraper/logs/scraper.log"

# 2. Sync new downloads if any
cd ~/swara-bharat/scripts
./sync_from_pi.sh

# 3. Activate Python environment
cd ~/swara-bharat
source venv/bin/activate

# 4. Check Git status
git status
git pull origin main
```

**Work Session (1-2 hours)**

**Option A: Data Processing Day**
```bash
# Process new downloads
python3 scripts/process_audio.py

# Label emotions
python3 scripts/label_emotions_ui.py

# Update dataset
python3 scripts/update_dataset.py
```

**Option B: Development Day**
```bash
# Work on scripts (with Claude Code)
code .  # Open in VS Code

# Test new features
python3 scripts/test_new_feature.py

# Run quality checks
python3 scripts/verify_data_quality.py
```

**Option C: Training Day**
```bash
# Prepare for training
python3 scripts/prepare_training_data.py

# Upload to HuggingFace
python3 scripts/upload_to_hf.py

# Switch to Kaggle for training
# Open: https://www.kaggle.com/code
```

**Evening Wrap-up (10 mins)**
```bash
# Commit progress
git add .
git commit -m "Progress: [what you did today]"
git push origin main

# Update progress log
echo "$(date): [Today's progress]" >> docs/progress.md

# Add new URLs for Pi to download tomorrow
echo "https://youtube.com/watch?v=..." >> ~/swara-scraper/urls.txt
scp ~/swara-scraper/urls.txt pi@swara-scraper.local:~/swara-scraper/
```

### Weekly Workflow

**Every Sunday (2 hours planning)**
```bash
# 1. Review week's progress
git log --since="1 week ago" --oneline

# 2. Check metrics
python3 scripts/weekly_stats.py
# Shows:
# - Hours of data collected
# - Audio processed
# - Labels completed
# - Models trained

# 3. Plan next week
# Update: docs/roadmap.md
# Create issues on GitHub for tasks

# 4. Community engagement
# - Check GitHub issues/PRs
# - Respond to questions
# - Update documentation
```

### Monthly Workflow

**End of Month (4 hours)**
```bash
# 1. Comprehensive testing
python3 scripts/run_all_tests.py

# 2. Update documentation
# - README progress
# - API docs if changed
# - Tutorial videos

# 3. Release preparation (if milestone reached)
# - Tag version: git tag v0.1.0
# - Create release notes
# - Update changelog

# 4. Community update
# - Blog post / LinkedIn update
# - Demo video
# - Metrics sharing (hours of data, languages, users)
```

---

## Data Collection Strategy

### YouTube Source Strategy

#### Kannada Sources

**News Channels (Neutral + Professional tone)**
```
Primary (Daily downloads):
1. TV9 Kannada - https://www.youtube.com/@tv9kannada
2. Public TV - https://www.youtube.com/@PublicTV  
3. Udaya News - https://www.youtube.com/@udayanewstv
4. Suvarna News - https://www.youtube.com/@suvarnanews

Focus: News bulletins (5-10 min clips)
Emotion: Neutral, Professional, sometimes Urgent
Dialect: Mostly Bangalore, some Mysore
```

**Comedy Shows (Happy + Sarcastic + Excited)**
```
1. Majaa Bharatha clips
2. Kannada stand-up comedians
3. Comedy sketches

Focus: 2-5 min clips
Emotion: Happy, Sarcastic, Excited, Exaggerated
Dialect: Bangalore, colloquial
```

**Educational Content (Neutral + Empathetic)**
```
1. Kannada educational channels
2. Tutorial videos
3. Explainer content

Focus: Clear speech, slower pace
Emotion: Neutral, Patient, Encouraging
Dialect: Standard Kannada
```

**Motivational Speakers (Empathetic + Excited)**
```
1. Kannada motivational talks
2. Life advice content
3. Inspirational speeches

Emotion: Empathetic, Excited, Inspiring
Dialect: Formal Kannada
```

**Podcasts/Interviews (Conversational)**
```
1. Kannada podcasts
2. Interview shows
3. Discussion programs

Emotion: Natural, Conversational, varied
Dialect: Mixed
```

#### Dialect-Specific Sources

**Mysore Kannada:**
- Mysore local news
- Cultural programs
- Traditional storytelling

**Dharwad/North Karnataka:**
- North Karnataka news channels
- Folk content
- Agricultural programs

**Coastal Karnataka:**
- Mangalore/Udupi local channels
- Tulu-Kannada mixed content
- Coastal news

### Automated Collection Workflow

**keywords.json structure:**
```json
{
  "kannada_news": [
    "ಕನ್ನಡ ಸುದ್ದಿ",
    "tv9 kannada news",
    "public tv news kannada",
    "udaya news kannada"
  ],
  "kannada_comedy": [
    "kannada comedy",
    "kannada stand up",
    "majaa bharatha"
  ],
  "kannada_education": [
    "kannada tutorial",
    "kannada explanation",
    "kannada science"
  ],
  "kannada_motivational": [
    "kannada motivation",
    "kannada inspirational speech"
  ]
}
```

**Pi auto-scraper logic:**
```python
# Pseudo-code (Claude Code will write full version)

1. Load keywords from keywords.json
2. For each category:
   - Search YouTube
   - Filter: 
     * Duration 3-15 minutes
     * Upload date: last 30 days
     * Minimum views: 1000
   - Download top 5 results as MP3 (320kbps)
   - Save metadata (title, channel, URL, date)
   - Log progress
3. Wait 6 hours
4. Repeat

Daily quota: ~50-100 videos
Storage needed: ~5-10 GB/day
```

### Quality Filters

**Automatic Filters (in processing script):**
```python
def filter_audio_quality(audio_file):
    """
    Returns True if audio passes quality checks
    """
    checks = {
        'duration': 3 <= duration <= 900,  # 3 sec - 15 min
        'sample_rate': sample_rate >= 16000,
        'channels': channels == 1,  # mono
        'noise_level': snr > 10,  # signal-to-noise ratio
        'silence_ratio': silence < 0.3,  # <30% silence
        'language_detected': 'kannada' in detected_languages
    }
    return all(checks.values())
```

**Manual Review (sampling):**
- Random 10% of collected data
- Listen for quality
- Verify emotion labels
- Check dialect accuracy
- Remove bad samples

### Data Organization

**Directory structure:**
```
data/
├── raw/                          # Direct downloads from YouTube
│   ├── kannada_news/
│   ├── kannada_comedy/
│   └── kannada_education/
│
├── processed/                    # After cleaning
│   ├── kannada/
│   │   ├── bangalore/
│   │   ├── mysore/
│   │   └── dharwad/
│   └── metadata/
│
├── segments/                     # Individual clips (3-15 sec)
│   ├── neutral/
│   │   ├── bangalore/
│   │   │   ├── clip_0001.wav
│   │   │   ├── clip_0001.txt
│   │   │   └── clip_0001.json  # metadata
│   │   └── mysore/
│   ├── happy/
│   ├── empathetic/
│   ├── sarcastic/
│   └── excited/
│
└── final/                        # Ready for training
    ├── train/
    ├── validation/
    ├── test/
    └── metadata.csv
```

**metadata.csv format:**
```csv
audio_path,text,language,dialect,emotion,speaker_id,duration,source_url,quality_score
segments/neutral/bangalore/clip_0001.wav,"ನಮಸ್ಕಾರ ಇದು ಸುದ್ದಿ",kannada,bangalore,neutral,spk_001,3.5,https://youtube.com/watch?v=...,0.92
segments/happy/bangalore/clip_0002.wav,"ಧನ್ಯವಾದಗಳು",kannada,bangalore,happy,spk_001,2.1,https://youtube.com/watch?v=...,0.88
```

### Ethical Data Collection

**Transparency:**
- Document all sources
- Keep URLs and channel names
- Attribution in model card
- Remove on request process

**Privacy:**
- Only use public YouTube content
- No private/unlisted videos
- No personal conversations
- Anonymize any personal info in transcripts

**Copyright Respect:**
- News content (fair use for education/research)
- Short clips only (3-15 seconds each)
- Transformative use (training AI)
- Non-commercial initially
- Credit creators prominently

**Removal Process:**
```
1. Email: data-removal@swara-bharat.org
2. Provide: YouTube URL or clip details
3. Response time: 48 hours
4. Action: Remove from dataset, retrain if needed
5. Confirm: Email confirmation of removal
```

---

## Model Training

### Training Environment Setup (Kaggle)

**Kaggle Notebook Structure:**
```
swara-bharat-training/
├── 01_setup.ipynb              # Install dependencies
├── 02_data_preparation.ipynb   # Load and prepare data
├── 03_model_config.ipynb       # Configure XTTS
├── 04_training.ipynb           # Main training loop
├── 05_evaluation.ipynb         # Test and evaluate
└── 06_export.ipynb             # Export to HuggingFace
```

**Template: 01_setup.ipynb**
```python
# Cell 1: Check GPU
!nvidia-smi

# Cell 2: Install packages
!pip install -q TTS transformers datasets
!pip install -q pyannote.audio librosa soundfile

# Cell 3: Setup HuggingFace
from huggingface_hub import notebook_login
notebook_login()

# Cell 4: Load dataset from HuggingFace
from datasets import load_dataset
dataset = load_dataset("manjussha/swara-bharat-kannada-data")

print(f"Training samples: {len(dataset['train'])}")
print(f"Validation samples: {len(dataset['validation'])}")
print(f"Test samples: {len(dataset['test'])}")
```

### Training Configuration

**XTTS Config (config.json):**
```json
{
  "model": "xtts_v2",
  "language": "kn",
  "dataset_path": "manjussha/swara-bharat-kannada-data",
  
  "training": {
    "batch_size": 8,
    "learning_rate": 1e-4,
    "num_epochs": 100,
    "save_step": 10,
    "eval_step": 10,
    "gradient_accumulation_steps": 2
  },
  
  "model_config": {
    "emotion_embedding_dim": 64,
    "emotions": ["neutral", "happy", "empathetic", "sarcastic", "excited"],
    "dialects": ["bangalore", "mysore", "dharwad", "coastal", "north_karnataka"]
  },
  
  "audio": {
    "sample_rate": 22050,
    "hop_length": 256,
    "win_length": 1024
  },
  
  "output": {
    "output_path": "./outputs/",
    "checkpoint_path": "./checkpoints/"
  }
}
```

### Training Script (template)
```python
# 04_training.ipynb

# Cell 1: Imports and setup
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from TTS.trainer import Trainer
import torch

# Cell 2: Load config
config = XttsConfig()
config.load_json("config.json")

# Cell 3: Initialize model
model = Xtts.init_from_config(config)
model.cuda()

# Cell 4: Prepare data
train_samples = prepare_samples(dataset['train'])
eval_samples = prepare_samples(dataset['validation'])

# Cell 5: Training loop
trainer = Trainer(
    config=config,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
    output_path="./outputs/"
)

# Cell 6: Start training (will take 12-24 hours)
trainer.fit()

# Cell 7: Evaluate best checkpoint
best_model = load_checkpoint("./outputs/best_model.pth")
evaluate_model(best_model, dataset['test'])

# Cell 8: Generate test samples
test_sentences = [
    ("ನಮಸ್ಕಾರ", "neutral", "bangalore"),
    ("ಧನ್ಯವಾದಗಳು", "happy", "bangalore"),
    ("ನಾವು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ", "empathetic", "mysore"),
]

for text, emotion, dialect in test_sentences:
    audio = generate_speech(text, emotion, dialect)
    save_audio(audio, f"sample_{emotion}_{dialect}.wav")
    display(Audio(audio, rate=22050))
```

### Monitoring Training

**Metrics to track:**
```python
metrics = {
    'training_loss': [],      # Should decrease
    'validation_loss': [],    # Should decrease
    'mel_loss': [],          # Spectral quality
    'duration_loss': [],     # Timing accuracy
    'emotion_accuracy': [],  # Emotion classification
    'mos_score': []          # Mean Opinion Score (manual)
}
```

**Early stopping criteria:**
```python
# Stop if:
# 1. Validation loss increases for 5 epochs
# 2. Training loss < 0.1 but validation loss > 0.5 (overfitting)
# 3. No improvement in 20 epochs
# 4. Manual quality check fails
```

### Post-Training Optimization

**Model Quantization:**
```python
# Reduce model size 4x with minimal quality loss
from torch.quantization import quantize_dynamic

# Original model: 2.1 GB
quantized_model = quantize_dynamic(
    model, 
    {torch.nn.Linear}, 
    dtype=torch.qint8
)
# Quantized model: ~600 MB

# Test quality difference
compare_outputs(model, quantized_model, test_samples)
```

**ONNX Export:**
```python
# For faster inference
import torch.onnx

dummy_input = torch.randn(1, 256)
torch.onnx.export(
    model,
    dummy_input,
    "swara_bharat_kannada.onnx",
    opset_version=14,
    input_names=['text_tokens'],
    output_names=['audio'],
    dynamic_axes={'text_tokens': {0: 'batch_size'}}
)
```

### Evaluation

**Automated Metrics:**
```python
def evaluate_model(model, test_dataset):
    results = {
        'wer': [],  # Word Error Rate (transcribe back)
        'emotion_accuracy': [],
        'naturalness_score': [],
        'inference_time': []
    }
    
    for sample in test_dataset:
        # Generate audio
        audio = model.generate(sample['text'], sample['emotion'])
        
        # Transcribe back (using Whisper)
        transcription = whisper.transcribe(audio)
        wer = calculate_wer(sample['text'], transcription)
        results['wer'].append(wer)
        
        # Detect emotion
        detected_emotion = emotion_classifier(audio)
        correct = detected_emotion == sample['emotion']
        results['emotion_accuracy'].append(correct)
        
        # Time it
        start = time.time()
        _ = model.generate(sample['text'], sample['emotion'])
        inference_time = time.time() - start
        results['inference_time'].append(inference_time)
    
    return {
        'avg_wer': np.mean(results['wer']),
        'emotion_accuracy': np.mean(results['emotion_accuracy']),
        'avg_inference_time': np.mean(results['inference_time'])
    }
```

**Manual Evaluation (MOS - Mean Opinion Score):**
```python
# Recruit 10 native Kannada speakers
# Present 20 random samples per speaker
# Rate on scale 1-5:
# 5 = Excellent (native-like)
# 4 = Good (minor issues)
# 3 = Fair (understandable but unnatural)
# 2 = Poor (hard to understand)
# 1 = Bad (unintelligible)

# Target for release: MOS > 3.5
```

---

## Dashboard Development

### Technology Stack

**Frontend:**
```
Framework: React 18
Styling: Tailwind CSS
State: Zustand (lightweight)
UI Components: shadcn/ui
Audio: Howler.js
File Upload: react-dropzone
Forms: react-hook-form
```

**Backend:**
```
API: FastAPI (Python) or Express.js (Node.js)
Auth: JWT tokens (optional for v0.5)
Database: PostgreSQL (for user projects, optional)
Cache: Redis (for fast responses)
Storage: HuggingFace Hub (models), S3-compatible (user files)
```

**Deployment:**
```
Frontend: Vercel (free tier)
Backend: Render (free tier) or Railway
Models: HuggingFace Inference API
CDN: Cloudflare (free)
```

### Dashboard Pages

#### 1. Home / Landing Page

**Features:**
- Hero section with demo
- Quick TTS generator
- Language selector
- Sample outputs
- Getting started guide

**React Component Structure:**
```jsx
<HomePage>
  <Header />
  <HeroSection>
    <QuickDemo />
  </HeroSection>
  <FeaturesSection />
  <LanguagesSection />
  <ExamplesSection />
  <CTASection />
  <Footer />
</HomePage>
```

#### 2. TTS Studio (Main Feature)

**Layout:**
```
┌────────────────────────────────────────────┐
│ Header: Logo | TTS | STT | Projects       │
├────────────────────────────────────────────┤
│                                            │
│  ┌──────────────────┐  ┌────────────────┐ │
│  │ Script Editor    │  │ Voice Config   │ │
│  │                  │  │                │ │
│  │ [Text area]      │  │ Language: [▼]  │ │
│  │                  │  │ Dialect: [▼]   │ │
│  │                  │  │ Emotion: [▼]   │ │
│  │                  │  │ Speed: [====] │ │
│  │                  │  │                │ │
│  │                  │  │ [Generate]     │ │
│  └──────────────────┘  └────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Audio Player                          │ │
│  │ [▶ Play] [Download] [Share]         │ │
│  │ Waveform visualization               │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  Recent Generations:                       │
│  • Sample 1 - 2 min ago                   │
│  • Sample 2 - 5 min ago                   │
│                                            │
└────────────────────────────────────────────┘
```

**Key Features:**
- Real-time character count
- Script templates library
- Voice preview samples
- Batch generation (multiple scripts)
- Export formats (WAV, MP3, OGG)
- Project save/load

#### 3. STT Studio

**Layout:**
```
┌────────────────────────────────────────────┐
│ Audio to Text Converter                    │
├────────────────────────────────────────────┤
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Upload Audio                          │ │
│  │                                       │ │
│  │ [Drag & drop or click to upload]     │ │
│  │                                       │ │
│  │ Supported: MP3, WAV, M4A, OGG        │ │
│  │ Max size: 25 MB                      │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  Language: [Auto-detect ▼]                │
│  Include emotion analysis: [✓]            │
│                                            │
│  [Transcribe]                             │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Results                               │ │
│  │                                       │ │
│  │ Transcription:                        │ │
│  │ [Editable text area]                  │ │
│  │                                       │ │
│  │ Detected:                             │ │
│  │ Language: Kannada (Bangalore)        │ │
│  │ Emotion: Happy (confidence: 0.87)    │ │
│  │ Speaker: Male                         │ │
│  │                                       │ │
│  │ [Copy] [Download] [Send to TTS]      │ │
│  └──────────────────────────────────────┘ │
│                                            │
└────────────────────────────────────────────┘
```

#### 4. Projects Manager

**Features:**
- Save scripts and configurations
- Version history
- Folders/tags organization
- Search and filter
- Export/import projects

#### 5. Voice Library

**Gallery of available voices:**
```
┌────────────────────────────────────────────┐
│ Available Voices                           │
├────────────────────────────────────────────┤
│                                            │
│  Filters: [Language ▼] [Dialect ▼] [⚥]   │
│                                            │
│  ┌────────┐ ┌────────┐ ┌────────┐        │
│  │ Voice 1│ │ Voice 2│ │ Voice 3│        │
│  │ [🔊]   │ │ [🔊]   │ │ [🔊]   │        │
│  │        │ │        │ │        │        │
│  │ Bangal │ │ Mysore │ │ Dhwrd  │        │
│  │ Female │ │ Male   │ │ Female │        │
│  │        │ │        │ │        │        │
│  │ [Use]  │ │ [Use]  │ │ [Use]  │        │
│  └────────┘ └────────┘ └────────┘        │
│                                            │
│  + Upload your voice (Pro feature)         │
│                                            │
└────────────────────────────────────────────┘
```

#### 6. API Playground

**For developers:**
```
┌────────────────────────────────────────────┐
│ API Documentation & Playground             │
├────────────────────────────────────────────┤
│                                            │
│  Endpoint: POST /api/v1/tts               │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Request Body (JSON):                  │ │
│  │                                       │ │
│  │ {                                     │ │
│  │   "text": "ನಮಸ್ಕಾರ",                │ │
│  │   "language": "kn",                   │ │
│  │   "dialect": "bangalore",             │ │
│  │   "emotion": "happy"                  │ │
│  │ }                                     │ │
│  │                                       │ │
│  │ [Try It]                              │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Response:                             │ │
│  │                                       │ │
│  │ {                                     │ │
│  │   "audio_url": "https://...",        │ │
│  │   "duration": 2.3,                    │ │
│  │   "format": "wav"                     │ │
│  │ }                                     │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  Code Examples:                            │
│  [Python] [JavaScript] [cURL] [PHP]       │
│                                            │
└────────────────────────────────────────────┘
```

### Implementation Roadmap

**Week 1-2: Frontend Setup**
```bash
# Create React app
npx create-react-app swara-bharat-dashboard
cd swara-bharat-dashboard

# Install dependencies
npm install tailwindcss @headlessui/react
npm install zustand react-router-dom
npm install howler react-dropzone
npm install @tanstack/react-query axios

# Setup Tailwind
npx tailwindcss init

# Project structure
src/
├── components/
│   ├── common/          # Buttons, inputs, etc.
│   ├── tts/            # TTS-specific components
│   ├── stt/            # STT-specific components
│   └── layout/         # Header, footer, sidebar
├── pages/
│   ├── Home.jsx
│   ├── TTSStudio.jsx
│   ├── STTStudio.jsx
│   └── VoiceLibrary.jsx
├── services/           # API calls
├── hooks/             # Custom React hooks
├── store/             # Zustand store
└── utils/             # Helpers
```

**Week 3: Backend API**

**Option A: FastAPI (Python)**
```python
# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from TTS.api import TTS

app = FastAPI()

# CORS for React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model (once at startup)
tts_model = TTS("manjussha/swara-bharat-kannada")

class TTSRequest(BaseModel):
    text: str
    language: str = "kn"
    dialect: str = "bangalore"
    emotion: str = "neutral"

@app.post("/api/v1/tts")
async def generate_speech(request: TTSRequest):
    # Generate audio
    audio = tts_model.tts(
        text=request.text,
        emotion=request.emotion,
        speaker=f"{request.dialect}_voice"
    )
    
    # Save and return URL
    # (Implementation details...)
    
    return {
        "audio_url": "https://...",
        "duration": len(audio) / 22050,
        "format": "wav"
    }

@app.post("/api/v1/stt")
async def transcribe_audio(file: UploadFile = File(...)):
    # Whisper transcription
    # (Implementation details...)
    
    return {
        "text": "transcribed text",
        "language": "kn",
        "confidence": 0.95
    }
```

**Week 4: Integration & Testing**
- Connect frontend to backend
- Test all features
- Fix bugs
- Performance optimization
- Deploy to Vercel + Render

---

## API & Integration

### Public API Design

**Base URL:** `https://api.swara-bharat.org/v1`

**Authentication:** API keys (future)

#### Endpoints

**1. Text-to-Speech**
```
POST /tts

Request:
{
  "text": "ನಮಸ್ಕಾರ ಹೇಗಿದ್ದೀರಿ",
  "language": "kn",
  "dialect": "bangalore",
  "emotion": "happy",
  "speed": 1.0,
  "format": "wav"
}

Response:
{
  "audio_url": "https://cdn.swara-bharat.org/audio/abc123.wav",
  "duration_seconds": 2.3,
  "text": "ನಮಸ್ಕಾರ ಹೇಗಿದ್ದೀರಿ",
  "metadata": {
    "language": "kn",
    "dialect": "bangalore",
    "emotion": "happy"
  }
}
```

**2. Speech-to-Text**
```
POST /stt

Request: (multipart/form-data)
- file: audio file
- language: "kn" (optional, auto-detect if not provided)

Response:
{
  "text": "ನಮಸ್ಕಾರ ಹೇಗಿದ್ದೀರಿ",
  "language": "kn",
  "dialect": "bangalore",
  "confidence": 0.95,
  "emotion": "happy",
  "duration_seconds": 2.3
}
```

**3. Conversational AI** (Phase 3)
```
POST /chat

Request:
{
  "message": "What's the weather?",
  "language": "kn",
  "voice_response": true,
  "emotion": "neutral"
}

Response:
{
  "text": "ಇಂದು ಬೆಂಗಳೂರಿನಲ್ಲಿ ಮಳೆಯಾಗಬಹುದು",
  "audio_url": "https://...",
  "emotion": "informative"
}
```

**4. List Voices**
```
GET /voices?language=kn&dialect=bangalore

Response:
{
  "voices": [
    {
      "id": "kn_bangalore_female_01",
      "name": "Bangalore Female Professional",
      "language": "kn",
      "dialect": "bangalore",
      "gender": "female",
      "sample_url": "https://..."
    },
    ...
  ]
}
```

### SDK Development

**Python SDK:**
```python
# pip install swara-bharat

from swara_bharat import SwaraBharat

client = SwaraBharat(api_key="your_key")

# Generate speech
audio = client.tts(
    text="ನಮಸ್ಕಾರ",
    language="kn",
    emotion="happy"
)
audio.save("output.wav")

# Transcribe
text = client.stt("audio.wav")
print(text)
```

**JavaScript SDK:**
```javascript
// npm install swara-bharat-js

import SwaraBharat from 'swara-bharat-js';

const client = new SwaraBharat({ apiKey: 'your_key' });

// Generate speech
const audio = await client.tts({
  text: 'ನಮಸ್ಕಾರ',
  language: 'kn',
  emotion: 'happy'
});

// Play in browser
const audioElement = new Audio(audio.url);
audioElement.play();
```

### Integrations

**1. WordPress Plugin**
```
Features:
- Gutenberg block for TTS
- Automatic post narration
- Multilingual support
- Voice selection

Usage:
[swara-bharat text="ನಮಸ್ಕಾರ" language="kn" emotion="happy"]
```

**2. Discord Bot**
```
Commands:
/speak [text] - Generate Kannada speech
/listen [attach audio] - Transcribe audio
/voice [list/select] - Choose voice
```

**3. Chrome Extension**
```
Features:
- Select text → Right-click → "Speak in Kannada"
- Auto-translate + speak
- Save favorite voices
```

**4. Zapier Integration**
```
Triggers:
- New form submission → Generate audio notification
- New email → Read aloud in Kannada
- Calendar event → Voice reminder
```

---

## Community & Growth

### Community Building Strategy

**Month 1-3: Foundation**
- GitHub repository public
- Clear documentation
- Welcoming README
- Contribution guidelines
- Issue templates

**Month 4-6: Early Adopters**
- Launch on ProductHunt
- Post on HackerNews
- Reddit (r/LocalLLaMA, r/MachineLearning, r/Kannada)
- LinkedIn/Twitter announcements
- Email 50 potential users directly

**Month 7-9: Growth**
- Conference talks (PyData, FOSSASIA)
- Blog posts and tutorials
- YouTube demos
- Podcast appearances
- University partnerships (IIT, IIIT)

**Month 10-12: Scale**
- Media coverage (YourStory, Inc42)
- Academic paper publication
- Corporate pilots (3-5 companies)
- Government engagement
- International visibility

### Contribution Workflow

**Types of Contributions:**

1. **Code** (GitHub PRs)
   - Bug fixes
   - New features
   - Performance improvements
   - Documentation

2. **Data** (Voice donations)
   - Record 30-60 min of speech
   - Multiple emotions
   - Different dialects
   - Quality validation

3. **Language Support**
   - New language data collection
   - Translation of docs
   - Dialect expertise
   - Cultural context

4. **Testing & Feedback**
   - Bug reports
   - Feature requests
   - Quality assessment
   - Use case examples

**Recognition System:**
- Contributors.md (all contributors listed)
- Badges (Bronze/Silver/Gold based on contribution)
- Certificates (shareable on LinkedIn)
- Featured profiles (monthly spotlight)
- Conference speaker opportunities

### Governance

**Decision Making:**
- Benevolent dictator (you) for first year
- Core team (3-5 people) from month 6
- RFC process for major changes
- Community voting on features

**Code of Conduct:**
- Contributor Covenant
- Zero tolerance for harassment
- Inclusive language
- Respectful disagreement

### Funding Strategy

**Year 1 (Bootstrap):**
- ₹10,000-15,000 from personal funds
- Free tier cloud services
- Volunteer contributors

**Year 2 (Grants):**
- Mozilla Open Source Support (MOSS)
- Google.org grants
- Indian government Digital India grants
- University research grants
- Target: ₹5-10 lakhs

**Year 3 (Sustainability):**
- Corporate sponsorships (AWS, Google Cloud credits)
- Premium API tier (freemium model)
- Consulting/support services
- Training workshops
- Target: Self-sustaining

---

## Cost Breakdown

### Year 1 Costs (Months 1-12)

**One-Time Costs:**
```
External drive (1TB SSD): ₹5,000
Raspberry Pi accessories: ₹2,000
Domain (swara-bharat.org): ₹800
Total one-time: ₹7,800
```

**Monthly Recurring:**
```
Internet (existing): ₹0
Electricity for Pi: ₹200
Cloud services (all free tier): ₹0
Total monthly: ₹200
```

**Yearly Recurring:**
```
Domain renewal: ₹800/year
Monthly costs: ₹200 × 12 = ₹2,400
Total yearly recurring: ₹3,200
```

**Optional (Quality Improvements):**
```
Colab Pro (if needed): ₹800/month × 3 months = ₹2,400
Voice actors (3 languages): ₹15,000
Better microphone: ₹5,000
Total optional: ₹22,400
```

**Total Year 1:**
- Minimum: ₹11,000 (bootstrap mode)
- Recommended: ₹30,000 (better quality)
- Maximum: ₹50,000 (professional quality)

### Cost per Language

**Data Collection & Processing:**
```
YouTube downloads: ₹0 (free)
Processing time (your time): 20 hours
Labeling (with volunteers): ₹0
Voice actors (optional): ₹5,000
Total: ₹0-5,000
```

**Training:**
```
Kaggle GPU (free): ₹0
Or Colab Pro: ₹800
Data storage (HF): ₹0
Total: ₹0-800
```

**Per Language Total: ₹0-5,800**

### Break-Even Analysis

**If you add premium tier in Year 2:**
```
Free tier: Unlimited (with rate limits)
Premium tier: ₹500/month per user
  - Faster processing
  - Higher limits
  - Voice cloning
  - Priority support

Break-even: 20-30 premium users
Timeline: Achievable by Month 18-24
```

---

## Success Metrics

### Technical Metrics

**v0.1 (Month 3):**
- [ ] 10+ hours Kannada training data
- [ ] 5 dialects supported
- [ ] 5 emotions working
- [ ] Model MOS score > 3.5
- [ ] Inference time < 5 seconds
- [ ] WER (Word Error Rate) < 15%

**v0.5 (Month 6):**
- [ ] 3 languages (Kannada, Tamil, Hindi)
- [ ] STT working (WER < 10%)
- [ ] Dashboard functional
- [ ] API response time < 2 seconds
- [ ] 99% uptime

**v0.8 (Month 9):**
- [ ] Conversational AI working
- [ ] Multi-turn dialog supported
- [ ] Latency < 3 seconds end-to-end
- [ ] Emotion detection accuracy > 80%

**v1.0 (Month 12):**
- [ ] 5+ languages
- [ ] Voice cloning working
- [ ] API handles 1000+ requests/day
- [ ] Model size optimized (<1 GB quantized)

### Community Metrics

**Month 3 (v0.1 launch):**
- [ ] 50+ GitHub stars
- [ ] 10+ contributors
- [ ] 100+ demo users
- [ ] 5+ feedback sessions

**Month 6 (v0.5):**
- [ ] 200+ GitHub stars
- [ ] 30+ contributors
- [ ] 500+ active users
- [ ] 10+ production deployments

**Month 9 (v0.8):**
- [ ] 500+ GitHub stars
- [ ] 50+ contributors
- [ ] 2,000+ active users
- [ ] 25+ production deployments
- [ ] 1 academic citation

**Month 12 (v1.0):**
- [ ] 1,000+ GitHub stars
- [ ] 100+ contributors
- [ ] 5,000+ active users
- [ ] 50+ production deployments
- [ ] 3+ academic citations
- [ ] 10+ media mentions

### Business Metrics (if applicable)

**Month 12:**
- [ ] API calls: 100,000+/month
- [ ] Premium users: 20-30
- [ ] Revenue: ₹10,000-15,000/month (if premium tier)
- [ ] Grant funding: ₹5-10 lakhs secured
- [ ] Corporate pilots: 3-5 companies

### Impact Metrics

**Qualitative:**
- [ ] Used in at least 1 educational institution
- [ ] Helped 1 content creator grow their channel
- [ ] Accessibility win (helped 1 visually impaired user)
- [ ] Preserved 1 endangered dialect

**Quantitative:**
- [ ] Total audio generated: 10,000+ hours
- [ ] Languages preserved: 5+
- [ ] Dialects documented: 15+
- [ ] Contributors from: 10+ cities

---

## Risk Mitigation

### Technical Risks

**Risk: Training data quality issues**
- Mitigation: Multi-stage quality checks, manual sampling
- Fallback: Reduce dataset size, focus on quality over quantity

**Risk: Model doesn't converge**
- Mitigation: Start with proven architecture (XTTS), incremental changes
- Fallback: Use pre-trained models with minimal fine-tuning

**Risk: Inference too slow**
- Mitigation: Model quantization, caching, CDN
- Fallback: Async processing, queue system

**Risk: HuggingFace rate limits**
- Mitigation: Self-hosting option, multiple accounts
- Fallback: Paid inference endpoints for premium users

### Community Risks

**Risk: Low adoption**
- Mitigation: Active marketing, clear value prop, easy onboarding
- Fallback: Pivot to specific niche (e.g., education only)

**Risk: No contributors**
- Mitigation: Good documentation, easy issues, recognition
- Fallback: Solo project for Year 1, ok

**Risk: Negative feedback**
- Mitigation: Quick response, transparent roadmap, user surveys
- Fallback: Iterate based on feedback, pivot if needed

### Legal Risks

**Risk: Copyright claims on training data**
- Mitigation: Document all sources, remove on request, fair use
- Fallback: Pivot to community-contributed data only

**Risk: Trademark issues with name**
- Mitigation: Check trademark databases, use .org domain
- Fallback: Rename if needed (early is easier)

### Financial Risks

**Risk: Costs exceed budget**
- Mitigation: Stick to free tiers, careful spending
- Fallback: Pause expensive features, seek grants

**Risk: Can't monetize**
- Mitigation: Open source first, monetization optional
- Fallback: Remain free/donation-based, that's ok

---

## Appendix

### Useful Resources

**Learning:**
- Fast.ai course: https://course.fast.ai
- HuggingFace Audio Course: https://huggingface.co/learn/audio-course
- TTS Papers: https://github.com/erogol/TTS-papers

**Communities:**
- r/LocalLLaMA
- r/MachineLearning
- HuggingFace Discord
- AI4Bharat community

**Tools:**
- Claude Code (AI coding assistant)
- GitHub Copilot
- Cursor (AI code editor)

### Glossary

- **TTS:** Text-to-Speech
- **STT:** Speech-to-Text
- **LLM:** Large Language Model
- **WER:** Word Error Rate
- **MOS:** Mean Opinion Score
- **Quantization:** Reducing model size
- **Fine-tuning:** Adapting pre-trained model
- **Inference:** Running model to generate output

### Contact

**Project Maintainer:**
- Name: Manju
- GitHub: @manjussha
- Email: (to be added)

**Project Links:**
- GitHub: https://github.com/manjussha/swara-bharat
- HuggingFace: https://huggingface.co/swara-bharat
- Website: https://swara-bharat.org (future)
- Discord: (to be created)

---

**Last Updated:** [Current Date]  
**Version:** 1.0  
**Status:** 🚀 Ready to Start

---

**Next Steps:**
1. Setup Mac (Day 1)
2. Setup Pi (Day 1)
3. Start data collection (Week 1)
4. Build processing pipeline (Week 2-3)
5. Train first model (Week 4-8)
6. Release v0.1 (Week 12)

**Remember:** 1-2 hours daily. Consistent progress > perfection.

Let's build Swara-Bharat! 🎙️🇮🇳