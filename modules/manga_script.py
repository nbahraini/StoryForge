"""ماژول Manga Script"""
import streamlit as st
from datetime import datetime
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("manga_gen"))
    
    # اضافه کردن key منحصر به فرد
    chapter_num = st.number_input(t("chapter_num"), min_value=1, value=1, key="manga_chapter_num")
    chapter_outline = st.text_area(t("chapter_outline"), height=150, key="manga_chapter_outline")
    
    if st.button(t("gen_script"), type="primary", key="btn_gen_manga_script"):
        if chapter_outline:
            ctx = _get_context()
            prompt = f"""
            فصل {chapter_num} را به Manga Script تبدیل کن:
            {chapter_outline}
            
            {ctx}
            
            فرمت: PAGE X — N PANELS
            Panel 1: [Composition] — [Visual]
            Dialogue: ...
            SFX: ...
            
            Silent panelها و page-turn revealها را فراموش نکن.
            """
            with st.spinner("..."):
                result = ai_service.get_response(prompt)
                st.session_state.story_bible["scripts"]["manga"].append({
                    "chapter": chapter_num,
                    "outline": chapter_outline,
                    "script": result,
                    "created": datetime.now().isoformat()
                })
                st.markdown(result)
        else:
            st.warning(t("enter_outline"))
    
    if st.session_state.story_bible["scripts"]["manga"]:
        st.divider()
        st.subheader(t("saved_scripts"))
        for i, script in enumerate(st.session_state.story_bible["scripts"]["manga"]):
            with st.expander(f"{t('chapters')} {script['chapter']}", key=f"exp_manga_{i}"):
                st.markdown(script["script"])

def _get_context():
    bible = st.session_state.story_bible
    parts = []
    if bible["characters"]:
        chars = ", ".join(bible["characters"].keys())
        parts.append(f"Characters: {chars}")
    return "\n".join(parts) if parts else "Empty"