# Restaurant POS System (Based on Frappe & ERPNext)

نظام POS متكامل لإدارة المطاعم باستخدام Frappe و ERPNext، يدعم URY Mosaic و URY POS و Doppio.

## ✅ المتطلبات

- Python 3.11
- Node.js 20
- Redis
- Yarn
- wkhtmltopdf
- MariaDB 10.6+

## 📦 خطوات التثبيت

```bash
git clone https://github.com/kamel135/restaurant-pos.git
cd restaurant-pos

# إنشاء بيئة افتراضية
python3 -m venv env
source env/bin/activate

# تثبيت bench
pip install frappe-bench
bench init frappe-bench --frappe-branch version-15
cd frappe-bench

# نسخ التطبيقات
cp -r ../restaurant-pos/apps/* apps/

# إعداد التطبيقات
bench get-app erpnext --branch version-15
bench get-app --branch main https://github.com/ury-erp/ury_mosaic.git
bench get-app --branch main https://github.com/ury-erp/ury_pos.git
bench get-app --branch main https://github.com/ury-erp/doppio.git

# إنشاء موقع جديد
bench new-site erpnext.local
bench --site erpnext.local install-app frappe
bench --site erpnext.local install-app erpnext
bench --site erpnext.local install-app ury
bench --site erpnext.local install-app ury_mosaic
bench --site erpnext.local install-app ury_pos
bench --site erpnext.local install-app restaurant_pos
bench --site erpnext.local install-app doppio

# تشغيل النظام
bench start
