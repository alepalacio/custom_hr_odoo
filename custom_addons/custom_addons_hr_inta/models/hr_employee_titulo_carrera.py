from odoo import models, fields


class HrEmployeeTituloCarrera(models.Model):
    
    _name = 'hr.employee.titulo_carrera'
    _description = 'Titulo Carrera'

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