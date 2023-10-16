# Copyright (c) 2023, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Location(Document):
	def before_save(self):
        product_name = self.product_name
        quantity = self.quantity

        try:
            product_doc = frappe.get_doc('Product', product_name)
            product_doc.quantity += quantity
            product_doc.save()
            frappe.msgprint(f"Product quantity updated to {product_doc.quantity}"
			)
        except frappe.DoesNotExistError:
            frappe.msgprint("Product not found."
			)
        except Exception as e:
            frappe.msgprint(f"Error updating product quantity: {str(e)}"
			)
