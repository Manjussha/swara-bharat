#!/usr/bin/env python3
"""
Swara-Bharat Live Dashboard
Web interface to monitor YouTube download automation
"""

from flask import Flask, render_template, jsonify
import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
import psutil

app = Flask(__name__)

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
LOGS_DIR = BASE_DIR / "logs"
CONFIG_FILE = Path(__file__).parent / "config.json"

def get_system_stats():
    """Get system statistics"""
    disk = psutil.disk_usage('/')
    memory = psutil.virtual_memory()

    return {
        'disk_total': disk.total / (1024**3),  # GB
        'disk_used': disk.used / (1024**3),
        'disk_free': disk.free / (1024**3),
        'disk_percent': disk.percent,
        'memory_total': memory.total / (1024**3),
        'memory_used': memory.used / (1024**3),
        'memory_percent': memory.percent,
        'cpu_percent': psutil.cpu_percent(interval=1)
    }

def get_download_stats():
    """Get download statistics"""
    stats = {
        'total_files': 0,
        'total_size_mb': 0,
        'by_category': {},
        'recent_downloads': []
    }

    if not DATA_DIR.exists():
        return stats

    # Count files by category
    for category_dir in DATA_DIR.iterdir():
        if category_dir.is_dir():
            files = list(category_dir.glob('*.mp3'))
            count = len(files)
            size = sum(f.stat().st_size for f in files) / (1024**2)  # MB

            stats['by_category'][category_dir.name] = {
                'count': count,
                'size_mb': round(size, 2)
            }
            stats['total_files'] += count
            stats['total_size_mb'] += size

            # Get recent files from this category
            for f in sorted(files, key=lambda x: x.stat().st_mtime, reverse=True)[:5]:
                stats['recent_downloads'].append({
                    'name': f.name,
                    'category': category_dir.name,
                    'size_mb': round(f.stat().st_size / (1024**2), 2),
                    'time': datetime.fromtimestamp(f.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                })

    stats['total_size_mb'] = round(stats['total_size_mb'], 2)
    stats['recent_downloads'] = sorted(stats['recent_downloads'],
                                      key=lambda x: x['time'],
                                      reverse=True)[:10]

    return stats

def get_process_status():
    """Check if scraper is running"""
    try:
        result = subprocess.run(
            ['pgrep', '-f', 'smart_scraper.py'],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except:
        return False

def get_recent_logs(lines=50):
    """Get recent log entries"""
    log_file = LOGS_DIR / "scraper.log"
    if not log_file.exists():
        return []

    try:
        with open(log_file, 'r') as f:
            return f.readlines()[-lines:]
    except:
        return []

def get_config():
    """Get current configuration"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/stats')
def api_stats():
    """API endpoint for all statistics"""
    return jsonify({
        'system': get_system_stats(),
        'downloads': get_download_stats(),
        'process': {
            'running': get_process_status(),
            'status': 'Running' if get_process_status() else 'Idle'
        },
        'config': get_config(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/logs')
def api_logs():
    """API endpoint for logs"""
    return jsonify({
        'logs': get_recent_logs(100),
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Create necessary directories
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    # Run server
    app.run(host='0.0.0.0', port=5000, debug=False)
