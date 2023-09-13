from odoo import models, fields


class HrEmployeeSituacionRevista1(models.Model):
    
    _name = 'hr.employee.situacion_revista_1'
    _description = 'Situacion Revista 1'

    descripcion = fields.Char(string="Descripcion")
    id_buxis = fields.Integer(string="ID Buxis")
