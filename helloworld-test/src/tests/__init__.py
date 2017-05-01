__all__ = 'test_app'

import os
import logging

logger = logging.getLogger(__name__)

URL = os.getenv('TARGET')
print('__init__')

if not URL:
    URL = 'http://localhost:5000'
    logger.warn("TARGET env not set, defaulting to %s" % URL)

from . import test_app

test_app.URL = URL



