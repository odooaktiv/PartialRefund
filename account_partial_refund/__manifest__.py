# -*- coding: utf-8 -*-

{
    'name': 'Partial Refund',
    'version': '10.0.1.0.0',
    'category': 'account',
    'license': 'AGPL-3',
    'description': """
Partial Refund
===================================================
""",
    'website': 'www.aktivsoftware.com',
    'author': 'Aktiv software',
    'license': "AGPL-3",
    'maintainer': 'Aktiv software',
    'depends': ['account'],
    'data': [
        'views/account_invoice_view.xml',
        'wizard/account_invoice_refund_view.xml',
    ],

    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
