from odoo import models, fields


class HrEmployeeGrupoFamiliar(models.Model):
    """ Modelo personalizado para grupo familiar """

    
    _name = 'hr.employee.grupo_familiar'
    _description = 'Grupo Familiar'

    nombre = fields.Char(
        string="Nombre"
        )
    tipo_dni = fields.Selection([
        ('du', 'DU'),
        ('pa', 'PA'),
        ('lc', 'LC'),
        ('le', 'LE'),
        ('ci', 'CI'),
        ], string="Tipo DNI")
    dni = fields.Char(
        string="DNI"
        )
    fecha_nacimiento = fields.Date(
        string="Fecha de nacimiento"
    )
    vinculo = fields.Selection([
        ('hijo', 'Hijo'),
        ('conyuge', 'Cónyuge'),
        ('otro', 'Otro'),
        ], string="Vínculo")
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ], string="Género")
    activo = fields.Boolean(
        default=False, 
        string="Activo"
        )
    fecha_desvinculacion = fields.Date(
        string="Fecha de desvinculación"
        )
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
            name = f"{record.nombre}"
            result.append((record.id, name))
        return result