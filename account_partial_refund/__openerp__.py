# -*- coding: utf-8 -*-

{
    'name': 'Partial Refund',
    'version': '1.0',
    'category': 'account',
    'description': """
Partial Refund
===================================================
""",
    'website': 'www.aktivsoftware.com',
    'author': 'Aktiv software',
    'maintainer': 'Aktivsoftware',
    'depends': ['account'],
    'data': [
        'views/account_invoice_view.xml',
        'wizard/account_invoice_refund_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
