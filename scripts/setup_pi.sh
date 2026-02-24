#!/bin/bash
# Setup script for Raspberry Pi

echo "🚀 Setting up Swara-Bharat Smart Scraper on Raspberry Pi"
echo "=========================================================="

# Update system
echo "📦 Updating system packages..."
sudo apt update
sudo apt upgrade -y

# Install Python and pip
echo "🐍 Installing Python 3..."
sudo apt install -y python3 python3-pip python3-venv

# Install ffmpeg (required for yt-dlp audio extraction)
echo "🎵 Installing ffmpeg..."
sudo apt install -y ffmpeg

# Create virtual environment
echo "📁 Creating virtual environment..."
cd ~/swara-bharat
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python packages..."
pip install --upgrade pip
pip install -r scripts/requirements.txt

# Create directories
echo "📂 Creating project directories..."
mkdir -p data/raw/{news,comedy,educational,motivational}
mkdir -p logs
mkdir -p models

# Setup environment file
echo "🔑 Setting up environment variables..."
if [ ! -f scripts/.env ]; then
    cp scripts/.env.example scripts/.env
    echo "⚠️  Please edit scripts/.env and add your HuggingFace token!"
fi

# Test installations
echo "🧪 Testing installations..."
echo "Python version:"
python3 --version

echo "yt-dlp version:"
yt-dlp --version

echo "ffmpeg version:"
ffmpeg -version | head -n 1

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit scripts/.env and add your HuggingFace token"
echo "2. Run: source venv/bin/activate"
echo "3. Test: python3 scripts/smart_scraper.py"
echo ""
echo "To schedule automation:"
echo "Run: crontab -e"
echo "Add: 0 2 * * * cd ~/swara-bharat && venv/bin/python3 scripts/smart_scraper.py"
