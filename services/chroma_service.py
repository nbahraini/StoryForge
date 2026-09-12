"""سرویس Vector Database با ChromaDB"""
import chromadb
from chromadb.config import Settings
from config import CHROMA_DB_DIR

class ChromaService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))
        self.collection = self.client.get_or_create_collection(
            name="story_chapters",
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_chapter(self, chapter_id, content, metadata=None):
        """افزودن فصل به Vector DB"""
        self.collection.add(
            documents=[content],
            metadatas=[metadata or {}],
            ids=[chapter_id]
        )
    
    def search_similar(self, query, n_results=5):
        """جستجوی معنایی"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
    
    def delete_chapter(self, chapter_id):
        """حذف فصل"""
        self.collection.delete(ids=[chapter_id])
    
    def get_all_chapters(self):
        """دریافت تمام فصل‌ها"""
        return self.collection.get()

# Singleton instance
chroma_service = ChromaService()