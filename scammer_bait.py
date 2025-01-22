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
        self.driver.get(config.openToWork)
        time.sleep(5)
        print("#opentowork URL...")

    def find_posts_comments_by_fake_users(self):
        # On the openToWork page, find a post that has been commented on by a fake user.
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

    def report_fake_user(self):
        try:
            more_button_xpath = '//*[@id="ember69-profile-overflow-action"]/span'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, more_button_xpath))).click()

            triple_dots_xpath = '//*[@id="ember69-profile-overflow-action"]/span/button'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, triple_dots_xpath))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, triple_dots_xpath))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, triple_dots_xpath))).click()

            report_button_xpath = '//*[@id="ember76"]/span'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, report_button_xpath))).click()
        except Exception as e:
            print(f"An error occurred while reporting fake user: {str(e)}")

    def run_bot(self):
        """The methods are called sequentially."""
        self.sign_in()
        self.get_opentowork_url()
        self.find_posts_comments_by_fake_users()  # This method needs to be implemented
        self.get_fakeuser_url()
        self.report_fake_user()
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
