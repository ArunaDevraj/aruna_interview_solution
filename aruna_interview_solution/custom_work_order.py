import frappe

def create_sales_order_on_submit(doc, method):
    # Create a new Sales Order document
    sales_order = frappe.new_doc("Sales Order")

    # Fetch default customer from Selling Settings
    default_customer = frappe.db.get_value("Selling Settings", None, "default_customer")
    if not default_customer:
        frappe.throw("Please set a Default Customer in Selling Settings.")

    sales_order.customer = default_customer
    sales_order.transaction_date = frappe.utils.nowdate()
    sales_order.delivery_date = frappe.utils.add_days(frappe.utils.nowdate(), 7)  # Delivery in 7 days

    # Add items from Custom Work Order
    for item in doc.items:
        sales_order.append("items", {
            "item_code": item.item_code,
            "qty": item.qty,
            "rate": item.rate,
#           "warehouse": item.warehouse or "Stores"
        })

    # Insert and submit the Sales Order
    sales_order.insert()
    sales_order.submit()

    frappe.msgprint(f"Sales Order {sales_order.name} created from Custom Work Order {doc.name}.")
