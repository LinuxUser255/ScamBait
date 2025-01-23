#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def initialize_driver():
    """Initialize and return a webdriver instance."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def safe_find_element(driver, by, value, timeout=10):
    """
    Safely find an element with explicit wait and error handling.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Element not found: {by}={value}")
        return None

def click_element(driver, by, value):
    """
    Safely click an element.
    """
    element = safe_find_element(driver, by, value)
    if element:
        element.click()
        return True
    return False

def debug_xpath(driver, xpath):
    """
    Debug XPath selector by printing matching elements or suggesting fixes.
    """
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        if elements:
            print(f"Found {len(elements)} element(s) matching XPath: {xpath}")
            for i, element in enumerate(elements, 1):
                print(f"Element {i}: {element.tag_name}")
        else:
            print(f"No elements found matching XPath: {xpath}")
            # Suggest potential fixes
            if "//" not in xpath:
                print("Suggestion: Try adding '//' at the beginning of your XPath")
            if "contains" in xpath and "'" in xpath and '"' in xpath:
                print("Suggestion: Check your quote usage in the 'contains' function")
    except Exception as e:
        print(f"Error evaluating XPath: {e}")

def report_profile(driver, profile_url):
    """
    Navigate to a profile and report it.
    """
    driver.get(profile_url)
    
    # Click on the overflow menu
    if not click_element(driver, By.XPATH, "//button[contains(@id, 'overflow-action')]"):
        print("Failed to find overflow menu button")
        return False
    
    # Click on the report button
    if not click_element(driver, By.XPATH, "//div[text()='Report']/parent::button"):
        print("Failed to find report button")
        return False
    
    # Additional steps for reporting...
    
    print(f"Successfully reported profile: {profile_url}")
    return True

# Main function to demonstrate usage
def run_xpath_elements():
    driver = initialize_driver()
    try:
        profile_url = "https://www.linkedin.com/in/fake-profile"
        if report_profile(driver, profile_url):
            print("Profile reported successfully")
        else:
            print("Failed to report profile")
            
        # Debugging XPath
        problematic_xpath = "//button[contains(@id, 'ember* profile-overflow-action')]/svg"
        debug_xpath(driver, problematic_xpath)
    finally:
        driver.quit()
