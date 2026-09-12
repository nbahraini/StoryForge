"""تنظیمات مرکزی نرم‌افزار"""
import os
from pathlib import Path

# مسیرهای پایه
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
STORY_BIBLES_DIR = DATA_DIR / "story_bibles"
VERSIONS_DIR = DATA_DIR / "versions"
EXPORTS_DIR = DATA_DIR / "exports"
CHROMA_DB_DIR = DATA_DIR / "chroma_db"

# ایجاد پوشه‌ها
for dir_path in [STORY_BIBLES_DIR, VERSIONS_DIR, EXPORTS_DIR, CHROMA_DB_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# تنظیمات پیش‌فرض AI
DEFAULT_AI_CONFIG = {
    "api_base": "https://api.openai.com/v1",
    "model": "gpt-4o-mini",
    "temperature": 0.8,
    "max_tokens": 4000
}

# تنظیمات ComfyUI
COMFYUI_CONFIG = {
    "host": "http://127.0.0.1:8188",
    "workflow_file": "character_workflow.json"
}

# زبان‌های پشتیبانی
SUPPORTED_LANGUAGES = ["fa", "en", "ja"]
DEFAULT_LANGUAGE = "fa"

# نسخه نرم‌افزار
APP_VERSION = "2.0.0"