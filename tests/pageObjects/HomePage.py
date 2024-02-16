from selenium.webdriver.common.by import By

from tests.pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.XPATH, "//input[@name='email']")
    pwd = (By.ID, "exampleInputPassword1")
    email_check = (By.ID, "exampleCheck1")
    name_radio = (By.CSS_SELECTOR, "#inlineRadio1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    input = (By.XPATH, "(//input[@type='text'])[3]")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_pwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def get_email_check(self):
        return self.driver.find_element(*HomePage.email_check)

    def get_name_radio(self):
        return self.driver.find_element(*HomePage.name_radio)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)

    def get_input(self):
        return self.driver.find_element(*HomePage.input)