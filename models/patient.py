from datetime import date
from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    image_1920 = fields.Image(string="Image", max_width=1920, max_height=1920)
    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    birth_date = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    patient_tag = fields.Many2many('patient.tag', string="Patient Tag")
    gender = fields.Selection(
        [
            ('male', "Male"),
            ('female', "Female"),
            ('other', "Other"),
        ],
        string="Gender",
        default='male',
        required=True,
        tracking=True
    )
    active = fields.Boolean(string="Active", default=True, tracking=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
            else:
                record.age = 0
