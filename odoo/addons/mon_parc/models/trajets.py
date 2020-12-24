# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trajet(models.Model):
    _name = 'mon_parc.trajet'
    _rec_name = 'trajet'
        

    trajet = fields.Char('Trajet',  required=True)
    pointdepart = fields.Char('point de depart')
    pointarrivee = fields.Char('point d\'arrivée')
    kilometrage  = fields.Float('Kilométrage',  required=True)
    gasoil  = fields.Float('Gasoil',  required=True)
    peage = fields.Char('Point de péage à l’autoroute',  required=True)
    
    # detail = fields.Char('Détail',  required=True)

