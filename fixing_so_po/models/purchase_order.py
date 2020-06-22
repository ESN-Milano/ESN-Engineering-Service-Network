from odoo import models, api, fields, _
from odoo.exceptions import Warning


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    to_fix = fields.Boolean('Fix invoiced status', default=False)

    def recompute_invoice_status(self):
        for order in self:
            order._get_invoiced()

    @api.depends('state', 'order_line.qty_invoiced', 'order_line.qty_received', 'order_line.product_qty')
    def _get_invoiced(self):
        for order in self:
            if order.to_fix:
                order.invoice_status = 'invoiced'
            else:
                super(PurchaseOrder, order)._get_invoiced()