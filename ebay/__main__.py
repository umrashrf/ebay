"""
entry point of the application
"""

import os
import json
import logging
import datetime

import boto3

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
ORDER_JSON = json.dumps(ORDERS_RESPONSE, sort_keys=True, indent=4)

S3 = boto3.resource("s3")
S3_BUCKET = S3.Bucket(settings.S3_BUCKET_ORDERS)
S3_BUCKET.put_object(Key=ORDER_FILENAME, Body=ORDER_JSON)

logging.debug(ORDER_JSON)
