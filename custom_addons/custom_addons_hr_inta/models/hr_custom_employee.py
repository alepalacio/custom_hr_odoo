from odoo import models, fields, api


class HrCustomEmployee(models.Model):
    """ Modelo heredado y personalizado de hr.employees """
    
    _inherit = 'hr.employee'

    cuil = fields.Char(string="Cuil")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced'),
        ('separado_de_hecho', 'Separado de Hecho'),
        ('separado', 'Separado'),
        ('union_civil', 'Union Civil'),
        ('unido_de_hecho', 'Unido de Hecho'),
        ('otros', 'Otros')
        ])
    nro_legajo = fields.Integer(
        string="Nro. legajo", 
        default=None
        )
    obra_social = fields.Char(
        string="Obra social", 
        default=None
        )
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
    address_home_id = fields.Many2one(
        'res.partner', 
        'Dirección', 
        help='Ingrese acá la dirección privada del empleado.',
        groups="hr.group_hr_user", 
        tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        )
    leave_date_from = fields.Date(string="Desde la fecha")
    leave_date_to = fields.Date(string="Hasta la fecha")
    sindicato = fields.Char(string="Sindicato")
    seguro = fields.Char(string="Seguro")
    art = fields.Char(string="ART")
    actividad_principal = fields.Char(string="Actividad principal")
    department_id = fields.Many2one(string="Unidad")
    parent_id = fields.Many2one(string="Responsable Jerárquico")
    identification_id = fields.Char(string="Documento")
    mobile_phone = fields.Char(string="Teléfono móvil laboral")
    work_phone = fields.Char(string="Teléfono laboral")
    