import frappe

def get_context(context):
    context.student_list = frappe.get_all("Student",{},['*'])