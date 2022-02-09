// Copyright (c) 2022, dexciss technology pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaction', {
	student: function(frm) {
		console.log("got the output")
	},
	posing_date: function(frm) {
		console.log("got the output posting date")
	}
});
