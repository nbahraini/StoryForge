برای من تو ی Qwen Coderیه ابزار مبتنی بر python برای من ایجاد کن مبتنی بر Web باشه UI اش و برروی Linux قابل اجرا باشه  که به Api های مختلف Ai Agent های مختلف وصل بشه و همونطور که در فایل های بالا شرح داده شده ساختار یه داستان رو بشه بهش داد Tab ی داشته باشه برای Brain Storm و کشیدن Relation بین کاراتر ها و نوشتن شرح شخصت ها و هدف داستان و بعد با کمک AI  بشه بخش های مختلف داستان و Skelet داستان و هدف ها و ... رو شرح داده در نرم افزار و با استفاده از AI ها بشه بسط و گسترش داده بخش ها و فصل ها رو و حتی در بخش ها و پیچ های داستانی یا AI به کاربر Hint بده یا کاربر بتونه هر زمان خواست درخواست هاش رو از طرق Ai بگه 



story_engine/
├── app.py                          # نقطه ورود اصلی
├── config.py                       # تنظیمات مرکزی
├── requirements.txt                # وابستگی‌ها
├── setup.sh                        # اسکریپت نصب
│
├── modules/                        # ماژول‌های اصلی (هر تب)
│   ├── __init__.py
│   ├── core_brainstorm.py         # تب 1: Core & Brainstorm
│   ├── world_lore.py              # تب 2: World & Lore
│   ├── characters.py              # تب 3: Characters + Mindmap
│   ├── relationships.py           # تب 4: Relationship Map
│   ├── plot_arcs.py               # تب 5: Plot & Arcs
│   ├── manga_script.py            # تب 6: Manga Script
│   ├── anime_planner.py           # تب 7: Anime Episode Planner (جدید)
│   ├── ai_copilot.py              # تب 8: AI Co-Pilot
│   ├── vector_search.py           # تب 9: Semantic Search (جدید)
│   ├── markdown_editor.py         # تب 10: Advanced Editor (جدید)
│   ├── export_manager.py          # تب 11: Export Manager (جدید)
│   ├── comfyui_connector.py       # تب 12: Image Generation (جدید)
│   ├── versioning.py              # تب 13: Version Control (جدید)
│   └── collaboration.py           # تب 14: Team Collaboration (جدید)
│
├── services/                       # سرویس‌های مشترک
│   ├── __init__.py
│   ├── ai_service.py              # مدیریت اتصال به AI
│   ├── database_service.py        # مدیریت Story Bible
│   ├── chroma_service.py          # Vector Database
│   ├── comfyui_service.py         # اتصال به ComfyUI
│   └── i18n_service.py            # چندزبانگی
│
├── utils/                          # توابع کمکی
│   ├── __init__.py
│   └── helpers.py
│
└── data/                           # داده‌های پروژه
    ├── story_bibles/              # Story Bibleهای ذخیره شده
    ├── versions/                  # نسخه‌های مختلف
    ├── exports/                   # فایل‌های خروجی
    └── chroma_db/                 # Vector Database
