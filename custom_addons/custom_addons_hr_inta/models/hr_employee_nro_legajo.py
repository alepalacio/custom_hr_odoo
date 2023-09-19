from odoo import models, fields


class HrEmployeeNroLegajo(models.Model):
    
    _inherit = 'hr.employee'

    nro_legajo = fields.Integer(
        string="Nro. legajo", 
        default=None
        )
