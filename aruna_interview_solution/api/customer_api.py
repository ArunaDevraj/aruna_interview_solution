import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def customer_handler():
    try:
        # Get the data from the request
        data = frappe.local.form_dict

        # Ensure data is not None
        if not data:
            return {"status": 400, "message": "No data provided."}

        customer_name = data.get("customer_name")
        mobile_number = data.get("mobile_number")
        email_address = data.get("email_address")
        address_line1 = data.get("address_line1")
        address_line2 = data.get("address_line2")
        city = data.get("city")
        pincode = data.get("pincode")
        state = data.get("state")
        country = data.get("country")
        sales_person = data.get("sales_person")
        salutation = data.get("salutation")
        address_title = data.get("address_title")  # Get the address title from the request

        # Add validation if necessary
        if not customer_name or not mobile_number:
            return {"status": 400, "message": "Customer name and mobile number are required."}
        if not address_title:
            return {"status": 400, "message": "Address title is mandatory."}  # Validate address title

        # Create a customer record
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_name,
            "mobile_no": mobile_number,
            "email_id": email_address,
            "sales_person": sales_person,
            "salutation": salutation
        })

        customer.insert()  # Save to database

        # Create an address record
        address = frappe.get_doc({
            "doctype": "Address",
            "address_title": address_title,  # Add the address title
            "address_line1": address_line1,
            "address_line2": address_line2,
            "city": city,
            "pincode": pincode,
            "state": state,
            "country": country,
            "customer": customer.name  # Link address to the customer
        })

        address.insert()  # Save the address to database

        # Check if a contact with the same mobile number already exists
        existing_contact = frappe.db.get_value(
            "Contact",
            {"mobile_no": mobile_number},
            "name"
        )

        if existing_contact:
            # Optionally, you can update the existing contact if needed
            contact = frappe.get_doc("Contact", existing_contact)
            contact.email_id = email_address  # Update email if necessary
            contact.address = address.name  # Update address
            contact.save()  # Save the updates
        else:
            # Create a new contact record and link the address
            contact = frappe.get_doc({
                "doctype": "Contact",
                "first_name": customer_name,  # Assuming you want to use the customer's name
                "mobile_no": mobile_number,
                "email_id": email_address,
                "customer": customer.name,  # Link contact to the customer
                "address": address.name,  # Link address to the contact
                "contact_name": f"{customer_name} - {customer.name}"  # Unique contact name
            })
            contact.insert()  # Save the contact to database

        return {"status": 200, "message": "Customer, address, and contact created/updated successfully."}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Customer API Error")
        return {"status": 500, "message": str(e)}
