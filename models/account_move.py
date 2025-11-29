# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    duca = fields.Char(
        string='DUCA',
        help='Número de Declaración Aduanera del embarque.',
        tracking=True
    )

    bl = fields.Char(
        string='BL',
        help='Número de BL/AWB del embarque.',
        tracking=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        """
        Override create to capture values from context and assign them to:
        - referencia_1, referencia_2, referencia_3 (from sam_gt module)
        - duca, bl (new fields)
        """
        for vals in vals_list:
            # Get values from context
            ctx = self.env.context

            # Assign referencia fields from context if provided
            if 'referencia_1' not in vals and ctx.get('default_referencia_1'):
                vals['referencia_1'] = ctx.get('default_referencia_1')

            if 'referencia_2' not in vals and ctx.get('default_referencia_2'):
                vals['referencia_2'] = ctx.get('default_referencia_2')

            if 'referencia_3' not in vals and ctx.get('default_referencia_3'):
                vals['referencia_3'] = ctx.get('default_referencia_3')

            # Assign duca and bl from context if provided
            if 'duca' not in vals and ctx.get('default_duca'):
                vals['duca'] = ctx.get('default_duca')

            if 'bl' not in vals and ctx.get('default_bl'):
                vals['bl'] = ctx.get('default_bl')

        return super(AccountMove, self).create(vals_list)
