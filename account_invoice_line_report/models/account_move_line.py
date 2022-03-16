
from odoo import models, fields, api,_

class AccountMoveLine(models.Model):
    _inherit = "account.invoice.report"

    label_name = fields.Char(string="Label Name")
    

    def _select(self):
        return super()._select() + ", line.name as label_name" 
