"""Unit tests for PDFService class"""

import pytest
from unittest.mock import patch, MagicMock
from app.services.pdf_service import PDFService

@pytest.fixture
def pdf_service(tmp_path):
    return PDFService(output_dir=str(tmp_path))


@patch("app.services.pdf_service.sync_playwright")
def test_save_pdf_playwright(mock_playwright, pdf_service):
    """Test without opening a real browser"""

    # Mock browser/page objects
    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    file_path = pdf_service.save_pdf("TestCompany", "https://example.com/10k")

    assert file_path.endswith("TestCompany_10K.pdf")
    mock_playwright.return_value.__enter__.return_value.chromium.launch.assert_called_once()
    mock_context.new_page.assert_called_once()
    mock_page.goto.assert_called_once_with(
        "https://example.com/10k",
        wait_until="load",
        timeout=120000,
        referer="https://www.sec.gov/"
    )
    mock_page.pdf.assert_called_once_with(
        path=file_path,
        format="A4",
        print_background=True
    )
    mock_browser.close.assert_called_once()