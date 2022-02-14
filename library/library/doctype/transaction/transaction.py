# Copyright (c) 2022, dexciss technology pvt ltd and contributors
# For license information, please see license.txt

from lib2to3.pgen2.grammar import opmap_raw
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import today

class Transaction(Document):
	def before_save(self):
		name = frappe.db.get_value("Student",{"name":self.student},["first_name","last_name"])
		full_name = "{0} {1}".format(name[0],name[1])
		self.student_full_name = full_name
	
	def validate(self):
		self.validate_count()
		self.set_date()
		if self.type == "Issue":
			for book in self.books:
				issued_book = self.count_issue(book.get("book"))
				returned_book = self.count_return(book.get("book"))
				if issued_book > returned_book:
					frappe.throw("Please return the book first")

	def count_issue(self,book):
		parent_doc = frappe.get_all("Transaction", {"student": self.student,"docstatus":1,"type":"Issue"},["name"])
		# finding same book inside child table
		book_list = []
		for doc in parent_doc:
			data = frappe.get_all("Book Details",{"parent":doc.get("name"),"book":book},['book'])
			for d in data:
				book_list.append(d.get("book"))
		return len(book_list)

	def count_return(self,book):
		parent_doc = frappe.get_all("Transaction", {"student": self.student,"docstatus":1,"type":"Return"},["name"])
		# finding same book inside child table
		book_list = []
		for doc in parent_doc:
			data = frappe.get_all("Book Details",{"parent":doc.get("name"),"book":book},['book'])
			for d in data:
				book_list.append(d.get("book"))
		return len(book_list)
	
	
	
	
	def on_submit(self):
		self.handle_book_count()

	#def on_cancel(self):
	# def after_insert(self):
	# 	print("####"*10)
	# 	print("after_insert called..")
	
	# def on_update(self):
	# 	print("####"*10)
	# 	print("on_update called..")
	
	# def before_rename(self):
	# 	print("####"*10)
	# 	print("before_rename called..")

	# def after_rename(self):
	# 	print("####"*10)
	# 	print("after_rename called..")

	#after_delete
	# def after_delete(self):
	# 	print("####"*10)
	# 	print("after_delete called..")

	# def on_cancel(self):
	# 	print("####"*10)
	# 	print("on_cancel called..")

			
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

	def validate_issue_return(self):
		# inside current doc's child table
		for book in self.books:
			issue_list = []
			return_list = []
			# to find the previous doc
			doc_list = frappe.get_all("Transaction", {"student":self.student,"type": "Issue", "docstatus" : 1},'name')
			for doc in doc_list:
				transaction_doc = frappe.get_doc("Transaction",doc.get("name"))
				for b in transaction_doc.get("books"):
					if book.get("book") == b.get("book"):
						issue_list.append(book.get("book"))
			
			

			# doc_list = frappe.get_all("Transaction", {"student":self.student,"type": "Return", "docstatus" : 1},'name')
			# print(doc_list)
			# for doc in doc_list:
			# 	transaction_doc = frappe.get_doc("Transaction",doc.get("name"))
			# 	for b in transaction_doc.get("books"):
			# 		if book.get("book") == b.get("book"):
			# 			return_list.append(book.get("book"))
			# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
			# print(return_list)
				




			

