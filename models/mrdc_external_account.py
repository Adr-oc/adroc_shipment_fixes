# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MrdcExternalAccount(models.Model):
    _inherit = 'mrdc.external_account'

    referencia_1 = fields.Char(
        string='Referencia 1',
        help='Referencia 1 del embarque.',
        tracking=True
    )

    referencia_2 = fields.Char(
        string='Referencia 2',
        help='Referencia 2 del embarque.',
        tracking=True
    )

    referencia_3 = fields.Char(
        string='Referencia 3',
        help='Referencia 3 del embarque.',
        tracking=True
    )

    duca = fields.Char(
        string='DUCA',
        help='Número de Declaración Aduanera del embarque.',
        tracking=True
    )

    @api.model
    def default_get(self, fields):
        res = super(MrdcExternalAccount, self).default_get(fields)
        # Get shipment_id from context
        shipment_id = self.env.context.get('default_shipment_id')
        if shipment_id:
            shipment = self.env['mrdc.shipment'].browse(shipment_id)
            if shipment:
                res.update({
                    'referencia_1': shipment.ref_1,
                    'referencia_2': shipment.ref_2,
                    'referencia_3': shipment.ref_3,
                    'duca': shipment.customs_declaration_number,
                })
        return res
