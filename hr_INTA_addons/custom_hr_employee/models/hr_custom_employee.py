from odoo import models, fields


class HrCustomEmployee(models.Model):
    
    _inherit = 'hr.employee'

    situacion_revista_1_id = fields.Many2one(
        'hr.employee.situacion_revista_1', 
        string='Situacion Revista 1'
        )
    situacion_revista_2_id = fields.Many2one(
        'hr.employee.situacion_revista_2', 
        string='Situacion Revista 2'
        )