from odoo import models, fields


class HrEmployeeFormacion(models.Model):
    
    _name = 'hr.employee.formacion'
    _description = 'Formacion'

    titulo_carrera = fields.Char(string="Titulo de carrera") # Entidad aparte
    entidad_otorgante = fields.Selection([ # Entidad aparte
        ('entidad1', 'Entidad1'),
        ('entidad2', 'Entidad2'),
        ], string="Entidad Otorgante")
    nivel = fields.Selection([ # Select
        ('nivel1', 'Nivel1'),
        ('nivel2', 'Nivel2'),
        ], string="Nivel")
    area = fields.Selection([ # Entidad aparte
        ('area1', 'Area1'),
        ('area2', 'Area2'),
        ('otro', 'Otro'),
        ], string="Área")
    estado = fields.Selection([ # x_finalizado
        ('si', 'Sí'),
        ('en_curso', 'En Curso'),
        ('otro', 'Otro'),
        ], string="Estado")
    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de finalización")
    employee_id =fields.Many2one('hr.employee', string='Empleado')