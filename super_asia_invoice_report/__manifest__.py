# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2019 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': 'Superasia Invoice Reports',
    'version': '1.0',
    'category': 'Reports',
    'summary': 'Superasia Invoice Report',
    'author': "Bista Solutions",
    'website': 'http://www.bistasolutions.com',
    'depends': ['base','account', 'sale','website_sale','account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_sales_rep_report_wizard.xml',
        'views/superasia_report.xml',
        'views/invoice_sales_rep_report_wizard.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
}
