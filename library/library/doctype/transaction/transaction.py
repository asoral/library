# Copyright (c) 2022, dexciss technology pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transaction(Document):
	def before_save(self):
		name = frappe.db.get_value("Student",{"name":self.student},["first_name","last_name"])
		full_name = "{0} {1}".format(name[0],name[1])
		self.student_full_name = full_name
