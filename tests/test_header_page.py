# test_header_page.py
import allure
import pytest
from data.data import ExpectedAnswers
from urls import URL

class TestMainPage:

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver, home_page):
        home_page.click_header_order_button()
        home_page.click_scooter_logo()
        
        current_url = home_page.get_current_url()
        title_displayed = home_page.is_header_title_displayed()
        
        assert current_url == URL.MAIN
        assert title_displayed

    @allure.title('Проверка перехода на DZEN по логотипу Яндекс')
    def test_yandex_logo_redirect(self, driver, home_page, dzen_page):
        home_page.click_yandex_logo()
        home_page.switch_to_new_tab()
        
        current_url = home_page.get_current_url()
        assert current_url == URL.DZEN
        assert dzen_page.is_main_button_displayed()

    @allure.title('Проверка текста ответов в FAQ')
    @pytest.mark.parametrize('question_index', range(8))
    def test_faq_answers(self, driver, home_page, question_index):
        answer_text = home_page.get_faq_answer_text(question_index)
        expected_text = ExpectedAnswers.FAQ_ANSWERS[question_index]
        
        assert answer_text == expected_text