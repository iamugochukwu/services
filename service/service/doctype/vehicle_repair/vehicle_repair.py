
# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ugochukwu and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

from frappe import _
from frappe.utils import (cstr, validate_email_add, cint, comma_and, has_gravatar, now, getdate, nowdate)
from frappe.model.mapper import get_mapped_doc



class VehicleRepair(Document):pass

@frappe.whitelist()
def make_opportunity(customer, item, rate):
		
	doc = frappe.new_doc('Sales Invoice')
	doc.customer = customer
	doc.append("items", {
		"item_code": item,
		"rate":  rate
	})
	return doc
