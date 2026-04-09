# About SEC 10-K Fetcher

SEC 10-K Fetcher is a Python automation tool to download the latest 10-K filings from the U.S. Securities and Exchange Commission (SEC) EDGAR database for multiple companies. It uses **Playwright** to render filings and save them as PDFs.

## Features

* Modular architecture
* SEC API integration
* Configurable companies list
* Logger (console)

## Design Decisions

* Company CIKs are hardcoded to keep the implementation simple and focused on the core task.
* In a production system, CIKs would be dynamically resolved using the SEC lookup service:
  <https://www.sec.gov/search-filings/cik-lookup>
