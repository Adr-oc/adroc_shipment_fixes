# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MrdcShipment(models.Model):
    _inherit = 'mrdc.shipment'

    # Consignatario / Consignee
    consignee_name = fields.Char(
        string='Nombre del Consignatario',
        help='Nombre del consignatario relacionado con el embarque.',
        related='consignee_id.name',
    )

    consignee_id = fields.Many2one(
        'res.partner',
        string='Consignatario',
        help='Consignatario relacionado con el embarque.',
        tracking=True
    )

    consignee_vat = fields.Char(
        string='NIT del Consignatario',
        help='NIT del consignatario relacionado con el embarque.',
        related='consignee_id.vat',
    )

    # Shipper / Embarcador
    shipper_name = fields.Char(
        string='Nombre del Shipper',
        help='Nombre del embarcador relacionado con el embarque.',
        related='shipper_id.name',
    )

    shipper_id = fields.Many2one(
        'res.partner',
        string='Shipper',
        help='Embarcador relacionado con el embarque.',
        tracking=True
    )

    shipper_vat = fields.Char(
        string='NIT del Shipper',
        help='NIT del embarcador relacionado con el embarque.',
        related='shipper_id.vat',
    )

    # Notificador / Notify Party
    notify_name = fields.Char(
        string='Nombre del Notificador',
        help='Nombre del notificador relacionado con el embarque.',
        related='notify_id.name',
    )

    notify_id = fields.Many2one(
        'res.partner',
        string='Notificador',
        help='Notificador relacionado con el embarque.',
        tracking=True
    )

    notify_vat = fields.Char(
        string='NIT del Notificador',
        help='NIT del notificador relacionado con el embarque.',
        related='notify_id.vat',
    )

    # Descripción adicional
    description = fields.Text(
        string='Descripción',
        help='Descripción adicional del embarque. Este campo no se sincroniza.',
        tracking=True
    )

    # Sobrescribir el default del campo state
    state = fields.Selection(
        default='in_transit'
    )

    # Campo selectivo
    selectivo = fields.Selection(
        selection=[
            ('verde', 'Verde'),
            ('rojo', 'Rojo'),
        ],
        string='Selectivo',
        help='Indicador selectivo del embarque.',
        tracking=True
    )

    aduana_id = fields.Many2one(
        'mrdc.aduana',
        string='Aduana',
        help='Aduana relacionada con el embarque.',
        tracking=True
    )

    # Campo aduana (Selection)
    aduana_select_id = fields.Selection(
        selection=[
            ('ST', 'Aduana Santo Tomás de Castilla'),
            ('PQ', 'Aduana Puerto Quetzal'),
            ('PB', 'Aduana Puerto Barrios'),
            ('TU', 'Aduana Tecún Umán'),
            ('EC', 'Aduana El Carmen'),
            ('LM', 'Aduana La Mesilla'),
            ('MM', 'Aduana Melchor de Mencos'),
            ('EF', 'Aduana El Florido'),
            ('VH', 'Aduana de Vehículos'),
            ('CG', 'Aduana Central de Guatemala'),
            ('CH', 'Aduana Champerico'),
            ('PA', 'Aduana Pedro de Alvarado'),
            ('VN', 'Aduana Valle Nuevo'),
            ('SC', 'Aduana San Cristóbal'),
            ('AC', 'Aduana Agua Caliente'),
            ('LE', 'Aduana La Ermita'),
            ('CB', 'Aduana El Ceibo'),
            ('SE', 'Aduana Tikal/Santa Elena'),
            ('CA', 'Aduana Central de Aviación'),
            ('EA', 'Aduana Express Aéreo'),
            ('FP', 'Aduana Fardos Postales'),
            ('G1', 'Aduana Almacenadora Integrada'),
            ('G2', 'Aduana Alminter'),
            ('G3', 'Aduana Alpasa'),
            ('G4', 'Aduana Alsersa'),
            ('G5', 'Aduana Cealsa'),
            ('G6', 'Aduana Almaguate'),
            ('G7', 'Aduana Alcorsa'),
            ('G8', 'Aduana Centralsa'),
            ('TM', 'Aduana Tecún Umán Intermodal'),
            ('AG1', 'Almacenadora Guatemalteca, S.A. (ALMAGUATE)'),
            ('AP1', 'Almacenadora del País, S.A. (ALPASA)'),
            ('AS1', 'Almacenes y Servicios, S.A. (ALSERSA)'),
            ('AM1', 'Almacenadora Internacional (ALMINTER)'),
            ('AI3', 'Almacenes Generales, S.A. (ALGESA)'),
            ('CE1', 'Central Almacenadora, S.A. (CEALSA)'),
            ('AI2', 'Almacenadora Integrada, S.A.'),
            ('AT1', 'Almacenadora Tecún (ALMATECUN)'),
            ('CA1', 'Centroamericana de Almacenes, S.A. (CENTRALSA)'),
            ('AL1', 'Almacenadora Corporativa, S.A. (ALCORSA)'),
            ('CH1', 'Crédito Hipotecario Nacional (Almacén Fiscal)'),
            ('GC1', 'Grupo CLC, Sociedad Anónima'),
            ('DE1', 'Distribuidora Electrónica, S.A.'),
            ('CG1', 'Colgate Palmolive (Centro América), S.A.'),
            ('LS1', 'Logística de Servicios, S.A.'),
            ('CM1', 'DHL Global Forwarding (Guatemala), S.A.'),
            ('AV1', 'Productos Avon de Guatemala, S.A.'),
            ('DW1', 'Duwest Recubrimientos, Sociedad Anónima'),
            ('IM1', 'Inversiones y Proyectos Monterrey, S.A.'),
            ('CR1', 'CROPA, Sociedad Anónima'),
            ('1', 'Zeta Gas de Centroamérica, S.A.'),
            ('3', 'Almacenes de Guatemala, S.A.'),
            ('4', 'Chiquita Guatemala, S.A.'),
            ('5', 'Operadora Mundial, Sociedad Anónima'),
            ('PN2', 'Sociedad Protectora Niño Anexo Flores, Petén'),
            ('CF1', 'Centro de Integración Familiar'),
            ('PN1', 'Sociedad Protectora del Niño (Puerto Libre)'),
            ('VP1', 'Asociación Señoras Caridad San Vicente Paúl'),
        ],
        string='Aduana',
        help='Aduana relacionada con el embarque.',
        tracking=True
    )

    # Extender freight_agency_state para agregar opción 'Concluido'
    freight_agency_state = fields.Selection(
        selection_add=[
            ('concluded', 'Concluido'),
        ],
        ondelete={'concluded': 'set null'}
    )

    customs_agency_state = fields.Selection(
        selection_add=[
            ('concluded', 'Concluido'),
        ],
        ondelete={'concluded': 'set null'}
    )

    customs_broker_person_state = fields.Selection(
        selection_add=[
            ('concluded', 'Concluido'),
        ],
        ondelete={'concluded': 'set null'}
    )

    # Extender state para agregar opción 'Concluido'
    state = fields.Selection(
        selection_add=[
            ('concluded', 'Concluido'),
        ],
        ondelete={'concluded': 'set null'},
        default='in_transit'
    )

    good_carrier_state = fields.Selection(
        selection_add=[
            ('concluded', 'Concluido'),
        ],
        ondelete={'concluded': 'set null'}
    )

    barco = fields.Char(
        string='Barco',
        help='Nombre del barco.',
        tracking=True
    )

    # Campo nave
    nave = fields.Char(
        string='Nave',
        help='Nombre de la nave.',
        tracking=True
    )

    # Campo para controlar si bl_awb_number fue editado manualmente
    bl_awb_number_manual = fields.Boolean(
        string='BL/AWB Editado Manualmente',
        default=False,
        help='Indica si el campo BL/AWB fue editado manualmente y no debe sincronizarse.',
        copy=False
    )

    def _get_fields_to_sync(self):
        """
        Extend the fields to sync to include the new partner fields.
        Following the pattern used for partner_id (includes both many2one and related fields).
        """
        fields_to_sync = super()._get_fields_to_sync()

        # Excluir bl_awb_number de la sincronización si fue editado manualmente
        if self.bl_awb_number_manual and 'bl_awb_number' in fields_to_sync:
            fields_to_sync.remove('bl_awb_number')

        fields_to_sync.extend([
            # Partner string fields (NOT Many2one to avoid country_id issues)
            'consignee_name',
            'consignee_vat',
            'shipper_name',
            'shipper_vat',
            'notify_name',
            'notify_vat',
            # Selectivo field
            'selectivo',
            # Aduana field
            'aduana_select_id',
            # Nave field
            'nave',
        ])
        return fields_to_sync

    # def write(self, vals):
    #     """
    #     Override write to add tracking for tag_ids changes in the chatter.
    #     Many2many fields don't automatically track in Odoo even with tracking=True.

    #     Also mark bl_awb_number as manually edited if changed from UI.
    #     """
    #     # Si se está editando bl_awb_number y NO viene de sincronización, marcarlo como manual
    #     if 'bl_awb_number' in vals and not self.env.context.get('mrdc_shipment_sync_instances'):
    #         vals['bl_awb_number_manual'] = True

    #     # Call super first to perform the write
    #     res = super(MrdcShipment, self).write(vals)

    #     # Track tag changes after write
    #     if 'tag_ids' in vals:
    #         for record in self:
    #             record.message_post(
    #                 body="<strong>Etiquetas actualizadas</strong>",
    #                 subject='Cambio en Etiquetas de Embarque',
    #                 message_type='notification',
    #                 subtype_xmlid='mail.mt_note'
    #             )

    #     return res

    def action_reset_bl_manual_flag(self):
        """
        Resetea el flag de edición manual del BL/AWB para permitir
        que vuelva a sincronizarse con sistemas externos.
        """
        for record in self:
            record.bl_awb_number_manual = False
        return True

    def action_view_account_move_partner(self):
        """
        Override to add move_type filter to domain for customer invoices.
        Only show out_invoice and out_refund.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Facturas de Cliente',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [
                ('mrdc_shipment_id', '=', self.id),
                ('move_type', 'in', ['out_invoice', 'out_refund'])
            ],
            'context': {
                'default_mrdc_shipment_id': self.id,
                'default_move_type': 'out_invoice',
                'default_referencia_1': self.ref_1,
                'default_referencia_2': self.ref_2,
                'default_referencia_3': self.ref_3,
                'default_duca': self.customs_declaration_number,
                'default_bl': self.bl_awb_number,
            },
        }

    def action_view_account_move_supplier(self):
        """
        Override to add move_type filter to domain for supplier invoices.
        Only show in_invoice and in_refund.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Facturas de Proveedor',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [
                ('mrdc_shipment_id', '=', self.id),
                ('move_type', 'in', ['in_invoice', 'in_refund'])
            ],
            'context': {
                'default_mrdc_shipment_id': self.id,
                'default_move_type': 'in_invoice',
                'default_referencia_1': self.ref_1,
                'default_referencia_2': self.ref_2,
                'default_referencia_3': self.ref_3,
                'default_duca': self.customs_declaration_number,
                'default_bl': self.bl_awb_number,
            },
        }
