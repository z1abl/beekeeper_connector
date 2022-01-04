from odoo.http import request

# placing request.env['ir.config_parameter'] outside of function
# gives the error during the module-update
def get_config_param():
    base_url = request.env['ir.config_parameter'].sudo().get_param('beekeeper_base_url')
    token = request.env['ir.config_parameter'].sudo().get_param('beekeeper_token')

    users_url = f'{base_url}/users'
    custom_fields_url = f'{base_url}/customfields'

    headers = {
        'Authorization': f'Token {token}'
    }

    return {
        'baese_url': base_url,
        'token': token,
        'headers': headers,
        'users_url': users_url,
        'custom_fields_url': custom_fields_url
    }