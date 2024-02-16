import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        log_name = inspect.stack()[1][3]  # name which this method be called
        log = logging.getLogger(log_name)

        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        log.addHandler(file_handler)  # filehandler object

        log.setLevel(logging.DEBUG)
        return log

    def verify_link_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_alert_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, text)))

    def select_option_bytext(self, locator, text):
        sel = Select(locator)
        # dropdown.select_by_index(1)
        sel.select_by_visible_text(text)
