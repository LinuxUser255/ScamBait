#!/usr/bin/env python3

import os
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scam_bait_utils import debug_xpath


def browser_persist():
    while True:
        time.sleep(60)
        print("Browser session persist...")


class ScamBait:
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--window-size=800,600")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def sign_in(self):
        try:
            self.driver.get('https://www.linkedin.com/login')
            self.driver.find_element(By.ID, "username").send_keys(config.email)
            self.driver.find_element(By.ID, "password").send_keys(config.password)
            time.sleep(8)
            sign_in_button_xpath = ("//button[contains(@class, 'btn__primary--large') and contains(@type, 'submit') "
                                    "and (contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
                                    "'abcdefghijklmnopqrstuvwxyz'), 'sign in') or contains(translate(., "
                                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin'))]")
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath))
            )
            sign_in_button.click()
            if self.driver.current_url == 'https://www.linkedin.com/feed/':
                print("Login successful.")
        except Exception as e:
            print(f"An error occurred during sign-in: {str(e)}")

    def get_opentowork_url(self):
        pass

    def find_posts_comments_by_fake_users(self):
        pass


    def get_fakeuser_url(self):
        with open(os.path.join(os.path.dirname(__file__), "ScamerProfiles/fake_profiles.txt"), 'r') as f:
            fake_profiles = f.read().strip().splitlines()
        if fake_profiles:
            random_profile = random.choice(fake_profiles)
            self.driver.get(random_profile)
            time.sleep(5)
        else:
            print("No fake profiles found in the file.")

    from scam_bait_utils import debug_xpath

    # Debugging this step
    def report_fake_user(self):
        try:
            # Step One: Click the 'More' button
            more_button_xpath = "//*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]"
            print(f"Attempting to click 'More' button with XPath: {more_button_xpath}")
            
            # Debug the XPath
            debug_xpath(self.driver, more_button_xpath)
            
            more_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, more_button_xpath))
            )
            more_button.click()
            print("'More' button clicked successfully")
    
            # Step Two: Wait for the dropdown menu to appear
            time.sleep(2)
    
            # Step Three: Click the 'Report or block' option
            report_button_xpath = "//div[starts-with(@id, 'ember') and contains(@class, 'artdeco-dropdown__item') and contains(@aria-label, 'Report or block')]"
            print(f"Attempting to click 'Report or block' option with XPath: {report_button_xpath}")
            
            # Debug the XPath
            debug_xpath(self.driver, report_button_xpath)
            
            report_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, report_button_xpath))
            )
            report_button.click()
            print("'Report or block' option clicked successfully")
    
            print("Fake user reported successfully.")
        except Exception as e:
            print(f"An error occurred while reporting the fake user: {str(e)}")
            # Additional debugging information
            print(f"Current URL: {self.driver.current_url}")
            print(f"Page source: {self.driver.page_source[:500]}...")  # Print first 500 characters of page source


    def run_bot(self):
        """The methods are called sequentially."""
        self.sign_in()
        self.get_opentowork_url()
        self.find_posts_comments_by_fake_users()  # This method needs to be implemented
        self.get_fakeuser_url()
        # self.fakeuser_url()
        # self.click_more_button()
        self.report_fake_user()  # Make sure this line is uncommented
        browser_persist()


start_time = time.time()
# keep the browser open indefinitely
while True:
    try:
        ScamBait().run_bot()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Error occurred in {time.time() - start_time:.2f}s")
        continue
