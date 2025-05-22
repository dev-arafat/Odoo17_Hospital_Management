# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.3',
    'summary': ' Hospital Management System',
    'sequence': 10,
    'description': """
        Hospital Management System
    """,
    'category': 'Hospital',
    'website': '',
    'depends': ['mail'],
    'data': [
            'security/ir.model.access.csv',
            'views/menu.xml',
            'views/patient.xml',
            'views/appointment.xml',
            'views/female_patient.xml',
            'views/male_patient.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install':False,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'om_hospital/static/src/css/style.css',
        ],
},
'license': 'LGPL-3',
}
