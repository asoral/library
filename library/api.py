import frappe

@frappe.whitelist()
def get_full_name(x):
    doc = frappe.get_doc("Student",x)
    full_name = "{0} {1}".format(doc.get("first_name"),doc.get("last_name"))
    return full_name