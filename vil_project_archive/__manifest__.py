# -*- coding: utf-8 -*-
{
    'name': "Project Archive",

    'summary': """
        Mark as Archive and Active""",

    'description': """
        Mark as Archive and Active
    """,

    'author': "Viltco Technologies",
    'website': "https://www.viltco.com/",

    'category': 'project',
    'version': '0.1',
        'license': 'OPL-1',
          "price":  12,
    "currency": 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],
    'images': ['static/description/banner.png'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
