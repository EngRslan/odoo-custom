{
    'name': 'School Managment',
    'version': '1.0',
    'category': 'Administration',
    'sequence': 1,
    'summary': 'View and manage your school',
    'description': "",
    'website': 'https://www.proeyes.org',
    'license': 'LGPL-3',
    'depends': [
        'base_setup'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/sm_students_views.xml',
        'views/sm_students_status_views.xml',
        'views/sm_menus.xml'
    ],
    'application': True,
}