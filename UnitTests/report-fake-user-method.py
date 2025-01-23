#!/usr/bin/env python3

"""
Testing and debugging the `def click_more_button` method in scammer_bait.py
Persistant problems with getting the bot/Selenium proper code to 
Locate and click the 'More' button on a user's profile
"""

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from unittest.mock import MagicMock, patch
from selenium.webdriver.support import expected_conditions as EC
from scammer_bait import ScamBait

class TestClickMoreButton(unittest.TestCase):
    def setUp(self):
        self.scam_bait = ScamBait()


# ---- Begin of Trying to locate and click the More button ---- #
def test_click_more_button_when_present_and_clickable(self):
    # Mock the WebDriverWait and it's until method
    mock_wait = MagicMock()
    mock_element = MagicMock()
    mock_wait.until.return_value = mock_element
    self.scam_bait.driver = MagicMock()

    with patch('scammer_bait.WebDriverWait', return_value=mock_wait), \
         patch('scammer_bait.debug_xpath') as mock_debug_xpath, \
         patch('builtins.print') as mock_print:

        # Calling the click_more_button() method on the self.scam_bait object within this unit test
        self.scam_bait.click_more_button()

        # Assert that the page was scrolled
        self.scam_bait.driver.execute_script.assert_called_once_with("window.scrollTo(0, document.body.scrollHeight);")

        # Assert that WebDriverWait was called with correct parameters
        more_button_xpath = ("//button[contains(@class, 'artdeco-dropdown__trigger') and "
                             "contains(@class, 'artdeco-button--secondary') and "
                             "contains(@aria-label, 'More actions')]//span[contains(text(), 'More')]")
        mock_wait.until.assert_called_once_with(
            EC.element_to_be_clickable((By.XPATH, more_button_xpath))
        )

        # Assert that the 'More' button was clicked
        mock_element.click.assert_called_once()

        # Assert that debug_xpath was called
        mock_debug_xpath.assert_called_with(self.scam_bait.driver, more_button_xpath)

        # Assert that the success message was printed
        mock_print.assert_called_with("Successfully clicked 'More' button")
## ---- End of click_more_button method ---- #

       
## ---- Testing of Error Handling when the More button cannot be located ---- #  
def test_click_more_button_exception_handling(self):
    # Mock the WebDriverWait to raise a TimeoutException
    mock_wait = MagicMock()
    mock_wait.until.side_effect = TimeoutException("Element not found")
    
    self.scam_bait.driver = MagicMock()
    self.scam_bait.driver.current_url = "https://www.linkedin.com/in/fake-profile"
    self.scam_bait.driver.page_source = "Mocked page source"

    with patch('scammer_bait.WebDriverWait', return_value=mock_wait), \
         patch('scammer_bait.debug_xpath') as mock_debug_xpath, \
         patch('builtins.print') as mock_print:

        self.scam_bait.click_more_button()

        # Assert that the page was scrolled
        self.scam_bait.driver.execute_script.assert_called_once_with("window.scrollTo(0, document.body.scrollHeight);")

        # Assert that debug_xpath was called
        mock_debug_xpath.assert_called_once()

        # Assert that the error messages were printed
        mock_print.assert_any_call("An error occurred while clicking the 'More' button: Element not found")
        mock_print.assert_any_call("Current URL: https://www.linkedin.com/in/fake-profile")
        mock_print.assert_any_call("Page source: Mocked page source...")


if __name__ == '__main__':
    unittest.main()

