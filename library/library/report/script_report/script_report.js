// Copyright (c) 2016, dexciss technology pvt ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Script Report"] = {
	"filters": [
		{
			fieldname: "student",
			label: __("Student"),
            fieldtype: "Link",
			options: "Student",
			// reqd: 1,
			default: "",
		},
		{
			fieldname: "from_date",
			label: __("From Date"),
            fieldtype: "Date",
			
		},
	]
};
