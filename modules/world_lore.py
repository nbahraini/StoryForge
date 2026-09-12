"""ماژول World & Lore"""
import streamlit as st
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("tab_world"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t("world_setting"))
        world_setting = st.text_area(
            "",
            height=100,
            label_visibility="collapsed",
            value=st.session_state.story_bible["world_bible"].get("setting", "")
        )
        
        st.subheader(t("world_rules"))
        world_rules = st.text_area(
            "",
            height=150,
            label_visibility="collapsed",
            value="\n".join(st.session_state.story_bible["world_bible"].get("rules", []))
        )
        
        if st.button(t("save_rules")):
            st.session_state.story_bible["world_bible"]["setting"] = world_setting
            st.session_state.story_bible["world_bible"]["rules"] = [
                r.strip() for r in world_rules.split("\n") if r.strip()
            ]
            st.success(t("saved_success"))
    
    with col2:
        if st.button(t("design_power"), type="primary"):
            ctx = _get_context()
            prompt = f"""
            سیستم قدرت طراحی کن:
            {ctx}
            
            شامل: Source، Limitations، Costs، Counters، Progression، 
            Rare Abilities، Loopholes
            """
            with st.spinner("..."):
                result = ai_service.get_response(prompt)
                st.session_state.story_bible["world_bible"]["power_system_design"] = result
                st.markdown(result)
    
    if st.session_state.story_bible["world_bible"].get("power_system_design"):
        st.divider()
        st.subheader(t("saved_power"))
        st.markdown(st.session_state.story_bible["world_bible"]["power_system_design"])

def _get_context():
    bible = st.session_state.story_bible
    parts = []
    if bible["core_concept"].get("analysis"):
        parts.append(bible["core_concept"]["analysis"][:300])
    if bible["world_bible"].get("setting"):
        parts.append(f"Setting: {bible['world_bible']['setting']}")
    return "\n".join(parts) if parts else "Empty"