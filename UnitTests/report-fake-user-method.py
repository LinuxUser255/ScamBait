#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock, patch

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from scammer_bait import ScamBait
from scam_bait_utils import debug_xpath

class TestReportFakeUser(unittest.TestCase):
    def setUp(self):
        self.scam_bait = ScamBait()

def test_click_more_button(self):
    self.scam_bait.driver.get("https://www.linkedin.com/in/fake-profile")
    
    # Mock the WebDriverWait and debug_xpath functions
    self.scam_bait.driver.find_element = MagicMock()
    self.scam_bait.driver.find_element.return_value.click = MagicMock()
    WebDriverWait = MagicMock()
    debug_xpath = MagicMock()
    
    # Call the method
    self.scam_bait.report_fake_user()
    
    # Assert that the 'More' button was clicked
    more_button_xpath = "//*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]"
    WebDriverWait.assert_called_once_with(self.scam_bait.driver, 10)
    WebDriverWait.return_value.until.assert_called_once_with(
        EC.element_to_be_clickable((By.XPATH, more_button_xpath))
    )
    self.scam_bait.driver.find_element.return_value.click.assert_called_once()
    
    # Assert that debug_xpath was called
    debug_xpath.assert_called_once_with(self.scam_bait.driver, more_button_xpath)


def test_more_button_not_found(self):
    self.scam_bait.driver.get = MagicMock()
    self.scam_bait.driver.current_url = "https://www.linkedin.com/in/fake-profile"
    
    # Mock WebDriverWait to raise a TimeoutException
    mock_wait = MagicMock()
    mock_wait.until.side_effect = TimeoutException("Element not found")
    WebDriverWait = MagicMock(return_value=mock_wait)
    
    # Mock debug_xpath
    debug_xpath = MagicMock()
    
    with patch('scammer_bait.WebDriverWait', WebDriverWait), \
         patch('scammer_bait.debug_xpath', debug_xpath), \
         patch('builtins.print') as mock_print:
        
        self.scam_bait.report_fake_user()
        
        # Assert that debug_xpath was called
        debug_xpath.assert_called_once()
        
        # Assert that the error message was printed
        mock_print.assert_any_call("An error occurred while reporting the fake user: Element not found")
        
        # Assert that the current URL was printed
        mock_print.assert_any_call("Current URL: https://www.linkedin.com/in/fake-profile")
        
        # Assert that the page source was attempted to be printed
        mock_print.assert_any_call(f"Page source: {self.scam_bait.driver.page_source[:500]}...")


def test_click_report_or_block_option(self):
    self.scam_bait.driver.get = MagicMock()
    self.scam_bait.driver.current_url = "https://www.linkedin.com/in/fake-profile"
    
    # Mock WebDriverWait and its until method
    mock_wait = MagicMock()
    mock_element = MagicMock()
    mock_wait.until.return_value = mock_element
    WebDriverWait = MagicMock(return_value=mock_wait)
    
    # Mock debug_xpath
    debug_xpath = MagicMock()
    
    # Mock time.sleep
    time_sleep = MagicMock()
    
    with patch('scammer_bait.WebDriverWait', WebDriverWait), \
         patch('scammer_bait.debug_xpath', debug_xpath), \
         patch('time.sleep', time_sleep), \
         patch('builtins.print') as mock_print:
        
        self.scam_bait.report_fake_user()
        
        # Assert that the 'More' button was clicked
        mock_element.click.assert_called()
        
        # Assert that time.sleep was called
        time_sleep.assert_called_once_with(2)
        
        # Assert that the 'Report or block' option was clicked
        report_button_xpath = "//div[starts-with(@id, 'ember') and contains(@class, 'artdeco-dropdown__item') and contains(@aria-label, 'Report or block')]"
        WebDriverWait.return_value.until.assert_called_with(
            EC.element_to_be_clickable((By.XPATH, report_button_xpath))
        )
        mock_element.click.assert_called()
        
        # Assert that the success message was printed
        mock_print.assert_any_call("'Report or block' option clicked successfully")
        mock_print.assert_any_call("Fake user reported successfully.")


if __name__ == '__main__':
    unittest.main()
