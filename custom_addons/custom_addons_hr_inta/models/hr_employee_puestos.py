from odoo import models, fields


class HrEmployeePuestos(models.Model):
    """ Modelo personalizado para puestos """

    
    _name = 'hr.employee.puestos'
    _description = 'Puestos'

    puesto = fields.Char(string="Puesto")
    descripcion = fields.Char(string="Descripción")
    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de finalización")
    estado = fields.Boolean(string="Estado", default=False)
    employee_id = fields.Many2one(
        comodel_name="hr.employee", 
        required=False, 
        ondelete="cascade",
        string="Empleado"
        )
    
    def name_get(self):
        """ This method shows specific attribute in a related field."""
        
        result = []
        for record in self:
            name = f"{record.puesto}"
            result.append((record.id, name))
        return result