from selenium.webdriver.common.by import By


class TopRatedMoviesPageLocators(object):
    ARTICLE = (By.CLASS_NAME, "article")
    HEADER = (By.CLASS_NAME, "header")
    BY_LINE = (By.CLASS_NAME, "byline")
    SHARE_BUTTON = (By.CLASS_NAME, "share-button")

    """Main table locators"""
    MAIN_TABLE = (By.CLASS_NAME, "lister-list")

    """sort by drop-down"""
    SORT_BY = (By.ID, "lister-sort-by-options")
    SORT_BY_RANKING = (By.XPATH, "//*[@id='lister-sort-by-options']/option[contains(text(), 'Ranking')]")
    SORT_BY_IMDB_RATING = (By.XPATH, "//*[@id='lister-sort-by-options']/option[contains(text(), 'IMDb Rating')]")
    SORT_BY_RELEASE_DATE = (By.XPATH, "//*[@id='lister-sort-by-options']/option[contains(text(), 'Release Date')]")
    SORT_BY_NUMBER_OF_RATINGS = (
    By.XPATH, "//*[@id='lister-sort-by-options']/option[contains(text(), 'Number of Ratings')]")
    SORT_BY_YOUR_RATING = (By.XPATH, "//*[@id='lister-sort-by-options']/option[contains(text(), 'Your Rating')]")

    DESCENDING_ORDER = (By.XPATH, "//span[@class='global-sprite lister-sort-reverse ascending']")
    ASCENDING_ORDER = (By.XPATH, "//span[@class='global-sprite lister-sort-reverse descending']")
    POSTER_COLUMN = (By.CLASS_NAME, "posterColumn")
    TITLE_COLUMN = (By.CLASS_NAME, "titleColumn")
    RATING_IMDB_COLUMN = (By.CLASS_NAME, "ratingColumn imdbRating")
    WATCHLIST_COLUMN = (By.CLASS_NAME, "watchlistColumn")


class SignInPge(object):
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
