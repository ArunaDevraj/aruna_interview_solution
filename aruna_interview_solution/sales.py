import frappe

def create_custom_work_order_on_submit(doc, method):
    work_order = frappe.new_doc("Custom Work Order")
    work_order.sales_order = doc.name  # Link Sales Order to Custom Work Order

    # Ensure you use the correct child table field
    for item in doc.items:
        work_order.append("items", {  # Use the correct field name
            "item_code": item.item_code,
            "qty": item.qty,
            "rate": item.rate,
            "warehouse": item.warehouse
        })

    work_order.insert()
    frappe.msgprint(f"Custom Work Order {work_order.name} created.")
