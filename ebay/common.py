"""
Common functions are kept here
"""

import json
import logging
import xmltodict


def _get_data_from_response(call, data, response):
    try:
        json.loads(response.content)
    except json.JSONDecodeError as err:
        logging.warning('API did not return JSON string: %s', err)
        logging.debug(response.content)
        xml_response = xmltodict.parse(response.content)
        response_key = '{call}Response'.format(call=call)
        data = xml_response[response_key]
        return data
    return None
