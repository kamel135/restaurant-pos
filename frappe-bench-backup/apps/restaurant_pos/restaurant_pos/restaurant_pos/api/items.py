# restaurant_pos/restaurant_pos/api/items.py

import frappe
from frappe import _

@frappe.whitelist()
def get_items():
    # نحصل على كل الأصناف الفعالة
    items = frappe.get_all(
        "Item",
        fields=["name", "item_name", "image"],
        filters={"disabled": 0}
    )

    # نجيب السعر لكل صنف من جدول Item Price
    for item in items:
        price = frappe.db.get_value("Item Price", {"item_code": item.name}, "price_list_rate")
        item["price"] = price or 0.0

    return items
