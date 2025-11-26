# -*- coding: utf-8 -*-
from odoo import models, fields


class MrdcAduana(models.Model):
    _name = 'mrdc.aduana'
    _description = 'Aduanas de Guatemala'
    _order = 'name'

    code = fields.Char(
        string='Código',
        required=True,
        help='Código de la aduana'
    )
    name = fields.Char(
        string='Nombre',
        required=True,
        help='Nombre completo de la aduana'
    )
    active = fields.Boolean(
        string='Activo',
        default=True
    )

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'El código de aduana debe ser único!')
    ]
