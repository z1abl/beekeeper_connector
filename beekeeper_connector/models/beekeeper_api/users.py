from odoo.http import request
from . import api_config

import logging
import json
import requests

_logger = logging.getLogger(__name__)

config_param = api_config.get_config_param

def get_user_by_tenant_user_id(tenant_user_id):
    url = f'{config_param()["users_url"]}/by_tenant_user_id/{tenant_user_id}'
    return requests.get(url,headers=config_param()["headers"])

def update_user_by_id(bkpr_user_id,user_fields):
    url = f'{config_param()["users_url"]}/{bkpr_user_id}?custom_fields.max_visibility=admin'
    return requests.put(url,headers=config_param()["headers"],json=user_fields)

def create_user(user_fields):
    return requests.post(config_param()["users_url"],headers=config_param()["headers"],json=user_fields)
