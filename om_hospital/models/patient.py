from email.policy import default

from openpyxl.descriptors import String
from datetime import datetime, date
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.populate import compute


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(String="Name",required=True,tracking=True)
    ref = fields.Char(String="Reference",tracking=True)
    birth_date = fields.Date(String="Date of Birth")
    age = fields.Integer(String="Age",compute='_compute_age',required=True,tracking=True)
    gender = fields.Selection(
        [
            ('male', "Male"),
            ('female', "Female"),
            ('other', "Other"),
        ],
        String="Gender",
        default='male',
        required=True,
        tracking=True
    )
    active = fields.Boolean(String="active", default=True,tracking=True)


    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
                record.age = age
            else:
                record.age = 1


