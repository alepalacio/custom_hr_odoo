from odoo import models, fields


class HrEmployeeSituacionRevista1(models.Model):
    
    _name = 'hr.employee.situacion_revista_1'
    _description = 'Situacion Revista 1'

    descripcion = fields.Char(string="Descripcion")
    legado = fields.Char(string="Legado")
    
    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.descripcion}"
            result.append((record.id, name))
        return result
