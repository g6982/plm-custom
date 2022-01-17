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
    # amount_due_khr = fields.Monetary(compute = '_compute_amount_due_khr', string="Amount Due in KHR", currency_field='khr_currency_id')
    # amount_due_thb = fields.Monetary(compute = '_compute_amount_due_thb', string="Amount Due in THB", currency_field='thb_currency_id')

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
    

    


