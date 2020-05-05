from odoo import fields, models, api


class SaleOrder (models.Model):
    _inherit = 'sale.order'

    agreed_date = fields.Date(string='Data Concordata')
    estimated_delivery_date = fields.Date(string='Data Consegna Stimata')
