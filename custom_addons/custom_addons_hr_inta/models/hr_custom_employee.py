from odoo import models, fields, api


class HrCustomEmployee(models.Model):
    
    _inherit = 'hr.employee'

    situacion_revista_1_id = fields.Many2one(
        'hr.employee.situacion_revista_1', 
        string='Situacion Revista 1'
        )
    situacion_revista_2_id = fields.Many2one(
        'hr.employee.situacion_revista_2', 
        string='Situacion Revista 2'
        )
    puesto_id = fields.One2many(
        'hr.employee.puestos', 
        "employee_id", 
        string="Puestos"
        )
    formacion_id = fields.One2many(
        "hr.employee.formacion",
        "employee_id",
        string="Formación"
    )
    formacion_titulo_carrera_descripcion = fields.Char(
        string="Descripción del Título de Carrera",
        compute="_compute_titulo_carrera_descripcion",
        store=True,
        #readonly=True,
        )
    grupo_familiar_id = fields.One2many(
        "hr.employee.grupo_familiar",
        "employee_id",
        string="Grupo Familiar"
    )
    
    @api.depends("formacion_id")
    def _compute_titulo_carrera_descripcion(self):
        for record in self:
            if record.formacion_id:
                record.formacion_titulo_carrera_descripcion = record.formacion_id.titulo_carrera_id.descripcion
            else:
                record.formacion_titulo_carrera_descripcion = None