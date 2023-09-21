from odoo import models, fields


class HrEmployeeCargos(models.Model):
    
    _name = 'hr.employee.cargos'
    _description = 'Cargos'

    descripcion = fields.Char(string="Descripción del cargo", default=None)
    legado = fields.Char(string="Legado", default=None)
    
    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result