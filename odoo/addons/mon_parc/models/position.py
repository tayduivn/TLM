

from odoo import models, fields, api


class position(models.Model):
    _name = 'mon_parc.position'
    # _rec_name = 'nom'

    client_id = fields.Many2one(comodel_name='res.partner', string='Client', domain="[('customer_rank' , '=', 1)]")
    trajet_id = fields.Many2one(comodel_name='mon_parc.trajet', string='Trajet')

    Palette = fields.Char('Palette')
    Suspendu = fields.Char('Suspendu')
    Coli = fields.Char('Coli')
    Rouleau = fields.Char('Rouleau')
    Piece = fields.Char('Piece')
    Poids = fields.Char('Poids')
    Volume = fields.Char('Volume')
