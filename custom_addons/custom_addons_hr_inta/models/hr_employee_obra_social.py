from odoo import models, fields


class HrEmployeeObraSocial(models.Model):
    
    _inherit = 'hr.employee'

    obra_social = fields.Char(
        string="Obra social", 
        default=None
        )