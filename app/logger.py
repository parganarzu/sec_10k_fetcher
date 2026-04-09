""" Logger for SEC 10-K Fetcher """

import logging
import sys

def setup_logger():
    logger = logging.getLogger("sec_fetcher")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger