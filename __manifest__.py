# -*- coding: utf-8 -*-
{
    'name': "Beekeeper connector",

    'summary': """
        Beekeeper connector""",

    'description': """
       Sync employees between Odoo and Beekeeper.
    """,

    'author': "Edward",
    'website': "http://odoo.apps-script.ninja",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/beekeeper.res_config_settings_view_form.xml',
        'views/beekeeper.hr_view_employee_form.xml',
        'views/beekeeper.custom_fields.xml',
        'views/menu/beekeeper.actions.xml',
        'views/menu/beekeeper.menu.xml',
        'schedulers/schedulers.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'images': []
}
