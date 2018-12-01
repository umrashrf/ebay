"""
entry point of the application
"""

import os
import json
import datetime

from . import settings
from .trading_api import TradingAPI

AUTH_TOKEN = os.getenv('EBAY_AUTH_TOKEN', None)

API = TradingAPI()
API.set_token(AUTH_TOKEN)

TODAY = datetime.datetime.now()
TODAY_NAME = TODAY.strftime('%y_%m_%dT%H_%M_%S')

ORDERS_RESPONSE = API.execute('GetOrders', {'RuName': settings.EBAY_RU_NAME,
                                            'CreateTimeFrom': TODAY,
                                            'CreateTimeTo': TODAY})

ORDER_FILENAME = os.path.join(settings.ORDERS_DIR, f'orders_{TODAY_NAME}.json')
with open(ORDER_FILENAME, 'w') as fp:
    json.dump(ORDERS_RESPONSE, fp, sort_keys=True, indent=4)

print(ORDERS_RESPONSE)
