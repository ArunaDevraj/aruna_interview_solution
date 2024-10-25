import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def update_customer():
    try:
        data = frappe.local.form_dict

        if not data:
            return {"status": 400, "message": "No data provided."}

        customer_name = data.get("customer_name")
        mobile_number = data.get("mobile_number")
        email_address = data.get("email_address")

        # Fetch the customer using mobile number
        customer_id = frappe.db.get_value("Customer", {"mobile_no": mobile_number}, "name")
        if not customer_id:
            return {"status": 404, "message": f"Customer not found with mobile number {mobile_number}"}

        # Update the customer fields
        customer = frappe.get_doc("Customer", customer_id)
        if customer_name:
            customer.customer_name = customer_name
        if email_address:
            customer.email_id = email_address

        # Save and commit changes
        customer.save()
        frappe.db.commit()

        return {"status": 200, "message": "Customer updated successfully."}

    except Exception as e:
        frappe.log_error(f"Error: {str(e)}", "Customer Update API Error")
        return {"status": 500, "message": str(e)}


@frappe.whitelist(allow_guest=True)
def update_address():
    try:
        data = frappe.local.form_dict

        if not data:
            return {"status": 400, "message": "No data provided."}

        address_title = data.get("address_title")
        address_line2 = data.get("address_line2")

        # Fetch the address using the address title
        address_id = frappe.db.get_value("Address", {"address_title": address_title}, "name")
        if not address_id:
            return {"status": 404, "message": f"Address not found with title {address_title}"}

        # Update the address fields
        address = frappe.get_doc("Address", address_id)
        if address_line2:
            address.address_line2 = address_line2

        # Save and commit changes
        address.save()
        frappe.db.commit()

        return {"status": 200, "message": "Address updated successfully."}

    except Exception as e:
        frappe.log_error(f"Error: {str(e)}", "Address Update API Error")
        return {"status": 500, "message": str(e)}


@frappe.whitelist(allow_guest=True)
def update_contact():
    try:
        data = frappe.local.form_dict

        if not data:
            return {"status": 400, "message": "No data provided."}

        contact_name = data.get("contact_name")
        mobile_number = data.get("mobile_number")
        email_ids = data.get("email_ids", [])  # Expecting a list of email IDs

        # Fetch the contact using the contact name
        contact_id = frappe.db.get_value("Contact", {"first_name": contact_name}, "name")
        if not contact_id:
            return {"status": 404, "message": f"Contact not found with name {contact_name}"}

        # Update the contact fields
        contact = frappe.get_doc("Contact", contact_id)
        if mobile_number:
            contact.mobile_no = mobile_number

        # Update Email IDs child table
        if email_ids:
            contact.email_ids.clear()  # Clear existing email IDs

            for email in email_ids:
                # Append new email entries to the child table
                contact.append("email_ids", {"email_id": email})

        # Save and commit changes
        contact.save()
        frappe.db.commit()

        return {"status": 200, "message": "Contact updated successfully."}

    except Exception as e:
        frappe.log_error(f"Error: {str(e)}", "Contact Update API Error")
        return {"status": 500, "message": str(e)}
