"""ماژول Anime Episode Planner"""
import streamlit as st
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("tab_anime"))
    
    st.info("🎬 تبدیل فصل‌های مانگا به اپیزودهای انیمه با زمان‌بندی دقیق")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # اضافه کردن key منحصر به فرد
        episode_num = st.number_input("شماره اپیزود:", min_value=1, value=1, key="anime_episode_num")
        duration = st.selectbox("مدت اپیزود:", ["20 دقیقه", "22 دقیقه", "24 دقیقه"], key="anime_duration")
        
        chapters = st.session_state.story_bible.get("chapters", [])
        chapter_options = [f"Chapter {c.get('number', i+1)}" for i, c in enumerate(chapters)]
        
        chapters_to_adapt = st.multiselect(
            "فصل‌های مانگا برای اقتباس:",
            options=chapter_options or ["Chapter 1"],
            default=chapter_options[:1] if chapter_options else ["Chapter 1"],
            key="anime_chapters_select"
        )
        
        if st.button("🎬 تولید Anime Episode Plan", type="primary", key="btn_gen_anime_plan"):
            prompt = f"""
            اپیزود {episode_num} انیمه ({duration}) را از فصل‌های {chapters_to_adapt} بساز.
            
            ساختار:
            - Cold Open (30 ثانیه)
            - Opening (90 ثانیه)
            - Act 1 (5 دقیقه)
            - Act 2 (7 دقیقه)
            - Climax (5 دقیقه)
            - Ending (2 دقیقه)
            - Post-credit scene (30 ثانیه)
            
            برای هر بخش: location، characters، action، dialogue، music mood
            """
            
            with st.spinner("در حال برنامه‌ریزی..."):
                result = ai_service.get_response(prompt)
                st.session_state.story_bible["episodes"].append({
                    "number": episode_num,
                    "duration": duration,
                    "chapters": chapters_to_adapt,
                    "plan": result
                })
                st.markdown(result)
    
    with col2:
        st.subheader("📺 اپیزودهای برنامه‌ریزی شده")
        for i, ep in enumerate(st.session_state.story_bible.get("episodes", [])):
            with st.expander(f"اپیزود {ep['number']} ({ep['duration']})", key=f"exp_anime_{i}"):
                st.markdown(ep["plan"])