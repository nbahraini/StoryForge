"""ماژول Versioning"""
import streamlit as st
import os
from services.database_service import db_service
from services.i18n_service import t
from config import VERSIONS_DIR

def render():
    st.header(t("tab_versions"))
    
    st.info("🔄 مدیریت نسخه‌های مختلف Story Bible")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💾 ساخت نسخه جدید")
        version_name = st.text_input(
            "نام نسخه:",
            value=f"v_{st.session_state.story_bible['metadata']['last_modified'][:10]}"
        )
        
        if st.button("📸 Snapshot", type="primary"):
            file_path = db_service.create_version(version_name=version_name)
            st.success(f"نسخه '{version_name}' ذخیره شد!")
    
    with col2:
        st.subheader("📜 لیست نسخه‌ها")
        versions = db_service.list_versions()
        
        if versions:
            for version in versions:
                col_v, col_load, col_delete = st.columns([2, 1, 1])
                with col_v:
                    st.text(version)
                with col_load:
                    if st.button("📂 Load", key=f"load_{version}"):
                        loaded = db_service.load_version(version)
                        if loaded:
                            st.session_state.story_bible = loaded
                            st.success("بارگذاری شد!")
                            st.rerun()
                with col_delete:
                    if st.button("🗑️", key=f"del_{version}"):
                        os.remove(VERSIONS_DIR / f"{version}.json")
                        st.rerun()
        else:
            st.info("هنوز نسخه‌ای ذخیره نشده است.")