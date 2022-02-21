// Copyright (c) 2022, dexciss technology pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaction', {
	refresh : function(abd){
		abd.set_query('student', () => {
			return {
				filters: {
					class: ['in',['+2','10	']]
				}
			}
		})
	},
	student: function(frm) {
		console.log("got the output")
		console.log(frm)
		if(frm.doc.student){
			// frappe.call({
			// 	method: "library.api.get_full_name",
			// 	args: {
			// 		docname: frm.doc.student
			// 	},
			// 	callback: function(resp){
			// 		console.log("resp is: ",resp)
			// 		if(resp.message) {
			// 			console.log("resp is: ",resp.message)
			// 			frm.doc.student_full_name = resp.message
			// 			frm.refresh_field("student_full_name")
			// 		}
			// 	}
			// })

			frappe.call({
				method : "library.api.get_full_name",
				args: {
					x : frm.doc.student
				},
				callback: function(x){
					console.log("r is: ",x)
					if (x.message)
					{
						frm.doc.student_full_name = x.message,
						frm.refresh_field("student_full_name")}
				}})

		}
	},
	posing_date: function(frm) {
		console.log("got the output posting date")
	}
	//default function 1. before_save,after_save,validate,
});


frappe.ui.form.on("Book Details",{
	book: function(frm,cdt,cdn){
		console.log("onchange event on book....")
		var row = locals[cdt][cdn];
		row.author = "test"
		frm.refresh_field("books")
	}
})
