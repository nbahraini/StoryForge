"""ماژول Plot & Arcs"""
import streamlit as st
from datetime import datetime
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("tab_plot"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t("master_arc"))
        if st.button(t("design_master"), type="primary"):
            ctx = _get_context()
            prompt = f"""
            Master Arc طراحی کن:
            {ctx}
            
            شامل: Beginning، Inciting Incident، First Reversal، Midpoint، 
            Major Loss، Revelation، Final Confrontation، Resolution
            """
            with st.spinner("..."):
                result = ai_service.get_response(prompt)
                st.session_state.story_bible["master_arc"]["design"] = result
                st.markdown(result)
    
    with col2:
        st.subheader(t("new_arc"))
        arc_name = st.text_input(t("arc_name"))
        arc_goal = st.text_area(t("arc_goal"), height=100)
        
        if st.button(t("build_arc")):
            if arc_name:
                ctx = _get_context()
                prompt = f"""
                برای Arc '{arc_name}' با هدف '{arc_goal}' Arc Bible بساز:
                {ctx}
                
                شامل: Protagonist's Goal، Antagonist، Mystery، Emotional Conflict، 
                Midpoint Twist، Climax، Permanent Consequence
                """
                with st.spinner("..."):
                    result = ai_service.get_response(prompt)
                    st.session_state.story_bible["arcs"].append({
                        "name": arc_name,
                        "goal": arc_goal,
                        "bible": result,
                        "created": datetime.now().isoformat()
                    })
                    st.success(f"{arc_name} ✓")
    
    if st.session_state.story_bible["arcs"]:
        st.divider()
        st.subheader(t("arc_list"))
        for arc in st.session_state.story_bible["arcs"]:
            with st.expander(f"📖 {arc['name']}"):
                st.markdown(f"**{t('arc_goal')}:** {arc['goal']}")
                st.markdown(arc["bible"])

def _get_context():
    bible = st.session_state.story_bible
    parts = []
    if bible["core_concept"].get("analysis"):
        parts.append(bible["core_concept"]["analysis"][:300])
    if bible["characters"]:
        chars = ", ".join([f"{n} ({d.get('role', '?')})" for n, d in bible["characters"].items()])
        parts.append(f"Characters: {chars}")
    return "\n".join(parts) if parts else "Empty"