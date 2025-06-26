import frappe


def validate(doc,method):
    update_menu_item(doc,method)
    
    
def update_menu_item(doc, event):
    menu_items = frappe.get_all('URY Menu Item', filters={'item': doc.item_code})
    for menu_item in menu_items:
        frappe.db.set_value('URY Menu Item', menu_item.name, 'item_name', doc.item_name)