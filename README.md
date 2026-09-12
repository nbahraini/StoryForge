# 🎬 Manga/Anime Story Engine | موتور داستان مانگا و انیمه

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![AI](https://img.shields.io/badge/AI-OpenAI_Compatabile-10A37F.svg)](https://openai.com/)
[![Vector DB](https://img.shields.io/badge/Database-ChromaDB-FFD166.svg)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🇬🇧 English / 🇮🇷 فارسی

### 🇬🇧 Overview
**Manga/Anime Story Engine** is a fully modular, AI-powered workspace designed specifically for writers, manga artists, and anime creators. Instead of letting AI randomly generate text, this tool enforces a professional production pipeline: from a 2-line idea to a complete Story Bible, Character Sheets, Arc Planning, Manga Scripts, and Anime Episode Breakdowns. It features a built-in Vector Database (ChromaDB) for semantic search to prevent plot holes, interactive mindmaps, and ComfyUI integration for character visualization.

### 🇮🇷 معرفی
**موتور داستان مانگا و انیمه** یک محیط کاری ماژولار و مبتنی بر هوش مصنوعی است که به‌طور خاص برای نویسندگان، مانگاکاها و سازندگان انیمه طراحی شده است. به جای اینکه هوش مصنوعی به صورت تصادفی متن تولید کند، این ابزار یک خط تولید حرفه‌ای را اعمال می‌کند: از یک ایده دو خطی تا Story Bible کامل، شناسنامه شخصیت‌ها، برنامه‌ریزی آرک‌ها، اسکریپت مانگا و شکست اپیزودهای انیمه. این ابزار دارای پایگاه داده برداری (ChromaDB) برای جستجوی معنایی جهت جلوگیری از حفره‌های داستانی، مایندمپ‌های تعاملی و اتصال به ComfyUI برای تصویرسازی شخصیت‌ها است.

---

## ✨ Features | ویژگی‌ها

| 🇬🇧 English | 🇮🇷 فارسی |
| :--- | :--- |
| 🧠 **Core & Brainstorming**: Transform 2-line ideas into Core Concepts, Loglines, and Premises. | 🧠 **ایده‌پردازی**: تبدیل ایده‌های دو خطی به Core Concept، Logline و Premise. |
| 🌍 **Worldbuilding Bible**: Define rules, power systems, factions, and timeline with strict Canon/Open Questions separation. | 🌍 **جهان‌سازی**: تعریف قوانین، سیستم قدرت، گروه‌ها و جدول زمانی با تفکیک حقایق قطعی و سوالات باز. |
| 👥 **Character Sheets & Mindmaps**: Deep psychological profiles (Want, Need, Wound, Lie) + Interactive ECharts/Pyvis relationship graphs. | 👥 **شناسنامه شخصیت و مایندمپ**: پروفایل روانشناختی عمیق + گراف‌های تعاملی روابط شخصیت‌ها. |
| 📖 **Plot & Arcs**: Master Arc → Saga → Arc → Beat Sheet → Chapter Outline pipeline. | 📖 **پلات و آرک‌ها**: خط لوله طراحی از Master Arc تا Saga، آرک، Beat Sheet و خلاصه فصل. |
| ✍️ **Manga & Anime Scripting**: Panel-by-panel manga scripting (with page-turn reveals) and timed anime episode breakdowns. | ✍️ **اسکریپت نویسی**: اسکریپت پنل‌به‌پنل مانگا (با رعایت Page-turn) و زمان‌بندی اپیزودهای انیمه. |
| 🔍 **Semantic Search (ChromaDB)**: Search across all written chapters to find and prevent plot holes and continuity errors. | 🔍 **جستجوی معنایی**: جستجو در تمام فصل‌های نوشته شده برای پیدا کردن و جلوگیری از حفره‌های داستانی. |
| 📝 **Advanced Markdown Editor**: Write chapters with auto-save and one-click Vector DB indexing. | 📝 **ویرایشگر پیشرفته**: نوشتن فصل‌ها با ذخیره خودکار و ایندکس یک‌کلیکه در پایگاه داده برداری. |
| 🎨 **ComfyUI Integration**: Generate character concept art directly from Character Sheets. | 🎨 **اتصال به ComfyUI**: تولید کانسپت آرت شخصیت‌ها مستقیماً از روی شناسنامه شخصیت. |
| 🔄 **Version Control**: Snapshot your Story Bible at any point and revert if needed. | 🔄 **کنترل نسخه**: ثبت لحظه‌ای (Snapshot) از Story Bible و قابلیت بازگشت به نسخه‌های قبل. |
| 🌐 **Multi-language**: Full UI support for English, Persian (with RTL), and Japanese. AI responds in the selected language. | 🌐 **چندزبانگی**: پشتیبانی کامل از انگلیسی، فارسی (با چینش راست‌چین) و ژاپنی. پاسخ‌دهی AI به زبان انتخابی. |

---

## 🛠️ Tech Stack | تکنولوژی‌های استفاده شده

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **AI Engine**: OpenAI API (Compatible with Groq, Ollama, Anthropic, etc.)
- **Vector Database**: [ChromaDB](https://www.trychroma.com/) (for semantic memory)
- **Graph Visualization**: `pyvis` & `streamlit-echarts`
- **Data Management**: JSON-based local storage with versioning
- **Image Generation**: ComfyUI API integration

---

## 🚀 Installation & Setup | نصب و راه‌اندازی

### 🇬🇧 English
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/manga-story-engine.git
   cd manga-story-engine
