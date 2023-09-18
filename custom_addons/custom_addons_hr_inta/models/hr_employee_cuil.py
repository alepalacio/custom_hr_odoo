from odoo import models, fields


class HrEmployeeCuil(models.Model):
    
    _inherit = 'hr.employee'

    cuil = fields.Char(string="Cuil")
