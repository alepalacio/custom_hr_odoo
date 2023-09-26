from odoo import models, fields, api


class HrEmployeeFormacion(models.Model):
    """ Modelo personalizado para formaciones"""

    
    _name = 'hr.employee.formacion'
    _description = 'Formacion'

    titulo_carrera_id = fields.Many2one(
        'hr.employee.titulo_carrera',
        string="Título"
        )
    formacion_titulo_carrera_descripcion = fields.Char(
        string="Título",
        related='titulo_carrera_id.descripcion',
        store=True,
        readonly=True,
        )
    entidad_otorgante_id = fields.Many2one(
        'hr.employee.entidad_otorgante',
        string="Entidad Otorgante"
        )
    entidad_otorgante_descripcion = fields.Char(
        string="Entidad Otorgante",
        related="entidad_otorgante_id.descripcion",
        store=True,
        readonly=True
    )
    area_id = fields.Many2one(
        'hr.employee.area',
        string="Área"
        )
    area_descripcion = fields.Char(
        string="Área",
        related="area_id.descripcion",
        store=True,
        readonly=True
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
    estado = fields.Selection([
        ('si', 'Sí'),
        ('en_curso', 'En Curso'),
        ('finalizado', 'Finalizado'),
        ('abandono', 'Abandonó'),
        ('baja', 'Baja'),
        ('no_inicio', 'No Inició'),
        ('otro', 'Otro'),
        ('renuncia', 'Renuncia'),
        ('suspendido', 'Suspendido'),
        ], string="Estado")
    fecha_inicio = fields.Date(string="Fecha Inicio")
    fecha_fin = fields.Date(string="Fecha Fin")
    employee_id =fields.Many2one('hr.employee', string='Empleado')