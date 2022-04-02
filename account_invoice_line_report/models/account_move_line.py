
from odoo import models, fields, api,_

class AccountMoveLine(models.Model):
    _inherit = "account.invoice.report"

    label_name = fields.Char(string="Label Name")
    expense_date = fields.Date(string="Expense Date")
    sub_pricetotal = fields.Float(string="Amount in Currency")
    

    def _select(self):
        return super()._select() + ", line.name as label_name , line.product_line_date as expense_date " 
