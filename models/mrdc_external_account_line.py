# -*- coding: utf-8 -*-
from odoo import models, api


class MrdcExternalAccountLine(models.Model):
    _inherit = 'mrdc.external_account.line'

    def create_expense(self, raise_error=True):
        """
        Override to add ref_3 and duca to the created expense
        """
        result = super(MrdcExternalAccountLine, self).create_expense(raise_error=raise_error)

        if result and self.external_account_id:
            # Update the created expense with ref_3 and duca
            result.write({
                'referencia_3': self.external_account_id.referencia_3,
                'duca': self.external_account_id.duca,
            })

        return result
