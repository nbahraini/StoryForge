"""سرویس چندزبانگی"""
import streamlit as st

TRANSLATIONS = {
    "en": {
        "app_title": "🎬 Manga/Anime Story Engine",
        "tab_core": "🧠 Core & Brainstorm",
        "tab_world": "🌍 World & Lore",
        "tab_chars": "👥 Characters",
        "tab_relations": "🕸️ Relations",
        "tab_plot": "📖 Plot & Arcs",
        "tab_script": "✍️ Manga Script",
        "tab_anime": "🎬 Anime Planner",
        "tab_copilot": "💬 AI Co-Pilot",
        "tab_search": "🔍 Semantic Search",
        "tab_editor": "📝 Editor",
        "tab_export": "📊 Export",
        "tab_images": "🎨 Image Gen",
        "tab_versions": "🔄 Versions",
        "tab_collab": "👥 Team",
        
        # Core & Brainstorm
        "idea_input": "Write your 2-line story idea:",
        "generate_core": "🚀 Generate Core Concept",
        "generate_logline": "✨ Generate Logline & Premise",
        "saved_core": "📝 Saved Core Concept",
        "enter_idea": "Please enter your idea first.",
        
        # World & Lore
        "world_setting": "World Setting:",
        "world_rules": "Main World Rules:",
        "save_rules": "💾 Save World Rules",
        "design_power": "🔮 Design Power System with AI",
        "saved_power": "📜 Designed Power System",
        
        # Characters
        "new_char": "New Character",
        "char_name": "Character Name:",
        "char_role": "Role:",
        "build_sheet": "🎭 Build Character Sheet with AI",
        "char_list": "Character List",
        "mindmap_title": "🧠 Character Mindmap",
        "mindmap_view": "Mindmap View",
        "graph_view": "Relationship Graph",
        "no_chars": "No characters created yet.",
        "enter_name": "Please enter character name.",
        
        # Relationships
        "graph_title": "🕸️ Relationship Graph",
        "add_relation": "Add Relationship",
        "char1": "First Character:",
        "char2": "Second Character:",
        "rel_type": "Relationship Type:",
        "rel_desc": "Relationship Description:",
        "add_rel_btn": "➕ Add Relationship",
        "rel_list": "📋 Relationships List",
        "no_rels": "No relationships defined yet.",
        "need_2_chars": "At least 2 characters required.",
        
        # Plot & Arcs
        "master_arc": "Master Arc",
        "design_master": "🎯 Design Master Arc with AI",
        "new_arc": "New Arc",
        "arc_name": "Arc Name:",
        "arc_goal": "Arc Goal:",
        "build_arc": "✨ Build Arc Bible with AI",
        "arc_list": "📚 Arcs List",
        
        # Manga Script
        "manga_gen": "✍️ Manga Script Generator",
        "chapter_num": "Chapter Number:",
        "chapter_outline": "Chapter Summary:",
        "gen_script": "🎬 Generate Manga Script",
        "saved_scripts": "📜 Saved Scripts",
        "chapters": "Chapters",
        "enter_outline": "Please enter chapter summary.",
        
        # AI Co-Pilot
        "copilot_title": "💬 AI Co-Pilot",
        "copilot_caption": "Chat with AI in different roles",
        "ai_role": "Current AI Role:",
        "chat_input": "Ask your question...",
        "clear_chat": "🗑️ Clear Chat History",
        
        # Common
        "save": "💾 Save",
        "load": "📂 Load",
        "delete": "🗑️ Delete",
        "saved_success": "Saved!",
        "loaded_success": "Loaded!",
        "cleared_success": "Cleared!",
        "added_success": "Added!",
        
        # AI Roles
        "roles": {
            "Story Editor": "Story Editor (Twist & Plot suggestions)",
            "Continuity Editor": "Continuity Editor (Check contradictions & Plot Holes)",
            "Character Writer": "Character Writer (Character development)",
            "Worldbuilding Designer": "Worldbuilding Designer (World design)",
            "Manga Scriptwriter": "Manga Scriptwriter (Script writing)",
            "Anime Adapter": "Anime Adapter (Convert to anime)",
            "Dialogue Specialist": "Dialogue Specialist (Dialogue optimization)",
            "Pacing Expert": "Pacing Expert (Story rhythm adjustment)"
        },
        
        # Relationship Types
        "rel_types": ["Ally", "Enemy", "Rival", "Mentor/Student", "Family", "Romantic", "Complex", "Secret"],
        
        # Character Roles
        "char_roles": ["Protagonist", "Antagonist", "Supporting", "Mentor", "Rival", "Love Interest"]
    },
    
    "fa": {
        "app_title": "🎬 موتور داستان مانگا/انیمه",
        "tab_core": "🧠 ایده و Brainstorm",
        "tab_world": "🌍 جهان و Lore",
        "tab_chars": "👥 شخصیت‌ها",
        "tab_relations": "🕸️ روابط",
        "tab_plot": "📖 پلات و آرک‌ها",
        "tab_script": "✍️ اسکریپت مانگا",
        "tab_anime": "🎬 برنامه‌ریز انیمه",
        "tab_copilot": "💬 دستیار هوشمند",
        "tab_search": "🔍 جستجوی معنایی",
        "tab_editor": "📝 ویرایشگر",
        "tab_export": "📊 خروجی",
        "tab_images": "🎨 تولید تصویر",
        "tab_versions": "🔄 نسخه‌ها",
        "tab_collab": "👥 تیم",
        
        # Core & Brainstorm
        "idea_input": "ایده دو خطی داستان خود را بنویسید:",
        "generate_core": "🚀 تولید Core Concept",
        "generate_logline": "✨ تولید Logline و Premise",
        "saved_core": "📝 Core Concept ذخیره شده",
        "enter_idea": "لطفاً ابتدا ایده را وارد کنید.",
        
        # World & Lore
        "world_setting": "تنظیمات جهان:",
        "world_rules": "قوانین اصلی جهان:",
        "save_rules": "💾 ذخیره قوانین جهان",
        "design_power": "🔮 طراحی سیستم قدرت با AI",
        "saved_power": "📜 سیستم قدرت طراحی شده",
        
        # Characters
        "new_char": "شخصیت جدید",
        "char_name": "نام شخصیت:",
        "char_role": "نقش:",
        "build_sheet": "🎭 ساخت Character Sheet با AI",
        "char_list": "لیست شخصیت‌ها",
        "mindmap_title": "🧠 مایندمپ شخصیت‌ها",
        "mindmap_view": "نمای مایندمپ",
        "graph_view": "نمای گراف روابط",
        "no_chars": "هنوز شخصیتی ساخته نشده است.",
        "enter_name": "لطفاً نام شخصیت را وارد کنید.",
        
        # Relationships
        "graph_title": "🕸️ گراف روابط",
        "add_relation": "افزودن رابطه",
        "char1": "شخصیت اول:",
        "char2": "شخصیت دوم:",
        "rel_type": "نوع رابطه:",
        "rel_desc": "توضیح رابطه:",
        "add_rel_btn": "➕ افزودن رابطه",
        "rel_list": "📋 لیست روابط",
        "no_rels": "هنوز رابطه‌ای تعریف نشده است.",
        "need_2_chars": "حداقل ۲ شخصیت نیاز است.",
        
        # Plot & Arcs
        "master_arc": "Master Arc",
        "design_master": "🎯 طراحی Master Arc با AI",
        "new_arc": "آرک جدید",
        "arc_name": "نام آرک:",
        "arc_goal": "هدف آرک:",
        "build_arc": "✨ ساخت Arc Bible با AI",
        "arc_list": "📚 لیست آرک‌ها",
        
        # Manga Script
        "manga_gen": "✍️ تولیدکننده اسکریپت مانگا",
        "chapter_num": "شماره فصل:",
        "chapter_outline": "خلاصه فصل:",
        "gen_script": "🎬 تولید اسکریپت مانگا",
        "saved_scripts": "📜 اسکریپت‌های ذخیره شده",
        "chapters": "فصل‌ها",
        "enter_outline": "لطفاً خلاصه فصل را وارد کنید.",
        
        # AI Co-Pilot
        "copilot_title": "💬 دستیار هوشمند AI",
        "copilot_caption": "با AI در نقش‌های مختلف صحبت کنید",
        "ai_role": "نقش فعلی AI:",
        "chat_input": "سؤال یا درخواست خود را بنویسید...",
        "clear_chat": "🗑️ پاک کردن تاریخچه چت",
        
        # Common
        "save": "💾 ذخیره",
        "load": "📂 بارگذاری",
        "delete": "🗑️ حذف",
        "saved_success": "ذخیره شد!",
        "loaded_success": "بارگذاری شد!",
        "cleared_success": "پاک شد!",
        "added_success": "اضافه شد!",
        
        # AI Roles
        "roles": {
            "Story Editor": "ویراستار داستان (پیشنهاد پیچش و Plot)",
            "Continuity Editor": "ویراستار پیوستگی (بررسی تناقضات و Plot Hole)",
            "Character Writer": "نویسنده شخصیت (توسعه شخصیت‌ها)",
            "Worldbuilding Designer": "طراح جهان‌سازی (طراحی جهان)",
            "Manga Scriptwriter": "نویسنده اسکریپت مانگا (نوشتن اسکریپت)",
            "Anime Adapter": "اقتباس‌گر انیمه (تبدیل به انیمه)",
            "Dialogue Specialist": "متخصص دیالوگ (بهینه‌سازی دیالوگ‌ها)",
            "Pacing Expert": "متخصص ریتم (تنظیم ریتم داستان)"
        },
        
        # Relationship Types
        "rel_types": ["متحد", "دشمن", "رقیب", "استاد/شاگرد", "خانواده", "عاشقانه", "پیچیده", "مخفی"],
        
        # Character Roles
        "char_roles": ["قهرمان اصلی", "آنتاگونیست", "پشتیبان", "مرشد", "رقیب", "علاقه عاشقانه"]
    },
    
    "ja": {
        "app_title": "🎬 マンガ/アニメ ストーリーエンジン",
        "tab_core": "🧠 コア & ブレインストーム",
        "tab_world": "🌍 世界設定",
        "tab_chars": "👥 キャラクター",
        "tab_relations": "🕸️ 関係図",
        "tab_plot": "📖 プロット & アーク",
        "tab_script": "✍️ マンガ脚本",
        "tab_anime": "🎬 アニメプランナー",
        "tab_copilot": "💬 AIコパイロット",
        "tab_search": "🔍 セマンティック検索",
        "tab_editor": "📝 エディター",
        "tab_export": "📊 エクスポート",
        "tab_images": "🎨 画像生成",
        "tab_versions": "🔄 バージョン",
        "tab_collab": "👥 チーム",
        
        # Core & Brainstorm
        "idea_input": "2行のストーリーアイデアを書いてください:",
        "generate_core": "🚀 コアコンセプト生成",
        "generate_logline": "✨ ログライン & プレミス生成",
        "saved_core": "📝 保存されたコアコンセプト",
        "enter_idea": "まずアイデアを入力してください。",
        
        # World & Lore
        "world_setting": "世界設定:",
        "world_rules": "世界の主要ルール:",
        "save_rules": "💾 世界ルール保存",
        "design_power": "🔮 AIでパワーシステム設計",
        "saved_power": "📜 設計されたパワーシステム",
        
        # Characters
        "new_char": "新キャラクター",
        "char_name": "キャラクター名:",
        "char_role": "役割:",
        "build_sheet": "🎭 AIでキャラクターシート作成",
        "char_list": "キャラクターリスト",
        "mindmap_title": "🧠 キャラクターマインドマップ",
        "mindmap_view": "マインドマップ表示",
        "graph_view": "関係グラフ表示",
        "no_chars": "キャラクターがまだ作成されていません。",
        "enter_name": "キャラクター名を入力してください。",
        
        # Relationships
        "graph_title": "🕸️ 関係グラフ",
        "add_relation": "関係追加",
        "char1": "最初のキャラクター:",
        "char2": "二番目のキャラクター:",
        "rel_type": "関係タイプ:",
        "rel_desc": "関係の説明:",
        "add_rel_btn": "➕ 関係追加",
        "rel_list": "📋 関係リスト",
        "no_rels": "関係がまだ定義されていません。",
        "need_2_chars": "少なくとも2人のキャラクターが必要です。",
        
        # Plot & Arcs
        "master_arc": "マスターアーク",
        "design_master": "🎯 AIでマスターアーク設計",
        "new_arc": "新アーク",
        "arc_name": "アーク名:",
        "arc_goal": "アークの目標:",
        "build_arc": "✨ AIでアークバイブル作成",
        "arc_list": "📚 アークリスト",
        
        # Manga Script
        "manga_gen": "✍️ マンガ脚本ジェネレーター",
        "chapter_num": "章番号:",
        "chapter_outline": "章の概要:",
        "gen_script": "🎬 マンガ脚本書き出し",
        "saved_scripts": "📜 保存された脚本",
        "chapters": "章",
        "enter_outline": "章の概要を入力してください。",
        
        # AI Co-Pilot
        "copilot_title": "💬 AIコパイロット",
        "copilot_caption": "様々な役割でAIと会話",
        "ai_role": "現在のAI役割:",
        "chat_input": "質問を入力...",
        "clear_chat": "🗑️ チャット履歴削除",
        
        # Common
        "save": "💾 保存",
        "load": "📂 読み込み",
        "delete": "🗑️ 削除",
        "saved_success": "保存しました！",
        "loaded_success": "読み込みました！",
        "cleared_success": "削除しました！",
        "added_success": "追加しました！",
        
        # AI Roles
        "roles": {
            "Story Editor": "ストーリー編集者（ひねり・プロット提案）",
            "Continuity Editor": "連続性編集者（矛盾・プロットホール確認）",
            "Character Writer": "キャラクターライター（キャラクター開発）",
            "Worldbuilding Designer": "世界設定デザイナー（世界設計）",
            "Manga Scriptwriter": "マンガ脚本家（脚本書き）",
            "Anime Adapter": "アニメアダプター（アニメ変換）",
            "Dialogue Specialist": "セリフ専門家（セリフ最適化）",
            "Pacing Expert": "ペーシング専門家（ストーリーリズム調整）"
        },
        
        # Relationship Types
        "rel_types": ["味方", "敵", "ライバル", "師弟", "家族", "恋愛", "複雑", "秘密"],
        
        # Character Roles
        "char_roles": ["主人公", "敵役", "サポート", "師匠", "ライバル", "恋愛対象"]
    }
}

def t(key):
    """دریافت ترجمه بر اساس زبان فعلی"""
    lang = st.session_state.get("lang", "fa")
    keys = key.split(".")
    value = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    
    for k in keys:
        if isinstance(value, dict):
            value = value.get(k)
            if value is None:
                return key
        else:
            return key
    
    return value