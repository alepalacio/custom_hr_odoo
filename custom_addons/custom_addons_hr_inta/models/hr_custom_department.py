from odoo import models, fields, api


class HrCustomDepartment(models.Model):
    """ Modelo heredado y personalizado de hr.departments """
    
    _inherit = 'hr.department'

    name = fields.Char('Nombre Unidad', required=True)
    parent_id = fields.Many2one(string="Unidad padre")
    tipo_unidad_id = fields.Many2one(
        'hr.department.tipo_unidad', 
        string='Tipo Unidad'
        )
