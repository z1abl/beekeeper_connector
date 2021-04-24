# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request
from ..models.beekeeper_api import users as users_api


import logging
import json
import requests


_logger = logging.getLogger(__name__)

class BeekeeperHrEmployee(models.Model):
    _inherit = ['hr.employee']

    bkpr_user = fields.Boolean(string='Beekeeper user', default=False)

    # employees in Odoo (both active/archived)
    def get_bkpr_users(self):
        bkpr_users = self.env['hr.employee'].search(['&',('bkpr_user','=',True),'|',('active','=',True),('active','=',False)])
        return bkpr_users

    # TODO include employee's photo
    # prepares employee from Odoo for payload
    def prepare_user_fields(self,user):
        user_fields = {}
        # custom fields which were mapped in Odoo
        custom_fields_odoo = self.env['custom.field'].search([('field_name', '!=', False)])
        custom_fields_for_request = []
        for field in custom_fields_odoo:
            if user[field['field_name']]:
                custom_fields_for_request.append({'key': field['key'], 'value': str(user[field['field_name']])})

        user_fields['tenantuserid'] = user.id
        user_fields['name'] = f'odoo_{user.id}'
        user_fields['suspended'] = not user.active

        if user.work_email:
            user_fields['email'] = user.work_email

        #TODO prepare phone number according to Bkpr requirements
        if user.mobile_phone:
            user_fields['mobile'] = user.mobile_phone

        if custom_fields_for_request:
            user_fields['custom_fields'] = custom_fields_for_request

        return user_fields

    # syncs employees between Odoo and Bkpr
    def users_sync(self):
        # employees which should be synced
        users = BeekeeperHrEmployee.get_bkpr_users(self)
        # refreshing custom fields in Odoo
        self.env['custom.field'].fields_sync()

        for user in users:
            user_fields = BeekeeperHrEmployee.prepare_user_fields(self,user)
            # tenantuserid in Beekeeper = employees id in Odoo
            user_response = users_api.get_user_by_tenant_user_id(user_fields['tenantuserid'])
            bkpr_user_id = None
            if user_response.ok:
                bkpr_user_id = user_response.json()['id']

            # updates already existing user
            if bkpr_user_id:
                try:
                    user_update_response = users_api.update_user_by_id(bkpr_user_id,user_fields)

                    if user_update_response.ok:
                        _logger.info(f'UPDATE id: {user.id} OK.')
                    else:
                        _logger.info(f'UPDATE id: {user.id}, {user_update_response.content}')

                except Exception as e:
                    _logger.error(e)
            # creates new user
            else:
                try:
                    user_create_response = users_api.create_user(user_fields)
                    if user_create_response.ok:
                        _logger.info(f'CREATE id: {user.id} OK.')
                    else:
                        _logger.info(f'CREATE id: {user.id}, {user_create_response.content}')

                except Exception as e:
                    _logger.error(e)


