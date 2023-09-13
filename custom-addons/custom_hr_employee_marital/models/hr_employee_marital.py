from odoo import models, fields


class HrEmployeeMarital(models.Model):
    
    _inherit = 'hr.employee'

    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced'),
        ('separado_de_hecho', 'Separado de Hecho'),
        ('separado', 'Separado'),
        ('union_civil', 'Union Civil'),
        ('unido_de_hecho', 'Unido de Hecho'),
        ('otros', 'Otros')
        ])
