import time

import pytest

from TestData.HomePageData import HomePageData
from tests.pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# new branch- develop
class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        home_page = HomePage(self.driver)

        # ID, Xpath, CSSSelector, Class name, name, linkText
        # Xpath - // tagname[@attribute='value'] -> //input[@type='submit']
        # CSS - tagname[attribute='value'] ->input[type='submit'], #id, .classname
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Heidi")
        home_page.get_name().send_keys(get_data["name"])
        # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        home_page.get_name_radio().click()

        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        home_page.get_pwd().send_keys("123456")

        # driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        home_page.get_email().send_keys(get_data["email"])
        # driver.find_element(By.ID, "exampleCheck1").click()
        home_page.get_email_check().click()
        time.sleep(3)
        # select
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # sel = Select(home_page.get_gender())
        # dropdown.select_by_index(1)
        # sel.select_by_visible_text("Female")
        self.select_option_bytext(home_page.get_gender(), get_data["gender"])

        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        home_page.get_submit().click()

        # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        message = home_page.get_alert().text
        assert "Success" in message
        assert "Success" in message
        self.driver.refresh()

        # # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HelloAgain")
        # home_page.get_input().send_keys("HelloAgain")
        # time.sleep(2)
        # # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        # home_page.get_input().clear()
        # time.sleep(2)
        # print(message)

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
