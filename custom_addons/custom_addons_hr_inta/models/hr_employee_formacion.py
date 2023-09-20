from odoo import models, fields, api


class HrEmployeeFormacion(models.Model):
    
    _name = 'hr.employee.formacion'
    _description = 'Formacion'

    titulo_carrera_id = fields.Many2one(
        'hr.employee.titulo_carrera',
        string="Titulo de carrera"
        )
    # formacion_titulo_carrera_descripcion = fields.Char(
    #     string="Descripción del Título de Carrera",
    #     compute="_compute_titulo_carrera_descripcion",
    #     store=True,
    #     #readonly=True,
    #     )
    entidad_otorgante_id = fields.Many2one(
        'hr.employee.entidad_otorgante',
        string="Entidad Otorgante"
        )
    nivel = fields.Selection([
        ('diplomatura', 'Diplomatura'),
        ('doctorado', 'Doctorado'),
        ('especializacion', 'Especialización'),
        ('maestria', 'Maestría'),
        ('post_doctorado', 'Post Doctorado'),
        ('primario', 'Primario'),
        ('secundario', 'Secundario'),
        ('terciario', 'Terciaro - Tecnicatura'),
        ('universitario', 'Universitario')
        ], string="Nivel")
    area_id = fields.Many2one(
        'hr.employee.area',
        string="Área"
        )
    estado = fields.Selection([
        ('si', 'Sí'),
        ('en_curso', 'En Curso'),
        ], string="Estado")
    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de finalización")
    employee_id =fields.Many2one('hr.employee', string='Empleado')
    
    # @api.depends("descripcion")
    # def _compute_titulo_carrera_descripcion(self):
    #     for record in self:
    #         if record.titulo_carrera_id:
    #             record.formacion_titulo_carrera_descripcion = record.titulo_carrera_id.descripcion
    #         else:
    #             record.formacion_titulo_carrera_descripcion = None