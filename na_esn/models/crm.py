# Copyright (C) 2019 Nexapp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, exceptions


class CustomCrm(models.Model):
    _inherit = 'crm.lead'

    settore = fields.Many2one('crm.lead.tag', string="Settore")
