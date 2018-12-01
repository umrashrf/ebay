"""
entry point of the application
"""

import os
import sys
import json
import time
import logging
import datetime

from datetime import timedelta
from urllib.parse import urljoin

from . import settings
from .trading_api import TradingAPI

logging.basicConfig(level=settings.LOG_LEVEL,
                    format='%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
                    datefmt='%m-%d %H:%M',
                    stream=sys.stdout)

API = TradingAPI()
if os.path.exists('token.txt'):
    with open('token.txt') as fp:
        API.set_token(fp.read().strip())

STATUS_RESPONSE = API.execute('GetTokenStatus', {'RuName': settings.EBAY_RU_NAME})
if STATUS_RESPONSE['TokenStatus']['Status'] != 'Active':
    SESSION_RESPONSE = API.execute('GetSessionID', {'RuName': settings.EBAY_RU_NAME})
    SESSION_ID = SESSION_RESPONSE['SessionID']

    logging.info('Please go to this link and press Agree')
    QUERY_STRING = '?SignIn&runame={}&SessID={}'.format(settings.EBAY_RU_NAME,
                                                        SESSION_ID)
    logging.info(urljoin(settings.EBAY_SIGNIN_ENDPOINT, QUERY_STRING))

    WAIT_TIMEOUT = 30
    while WAIT_TIMEOUT > 0:
        logging.info(f'Waiting T-{WAIT_TIMEOUT} seconds')
        time.sleep(1)
        WAIT_TIMEOUT -= 1

    TOKEN_RESPONSE = API.execute('FetchToken', {'RuName': settings.EBAY_RU_NAME,
                                                'SessionID': SESSION_ID})
    AUTH_TOKEN = TOKEN_RESPONSE['eBayAuthToken']
    with open('token.txt', 'w') as fp:
        fp.write(AUTH_TOKEN)
    logging.info('Success!')

ORDERS_RESPONSE = API.execute('GetOrders', {'RuName': settings.EBAY_RU_NAME,
                                            'CreateTimeFrom': datetime.datetime.now()-timedelta(days=60),
                                            'CreateTimeTo': datetime.datetime.now()})
print(ORDERS_RESPONSE)
ORDER_FILENAME = os.path.join(settings.ORDERS_DIR, 'orders.json')
with open(ORDER_FILENAME, 'w') as fp:
    json.dump(ORDERS_RESPONSE, fp, sort_keys=True, indent=4)
