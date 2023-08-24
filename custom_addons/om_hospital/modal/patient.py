from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = 'hospital.tag'
    _description = 'Hospital Tag'

    name   = fields.Char(string='name')
    ref    = fields.Char(string='reference')
    age    = fields.Integer(string='age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    active = fields.Boolean(string='active', default=True)