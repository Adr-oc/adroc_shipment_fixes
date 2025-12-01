# -*- coding: utf-8 -*-
{
    'name': "Adroc - Shipment Fixes",

    'summary': """
        Custom fixes and enhancements for shipment module (Odoo 19).
        """,

    'description': """
        Custom fixes and enhancements for shipment module.
        Migrated to Odoo 19 Community Edition.

        Main changes:
        - attrs and states replaced with direct attributes
        - tree tags replaced with list tags
        - Compatible with Odoo 19 API
        """,

    'author': "Adroc",
    'category': 'Tools',
    'version': '19.0.1.0.0',

    'depends': [
        'mrdc_shipment_base',
        'mrdc_shipment_carrier',
        'mrdc_shipment_customs_agency',
        'mrdc_shipment_customs_broker_person',
        'mrdc_shipment_freight_agency',
        'mrdc_shipment_good_carrier',
        'mrdc_shipment_importer_exporter',
    ],

    "data": [
        "security/ir.model.access.csv",
        "data/mrdc_aduana_data.xml",
        "views/mrdc_shipment_views.xml",
        "views/account_move_views.xml",
        "views/mrdc_external_account_views.xml",
        # Reportes multimoneda
        "report/cuenta_ajena_multicurrency_report.xml",
        "report/cuenta_ajena_multicurrency_pdf.xml",
        "report/mrdc_external_account_gtq_report.xml",
        "report/mrdc_external_account_pdf.xml",
        "report/mrdc_external_account_usd_report.xml",
        "report/mrdc_external_account_usd_pdf.xml",
    ],

    'license': 'OPL-1',
}
