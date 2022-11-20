from odoo import models, fields

class PropertyModel(models.Model):
    _name = "estate.property"
    _description = "System Properties"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=lambda self:fields.Date.today())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    is_active = fields.Boolean(default=True)
    status = fields.Selection(selection=[('New','new'),('Offer Recieved','offer_recieved'),('Offer Accepted','offer_accepted'),('Cancelled','cancelled')])
    garden_orientation = fields.Selection(selection=[('north','North'),('south','South'),('east','East'),('west','West')])