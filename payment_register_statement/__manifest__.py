# -*- coding: utf-8 -*-
{
    'name': "Payment Register → Statement Line (Cash Journals)",
    'version': '17.0.1.0.1',
    'summary': "Auto-create bank statement lines when registering cash payments",
    'description': """
    When you register a payment via a cash journal, this module automatically
    creates and closes the corresponding bank statement line.
    """,
    'author': "Mohamed Elkmeshi",
    'website': "https://github.com/melkmeshi/payment_register_statement",
    'license': 'LGPL-3',
    'category': 'Accounting/Payments',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
