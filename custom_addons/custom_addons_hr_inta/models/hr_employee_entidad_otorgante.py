from odoo import models, fields


class HrEmployeeEntidadOtorgante(models.Model):
    """ Modelo personalizado para entidad otorgante"""

    _name = 'hr.employee.entidad_otorgante'
    _description = 'Entidad Otorgante'

    descripcion = fields.Char(
        string="Descripción", 
        default=None
        )
    legado = fields.Integer(string="Legado", default=None)

    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result