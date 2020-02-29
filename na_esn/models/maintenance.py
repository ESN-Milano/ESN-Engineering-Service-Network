# Copyright (C) 2019 Nexapp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, exceptions


class CustomMaintenance(models.Model):
    _inherit = 'maintenance.request'

    tecnici = fields.Many2many('res.users', string="Tecnici")
    tecnici_char = fields.Char(store=True)

    @api.onchange('tecnici')
    def _onchange_tecnici(self):
        for maintenance in self:
            maintenance.tecnici_char = ''
            string_tecnici = ''
            for tecnico in maintenance.tecnici:
                if not string_tecnici:
                    string_tecnici += 'Tecnici: ' + tecnico.name
                else:
                    string_tecnici += ', ' + tecnico.name
            maintenance.tecnici_char = string_tecnici
