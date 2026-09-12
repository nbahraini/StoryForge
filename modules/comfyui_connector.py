"""ماژول ComfyUI Connector"""
import streamlit as st
from services.comfyui_service import comfyui_service
from services.i18n_service import t

def render():
    st.header(t("tab_images"))
    
    if not comfyui_service.check_connection():
        st.error("❌ اتصال به ComfyUI برقرار نیست. لطفاً ComfyUI را اجرا کنید.")
        st.info("ComfyUI باید در آدرس http://127.0.0.1:8188 در حال اجرا باشد.")
        return
    
    st.success("✅ اتصال به ComfyUI برقرار است")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎨 تولید تصویر کاراکتر")
        
        chars = list(st.session_state.story_bible["characters"].keys())
        if not chars:
            st.warning("هیچ شخصیتی تعریف نشده است.")
            return
        
        character_name = st.selectbox("شخصیت:", chars)
        char_data = st.session_state.story_bible["characters"][character_name]
        
        prompt = st.text_area(
            "توضیح تصویر:",
            value=f"anime character, {character_name}, {char_data.get('role', '')}, detailed face, high quality, masterpiece",
            height=100
        )
        
        negative_prompt = st.text_area("Negative Prompt:", value="low quality, blurry, deformed")
        
        steps = st.slider("Steps:", 10, 50, 20)
        cfg = st.slider("CFG Scale:", 1, 15, 7)
        
        if st.button("🖼️ تولید تصویر", type="primary"):
            with st.spinner("در حال تولید..."):
                result = comfyui_service.get_image(prompt, negative_prompt, steps, cfg)
                
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.success("تصویر در ComfyUI در حال تولید است...")
                    st.info("برای دیدن نتیجه، ComfyUI UI را در مرورگر باز کنید.")
    
    with col2:
        st.subheader("📋 Character Sheets")
        for name, data in st.session_state.story_bible["characters"].items():
            with st.expander(f"👤 {name}"):
                st.markdown(data.get("sheet", "No sheet")[:500])