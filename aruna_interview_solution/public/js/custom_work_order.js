frappe.ui.form.on('Custom Work Order', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {  // Show the button only when submitted
            frm.add_custom_button(__('Add Sales Order'), function() {
                frappe.new_doc('Sales Order', {
                    custom_work_order: frm.doc.name  // Link the work order to sales order
                });
            }, __('Create'));  // Optional: Group the button under 'Create'
        }
    }
});
