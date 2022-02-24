# Copyright (c) 2013, dexciss technology pvt ltd and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	return [
        {
            "label": "Student ID",
            "fieldtype": "Data",
            "fieldname": "student_id",
            "width": 700,
        },
        {
            "label": "Student Name",
            "fieldtype": "Data",
            "fieldname": "student_name",
            "width": 200,
        },
        {
            "label": "Transaction",
            "fieldtype": "Data",
            "fieldname": "transaction",
            "width": 150,
        },  
    ]

def get_data(filters):
    fil = {}
    if filters.get("student"):
        fil['student'] = filters.get("student")
    all_data = frappe.get_all("Transaction",fil,["*"])

    data = []
    for i in all_data:
        temp = {}
        temp['transaction'] = i.get("name")
        temp['student_id'] = i.get("student")
        temp['student_name'] = i.get("student_full_name")
        data.append(temp)
    return data
