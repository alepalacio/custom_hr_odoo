{
    'name': 'Custom Addons Hr INTA',
    'version': '16.0.1.0.0',
    'author': 'Alejandro Palacio',
    'license': 'AGPL-3',
    'website': 'https://git.kan.com.ar/kan/inta/hr-odoo',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_custom_employee_view.xml',
        'views/hr_custom_department_view.xml',
        'views/hr_custom_employee_cuil_view.xml',
    ],
    'installable': True,
    'application': True,
}