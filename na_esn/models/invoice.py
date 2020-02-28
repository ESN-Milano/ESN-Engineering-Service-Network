# Thanks to Prakash - Odoo Forum
# (C) 2013-2016 Camptocamp SA (Yannick Vaucher)
# (C) 2004-2016 Odoo S.A. (www.odoo.com)
# (C) 2015-2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#Thanks to aslamsha22 https://stackoverflow.com/users/7951914/aslamsha22 - Stackoverflow
# Copyright (C) 2019 Nexapp

from odoo import api, fields, models, exceptions
from odoo.exceptions import UserError, AccessError, ValidationError
from datetime import date


class CustomFattura(models.Model):
    _inherit = 'account.invoice'

    metodo_pagamento = fields.Many2one('metodi.pagamento', string='Metodo di Pagamento', default=lambda self: self.env['metodi.pagamento'].search([('name','=','Bonifico')]))
    is_tranche = fields.Boolean(string='Utilizza tranche pagamenti', help="La funzionalita tranche pagamenti viene utilizzata per gestire l'importo da versare alla consegna e al collaudo")
    data_consegna = fields.Date(string='Data Consegna', copy=False)
    data_collaudo = fields.Date(string='Data Collaudo', copy=False)
    importo_consegna = fields.Float(string='Importo alla consegna')
    importo_collaudo = fields.Float(string='Importo al collaudo')
    is_consegna_due = fields.Boolean(compute='_compute_is_consegna_due')
    is_consegna_due_stored = fields.Boolean()
    is_consegna_payed = fields.Boolean()
    is_collaudo_due = fields.Boolean(compute='_compute_is_collaudo_due')
    is_collaudo_due_stored = fields.Boolean()
    is_collaudo_payed = fields.Boolean()
    # Serve per capire se il metodo di pagamento e RIBA
    is_riba_due = fields.Boolean(compute='_compute_is_riba_due')
    is_riba_due_stored = fields.Boolean(copy=False)

    # code from https://stackoverflow.com/questions/45912670/how-to-set-character-limit-in-text-field
    @api.one
    @api.constrains('comment')
    def _check_comment(self):
        if self.comment:
            if len(self.comment) > 200:
                raise ValidationError('Il numero di caratteri del campo Termini e condizioni non puo essere maggiore di 200')

    @api.depends('metodo_pagamento')
    def _compute_is_riba_due(self):
        for invoice in self:
            if invoice.state in ['draft', 'open', 'paid', 'proforma', 'proforma2']:
                try:
                    if invoice.metodo_pagamento:
                        mp = invoice.metodo_pagamento.name.replace('.', '')
                        mp = mp.replace(" ", "")
                        if mp.upper() == "RIBA":
                            # if invoice.date_due[:7] == date.today().strftime('%Y-%m'):
                                invoice.is_riba_due = True
                                if not invoice.is_riba_due_stored:
                                    invoice.write({
                                        'is_riba_due_stored': True
                                    })
                            # else:
                            #     invoice.is_riba_due = False
                            #     invoice.write({
                            #         'is_riba_due_stored': False
                            #     })
                except:
                    pass
            elif invoice.state in ['cancel']:
                invoice.is_riba_due = False
                if invoice.is_riba_due_stored:
                    invoice.write({
                        'is_riba_due_stored': False
                    })

    def _compute_is_consegna_due(self):
        for invoice in self:
            if invoice.state in ['draft', 'open', 'paid', 'proforma', 'proforma2'] and invoice.is_tranche:
                if invoice.data_consegna < fields.Date.today() and not invoice.is_consegna_payed:
                    invoice.is_consegna_due = True
                    if not invoice.is_consegna_due_stored:
                        invoice.write({
                            'is_consegna_due_stored': True
                        })
                else:
                    invoice.is_consegna_due = False
                    if invoice.is_consegna_due_stored:
                        invoice.write({
                            'is_consegna_due_stored': False
                        })
            elif invoice.state in ['draft', 'open', 'paid', 'proforma', 'proforma2', 'cancel']:
                invoice.is_consegna_due = False
                if invoice.is_consegna_due_stored:
                    invoice.write({
                        'is_consegna_due_stored': False
                    })

    def _compute_is_collaudo_due(self):
        for invoice in self:
            if invoice.state in ['draft', 'open', 'paid', 'proforma', 'proforma2'] and invoice.is_tranche:
                if invoice.data_collaudo < fields.Date.today() and not invoice.is_collaudo_payed:
                    invoice.is_collaudo_due = True
                    if not invoice.is_collaudo_due_stored:
                        invoice.write({
                            'is_collaudo_due_stored': True
                        })
                else:
                    invoice.is_collaudo_due = False
                    if invoice.is_collaudo_due_stored:
                        invoice.write({
                            'is_collaudo_due_stored': False
                        })
            elif invoice.state in ['draft', 'open', 'paid', 'proforma', 'proforma2', 'cancel']:
                invoice.is_collaudo_due = False
                if invoice.is_collaudo_due_stored:
                    invoice.write({
                        'is_collaudo_due_stored': False
                    })

    @api.onchange('partner_id')
    def partner_id_mp(self):
        for p in self:
            if p.partner_id.metodo_pagamento:
                p.metodo_pagamento = p.partner_id.metodo_pagamento

    @api.onchange('is_tranche')
    def change_is_tranche(self):
        for invoice in self:
            if invoice.is_tranche:
                try:
                    move = self.env['stock.picking'].search([('origin', '=', invoice.origin)])
                    invoice.data_consegna = move[0].date_done
                except:
                    pass
