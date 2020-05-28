from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
