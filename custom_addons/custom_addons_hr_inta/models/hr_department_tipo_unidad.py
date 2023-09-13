from odoo import models, fields


class HrDepartmentTipoUnidad(models.Model):
    
    _name = 'hr.department.tipo_unidad'
    _description = 'Departamento - Tipo Unidad'

    descripcion = fields.Char(string="Descripcion")
    id_buxis = fields.Char(string="ID Buxis")
