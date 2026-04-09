import requests


class SECClient:
    BASE_URL = "https://data.sec.gov/submissions/CIK{}.json"

    def __init__(self, email: str):
        self.headers = {
            "User-Agent": f"SEC Automation ({email})",
            "Accept-Encoding": "gzip, deflate",
        }

    def get_latest_10k_url(self, cik: str):
        """Fetches the URL of the latest 10-K filing for a given CIK.
        Args:
            cik (str): The Central Index Key of the company.
        Returns:
            str: The URL of the latest 10-K filing, or None if not found.   
        """
        url = self.BASE_URL.format(cik)

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        data = response.json()
        filings = data["filings"]["recent"]

        for i, form in enumerate(filings["form"]):
            if form == "10-K":
                acc = filings["accessionNumber"][i].replace("-", "")
                doc = filings["primaryDocument"][i]

                return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{doc}"

        return None