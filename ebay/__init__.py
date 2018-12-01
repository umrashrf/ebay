"""
Used for initializing logging

There are more than one entry points so this is needed
"""

import sys
import logging

from . import settings

logging.basicConfig(level=settings.LOG_LEVEL,
                    format='%(asctime)s | %(levelname)-8s | %(message)s | %(name)-12s',
                    datefmt='%m-%d %H:%M',
                    stream=sys.stdout)
