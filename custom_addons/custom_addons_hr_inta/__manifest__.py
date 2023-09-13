{
    'name': 'Custom Addons Hr INTA',
    'version': '16.0.1.0.0',
    'author': 'Alejandro Palacio',
    'license': 'AGPL-3',
    'website': 'https://git.kan.com.ar/kan/inta/hr-odoo',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_nro_legajo_views.xml',
        #'views/hr_department_tipo_unidad_views.xml',
        'views/hr_employee_situacion_revista_1_views.xml',
    ],
    'installable': True,
    'application': True,
}