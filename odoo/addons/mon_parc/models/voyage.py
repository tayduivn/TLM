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

    mission_id = fields.Many2one('fleet.vehicle.mission', 'Mission')
    # mission = fields.Float(compute="_get_mission",
    #                        inverse='_set_mission', string='Mission Value')
    

    @api.model
    def create(self, vals):
        rec = super(voyage, self).create(vals)
        # if not rec.remorque_id:
        rec._create_check_sequence()
        return rec


    def _create_check_sequence(self):
        self.mission_id = self.env['fleet.vehicle.mission'].sudo().create({
            'comment': self.commentaire,
            'date_arrivee': self.pointdepart,
            'date_sortie':  self.datearrivee,
            'vehicle_id': self.tracteur_id
            })

    # def create(self):
    #     self._get_mission()
    #     self._set_mission()

    # def _get_mission(self):
    #     self.mission = 0.0
    #     for record in self:
    #         record.mission = False
    #         if record.mission_id:
    #             record.mission = record.mission_id.value

    # def _set_mission(self):
    #     for record in self:
    #         # if not record.mission:
    #         #     raise UserError(_('Emptying the mission value of a vehicle is not allowed.'))
    #         self.mission = self.env['fleet.vehicle.mission'].create({
    #             'comment': record.commentaire,
    #             'date_arrivee': record.datedepart,
    #             'date_sortie': record.datedepart ,
    #             'vehicle_id': record.vehicle_id.id
    #         })
    #         self.mission_id = self.mission
