# Copyright (C) 2019 Nexapp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, exceptions


class CustomMaintenance(models.Model):
    _inherit = 'maintenance.request'

    na_technicians = fields.Many2many('res.partner', domain=[('is_tecnico', '=', True)], string="Tecnici")
    tecnici_char = fields.Char(store=True)

    @api.onchange('na_technicians')
    def _onchange_na_technicians(self):
        for maintenance in self:
            maintenance.tecnici_char = ''
            string_tecnici = ''
            for tecnico in maintenance.na_technicians:
                if not string_tecnici:
                    string_tecnici += tecnico.display_name
                else:
                    string_tecnici += ', ' + tecnico.display_name
            maintenance.tecnici_char = string_tecnici
