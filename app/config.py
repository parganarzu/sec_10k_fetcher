""" Configuration file for SEC 10-K Fetcher """

from app.models.company import Company

# Email used in SEC User-Agent
EMAIL = "parganarzu@gmail.com"
OUTPUT_DIR = "output"
COMPANIES = [
    Company(name="Apple", cik="0000320193"),
    Company(name="Meta Group", cik="0001000015"),
    Company(name="Alphabet", cik="0001652044"),
    Company(name="Amazon", cik="0001018724"),
    Company(name="Netflix", cik="0001065280"),
    Company(name="Goldman Sachs", cik="0000769993"),
]