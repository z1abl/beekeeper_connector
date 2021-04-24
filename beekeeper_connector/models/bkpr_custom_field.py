# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from ..models.beekeeper_api import custom_fields as custom_fields_api

import logging
import json
import requests

_logger = logging.getLogger(__name__)


class BeekeeperCustomField(models.Model):
    _name = 'custom.field'
    _rec_name = 'key'
    _description = 'Beekeeper custom field'

    field_name = fields.Char(string='Field name (Odoo)')
    key = fields.Char(string='Key (Beekeeper)')
    type = fields.Char(string='Type')

    # syncs custom_fields between Odoo and Bkpr
    def fields_sync(self):
        # custom fields in Bkpr
        custom_fields_bkpr = custom_fields_api.get_custom_fields()
        # custom fields' keys in Bkpr
        keys_bkpr = [field['key'] for field in custom_fields_bkpr]

        # custom fields in Odoo
        custom_fields_odoo = self.env['custom.field'].search([])
        # custom fields' keys in Odoo
        keys_odoo = [field['key'] for field in custom_fields_odoo]

        # deletes custom fields in Odoo which don't exist in Bkpr
        [field.unlink() for field in custom_fields_odoo if not field['key'] in keys_bkpr]

        # creates new custom field in Odoo if it doesn't exist yet
        for field in custom_fields_bkpr:
            if field['key'] not in keys_odoo:
                custom_field = self.env['custom.field'].create({
                    'key': field['key'],
                    'type': field['type']
                })


