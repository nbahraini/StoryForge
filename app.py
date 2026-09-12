"""نقطه ورود اصلی نرم‌افزار"""
import streamlit as st
from config import APP_VERSION
from services.database_service import db_service
from services.i18n_service import t

# ============================================
# 1. تنظیمات صفحه
# ============================================
st.set_page_config(
    page_title="Manga/Anime Story Engine",
    layout="wide",
    page_icon="🎬",
    initial_sidebar_state="expanded"
)

# ============================================
# 2. مقداردهی اولیه Session State
# ============================================
if "story_bible" not in st.session_state:
    st.session_state.story_bible = db_service.get_default_bible()

if "lang" not in st.session_state:
    st.session_state.lang = "fa"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_ai_role" not in st.session_state:
    st.session_state.current_ai_role = "Story Editor"

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

if "api_base" not in st.session_state:
    st.session_state.api_base = "https://api.openai.com/v1"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.8

if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 4000

if "editor_content" not in st.session_state:
    st.session_state.editor_content = ""

# ============================================
# 3. اعمال استایل RTL برای فارسی
# ============================================
def apply_language_style():
    lang = st.session_state.get("lang", "fa")
    if lang == "fa":
        st.markdown("""
        <style>
        .stApp { direction: rtl; }
        .stChatMessage { direction: rtl; text-align: right; }
        h1, h2, h3, h4, h5, p, span, label, div { font-family: 'Vazirmatn', 'Tahoma', sans-serif !important; }
        </style>
        <link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css" rel="stylesheet" type="text/css" />
        """, unsafe_allow_html=True)

apply_language_style()

# ============================================
# 4. سایدبار (تنظیمات و مدیریت)
# ============================================
with st.sidebar:
    st.title("⚙️ تنظیمات")
    st.caption(f"نسخه {APP_VERSION}")
    
    # انتخاب زبان
    lang_options = {"fa": "🇮🇷 فارسی", "en": "🇬🇧 English", "ja": "🇯🇵 日本語"}
    selected_lang = st.selectbox(
        "زبان / Language / 言語",
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=list(lang_options.keys()).index(st.session_state.lang)
    )
    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        st.rerun()
    
    st.divider()
    
    # تنظیمات AI
    st.subheader("🔑 AI Settings")
    st.session_state.api_key = st.text_input("API Key:", type="password", value=st.session_state.api_key)
    st.session_state.api_base = st.text_input("API Base:", value=st.session_state.api_base)
    st.session_state.model = st.text_input("Model:", value=st.session_state.model)
    st.session_state.temperature = st.slider("Temperature:", 0.0, 2.0, st.session_state.temperature, 0.1)
    
    st.divider()
    
    # مدیریت Story Bible
    st.subheader("💾 Story Bible")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save", use_container_width=True):
            db_service.save_bible()
            st.success("Saved!")
    with col2:
        if st.button("📂 Load", use_container_width=True):
            bibles = db_service.list_bibles()
            if bibles:
                st.session_state.story_bible = db_service.load_bible(bibles[0])
                st.success("Loaded!")
                st.rerun()
            else:
                st.warning("No saved bibles found.")

# ============================================
# 5. بدنه اصلی و تب‌ها
# ============================================
st.title(t("app_title"))

# وارد کردن ماژول‌ها
from modules import (
    core_brainstorm, world_lore, characters, relationships,
    plot_arcs, manga_script, anime_planner, ai_copilot,
    vector_search, markdown_editor, export_manager,
    comfyui_connector, versioning, collaboration
)

# تعریف تب‌ها
tabs = st.tabs([
    t("tab_core"), t("tab_world"), t("tab_chars"), t("tab_relations"),
    t("tab_plot"), t("tab_script"), t("tab_anime"), t("tab_copilot"),
    t("tab_search"), t("tab_editor"), t("tab_export"), t("tab_images"),
    t("tab_versions"), t("tab_collab")
])

# رندر ماژول‌ها در تب‌های مربوطه
with tabs[0]: core_brainstorm.render()
with tabs[1]: world_lore.render()
with tabs[2]: characters.render()
with tabs[3]: relationships.render()
with tabs[4]: plot_arcs.render()
with tabs[5]: manga_script.render()
with tabs[6]: anime_planner.render()
with tabs[7]: ai_copilot.render()
with tabs[8]: vector_search.render()
with tabs[9]: markdown_editor.render()
with tabs[10]: export_manager.render()
with tabs[11]: comfyui_connector.render()
with tabs[12]: versioning.render()
with tabs[13]: collaboration.render()

# ============================================
# 6. Footer
# ============================================
st.divider()
st.caption("Manga/Anime Story Engine v2.0 | Built with Streamlit + ChromaDB + OpenAI")