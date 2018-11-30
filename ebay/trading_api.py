"""
TradingAPI to execute functions on EBay Trading endpoint

Used by OrdersAPI
"""

from __future__ import unicode_literals

import logging
import xmltodict
import requests

from . import settings
from .common import _get_data_from_response


class TradingAPI:
    """
    TradingAPI class to get session and auth tokens
    """

    _last_response = None

    def __init__(self, site_id=2, token=None):
        self.site_id = site_id
        self._token = token
        self._dev_id = settings.EBAY_DEVID
        self._app_id = settings.EBAY_APPID
        self._cert_id = settings.EBAY_CERTID
        self._endpoint = settings.EBAY_TRADING_API_ENDPOINT
        self.ru_name = settings.EBAY_RU_NAME
        self.version = settings.EBAY_TRADING_API_VERSION

    def _get_requester_credentials(self):
        return {'eBayAuthToken': self._token}

    def _get_headers(self, call):
        return {
            'X-EBAY-API-COMPATIBILITY-LEVEL': str(self.version),
            'X-EBAY-API-DEV-NAME': self._dev_id,
            'X-EBAY-API-APP-NAME': self._app_id,
            'X-EBAY-API-CERT-NAME': self._cert_id,
            'X-EBAY-API-SITEID': str(self.site_id),
            'X-EBAY-API-CALL-NAME': call,
        }

    def _get_xml_request(self, call, kw_dict, include_requester_credentials):
        request_key = '{call}Request'.format(call=call)
        request_dict = {request_key: {
            '@xmlns': 'urn:ebay:apis:eBLBaseComponents',
        }}
        for key, value in kw_dict.items():
            request_dict[request_key][key] = value
        if self._token and include_requester_credentials:
            credentials = self._get_requester_credentials()
            request_dict[request_key]['RequesterCredentials'] = credentials
        data = xmltodict.unparse(request_dict)
        return data

    def execute(self, call, kw_dict, include_requester_credentials=True):
        """
        main function of this module
        """
        logging.info(f'Executing {call}')
        headers = self._get_headers(call)
        data = self._get_xml_request(
            call, kw_dict, include_requester_credentials)
        response = requests.post(self._endpoint, data=data, headers=headers)
        self._last_response = response
        return _get_data_from_response(call, data, response)

    def set_token(self, token):
        """
        Use this function to set previous token
        """
        self._token = token
