# Copyright 2017 Tecnativa - Carlos Dauden
# Copyright 2018 Tecnativa - Vicent Cubells
# Copyright 2020 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Invoice Line Report",
    "summary": "New view to manage invoice lines information",
    "version": "14.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/OCA/account-invoice-reporting",
    "author": "Tecnativa, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["account",],
    "data": [
        "reports/report.xml",
        "reports/account_invoice_report_view.xml",
        "reports/report_driver_expense.xml",
        "reports/report_vendor_expense_statement.xml",
        "reports/report_invoice_lines.xml",
        "reports/report_invoice_tax.xml",
        "reports/report_invoice_tax_by_government.xml",
        ],
    "installable": True,
}
