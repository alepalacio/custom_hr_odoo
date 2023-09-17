from odoo import models, fields


class HrEmployeeFormacion(models.Model):
    
    _name = 'hr.employee.formacion'
    _description = 'Formacion'

    titulo_carrera = fields.Char(string="Titulo de carrera")
    entidad_otorgante = fields.Selection([ # A CONSULTAR
        ('entidad1', 'Entidad1'),
        ('entidad2', 'Entidad2'),
        ], string="Entidad Otorgante")
    nivel = fields.Selection([
        ('nivel1', 'Nivel1'),
        ('nivel2', 'Nivel2'),
        ], string="Nivel")
    area = fields.Selection([
        ('area1', 'Area1'),
        ('area2', 'Area2'),
        ('otro', 'Otro'),
        ], string="Área")
    estado = fields.Selection([
        ('estado1', 'Estado1'),
        ('estado2', 'Estado2'),
        ('otro', 'Otro'),
        ], string="Estado")
    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de finalización")
    employee_id =fields.Many2one('hr.employee', string='Empleado')