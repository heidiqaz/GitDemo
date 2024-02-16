from selenium.webdriver.common.by import By

from tests.pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # card_titles = (By.XPATH, "//div[@class='card h-100']")
    card_titles = (By.XPATH, "//h4[@class='card-title']")
    card_footer = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    btn_checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    btn_checkout_confirm = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_titles)

    def get_card_footer(self):
        return self.driver.find_element(*CheckoutPage.card_footer)

    def get_btn_checkout(self):
        return self.driver.find_element(*CheckoutPage.btn_checkout)

    def get_btn_checkout_confirm(self):
        self.driver.find_element(*CheckoutPage.btn_checkout_confirm).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

