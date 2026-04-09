from app.config import COMPANIES, EMAIL
from app.logger import setup_logger
from app.services.sec_client import SECClient

logger = setup_logger()

def run():
    logger.info("SEC 10-K Fetcher Started")

    sec = SECClient(EMAIL)
    for company in COMPANIES:
        logger.info(f"Fetching {company.name} (CIK: {company.cik})")

        try:
            url = sec.get_latest_10k_url(company.cik)
            if not url:
                logger.warning(f"{company.name} → 10-K not found")
                continue

            # save pdf here ..

        except Exception as e:
            logger.error(f"{company.name} → Error: {e}")

    logger.info("All done!")


if __name__ == "__main__":
    run()