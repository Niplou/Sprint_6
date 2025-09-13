import allure
import pytest
from data.data import ExpectedAnswers, URL
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.dzen_page import DzenPage

class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.home_page = HomePage(driver)
        self.dzen_page = DzenPage(driver)
        self.home_page.accept_cookies()

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        self.home_page.click_header_order_button()
        self.home_page.click_scooter_logo()
        
        current_url = self.home_page.get_current_url()
        title_displayed = self.home_page.is_header_title_displayed()
        
        assert current_url == URL.QA_SCOOTER_MAIN
        assert title_displayed

    @allure.title('Проверка перехода на DZEN по логотипу Яндекс')
    def test_yandex_logo_redirect(self, driver):
        self.home_page.click_yandex_logo()
        self.home_page.switch_to_new_tab()
        
        current_url = self.home_page.get_current_url()
        assert current_url == URL.DZEN

    @allure.title('Проверка текста ответов в FAQ')
    @pytest.mark.parametrize('question_index', range(8))
    def test_faq_answers(self, driver, question_index):
        answer_text = self.home_page.get_faq_answer_text(question_index)
        expected_text = ExpectedAnswers.FAQ_ANSWERS[question_index]
        
        assert answer_text == expected_text