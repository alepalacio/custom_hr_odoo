{
    'name': 'Custom Addons Hr INTA',
    'version': '16.0.1',
    'author': 'Alejandro Palacio',
    'license': 'AGPL-3',
    'website': 'https://www.linkedin.com/in/alepalacio/',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_custom_department_view.xml',
        'views/hr_custom_employee_view.xml',
        'views/hr_custom_employee_formacion_view.xml',
        'views/hr_custom_employee_related_contacts_button.xml',
        ],
    'installable': True,
    'application': True,
}