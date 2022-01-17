# -*- coding: utf-8 -*-
{
    'name': "account_exc_rate",
    'summary': """ Add 2 fields more for exchange rate in khmer and thai bath """,
    'description': """
        Exchange Rate in KHR and THB
    """,
    'author': "Jenny Sun ",
    'category': 'Extra Tool',
    'version': '14.0.1.0.0',
    'depends': ['account'],
    'data': [
        'views/web.xml',
        'views/account_move_exc_rate_views.xml',
        'reports/report_tclearance_invoice.xml',        
        'reports/report_sale_invoice.xml',
        'reports/report_concrete_invoice.xml',
        'reports/report_transportation_invoice.xml',
        'reports/report.xml',
    ],
    'demo': [],
}
