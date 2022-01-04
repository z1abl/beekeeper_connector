from odoo.http import request
from . import api_config

import logging
import json
import requests

_logger = logging.getLogger(__name__)

config_param = api_config.get_config_param

def get_custom_fields():
    response = requests.get(config_param()['custom_fields_url'],headers=config_param()["headers"]).json()
    return response
