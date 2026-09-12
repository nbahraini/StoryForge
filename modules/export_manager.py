"""ماژول Export Manager"""
import streamlit as st
import json
from datetime import datetime
from pathlib import Path
from config import EXPORTS_DIR
from services.i18n_service import t

def render():
    st.header(t("tab_export"))
    
    st.info("📊 خروجی گرفتن از Story Bible در فرمت‌های مختلف")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Export به JSON", type="primary", use_container_width=True):
            file_path = EXPORTS_DIR / f"story_bible_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(st.session_state.story_bible, f, ensure_ascii=False, indent=2)
            st.success(f"ذخیره شد: {file_path}")
    
    with col2:
        if st.button("📝 Export به Markdown", use_container_width=True):
            md_content = _generate_markdown()
            file_path = EXPORTS_DIR / f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            st.success(f"ذخیره شد: {file_path}")
    
    with col3:
        if st.button("📜 Export به Final Draft", use_container_width=True):
            fdx_content = _generate_fdx()
            file_path = EXPORTS_DIR / f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.fdx"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fdx_content)
            st.success(f"ذخیره شد: {file_path}")
    
    st.divider()
    st.subheader("📁 فایل‌های خروجی")
    
    files = list(EXPORTS_DIR.glob("*"))
    if files:
        for file in files:
            st.text(f"{file.name} ({file.stat().st_size} bytes)")
    else:
        st.info("هنوز فایلی export نشده است.")

def _generate_markdown():
    bible = st.session_state.story_bible
    md = f"# {bible['metadata']['name']}\n\n"
    md += f"Created: {bible['metadata']['created']}\n\n"
    
    if bible["core_concept"].get("analysis"):
        md += "## Core Concept\n\n"
        md += bible["core_concept"]["analysis"] + "\n\n"
    
    if bible["characters"]:
        md += "## Characters\n\n"
        for name, data in bible["characters"].items():
            md += f"### {name} ({data['role']})\n\n"
            md += data["sheet"] + "\n\n"
    
    if bible["scripts"]["manga"]:
        md += "## Manga Scripts\n\n"
        for script in bible["scripts"]["manga"]:
            md += f"### Chapter {script['chapter']}\n\n"
            md += script["script"] + "\n\n"
    
    return md

def _generate_fdx():
    """تولید فرمت Final Draft (FDX)"""
    bible = st.session_state.story_bible
    fdx = '<?xml version="1.0" encoding="UTF-8"?>\n'
    fdx += '<FinalDraft DocumentType="Script" Template="No" Version="1">\n'
    fdx += '<Content>\n'
    
    for script in bible["scripts"]["manga"]:
        fdx += f'<Paragraph Type="Scene Heading">\n'
        fdx += f'<Text>CHAPTER {script["chapter"]}</Text>\n'
        fdx += '</Paragraph>\n'
        
        fdx += f'<Paragraph Type="Action">\n'
        fdx += f'<Text>{script["outline"]}</Text>\n'
        fdx += '</Paragraph>\n'
    
    fdx += '</Content>\n'
    fdx += '</FinalDraft>'
    return fdx