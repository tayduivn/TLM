# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mon_parc(models.Model):
     _name = 'mon_parc.mon_parc'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     def _clickme():
         print('hello azhar')
         return 'hello world '

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100
    