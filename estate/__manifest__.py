{
    'name': 'Realstate',
    'version': '1.2',
    'category': 'Sales',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': 'https://www.odoo.com/page/raslan',
    'depends': [
        'base_setup'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'application': True,
}