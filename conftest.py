# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(URL.MAIN)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    from pages.home_page import HomePage
    return HomePage(driver)

@pytest.fixture
def dzen_page(driver):
    from pages.dzen_page import DzenPage
    return DzenPage(driver)

@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)

@pytest.fixture(autouse=True)
def setup_cookies(driver, home_page):
    home_page.accept_cookies()
    yield

def pytest_make_parametrize_id(val):
    return repr(val)