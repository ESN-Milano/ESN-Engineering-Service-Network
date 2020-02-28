# Copyright (C) 2019 Nexapp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import  api, fields, models


class MetodiPagamento(models.Model):

    _name = 'metodi.pagamento'
    _order = 'name'
    _rec_name = 'name' #Serve per dire quale campo deve essere visualizzato nella selection

    name = fields.Char(string="Metodo di Pagamento", required=True)
    ignora_scadenza = fields.Boolean(string="Ignora scadenza", help="Non mostra la fattura tra le scadute anche se e "
                                                                    "stata superata la data di scadenza", default=False)

    _sql_constraints = [
        ('name', 'unique (name)', 'Esiste gia un metodo di pagamento con questo nome')
    ]
