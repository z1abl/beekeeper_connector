from odoo.http import request

base_url = request.env['ir.config_parameter'].sudo().get_param('beekeeper_base_url')
token = request.env['ir.config_parameter'].sudo().get_param('beekeeper_token')

headers = {
    'Authorization': f'Token {token}'
}