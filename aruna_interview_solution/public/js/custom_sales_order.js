frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {  // Show button only after submission
            frm.add_custom_button(__('Create Custom Work Order'), function() {
                frappe.new_doc('Custom Work Order', {
                    sales_order: frm.doc.name  // Link Sales Order to Custom Work Order
                });
            });
        }
    }
});
