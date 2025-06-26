import frappe
import json

@frappe.whitelist(allow_guest=False)
def create_pos_order():
    try:
        data = frappe.local.form_dict

        # لو body جاي كـ string
        if isinstance(data, str):
            data = json.loads(data)

        doc = frappe.new_doc("POS Order")
        doc.customer = data.get("customer")
        doc.order_type = data.get("order_type")
        doc.grand_total = data.get("grand_total")

        for item in data.get("items", []):
            doc.append("items", {
                "item_code": item["item_code"],
                "qty": item["qty"],
                "rate": item["rate"]
            })

        doc.insert()
        frappe.db.commit()

        return {"message": "POS Order created", "name": doc.name}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "POS API Error")
        return {"error": str(e)}
