import os
from app.logger import setup_logger
from playwright.sync_api import sync_playwright

logger = setup_logger()


class PDFService:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_pdf(self, company_name: str, url: str):
        """Generates a PDF of the SEC 10-K filing page for a given company.
        Args:
            company_name (str): The name of the company (used for filename).
            url (str): The URL of the 10-K filing page.
        Returns:
            str: The path to the generated PDF file.
        """

        file_path = f"{self.output_dir}/{company_name}_10K.pdf"
        logger.info(f"Generating PDF for {company_name}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                locale="en-US",
                timezone_id="America/New_York",
            )
            
            page = context.new_page()
            page.goto(
                url,
                wait_until="load",
                timeout=120000,
                referer="https://www.sec.gov/"
            )

            page.wait_for_timeout(3000)
            page.mouse.move(100, 200)
            page.mouse.wheel(0, 800)

            page.pdf(
                path=file_path,
                format="A4",
                print_background=True
            )

            browser.close()

        return file_path