"""ماژول Relationships"""
import streamlit as st
from datetime import datetime
from services.i18n_service import t

def render():
    st.header(t("graph_title"))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(t("add_relation"))
        chars = list(st.session_state.story_bible["characters"].keys())
        
        if len(chars) >= 2:
            rel_char1 = st.selectbox(t("char1"), chars)
            rel_char2 = st.selectbox(t("char2"), chars)
            rel_types = t("rel_types")
            rel_type = st.selectbox(t("rel_type"), rel_types)
            rel_desc = st.text_area(t("rel_desc"), height=100)
            
            if st.button(t("add_rel_btn"), type="primary"):
                if rel_char1 != rel_char2:
                    st.session_state.story_bible["relationships"].append({
                        "char1": rel_char1,
                        "char2": rel_char2,
                        "type": rel_type,
                        "description": rel_desc,
                        "created": datetime.now().isoformat()
                    })
                    st.success(t("added_success"))
                    st.rerun()
        else:
            st.warning(t("need_2_chars"))
    
    with col2:
        if st.session_state.story_bible["relationships"]:
            st.subheader(t("rel_list"))
            for i, rel in enumerate(st.session_state.story_bible["relationships"]):
                with st.expander(f"{rel['char1']} ↔ {rel['char2']} ({rel['type']})"):
                    st.markdown(f"**{t('rel_desc')}** {rel.get('description', '')}")
                    if st.button(t("delete"), key=f"del_rel_{i}"):
                        st.session_state.story_bible["relationships"].pop(i)
                        st.rerun()
        else:
            st.info(t("no_rels"))