"""سرویس مدیریت اتصال به AI"""
import streamlit as st
from openai import OpenAI

class AIService:
    def __init__(self):
        self.api_key = st.session_state.get("api_key")
        self.api_base = st.session_state.get("api_base", "https://api.openai.com/v1")
        self.model = st.session_state.get("model", "gpt-4o-mini")
        self.temperature = st.session_state.get("temperature", 0.8)
        self.max_tokens = st.session_state.get("max_tokens", 4000)
    
    def get_response(self, prompt, system_prompt=None, temperature=None):
        """دریافت پاسخ از AI"""
        if not self.api_key:
            return "⚠️ لطفاً API Key را وارد کنید."
        
        lang = st.session_state.get("lang", "fa")
        lang_instruction = {
            "fa": "پاسخ را به فارسی بنویس.",
            "en": "Write the response in English.",
            "ja": "回答を日本語で書いてください。"
        }.get(lang, "Write in English.")
        
        if system_prompt is None:
            role = st.session_state.get("current_ai_role", "Story Editor")
            system_prompt = f"You are an expert {role}. {lang_instruction}"
        else:
            system_prompt = f"{system_prompt} {lang_instruction}"
        
        client = OpenAI(api_key=self.api_key, base_url=self.api_base)
        
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature or self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ خطا: {str(e)}"

# Singleton instance
ai_service = AIService()