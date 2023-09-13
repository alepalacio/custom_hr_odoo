from odoo import models, fields


class HrEmployeeNroLegajo(models.Model):
    
    _inherit = 'hr.department'

    tipo_unidad = fields.Char(string="Nro. legajo")
