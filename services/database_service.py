"""سرویس مدیریت Story Bible"""
import json
import streamlit as st
from datetime import datetime
from config import STORY_BIBLES_DIR, VERSIONS_DIR

class DatabaseService:
    def __init__(self):
        self.current_bible_name = st.session_state.get("current_bible_name", "default")
    
    def get_default_bible(self):
        """ساخت Story Bible پیش‌فرض"""
        return {
            "metadata": {
                "name": self.current_bible_name,
                "created": datetime.now().isoformat(),
                "last_modified": datetime.now().isoformat(),
                "version": "2.0"
            },
            "core_concept": {"idea": "", "analysis": "", "logline_premise": ""},
            "world_bible": {"setting": "", "rules": [], "power_system_design": ""},
            "characters": {},
            "relationships": [],
            "master_arc": {"design": ""},
            "arcs": [],
            "chapters": [],
            "scripts": {"manga": [], "anime": []},
            "episodes": []
        }
    
    def save_bible(self, bible_data=None, name=None):
        """ذخیره Story Bible"""
        if bible_data is None:
            bible_data = st.session_state.story_bible
        if name is None:
            name = self.current_bible_name
        
        bible_data["metadata"]["last_modified"] = datetime.now().isoformat()
        file_path = STORY_BIBLES_DIR / f"{name}.json"
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(bible_data, f, ensure_ascii=False, indent=2)
        
        return file_path
    
    def load_bible(self, name):
        """بارگذاری Story Bible"""
        file_path = STORY_BIBLES_DIR / f"{name}.json"
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    
    def list_bibles(self):
        """لیست تمام Story Bibleها"""
        return [f.stem for f in STORY_BIBLES_DIR.glob("*.json")]
    
    def create_version(self, bible_data=None, version_name=None):
        """ساخت نسخه جدید"""
        if bible_data is None:
            bible_data = st.session_state.story_bible
        if version_name is None:
            version_name = f"v_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        file_path = VERSIONS_DIR / f"{version_name}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(bible_data, f, ensure_ascii=False, indent=2)
        
        return file_path
    
    def list_versions(self):
        """لیست تمام نسخه‌ها"""
        return [f.stem for f in VERSIONS_DIR.glob("*.json")]
    
    def load_version(self, version_name):
        """بارگذاری نسخه"""
        file_path = VERSIONS_DIR / f"{version_name}.json"
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

# Singleton instance
db_service = DatabaseService()