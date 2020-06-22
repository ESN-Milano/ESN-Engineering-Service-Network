from odoo import models, api, fields, _
from odoo.exceptions import Warning


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def update_so_and_po(self):
        so_list = ['SO/2020/021',
            'SO/2020/018',
            'SO/2020/016',
            'SO/2020/005',
            'SO/2020/004',
            'SO/2020/002',
            'SO/2019/415',
            'SO/2019/384',
            'SO/2019/369',
            'SO/2019/365',
            'SO/2019/289',
            'SO/2019/109',
            'SO/2019/102',
            'SO/2019/071',
            'SO/2019/007',
            'SO/2019/006',
            'SO/2018/296',
            'SO/2018/295',
            'SO/2018/285',
            'SO/2018/026',
            'SO/2018/012',
            'SO/2018/016',
            'SO/2018/041',
            'SO/2018/040',
            'SO/2018/013',]
        for name in so_list:
            order_id = self.env['sale.order'].search([('name','=',name)])
            for line in order_id.order_line:
                line.qty_invoiced = line.product_uom_qty
                line._compute_invoice_status()