from odoo import api, fields, models, _

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(String="Name", required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True )
    colour = fields.Integer(string="Colour")