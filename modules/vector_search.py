"""ماژول Vector Search"""
import streamlit as st
from services.chroma_service import chroma_service
from services.i18n_service import t

def render():
    st.header(t("tab_search"))
    
    st.info("💡 جستجوی معنایی در تمام فصل‌های نوشته شده برای جلوگیری از Plot Hole")
    
    query = st.text_area("سؤال یا موضوع مورد جستجو:", height=100)
    n_results = st.slider("تعداد نتایج:", 1, 20, 5)
    
    if st.button("🔍 جستجو", type="primary"):
        if query:
            with st.spinner("در حال جستجو..."):
                results = chroma_service.search_similar(query, n_results)
                
                if results["documents"]:
                    st.subheader("نتایج جستجو:")
                    for i, (doc, metadata, distance) in enumerate(zip(
                        results["documents"][0],
                        results["metadatas"][0],
                        results["distances"][0]
                    )):
                        with st.expander(f"نتیجه {i+1} - شباهت: {1-distance:.2f}"):
                            st.markdown(f"**فصل:** {metadata.get('chapter', 'N/A')}")
                            st.markdown(f"**Arc:** {metadata.get('arc', 'N/A')}")
                            st.markdown(doc)
                else:
                    st.warning("نتیجه‌ای یافت نشد.")
    
    st.divider()
    st.subheader("📊 آمار Vector Database")
    all_docs = chroma_service.get_all_chapters()
    st.metric("تعداد فصل‌های ایندکس شده", len(all_docs["ids"]))