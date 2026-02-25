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

def get_upload_stats():
    """Get upload statistics from upload_log.json"""
    stats = {
        'total_files': 0,
        'total_size_mb': 0,
        'by_category': {},
        'recent_uploads': []
    }

    upload_log = LOGS_DIR / "upload_log.json"
    if not upload_log.exists():
        return stats

    try:
        records = json.loads(upload_log.read_text())
    except:
        return stats

    for r in records:
        category = r.get('category', 'misc')
        size_mb = r.get('size_mb', 0)

        if category not in stats['by_category']:
            stats['by_category'][category] = {'count': 0, 'size_mb': 0}
        stats['by_category'][category]['count'] += 1
        stats['by_category'][category]['size_mb'] = round(
            stats['by_category'][category]['size_mb'] + size_mb, 2
        )
        stats['total_files'] += 1
        stats['total_size_mb'] += size_mb

    stats['total_size_mb'] = round(stats['total_size_mb'], 2)

    # Most recent 10 uploads
    stats['recent_uploads'] = [
        {
            'name': r.get('filename', ''),
            'category': r.get('category', ''),
            'size_mb': r.get('size_mb', 0),
            'time': r.get('uploaded_at', '')[:19].replace('T', ' '),
            'channel': r.get('channel', ''),
            'duration': r.get('duration', 0)
        }
        for r in reversed(records[-10:])
    ]

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
        'uploads': get_upload_stats(),
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
