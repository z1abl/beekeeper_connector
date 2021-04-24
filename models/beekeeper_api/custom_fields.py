import logging
import json
import requests

from . import api_config

token = api_config.token
base_url = api_config.base_url
headers = api_config.headers


_logger = logging.getLogger(__name__)


custom_fields_url = f'{base_url}/customfields'

def get_custom_fields():
    response = requests.get(custom_fields_url,headers=headers).json()
    return response
