# -*- coding: utf-8 -*-

from logging import log
from odoo.tools.misc import logged
from odoo import models, fields, api


class voyage(models.Model):
    _name = 'mon_parc.voyage'

    datedepart = fields.Date('date de départ')
    datearrivee = fields.Date('date d\'arrivée')
    pointdepart = fields.Char('point de depart')
    pointarrivee = fields.Char('point d\'arrivée')
    tracteur_id = fields.Many2one(comodel_name='mon_parc.tracteur')
    remorque_id = fields.Many2one(comodel_name='mon_parc.remorque')
    chauffeur_id = fields.Many2one(comodel_name='hr.employee', domain=[('department_id', '=', 6)])


