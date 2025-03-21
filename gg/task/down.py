def run_patch():
	import time

	time.sleep(60)

	print("Break Stated")

	x = 1 / 0

	print("Patching frappe_appointment")


import frappe


@frappe.whitelist(allow_guest=True)
def api():
	return "Hum Broke hai"
