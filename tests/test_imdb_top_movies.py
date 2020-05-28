from selenium.webdriver.common.by import By
from resources.locators import TopRatedMoviesPageLocators
from resources.pages.top_rated_movies_page import TopRatedMoviesPage
from tests.base_test_class import BaseTestClass


class TestImdbTopMoviesTests(BaseTestClass):

    def setUp(self):
        super().setUp()

    def test_check_sort_by_release_date(self):
        self.imdb250Page = TopRatedMoviesPage(self.driver)
        self.imdb250Page.choose_sort_by(TopRatedMoviesPageLocators.SORT_BY_RELEASE_DATE)
        self.imdb250Page.is_visible(TopRatedMoviesPageLocators.MAIN_TABLE)
        table = self.imdb250Page.get_main_table()
        rows = table.find_elements(By.TAG_NAME, "tr")
        for i in range(len(rows)):
            if i > 0:
                release_date = self.imdb250Page.get_release_date_from_row(rows[i])
                previous_release_date = self.imdb250Page.get_release_date_from_row(rows[i - 1])
                # print("{} <= {}".format(release_date, previous_release_date))
                assert release_date <= previous_release_date

    def test_check_descending_order_button_for_release_date_drop_down(self):
        self.imdb250Page = TopRatedMoviesPage(self.driver)
        self.imdb250Page.choose_sort_by(TopRatedMoviesPageLocators.SORT_BY_RELEASE_DATE)

        self.imdb250Page.click_on_descending_order_button()
        self.imdb250Page.is_visible(TopRatedMoviesPageLocators.ASCENDING_ORDER)
        self.imdb250Page.is_visible(TopRatedMoviesPageLocators.MAIN_TABLE)
        table = self.imdb250Page.get_main_table()
        rows = table.find_elements(By.TAG_NAME, "tr")

        for i in range(len(rows)):
            if i > 0:
                release_date = self.imdb250Page.get_release_date_from_row(rows[i])
                previous_release_date = self.imdb250Page.get_release_date_from_row(rows[i - 1])
                assert release_date >= previous_release_date

        self.imdb250Page.click_on_ascending_order_button()
        self.imdb250Page.is_visible(TopRatedMoviesPageLocators.DESCENDING_ORDER)
        self.imdb250Page.is_visible(TopRatedMoviesPageLocators.MAIN_TABLE)

        table_new = self.imdb250Page.get_main_table()
        rows_new = table_new.find_elements(By.TAG_NAME, "tr")
        for i in range(len(rows_new)):
            if i > 0:
                release_date = self.imdb250Page.get_release_date_from_row(rows_new[i])
                previous_release_date = self.imdb250Page.get_release_date_from_row(rows_new[i - 1])
                assert release_date <= previous_release_date
