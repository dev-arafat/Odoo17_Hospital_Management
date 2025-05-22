from email.policy import default

from openpyxl.descriptors import String

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name ='patient_id'

    patient_id = fields.Many2one('hospital.patient', String='Patient')
    gender = fields.Selection(
        [
            ('male', "Male"),
            ('female', "Female"),
            ('other', "Other"),
        ],
        String="Gender",
        related='patient_id.gender'
    )
    doctor_id = fields.Many2one('res.users',String="Doctor")
    appointment_time =fields.Datetime(String="Appointment Time",default=fields.Datetime.now)
    booking_date =fields.Date(String="Booking Date",default=fields.Date.context_today)
    ref = fields.Char(String="Reference",tracking=True)
    prescription = fields.Html(String="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="Status", default="draft", required=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.line','appointment_id',string='Pharmacy line')
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_button(self):
        print("button action")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "click successfully",
                'type': 'rainbow_man',
            }
        }
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state="cancel"


class AppointmentPharmacyLine(models.Model):
    _name = 'appointment.pharmacy.line'
    _description = 'Hospital Appointment PharmacyLine'

    product_id = fields.Many2one('product.product', string="Medicine", required=True)
    price_unit = fields.Float(string="Price")
    qty = fields.Float(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appoint")