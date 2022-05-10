

from odoo import models, fields, api,_

class AccountMoveLine(models.Model):
    _inherit = "account.invoice.report"

    label_name = fields.Char(string="Label Name")
    expense_date = fields.Date(string="Expense Date")
    sub_pricetotal = fields.Float(string="Amount in Currency")
    price_unit_cus = fields.Float(string="Price Unit")
    currency_id_name = fields.Many2one('res.currency',string="Currency Type")
    amount_in_currency = fields.Monetary(currency_field="currency_id_name",string="Amount in Currency")
    move_currency_id = fields.Many2one('res.currency',string="Currency Move Type")
    rate_khr_inh = fields.Float(string="Rate KHR")
    rate_thb_inh = fields.Float(string="Rate THB")
    driver = fields.Many2one('res.partner',"Driver Name")

    

    def _select(self):
        return super()._select() + " , move.driver_names as driver , move.rate_khr as rate_khr_inh , move.rate_thb as rate_thb_inh , line.amount_currency as amount_in_currency, move.currency_id as move_currency_id, line.name as label_name , line.product_line_date as expense_date , line.price_total as sub_pricetotal , line.price_unit as price_unit_cus , line.currency_id as currency_id_name " 
