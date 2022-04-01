# -*- coding: utf-8 -*-

from odoo import models, fields, api

class account_exc_rate(models.Model):
    _inherit='account.move'
    
    total_exc_khr = fields.Monetary(compute = '_compute_total_khmer', string="Total Amount in Khmer", currency_field='khr_currency_id')
    total_exc_thb = fields.Monetary(compute = '_compute_total_bat', string="Total Amount in THB", currency_field='thb_currency_id')
    rate_khr = fields.Float(string="Exchange Khmer")
    rate_thb = fields.Float(string="Exchange Thb")
    khr_currency_id = fields.Many2one('res.currency', compute = '_compute_total_khmer')
    thb_currency_id = fields.Many2one('res.currency', compute = '_compute_total_bat')
    source_origin = fields.Many2one('sale.origin', string="Source")
    approver = fields.Many2one('res.users', string="Approve By", help="សម្រាប់តែខាងផ្នែកដឹកជញ្ជូន:ត្រូវរើសអ្នកអនុញ្ញាតសម្រាប់ការស្នើរសុំបើកប្រាក់បំរុងមុន។")

    driver_names = fields.Many2one(
        comodel_name="res.partner",
        store=True,
        readonly=False,
        compute="_compute_driver_names",
        help="ឈ្មោះអ្នកបើកឡាន",
        
    )

    @api.depends("invoice_line_ids", "invoice_line_ids.move_line_ids")
    def _compute_driver_names(self):
        for invoice in self:
            invoice.driver_names = invoice.mapped(
                "invoice_line_ids.move_line_ids.picking_id.driver_name.id"
            )
    
    
    # functions to computer the total amunte that from input currency khmer and thb into USDD 
    @api.depends('amount_total')
    def _compute_total_khmer(self):
        for invoice in self:
            invoice.total_exc_khr = invoice.amount_total * invoice.rate_khr 
            invoice.khr_currency_id = self.env['res.currency'].search([('id','=',66)])

    def _compute_total_bat(self):
        for i in self:
            i.total_exc_thb = i.amount_total * i.rate_thb
            i.thb_currency_id = self.env['res.currency'].search([('id','=',137)])


    

    


