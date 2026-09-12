# 1. ساخت ساختار پوشه‌ها
./setup_project.sh

# 2. نصب وابستگی‌ها
source .venv/bin/activate
pip install -r requirements.txt

# 3. اجرا
streamlit run app.py