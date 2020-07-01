# -*- encoding: utf-8 -*-
{
    'name': 'ESN fix so and po',
    'version': '12.0.0',
    'description': """Fix So and PO error""",

    'depends': [
        'sale_management', 
        'purchase',
    ],
    'data': [
       'actions/actions.xml',
       'views/purchase_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}