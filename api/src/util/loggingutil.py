import logging
import os

if os.environ.get('USE_GRAYLOG') is not None and os.environ.get('USE_GRAYLOG') == 'true':
    import graypy
    handler = graypy.GELFUDPHandler('localhost', 12201)
else:
    handler = logging.StreamHandler()

logging.basicConfig(format="%(levelname)s:\t%(name)s:%(message)s", handlers=[handler], level=logging.DEBUG)
logger = logging.getLogger('game')
