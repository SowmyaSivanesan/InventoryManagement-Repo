# Copyright (c) 2023, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ProductMovements(Document):
	def before_save(self):
		if self.from_location:
			product_from_location=frappe.get_doc("Location",{"name":self.from_location,"product_name":self.product_name})
			product_from_location.quantity -= self.qty
			product_from_location.save()
			if self.to_location:
				product_to_location=frappe.get_doc("Location",{"name":self.to_location,"product_name":self.product_name})
				product_to_location.quantity += self.qty
				product_to_location.save()
			else:
				frappe.msgprint("To location not specified.Quantity not updated.")
		else:
			frappe.msgprint("From location not specified.Quantity updated in the 'to' location.")