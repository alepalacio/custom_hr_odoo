from odoo import models, fields


class HrEmployeeTituloCarrera(models.Model):
    """ Modelo personalizado para títulos de carrera """

    
    _name = 'hr.employee.titulo_carrera'
    _description = 'Titulo Carrera'

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