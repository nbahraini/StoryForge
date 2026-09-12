"""ماژول AI Co-Pilot"""
import streamlit as st
from services.ai_service import ai_service
from services.i18n_service import t

def render():
    st.header(t("copilot_title"))
    st.caption(t("copilot_caption"))
    
    roles_dict = t("roles")
    role_keys = list(roles_dict.keys())
    role_display = st.selectbox(
        t("ai_role"),
        role_keys,
        format_func=lambda x: roles_dict[x]
    )
    st.session_state.current_ai_role = role_display
    
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    if prompt := st.chat_input(t("chat_input")):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        ctx = _get_context()
        full_prompt = f"""
        نقش: {st.session_state.current_ai_role}
        
        Story Bible:
        {ctx}
        
        درخواست: {prompt}
        """
        
        with st.chat_message("assistant"):
            with st.spinner("..."):
                response = ai_service.get_response(full_prompt)
                st.markdown(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    if st.button(t("clear_chat")):
        st.session_state.chat_history = []
        st.rerun()

def _get_context():
    bible = st.session_state.story_bible
    parts = []
    if bible["core_concept"].get("analysis"):
        parts.append(bible["core_concept"]["analysis"][:500])
    if bible["characters"]:
        chars = ", ".join([f"{n} ({d.get('role', '?')})" for n, d in bible["characters"].items()])
        parts.append(f"Characters: {chars}")
    return "\n".join(parts) if parts else "Empty"