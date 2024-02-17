import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pageObjects.CheckoutPage import CheckoutPage
from tests.pageObjects.ConfirmPage import ConfirmPage
from tests.pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)

        # # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() #部分匹配
        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()  # 部分匹配
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        checkout_page = home_page.shopItem()
        log.info("getting all the call items")

        products = checkout_page.get_card_titles()
        for product in products:
            if "Blackberry" == product.text:
                log.info("product.text== black berry: " + product.text)
                checkout_page.get_card_footer().click()
                time.sleep(1)

        # self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkout_page.get_btn_checkout().click()

        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        confirm_page = checkout_page.get_btn_checkout_confirm()

        # self.driver.find_element(By.ID, "country").send_keys("ind")
        # confirm_page = ConfirmPage(self.driver)
        log.info("entering country name : ind")
        confirm_page.get_country_str().send_keys("ind")

        # self.driver.find_element(By.LINK_TEXT, "India").click()
        self.verify_link_presence("India")
        confirm_page.select_country().click()

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']/label").click()
        confirm_page.select_checkbox().click()
        time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        confirm_page.submit_confirm().click()

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='alert-success']")))
        self.verify_alert_presence("div[class*='alert-success']")
        text_match = confirm_page.get_alert_success().text
        log.info("alert text:" + text_match)
        # assert ("Success!" in self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)
        assert ("Success!" in confirm_page.get_alert_success().text)
        log.info("Success!")
        print(confirm_page.get_alert_success().text)








