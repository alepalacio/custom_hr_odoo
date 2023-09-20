from odoo import models, fields


class HrEmployeeArea(models.Model):
    
    _name = 'hr.employee.area'
    _description = 'Area'

    descripcion = fields.Char(
        string="Descripción", 
        default=None
        )
    legado = fields.Char(string="Legado")

    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result