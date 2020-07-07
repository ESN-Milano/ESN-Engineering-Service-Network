from odoo import models, api, fields, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    set_paid_state = fields.Boolean('Paid status', default=False)

    @api.depends('set_paid_state')
    def recompute_invoice_status(self):
        for order in self:
            if order.set_paid_state:
                order.state = 'paid'