# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettingsBeekeeper(models.TransientModel):
    _inherit = 'res.config.settings'

    module_beekeeper_connector = fields.Boolean("Beekeeper", default=True)
    beekeeper_token = fields.Char("Beekeeper API token", config_parameter='beekeeper_token', default='')
    beekeeper_base_url = fields.Char("Beekeeper base url", config_parameter='beekeeper_base_url', default='')
