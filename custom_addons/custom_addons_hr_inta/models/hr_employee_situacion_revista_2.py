from odoo import models, fields


class HrEmployeeSituacionRevista2(models.Model):
    
    _name = 'hr.employee.situacion_revista_2'
    _description = 'Situacion Revista 2'

    descripcion = fields.Char(string="Descripcion")
    id_buxis = fields.Char(string="ID Buxis")