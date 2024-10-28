app_name = "aruna_interview_solution"
app_title = "aruna_interview_solution"
app_publisher = "Aruna"
app_description = "Problem Solving"
app_email = "arunadevraj92@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "aruna_interview_solution",
# 		"logo": "/assets/aruna_interview_solution/logo.png",
# 		"title": "aruna_interview_solution",
# 		"route": "/aruna_interview_solution",
# 		"has_permission": "aruna_interview_solution.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aruna_interview_solution/css/aruna_interview_solution.css"
# app_include_js = "/assets/aruna_interview_solution/js/aruna_interview_solution.js"

# include js, css files in header of web template
# web_include_css = "/assets/aruna_interview_solution/css/aruna_interview_solution.css"
# web_include_js = "/assets/aruna_interview_solution/js/aruna_interview_solution.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "aruna_interview_solution/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Custom Work Order": "public/js/custom_work_order.js",
    "Sales Order": "public/js/custom_sales_order.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "aruna_interview_solution/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "aruna_interview_solution.utils.jinja_methods",
# 	"filters": "aruna_interview_solution.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "aruna_interview_solution.install.before_install"
# after_install = "aruna_interview_solution.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "aruna_interview_solution.uninstall.before_uninstall"
# after_uninstall = "aruna_interview_solution.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "aruna_interview_solution.utils.before_app_install"
# after_app_install = "aruna_interview_solution.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "aruna_interview_solution.utils.before_app_uninstall"
# after_app_uninstall = "aruna_interview_solution.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aruna_interview_solution.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": "aruna_interview_solution.sales.create_custom_work_order_on_submit"
# 		"on_cancel": "method",
# 		"on_trash": "method"
	},
	"Custom Work Order": {
		"on_submit": "aruna_interview_solution.custom_work_order.create_sales_order_on_submit"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aruna_interview_solution.tasks.all"
# 	],
# 	"daily": [
# 		"aruna_interview_solution.tasks.daily"
# 	],
# 	"hourly": [
# 		"aruna_interview_solution.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aruna_interview_solution.tasks.weekly"
# 	],
# 	"monthly": [
# 		"aruna_interview_solution.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "aruna_interview_solution.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "aruna_interview_solution.event.get_events"
	"POST /api/method/aruna_interview_solution.api.customer_api.customer_handler": "aruna_interview_solution.api.customer_api.customer_handler",
	"PUT /api/method/aruna_interview_solution.api.update_api.update_customer": "aruna_interview_solution.api.update_api.update_customer"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "aruna_interview_solution.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["aruna_interview_solution.utils.before_request"]
# after_request = ["aruna_interview_solution.utils.after_request"]

# Job Events
# ----------
# before_job = ["aruna_interview_solution.utils.before_job"]
# after_job = ["aruna_interview_solution.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"aruna_interview_solution.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {
        "dt": "Workflow",
        "filters": [["name", "in", ["Timesheet Workflow"]]]
    },
    {
        "dt": "Workflow State",
        "filters": [["workflow_name", "in", ["Timesheet Workflow"]]]
    },
    {
        "dt": "Workflow Action",
        "filters": [["workflow_name", "in", ["Timesheet Workflow"]]]
    }
]
