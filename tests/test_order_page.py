import allure
from helps.data import TestUsers
from pages.home_page import HomePage
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title('Оформление заказа через кнопку "Заказать" в хедере')
    def test_order_via_header_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.accept_cookies()
        home_page.click_header_order_button()
        order_page.complete_order_process(TestUsers.VITALY)
        
        assert order_page.is_order_success_displayed()

    @allure.title('Оформление заказа через кнопку "Заказать" на главной странице')
    def test_order_via_main_page_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.accept_cookies()
        home_page.click_main_order_button()
        order_page.complete_order_process(TestUsers.ALEXEY)
        
        assert order_page.is_order_success_displayed()