from odoo import models, fields


class StudentStatusModel(models.Model):
    _name = "sm.student.status"
    _description="School managment students Status"

    name = fields.Char(string="Name",required=True)