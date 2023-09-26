from odoo import models, fields


class HrDepartmentTipoUnidad(models.Model):
    """ Modelo personalizado para tipos de unidad """

    _name = 'hr.department.tipo_unidad'
    _description = 'Departamento - Tipo Unidad'

    descripcion = fields.Char(string="Descripcion")
    legado = fields.Integer(string="Legado", default=None)
    tipo_estructura =  fields.Selection([
        ('horizontal', 'Horizontal'),
        ('vertical_linea', 'Vertical Linea'),
        ('vertical_staff', 'Vertical Staff')
        ], string="Tipo Estructura"
        )
    
    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result
