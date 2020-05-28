from selenium.webdriver.common.by import By

from resources.locators import TopRatedMoviesPageLocators
from resources.pages.base_page import BasePage
from resources.testdata import TestData


class TopRatedMoviesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.TOP_250_MOVIES_URL)

    def choose_sort_by(self, sort_by):
        self.click(sort_by)

    def get_main_table(self):
        return self.driver.find_element(*TopRatedMoviesPageLocators.MAIN_TABLE)

    def click_on_descending_order_button(self):
        self.click(TopRatedMoviesPageLocators.DESCENDING_ORDER)

    def click_on_ascending_order_button(self):
        self.click(TopRatedMoviesPageLocators.ASCENDING_ORDER)

    def get_release_date_from_row(self, row):
        rank_and_title_column = row.find_elements(By.TAG_NAME, "td")[1]
        release_date = rank_and_title_column.find_elements(By.CLASS_NAME, "secondaryInfo")[0].text
        return int(release_date[1:-1])
