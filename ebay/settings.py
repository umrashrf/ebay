"""
Settings module to store all hard coded settings
"""

import logging

LOG_LEVEL = logging.INFO

# https://developer.ebay.com/devzone/account/appsettings/Consent/Default.aspx?env=production&index=0
EBAY_APPID = ''
EBAY_DEVID = ''
EBAY_CERTID = ''
EBAY_RU_NAME = ''

EBAY_TRADING_API_VERSION = '967'
EBAY_TRADING_API_ENDPOINT = 'https://api.ebay.com/ws/api.dll'
EBAY_SIGNIN_ENDPOINT = 'https://signin.ebay.com/ws/eBayISAPI.dll'

S3_BUCKET_ORDERS = 'umair-379877922710-ebay-orders-us-east-1'

ORDERS_DIR = ''
