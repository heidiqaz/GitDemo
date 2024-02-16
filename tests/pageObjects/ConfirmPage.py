from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country_input = (By.ID, "country")
    country_select = (By.LINK_TEXT, "India")
    check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']/label")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    alert_success = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def get_country_str(self):
        return self.driver.find_element(*ConfirmPage.country_input)

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.country_select)

    def select_checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_box)

    def submit_confirm(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def get_alert_success(self):
        return self.driver.find_element(*ConfirmPage.alert_success)
