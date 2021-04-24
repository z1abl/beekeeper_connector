import logging
import json
import requests


_logger = logging.getLogger(__name__)

from . import api_config

token = api_config.token
base_url = api_config.base_url
headers = api_config.headers

users_url = f'{base_url}/users'

def get_user_by_tenant_user_id(tenant_user_id):
    url = f'{users_url}/by_tenant_user_id/{tenant_user_id}'
    return requests.get(url,headers=headers)

def update_user_by_id(bkpr_user_id,user_fields):
    url = f'{users_url}/{bkpr_user_id}?custom_fields.max_visibility=admin'
    return requests.put(url,headers=headers,json=user_fields)

def create_user(user_fields):
     return requests.post(users_url,headers=headers,json=user_fields)
