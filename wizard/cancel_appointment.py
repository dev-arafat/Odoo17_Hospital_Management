from odoo import api, fields, models, _

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel appointment'

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
