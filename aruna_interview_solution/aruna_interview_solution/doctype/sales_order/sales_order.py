# File: custom_app/custom_app/doctype/sales_order/sales_order.py

import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist(allow_guest=True)
def make_custom_work_order(source_name, target_doc=None):
    def update_details(source, target):
        target.sales_orders = [dict(sales_order=source.name)]

    return get_mapped_doc(
        "Sales Order",
        source_name,
        {
            "Sales Order": {
                "doctype": "Custom Work Order",
                "field_map": {
                    "name": "sales_order",
                    "customer": "customer",
                },
            },
            "Sales Order Item": {
                "doctype": "Custom Work Order Item",
                "field_map": {"item_code": "item_code", "qty": "qty"},
            },
        },
        target_doc,
        update_details,
    )
