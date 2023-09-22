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
    grupo_familiar_id = fields.One2many(
        "hr.employee.grupo_familiar",
        "employee_id",
        string="Grupo Familiar"
    )
    cargo_id = fields.Many2one(
        "hr.employee.cargos",
        string="Cargo"
    )
    cargo_interino_id = fields.Many2one(
        "hr.employee.cargos",
        string="Cargo Interino"
    )