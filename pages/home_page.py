import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    
    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click_element(HomePageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Кликнуть на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_element(HomePageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Кликнуть на кнопку "Заказать" на главной странице')
    def click_main_order_button(self):
        self.scroll_to_element(HomePageLocators.MAIN_ORDER_BUTTON)
        self.click_element(HomePageLocators.MAIN_ORDER_BUTTON)

    @allure.step('Кликнуть на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Кликнуть на логотип Самокат')
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    @allure.step('Прокрутить к разделу FAQ')
    def scroll_to_faq_section(self):
        self.scroll_to_element(HomePageLocators.FAQ_SECTION_TITLE)

    @allure.step('Получить текст ответа на вопрос FAQ')
    def get_faq_answer_text(self, question_index: int) -> str:
        question_locator = HomePageLocators.get_question_locator(question_index)
        answer_locator = HomePageLocators.get_answer_locator(question_index)
        
        self.scroll_to_faq_section()
        self.click_element(question_locator)
        return self.get_element_text(answer_locator)

    @allure.step('Проверить отображение заголовка страницы')
    def is_header_title_displayed(self) -> bool:
        return self.is_element_displayed(HomePageLocators.HEADER_TITLE)