import datetime
import logging

from fx_rate.utility import get_fx_rate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    usd_jpy = get_fx_rate()
    res = 'timestamp={}, USDJPY={}'.format(
        datetime.datetime.utcnow() + datetime.timedelta(hours=9), usd_jpy)
    logger.info(res)


if __name__ == '__main__':
    main()
