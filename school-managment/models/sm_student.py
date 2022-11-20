from odoo import models, fields

class StudentModel(models.Model):
    _name="sm.student"
    _description="Scholl managment students"

    name=fields.Char(string="Student Name",required=True)
    email=fields.Char(string="Email",required=True)
    mobile=fields.Char(string="Mobile")
    father_name=fields.Char(string="Father Name",required=True)
    father_email=fields.Char(string="Father Email",required=True)
    father_mobile=fields.Char(string="Father Mobile",required=True)
    mother_name=fields.Char(string="Mother Name",required=True)
    mother_email=fields.Char(string="Mother Email")
    mother_mobile=fields.Char(string="Mother Mobile",required=True)
    addmition_date=fields.Date(string="Addmittion Date",required=True,default=lambda self:fields.Date.today())
    status = fields.Selection(string="Status",selection=[('pending','Pending'),('approved','Approved'),('discard','Discard'),('hold','Hold')],default="pending")

    user_id=fields.Many2one("res.users","Responsibale",default=lambda self:self.env.user)
    image = fields.Image(string="Image")
    status_id=fields.Many2one("sm.student.status","StatusNew")
