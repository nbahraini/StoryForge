"""ماژول Markdown Editor"""
import streamlit as st
from services.chroma_service import chroma_service
from services.i18n_service import t

def render():
    st.header(t("tab_editor"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # اضافه کردن key منحصر به فرد
        chapter_num = st.number_input("شماره فصل:", min_value=1, value=1, key="editor_chapter_num")
        chapter_title = st.text_input("عنوان فصل:", key="editor_chapter_title")
        
        content = st.text_area(
            "محتوای فصل (Markdown):",
            height=500,
            value=st.session_state.get("editor_content", ""),
            key="editor_content_area"
        )
        
        if content != st.session_state.get("editor_content"):
            st.session_state.editor_content = content
        
        col_save, col_index = st.columns(2)
        with col_save:
            if st.button("💾 ذخیره فصل", type="primary", key="btn_save_chapter"):
                chapter_data = {
                    "number": chapter_num,
                    "title": chapter_title,
                    "content": content
                }
                # حذف فصل قبلی با همان شماره برای جلوگیری از تکرار
                st.session_state.story_bible["chapters"] = [
                    c for c in st.session_state.story_bible["chapters"]
                    if c.get("number") != chapter_num
                ]
                st.session_state.story_bible["chapters"].append(chapter_data)
                st.success("ذخیره شد!")
        
        with col_index:
            if st.button("📚 ایندکس در Vector DB", key="btn_index_chapter"):
                chroma_service.add_chapter(
                    chapter_id=f"chapter_{chapter_num}",
                    content=content,
                    metadata={
                        "chapter": chapter_num,
                        "title": chapter_title
                    }
                )
                st.success("ایندکس شد!")
    
    with col2:
        st.subheader("📖 فصل‌های ذخیره شده")
        for chapter in st.session_state.story_bible.get("chapters", []):
            if st.button(f"📄 فصل {chapter['number']}: {chapter['title']}", key=f"btn_load_ch_{chapter['number']}"):
                st.session_state.editor_content = chapter["content"]
                st.rerun()
        
        st.divider()
        st.subheader("👁️ Preview")
        st.markdown(content)