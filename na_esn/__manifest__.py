# -*- encoding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2019  Nexapp
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
# Fort the security group for the meeting rooms: Original idea from module web_disable_export_group by Onestein,
# reviewed and modified for v11 by InfoTerra and Nexapp.

{
    'name': 'Nexapp ESN',
    'summary': 'Customizzazioni per ESN',
    'description': "Customizzazioni per ESN",
    'version': '1',
    'depends':	[
        'base',
        'crm',
        'sale',
        'purchase',
        'sale_management',
        'sale_stock',
        'maintenance',
        'account',
        'maintenance',
        'web_tree_dynamic_colored_field',
    ],
    'author': "Nexapp",
    'license': "AGPL-3",
    'website': 'https://www.nexapp.it',
    'category': 'Nexapp',
    'sequence':	100,
    'data': [
       'security/ir.model.access.csv',
       'views/metodipagamento_view.xml',
       'views/partner_view.xml',
       'views/invoice_view.xml',
       'views/crm_view.xml',
       'views/maintenance_view.xml',
       'views/order_view.xml',
       'report/invoice_report.xml',
       'report/order_report.xml',
       'report/purchase_report_templates.xml'

      ],
}
