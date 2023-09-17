from odoo import models, fields


class HrEmployeeGrupoFamiliar(models.Model):
    
    _name = 'hr.employee.grupo_familiar'
    _description = 'Grupo Familiar'

    nombre = fields.Char(string="Nombre")
    tipo_dni = fields.Selection([ # A CONSULTAR
        ('dni1', 'DNI'),
        ('dni2', 'DNI2'),
        ], string="Tipo DNI")
    dni = fields.Integer(string="DNI")
    vinculo = fields.Selection([
        ('madre', 'Madre'),
        ('padre', 'Padre'),
        ('hija/o', 'Hija/o'),
        ('hermana/o', 'Hermana/o'),
        ('otro', 'Otro'),
        ], string="Vinculo")
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ], string="Género")
    activo = fields.Boolean(default=False, string="Activo")
    fecha_desvinculacion = fields.Date(string="Fecha de desvinculación")
    employee_id =fields.Many2one('hr.employee', string='Empleado')