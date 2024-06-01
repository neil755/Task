# -*- coding: utf-8 -*-
{
    'name': "Task done by Neil",

    'summary': """
       Task""",

    'description': """
        Confirm a sale order and create multiple deliveries against each product.
Quotation should contain a mix of different products
 Identical products must include in a single delivery.
    """,

    'author': "Neil Antony Pinheiro",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
