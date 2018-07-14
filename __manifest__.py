# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################
{
    "name": "HR Timesheet Submit",
    "version": "1.1",
    "author": "Linserv AB",
    "category": "Employees",
    "summary": "HR Timesheet Submit",
    "website": "www.linserv.se",
    "contributors": [
        'Gediminas Venclova <gediminasv@live.com>'
    ],
    "license": "",
    "depends": ['base', 'account', 'timesheet_grid'],
    'description': """

        HR Timesheet Submit
         - An employee marks a groups of timesheet records in a selected period as “submitted”.
         - Warning for not submitted records in Validated Timesheets view.
        
    """,
    "demo": [],
    "data": [
        'views/inherited_account_analytic_line.xml',
        'views/account_analytic_line_validate_warning.xml',
        'static/src/xml/assets.xml'
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [
        'static/src/xml/inherited_grid_view.xml'
    ],
    "installable": True,
    "auto_install": False,
}
