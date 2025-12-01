# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

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
        string='Observaciones',
        help='Observaciones o referencia 3 del embarque.',
        tracking=True
    )

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

    def current_date_format(self, date):
        """Formato de fecha en español para reportes."""
        if not date:
            return ""
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        month = months[date.month - 1]
        return f"Guatemala, {date.day} de {month} de {date.year}"

    def primera_mayuscula(self, letras):
        """Convierte la primera letra a mayúscula."""
        if not letras:
            return ""
        return letras[0].upper() + letras[1:]

    def num_a_letras(self, num, completo=True):
        """Convierte un número a letras en español."""
        return num_a_letras(num, completo)


def num_a_letras(num, completo=True):
    """Convierte un número a letras en español."""
    en_letras = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve',
        '10': 'diez',
        '11': 'once',
        '12': 'doce',
        '13': 'trece',
        '14': 'catorce',
        '15': 'quince',
        '16': 'dieciseis',
        '17': 'diecisiete',
        '18': 'dieciocho',
        '19': 'diecinueve',
        '20': 'veinte',
        '21': 'veintiuno',
        '22': 'veintidos',
        '23': 'veintitres',
        '24': 'veinticuatro',
        '25': 'veinticinco',
        '26': 'veintiseis',
        '27': 'veintisiete',
        '28': 'veintiocho',
        '29': 'veintinueve',
        '3x': 'treinta',
        '4x': 'cuarenta',
        '5x': 'cincuenta',
        '6x': 'sesenta',
        '7x': 'setenta',
        '8x': 'ochenta',
        '9x': 'noventa',
        '100': 'cien',
        '1xx': 'ciento',
        '2xx': 'doscientos',
        '3xx': 'trescientos',
        '4xx': 'cuatrocientos',
        '5xx': 'quinientos',
        '6xx': 'seiscientos',
        '7xx': 'setecientos',
        '8xx': 'ochocientos',
        '9xx': 'novecientos',
        '1xxx': 'un mil',
        'xxxxxx': 'mil',
        '1xxxxxx': 'un millon',
        'x:x': 'millones'
    }

    num_limpio = str(num).replace(',', '')
    partes = num_limpio.split('.')

    entero = 0
    decimal = 0
    if partes[0]:
        entero = str(int(partes[0]))
    if len(partes) > 1 and partes[1]:
        decimal = partes[1][0:2].ljust(2, '0')

    num_en_letras = 'ERROR'
    if int(entero) < 30:
        num_en_letras = en_letras[entero]
    elif int(entero) < 100:
        num_en_letras = en_letras[entero[0] + 'x']
        if entero[1] != '0':
            num_en_letras = num_en_letras + ' y ' + en_letras[entero[1]]
    elif int(entero) < 101:
        num_en_letras = en_letras[entero]
    elif int(entero) < 1000:
        num_en_letras = en_letras[entero[0] + 'xx']
        if entero[1:3] != '00':
            num_en_letras = num_en_letras + ' ' + num_a_letras(entero[1:3], False)
    elif int(entero) < 2000:
        num_en_letras = en_letras[entero[0] + 'xxx']
        if entero[1:4] != '000':
            num_en_letras = num_en_letras + ' ' + num_a_letras(entero[1:4], False)
    elif int(entero) < 1000000:
        miles = int(entero.rjust(6)[0:3])
        cientos = entero.rjust(6)[3:7]
        num_en_letras = num_a_letras(str(miles), False) + ' ' + en_letras['xxxxxx']
        if cientos != '000':
            num_en_letras = num_en_letras + ' ' + num_a_letras(cientos, False)
    elif int(entero) < 2000000:
        num_en_letras = en_letras[entero[0] + 'xxxxxx']
        if entero[1:7] != '000000':
            num_en_letras = num_en_letras + ' ' + num_a_letras(entero[1:7], False)
    elif int(entero) < 1000000000000:
        millones = int(entero.rjust(12)[0:6])
        miles = entero.rjust(12)[6:12]
        num_en_letras = num_a_letras(str(millones), False) + ' ' + en_letras['x:x']
        if miles != '000000':
            num_en_letras = num_en_letras + ' ' + num_a_letras(miles, False)

    if not completo:
        return num_en_letras

    if decimal == 0:
        letras = '%s exactos' % num_en_letras
    else:
        letras = '%s con %s/100' % (num_en_letras, decimal)

    return letras
