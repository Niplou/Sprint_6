import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data.data import URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(URL.QA_SCOOTER_MAIN)
    yield driver
    driver.quit()

def pytest_make_parametrize_id(val):
    return repr(val)