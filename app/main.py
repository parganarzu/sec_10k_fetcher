from app.logger import setup_logger

logger = setup_logger()

def run():
    logger.info("SEC 10-K Fetcher Started")


if __name__ == "__main__":
    run()