#!/usr/bin/env python3

import os
import random
import time
import config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# scam_bait_utils.py: Might need editing in sloving click_more_button method issues.
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
        self.more_button_xpath = ("//button[contains(@class, 'artdeco-dropdown__trigger') and "
                                  "contains(@class, 'artdeco-button--secondary') and "
                                  "contains(@aria-label, 'More actions')]//span[contains(text(), 'More')]")

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

##--- Begin of get_fakeuser_url method ---- #
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

# ---- End of get_fakeuser_url method ----#



# ---- Begin of click_more_button method ---- #
    def click_more_button(self):
        try:
            more_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
            )
            #more_button.click() <-- using python to click the button. JS used below:
            self.driver.execute_script("arguments[0].click();", more_button)
            print("Successfully clicked 'More' button")
        except Exception as e:
            print(f"An error occurred while clicking the 'More' button: {str(e)}")
            print("Button visibility: Not found")
            print("Button enabled: Not found")

# ---- End of click_more_button method ---- #


# ---- Commenting out four trouble shooting bugs in the Click more button function ---- #
# ----Begin of Report a fake user method --- #
#    def report_fake_user(self):
#        try:
#            print(f"Attempting to click 'More' button with XPath: {more_button_xpath}")
#            more_button = WebDriverWait(self.driver, 10).until(
#                EC.element_to_be_clickable((By.XPATH, more_button_xpath))
#            )
#            self.driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
#            time.sleep(1)  # Give the page a moment to settle after scrolling
#            more_button.click()
#            print("Successfully clicked 'More' button")
#
#        except Exception as e:
#            print(f"An error occurred while reporting the fake user: {str(e)}")
#            print(f"Current URL: {self.driver.current_url}")
#            print(f"Page source: {self.driver.page_source[:500]}...")  # Print first 500 characters of page source
#
#            # Additional debugging
#            all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
#            print(f"Total number of buttons on the page: {len(all_buttons)}")
#            for i, button in enumerate(all_buttons[:5], 1):  # Print details of first 5 buttons
#                print(f"Button {i}: Class: {button.get_attribute('class')}, "
#                      f"Text: {button.text}, "
#                      f"Aria-label: {button.get_attribute('aria-label')}")

# ---- End of report_fake_user method ----#


# -- Run the bot --- #
    def run_bot(self):
        """The methods are called sequentially."""
        self.sign_in()
        self.get_opentowork_url()
        self.find_posts_comments_by_fake_users()  # This method needs to be implemented
        self.get_fakeuser_url()
        # self.fakeuser_url()
        self.click_more_button()
#        self.report_fake_user()  # Make sure this line is uncommented
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
