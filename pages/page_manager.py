from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage


class PageManager:
    def __init__(self, driver):
        self.driver = driver
        self._home_page = None
        self._order_page = None
        self._dzen_page = None

    @property
    def home(self):
        if self._home_page is None:
            self._home_page = HomePage(self.driver)
        return self._home_page

    @property
    def order(self):
        if self._order_page is None:
            self._order_page = OrderPage(self.driver)
        return self._order_page

    @property
    def dzen(self):
        if self._dzen_page is None:
            self._dzen_page = DzenPage(self.driver)
        return self._dzen_page