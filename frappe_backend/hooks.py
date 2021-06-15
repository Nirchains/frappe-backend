# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_backend"
app_title = "Frappe Backend"
app_publisher = "Pedro Antonio Fernández Gómez"
app_description = "Frappe backend styles and functions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pedro@hispalisdigital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["/assets/css/frappe_backend/v13.css"]
# app_include_js = "/assets/frappe_backend/js/frappe_backend.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_backend/css/frappe_backend.css"
# web_include_js = "/assets/frappe_backend/js/frappe_backend.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "DocType" : "custom_script/doctype.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_backend.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_backend.install.before_install"
# after_install = "frappe_backend.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_backend.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_backend.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_backend.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_backend.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_backend.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_backend.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_backend.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_backend.event.get_events"
# }

