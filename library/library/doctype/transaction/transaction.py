# Copyright (c) 2022, dexciss technology pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import today

class Transaction(Document):
	def before_save(self):
		name = frappe.db.get_value("Student",{"name":self.student},["first_name","last_name"])
		full_name = "{0} {1}".format(name[0],name[1])
		self.student_full_name = full_name

		# to understand list ORM
		# d = frappe.db.get_list("Book",["*"], limit = 1)
		# print("###>>"*10)
		# print(d)

		# to understand delete ORM
		#frappe.delete_doc("Book","Delete")

		# to understand insert in db
		doc = frappe.new_doc("Book")
		doc.book_name = "Chem"
		doc.avl = 10
		doc.insert()


	
	def validate(self):
		self.validate_count()
		self.set_date()

	def on_submit(self):
		self.handle_book_count()
			
	def validate_count(self):
		for book in self.books:
			avl_book = frappe.get_value("Book", {"name":book.get("book")},"avl")
			if avl_book < 1 and self.type == "Issue":
				msg = "Sorry {0} is not available! count is {1}".format(book.get('book'),avl_book)
				frappe.throw(_(msg))

	def set_date(self):
		if not self.posing_date:
			self.posing_date = today()
			self.from_date = today()

	def handle_book_count(self):
		if self.type == "Issue":
			for book in self.books:
				doc = frappe.get_doc("Book",book.get("book"))
				doc.avl = doc.avl - 1
				doc.save()



			

