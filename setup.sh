#!/bin/bash

echo "🧠 إنشاء بيئة العمل..."
python3 -m venv env
source env/bin/activate

echo "📦 تثبيت Frappe Bench..."
pip install frappe-bench

echo "⚙️ إعداد Frappe Bench..."
bench init frappe-bench --frappe-branch version-15
cd frappe-bench

echo "📁 نسخ التطبيقات..."
cp -r ../apps/* apps/

echo "🌍 إنشاء الموقع..."
bench new-site erpnext.local
bench --site erpnext.local install-app frappe
bench --site erpnext.local install-app erpnext
bench --site erpnext.local install-app ury
bench --site erpnext.local install-app ury_mosaic
bench --site erpnext.local install-app ury_pos
bench --site erpnext.local install-app restaurant_pos
bench --site erpnext.local install-app doppio

echo "✅ كل شيء جاهز. شغل bench start"
