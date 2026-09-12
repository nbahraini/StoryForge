"""ماژول Core & Brainstorm"""
import streamlit as st
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("tab_core"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        idea = st.text_area(
            t("idea_input"),
            height=150,
            placeholder="مثلاً: در شهری که خاطرات انسان‌ها قابل خرید و فروش‌اند..."
        )
        
        if st.button(t("generate_core"), type="primary", use_container_width=True):
            if idea:
                prompt = f"""
                این ایده را تحلیل کن و Core Concept بساز:
                {idea}
                
                خروجی: Genre، Tone، Themes، Protagonist، Goal، Main Conflict، 
                Stakes، Central Mystery، Unique Hook.
                
                اگر چیزی ضعیف یا کلیشه‌ای است، ۳ راه بهبود پیشنهاد بده.
                """
                with st.spinner("..."):
                    result = ai_service.get_response(prompt)
                    st.session_state.story_bible["core_concept"]["idea"] = idea
                    st.session_state.story_bible["core_concept"]["analysis"] = result
                    st.markdown(result)
            else:
                st.warning(t("enter_idea"))
    
    with col2:
        if st.button(t("generate_logline")):
            ctx = _get_context()
            prompt = f"بر اساس این اطلاعات Logline و Premise بنویس:\n{ctx}"
            with st.spinner("..."):
                result = ai_service.get_response(prompt)
                st.session_state.story_bible["core_concept"]["logline_premise"] = result
                st.markdown(result)
    
    if st.session_state.story_bible["core_concept"].get("analysis"):
        st.divider()
        st.subheader(t("saved_core"))
        st.markdown(st.session_state.story_bible["core_concept"]["analysis"])

def _get_context():
    bible = st.session_state.story_bible
    parts = []
    if bible["core_concept"].get("analysis"):
        parts.append(bible["core_concept"]["analysis"][:500])
    return "\n".join(parts) if parts else "Empty"