#!/usr/bin/env python3
"""
Swara-Bharat Smart YouTube Scraper
Uses Qwen model to intelligently search and download YouTube content
"""

import os
import json
import logging
from datetime import datetime
from pathlib import Path
import time
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
    logging.info(f"Loaded .env from {env_path}")

# Configuration
CONFIG = {
    "qwen_model": "Qwen/Qwen2.5-1.5B-Instruct",  # Lightweight model
    "language": "kannada",
    "categories": ["news", "comedy", "educational", "motivational"],
    "downloads_per_category": 5,
    "audio_format": "mp3",
    "audio_quality": "320",
    "output_dir": "./data/raw",
    "hf_dataset_name": "manjussha/swara-bharat-kannada-raw",
    "log_file": "./logs/scraper.log"
}

# Setup logging
os.makedirs("./logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class QwenSearchGenerator:
    """Uses Qwen to generate intelligent YouTube search queries"""

    def __init__(self, model_name="Qwen/Qwen2.5-1.5B-Instruct"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self._load_model()

    def _load_model(self):
        """Load Qwen model (use API or local)"""
        try:
            # Option 1: Use HuggingFace Inference API (no local resources needed)
            from huggingface_hub import InferenceClient
            self.client = InferenceClient(token=os.getenv("HF_TOKEN"))
            logger.info(f"Loaded Qwen model via API: {self.model_name}")
        except Exception as e:
            logger.warning(f"Could not load via API: {e}")
            logger.info("Will use fallback search queries")
            self.client = None

    def generate_search_queries(self, language, category, num_queries=5):
        """Generate YouTube search queries using Qwen"""

        prompt = f"""Generate {num_queries} specific YouTube search queries to find high-quality {language} {category} content.

Requirements:
- Language: {language.title()}
- Category: {category}
- Focus on: Clear speech, professional production, 5-15 minute videos
- Include popular channels and recent content

Output format (JSON):
{{"queries": ["query1", "query2", ...]}}

Generate the queries:"""

        if self.client:
            try:
                response = self.client.text_generation(
                    prompt,
                    model=self.model_name,
                    max_new_tokens=300
                )
                # Try to extract JSON from response
                queries = self._extract_queries_from_response(response)
                if queries:
                    return queries
            except Exception as e:
                logger.warning(f"Qwen API error: {e}, using fallback")

        # Fallback: Pre-defined queries
        return self._fallback_queries(language, category, num_queries)

    def _extract_queries_from_response(self, response):
        """Extract queries from Qwen response"""
        try:
            # Try to find JSON in response
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = response[start:end]
                data = json.loads(json_str)
                return data.get("queries", [])
        except:
            pass
        return None

    def _fallback_queries(self, language, category, num_queries):
        """Fallback search queries if Qwen fails"""
        templates = {
            "kannada": {
                "news": [
                    "ಕನ್ನಡ ಸುದ್ದಿ tv9 bulletin",
                    "kannada news public tv today",
                    "kannada news bulletin highlights",
                    "suvarna news kannada summary",
                    "udaya news kannada today"
                ],
                "comedy": [
                    "kannada comedy scenes",
                    "kannada stand up comedy",
                    "majaa bharatha comedy",
                    "kannada comedy clips",
                    "weekend with ramesh comedy"
                ],
                "educational": [
                    "kannada educational videos",
                    "kannada science explanation",
                    "kannada tutorial",
                    "kannada knowledge videos",
                    "kannada learning content"
                ],
                "motivational": [
                    "kannada motivational speech",
                    "kannada inspiration",
                    "kannada life advice",
                    "kannada success stories",
                    "kannada personality development"
                ],
                "interviews": [
                    "kannada celebrity interview",
                    "kannada actor interview",
                    "kannada politician interview",
                    "kannada exclusive interview",
                    "kannada interview talk show"
                ],
                "discussion": [
                    "kannada panel discussion",
                    "kannada debate program",
                    "kannada talk show",
                    "kannada roundtable discussion",
                    "kannada opinion show"
                ],
                "podcasts": [
                    "kannada podcast",
                    "kannada audio talk",
                    "kannada storytelling",
                    "kannada conversation show",
                    "kannada radio program"
                ],
                "documentary": [
                    "kannada documentary",
                    "kannada history documentary",
                    "kannada nature documentary",
                    "kannada culture documentary",
                    "kannada science documentary"
                ]
            }
        }

        queries = templates.get(language, {}).get(category, [])
        return queries[:num_queries]


class YouTubeDownloader:
    """Download YouTube videos as audio"""

    def __init__(self, output_dir, audio_format="mp3", quality="320"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.audio_format = audio_format
        self.quality = quality

    def search_youtube(self, query, max_results=5):
        """Search YouTube and return video URLs"""
        try:
            import yt_dlp

            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                search_query = f"ytsearch{max_results}:{query}"
                result = ydl.extract_info(search_query, download=False)

                videos = []
                if 'entries' in result:
                    for entry in result['entries']:
                        if entry:
                            duration = entry.get('duration', 0)
                            is_live = entry.get('is_live', False)

                            # Skip live streams and check duration
                            if is_live:
                                logger.info(f"Skipping live stream: {entry.get('title', 'Unknown')}")
                                continue
                            if duration and (duration < 180 or duration > 1800):
                                logger.info(f"Skipping (duration {duration}s): {entry.get('title', 'Unknown')}")
                                continue

                            videos.append({
                                'url': f"https://www.youtube.com/watch?v={entry['id']}",
                                'title': entry.get('title', 'Unknown'),
                                'duration': duration,
                                'channel': entry.get('channel', 'Unknown')
                            })

                return videos
        except Exception as e:
            logger.error(f"YouTube search error: {e}")
            return []

    def download_audio(self, url, category):
        """Download audio from YouTube URL"""
        try:
            import yt_dlp

            category_dir = self.output_dir / category
            category_dir.mkdir(exist_ok=True)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': self.audio_format,
                    'preferredquality': self.quality,
                }],
                'outtmpl': str(category_dir / '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                # Change extension to mp3
                filename = filename.rsplit('.', 1)[0] + f'.{self.audio_format}'

                logger.info(f"Downloaded: {info.get('title', 'Unknown')}")
                return {
                    'filename': filename,
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'url': url,
                    'channel': info.get('channel'),
                    'upload_date': info.get('upload_date')
                }
        except Exception as e:
            logger.error(f"Download error for {url}: {e}")
            return None


class HuggingFaceUploader:
    """Upload datasets to HuggingFace Hub"""

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.hf_token = os.getenv("HF_TOKEN")

    def _get_api(self):
        """Get HuggingFace API client and ensure repo exists"""
        from huggingface_hub import HfApi, create_repo
        api = HfApi(token=self.hf_token)
        try:
            create_repo(
                self.dataset_name,
                repo_type="dataset",
                private=False,
                exist_ok=True,
                token=self.hf_token
            )
        except:
            pass
        return api

    def upload_single(self, file_path, download_info):
        """Upload a single confirmed file to HuggingFace, then delete it locally"""
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return False

        file_size = os.path.getsize(file_path)
        if file_size == 0:
            logger.error(f"File is empty (0 bytes), skipping: {file_path}")
            return False

        try:
            api = self._get_api()

            # Upload audio file into category subfolder on HF
            category = download_info.get('category', 'misc')
            repo_path = f"audio/{category}/{os.path.basename(file_path)}"

            logger.info(f"☁️  Uploading: {os.path.basename(file_path)} ({file_size / 1024**2:.1f} MB)")
            api.upload_file(
                path_or_fileobj=file_path,
                path_in_repo=repo_path,
                repo_id=self.dataset_name,
                repo_type="dataset",
                token=self.hf_token
            )
            logger.info(f"✅ Uploaded to HF: {repo_path}")

            # Log upload to local upload_log.json for dashboard
            upload_record = {
                'filename': os.path.basename(file_path),
                'category': category,
                'size_mb': round(file_size / 1024**2, 2),
                'title': download_info.get('title', ''),
                'channel': download_info.get('channel', ''),
                'duration': download_info.get('duration', 0),
                'url': download_info.get('url', ''),
                'hf_path': repo_path,
                'uploaded_at': datetime.now().isoformat()
            }
            upload_log_path = Path("./logs/upload_log.json")
            try:
                existing = json.loads(upload_log_path.read_text()) if upload_log_path.exists() else []
                existing.append(upload_record)
                upload_log_path.write_text(json.dumps(existing, indent=2))
            except Exception as e:
                logger.warning(f"Could not update upload_log.json: {e}")

            # Delete local file after confirmed upload
            try:
                os.remove(file_path)
                logger.info(f"🗑️  Deleted local: {os.path.basename(file_path)}")
            except Exception as e:
                logger.warning(f"Could not delete local file: {e}")

            return True
        except Exception as e:
            logger.error(f"HuggingFace upload error: {e}")
            return False

    def update_metadata(self, all_downloads):
        """Update metadata.json on HuggingFace with all download records"""
        try:
            api = self._get_api()
            metadata_path = "/tmp/metadata.json"
            with open(metadata_path, 'w') as f:
                json.dump({
                    'downloads': all_downloads,
                    'config': CONFIG,
                    'timestamp': datetime.now().isoformat(),
                    'total': len(all_downloads)
                }, f, indent=2)
            api.upload_file(
                path_or_fileobj=metadata_path,
                path_in_repo="metadata.json",
                repo_id=self.dataset_name,
                repo_type="dataset",
                token=self.hf_token
            )
            logger.info(f"📋 Metadata updated ({len(all_downloads)} total records)")
        except Exception as e:
            logger.warning(f"Metadata update error: {e}")


def main():
    """Main automation workflow"""
    logger.info("=" * 60)
    logger.info("Swara-Bharat Smart YouTube Scraper Started")
    logger.info("=" * 60)

    # Initialize components
    qwen = QwenSearchGenerator(CONFIG["qwen_model"])
    downloader = YouTubeDownloader(
        CONFIG["output_dir"],
        CONFIG["audio_format"],
        CONFIG["audio_quality"]
    )
    uploader = HuggingFaceUploader(CONFIG["hf_dataset_name"])

    all_records = []   # Full history for metadata
    total_uploaded = 0
    total_failed = 0

    # Load already-uploaded URLs from previous runs so we never re-download them
    upload_log_path = Path("./logs/upload_log.json")
    seen_urls = set()
    if upload_log_path.exists():
        try:
            prev = json.loads(upload_log_path.read_text())
            seen_urls = {r['url'] for r in prev if r.get('url')}
            logger.info(f"📋 Loaded {len(seen_urls)} already-uploaded URLs — will skip these")
        except Exception as e:
            logger.warning(f"Could not load upload_log.json: {e}")

    # Process each category
    for category in CONFIG["categories"]:
        logger.info(f"\n📁 Processing category: {category.upper()}")

        # Generate search queries using Qwen
        logger.info(f"🤖 Generating search queries with Qwen...")
        queries = qwen.generate_search_queries(
            CONFIG["language"],
            category,
            num_queries=3
        )
        logger.info(f"📝 Generated {len(queries)} queries: {queries}")

        category_count = 0

        # Search and download for each query
        for query in queries[:2]:  # Limit to 2 queries per category
            logger.info(f"\n🔍 Searching: {query}")

            videos = downloader.search_youtube(query, max_results=5)
            logger.info(f"Found {len(videos)} valid videos")

            for video in videos:
                if category_count >= CONFIG["downloads_per_category"]:
                    break

                # Skip already processed URLs (same video appearing in different queries/categories)
                if video['url'] in seen_urls:
                    logger.info(f"⏭️  Skipping duplicate: {video['title'][:50]}")
                    continue
                seen_urls.add(video['url'])

                logger.info(f"⬇️  Downloading: {video['title'][:50]}...")

                download_info = downloader.download_audio(video['url'], category)

                if download_info and download_info.get('filename'):
                    download_info['category'] = category
                    download_info['search_query'] = query

                    # Immediately upload once download is confirmed complete
                    success = uploader.upload_single(download_info['filename'], download_info)

                    if success:
                        total_uploaded += 1
                        category_count += 1
                        all_records.append(download_info)
                        logger.info(f"[{total_uploaded} uploaded] {category}: {category_count}/{CONFIG['downloads_per_category']}")
                    else:
                        total_failed += 1
                        logger.warning(f"❌ Upload failed, file kept locally for retry")
                else:
                    logger.warning(f"Download failed or file missing, skipping")

                # Be nice to YouTube
                time.sleep(2)

    # Update final metadata on HuggingFace
    if all_records:
        uploader.update_metadata(all_records)

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info(f"✅ Scraping completed!")
    logger.info(f"📊 Uploaded: {total_uploaded} files")
    logger.info(f"❌ Failed:   {total_failed} files")
    logger.info(f"💾 Local files: Auto-deleted after each upload")
    logger.info(f"☁️  HuggingFace: {CONFIG['hf_dataset_name']}")
    logger.info(f"🎉 All {total_uploaded} files safely in cloud!")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
