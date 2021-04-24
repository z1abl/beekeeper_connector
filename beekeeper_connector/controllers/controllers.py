# -*- coding: utf-8 -*-
# from odoo import http


# class BeekeeperConnector(http.Controller):
#     @http.route('/beekeeper_connector/beekeeper_connector/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/beekeeper_connector/beekeeper_connector/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('beekeeper_connector.listing', {
#             'root': '/beekeeper_connector/beekeeper_connector',
#             'objects': http.request.env['beekeeper_connector.beekeeper_connector'].search([]),
#         })

#     @http.route('/beekeeper_connector/beekeeper_connector/objects/<model("beekeeper_connector.beekeeper_connector"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('beekeeper_connector.object', {
#             'object': obj
#         })
