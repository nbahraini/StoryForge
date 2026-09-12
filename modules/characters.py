"""ماژول Characters با Mindmap"""
import streamlit as st
from datetime import datetime
from services.ai_service import ai_service
from services.i18n_service import t
from streamlit_echarts import st_echarts

def render():
    st.header(t("tab_chars"))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(t("new_char"))
        char_name = st.text_input(t("char_name"))
        char_roles = t("char_roles")
        char_role = st.selectbox(t("char_role"), char_roles)
        
        if st.button(t("build_sheet"), type="primary"):
            if char_name:
                prompt = f"""
                برای '{char_name}' با نقش '{char_role}' Character Sheet کامل بساز:
                Want، Need، Fear، Wound، Lie، Strengths، Fatal Flaw، Secret، 
                Moral Limits، Speech Pattern، Arc.
                
                سپس ۵ موقعیت چالش‌برانگیز طراحی کن.
                """
                with st.spinner("..."):
                    sheet = ai_service.get_response(prompt)
                    st.session_state.story_bible["characters"][char_name] = {
                        "role": char_role,
                        "sheet": sheet,
                        "created": datetime.now().isoformat()
                    }
                    st.success(f"{char_name} ✓")
            else:
                st.warning(t("enter_name"))
    
    with col2:
        st.subheader(t("char_list"))
        if st.session_state.story_bible["characters"]:
            for name, data in st.session_state.story_bible["characters"].items():
                with st.expander(f"👤 {name} ({data['role']})"):
                    st.markdown(data["sheet"])
                    if st.button(f"{t('delete')} {name}", key=f"del_{name}"):
                        del st.session_state.story_bible["characters"][name]
                        st.rerun()
        else:
            st.info(t("no_chars"))
    
    # Mindmap
    st.divider()
    st.subheader(t("mindmap_title"))
    
    view_mode = st.radio(
        "",
        [t("mindmap_view"), t("graph_view")],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if st.session_state.story_bible["characters"]:
        if view_mode == t("mindmap_view"):
            _render_mindmap()
        else:
            _render_graph()
    else:
        st.info(t("no_chars"))

def _render_mindmap():
    chars = st.session_state.story_bible["characters"]
    rels = st.session_state.story_bible["relationships"]
    
    role_groups = {}
    for name, data in chars.items():
        role = data["role"]
        if role not in role_groups:
            role_groups[role] = []
        role_groups[role].append(name)
    
    nodes = []
    edges = []
    
    nodes.append({
        "id": "story_root",
        "name": "📖 Story",
        "symbolSize": 70,
        "category": 0,
        "itemStyle": {"color": "#FFD700"}
    })
    
    role_colors = {
        "Protagonist": "#4CAF50", "قهرمان اصلی": "#4CAF50", "主人公": "#4CAF50",
        "Antagonist": "#f44336", "آنتاگونیست": "#f44336", "敵役": "#f44336",
        "Supporting": "#2196F3", "پشتیبان": "#2196F3", "サポート": "#2196F3",
        "Mentor": "#9C27B0", "مرشد": "#9C27B0", "師匠": "#9C27B0",
        "Rival": "#FF9800", "رقیب": "#FF9800", "ライバル": "#FF9800",
        "Love Interest": "#E91E63", "علاقه عاشقانه": "#E91E63", "恋愛対象": "#E91E63"
    }
    
    for role, members in role_groups.items():
        role_id = f"role_{role}"
        nodes.append({
            "id": role_id,
            "name": role,
            "symbolSize": 50,
            "category": 1,
            "itemStyle": {"color": role_colors.get(role, "#607D8B")}
        })
        edges.append({"source": "story_root", "target": role_id})
        
        for member in members:
            nodes.append({
                "id": member,
                "name": member,
                "symbolSize": 40,
                "category": 2,
                "itemStyle": {"color": role_colors.get(role, "#607D8B")}
            })
            edges.append({"source": role_id, "target": member})
    
    for rel in rels:
        edges.append({
            "source": rel["char1"],
            "target": rel["char2"],
            "label": {"show": True, "formatter": rel["type"]},
            "lineStyle": {"type": "dashed", "color": "#FF6B6B"}
        })
    
    option = {
        "title": {"text": t("mindmap_title"), "left": "center"},
        "series": [{
            "type": "graph",
            "layout": "force",
            "roam": True,
            "draggable": True,
            "data": nodes,
            "links": edges,
            "force": {"repulsion": 400, "gravity": 0.1, "edgeLength": [100, 200]},
            "label": {"show": True, "position": "right"},
            "lineStyle": {"color": "source", "curveness": 0.2}
        }]
    }
    
    st_echarts(options=option, height="600px", key="mindmap")

def _render_graph():
    from pyvis.network import Network
    import streamlit.components.v1 as components
    
    net = Network(height="600px", width="100%", bgcolor="#1e1e1e", font_color="white", directed=True)
    
    for char_name, char_data in st.session_state.story_bible["characters"].items():
        color = "#4CAF50" if "Protagonist" in char_data["role"] else "#f44336" if "Antagonist" in char_data["role"] else "#2196F3"
        net.add_node(char_name, label=char_name, color=color, size=30)
    
    for rel in st.session_state.story_bible["relationships"]:
        net.add_edge(rel["char1"], rel["char2"], label=rel["type"])
    
    net.save_graph("relationship_graph.html")
    with open("relationship_graph.html", 'r', encoding='utf-8') as f:
        components.html(f.read(), height=620)