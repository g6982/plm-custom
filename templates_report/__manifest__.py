# -*- coding: utf-8 -*-
{
    'name': "Templates Report",
    'summary': """ PLM Templates Report for Sale, tclearance, transportation, concrete and concrete with tax """,
    'description': """
        PLM Templates Report
    """,
    'author': "Jenny Sun ",
    'category': 'Extra Tool',
    'version': '14.0.1.0.0',
    'depends': ['account'],
    'data': [
        'views/web.xml',
        'reports/report_tclearance_invoice.xml',        
        'reports/report_sale_invoice.xml',
        'reports/report_concrete_invoice.xml',
        'reports/report_transportation_invoice.xml',
        'reports/report.xml',
    ],
    'demo': [],
}
