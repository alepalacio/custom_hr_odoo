from odoo import models, fields


class HrDepartmentTipoUnidad(models.Model):
    
    _name = 'hr.department.tipo_unidad'
    _description = 'Departamento - Tipo Unidad'

    descripcion = fields.Char(string="Descripcion")
    legado = fields.Char(string="Legado", invisible=True, default=None, transient=True)
    tipo_estructura =  fields.Selection([ # Entidad aparte
        ('horizontal', 'Horizontal'),
        ('vertical_linea', 'Vertical Linea'),
        ('vertical_staff', 'Vertical Staff')
        ], string="Entidad Otorgante"
        )
    
    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result
