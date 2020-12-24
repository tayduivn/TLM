# -*- coding: utf-8 -*-

from logging import log
from odoo.tools.misc import logged
from odoo import models, fields, _ , api
from odoo.exceptions import UserError


class voyage(models.Model):
    _name = 'mon_parc.voyage'

    datedepart = fields.Date('date de départ')
    datearrivee = fields.Date('Date Date d\'échéance')
    pointdepart = fields.Char('point de depart')
    pointarrivee = fields.Char('point d\'arrivée')
    ndossier = fields.Char('N° Dossier')
    commentaire = fields.Char('Commentaire')
    factureid = fields.Char('N° Facture')
    Avance = fields.Char('Avance')
    reste = fields.Char('Le reste')

    tracteur_id = fields.Many2one(comodel_name='fleet.vehicle',  domain="[('tag_ids' , '=', 10)]")
    remorque_id = fields.Many2one(comodel_name='fleet.vehicle',  domain="[('tag_ids' , '=', 9)]")
    chauffeur_id = fields.Many2one(comodel_name='hr.employee', domain="[('department_id' , '=', 6)]")
    chauffeur2_id = fields.Many2one( comodel_name='hr.employee', domain="[('department_id' , '=', 6)]")
    client_id = fields.Many2one(comodel_name='res.partner', string='Client', domain="[('customer_rank' , '=', 1)]")

    trajets_id = fields.Many2one(comodel_name='mon_parc.trajet')

    type_voyage = fields.Selection([('Import', 'Import'), ('Export', 'Export')],  required=True)


    

    @api.model
    def create(self, vals):
        rec = super(voyage, self).create(vals)
        # if not rec.remorque_id:
        rec._create_check_sequence()
        rec._update_fleet_state()
        return rec

    


    def _create_check_sequence(self):
        self.mission_id = self.env['fleet.vehicle.mission'].sudo().create({
            'name': self.trajets_id.trajet,
            'comment': self.commentaire,
            'date_arrivee': self.datearrivee,
            'date_sortie':  self.datedepart,
            'vehicle_id': self.remorque_id.id
            })
        self.mission_id = self.env['fleet.vehicle.mission'].sudo().create({
            'name': self.trajets_id.trajet,
            'comment': self.commentaire,
            'date_arrivee': self.datearrivee,
            'date_sortie':  self.datedepart,
            'vehicle_id': self.tracteur_id.id
            })
    
    def _update_fleet_state(self):
        self.env['fleet.vehicle'].search([('id', '=', self.remorque_id.id)]).write({'state_id': 7})
        self.env['fleet.vehicle'].search([('id', '=', self.tracteur_id.id)]).write({'state_id': 7})
