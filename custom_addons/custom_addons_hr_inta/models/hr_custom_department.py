from odoo import models, fields


class HrCustomDepartment(models.Model):
    
    _inherit = 'hr.department'

    tipo_unidad_id = fields.Many2one(
        'hr.department.tipo_unidad', 
        string='Tipo Unidad'
        )
