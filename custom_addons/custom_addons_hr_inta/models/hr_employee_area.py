from odoo import models, fields


class HrEmployeeArea(models.Model):
    """ Modelo personalizado para áreas """

    _name = 'hr.employee.area'
    _description = 'Area'

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