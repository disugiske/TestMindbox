import logging
import sys

logger = logging.getLogger('API')
logging.basicConfig(
        datefmt="%d-%b-%y %H:%M:%S",
        level= logging.INFO,
        stream=sys.stdout,
    )
handler = logging.FileHandler('mindbox_api.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname).1s %(message)s"))
logger.addHandler(handler)