from typing_extensions import Required
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'account.move.line'

    plate_num = fields.Many2one(
        'res.partner', 
        string="Plate Number",
        help="ផ្លាកលេខឡាន",
        required=True,
        store=True,
    )
    inv_ref = fields.Char(string="Invoice Reference",required=True,store=True)




