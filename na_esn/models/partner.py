# Copyright (C) 2019 Nexapp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, exceptions

class CustomContatti(models.Model):
    _inherit = 'res.partner'

    nome_corretto = fields.Char(string="Nome semplice")
    metodo_pagamento = fields.Many2one('metodi.pagamento', string='Metodo di Pagamento')

    @api.model
    def create(self, values):
        if 'name' in values:
            values['nome_corretto'] = values['name'].replace('.', '')
        return super(CustomContatti, self).create(values)

    @api.multi
    def write(self, values):
        if 'name' in values:
            values['nome_corretto'] = values['name'].replace('.', '')
        return super(CustomContatti, self).write(values)
