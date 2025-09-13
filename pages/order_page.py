import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from helps.data import UserData

class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def enter_first_name(self, first_name: str):
        self.enter_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step('Заполнить поле "Фамилия"')
    def enter_last_name(self, last_name: str):
        self.enter_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step('Заполнить поле "Адрес"')
    def enter_address(self, address: str):
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, metro_station: str):
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        self.enter_text(OrderPageLocators.METRO_STATION_INPUT, metro_station)
        self.click_element(OrderPageLocators.METRO_STATION_OPTION)

    @allure.step('Заполнить поле "Телефон"')
    def enter_phone_number(self, phone_number: str):
        self.enter_text(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить информацию о клиенте')
    def fill_customer_info(self, user_data: UserData):
        self.enter_first_name(user_data.first_name)
        self.enter_last_name(user_data.last_name)
        self.enter_address(user_data.address)
        self.select_metro_station(user_data.metro_station)
        self.enter_phone_number(user_data.phone_number)
        self.click_next_button()

    @allure.step('Заполнить поле "Дата доставки"')
    def enter_delivery_date(self, delivery_date: str):
        self.click_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.enter_text(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)

    @allure.step('Выбрать срок аренды')
    def select_rental_period(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_THREE_DAYS)

    @allure.step('Выбрать цвет самоката')
    def select_scooter_color(self):
        self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)

    @allure.step('Заполнить поле "Комментарий"')
    def enter_comment(self, comment: str):
        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Заполнить информацию об аренде')
    def fill_rental_info(self, user_data: UserData):
        self.enter_delivery_date(user_data.delivery_date)
        self.select_rental_period()
        self.select_scooter_color()
        self.enter_comment(user_data.comment)
        self.click_order_button()

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step('Отменить заказ')
    def cancel_order(self):
        self.click_element(OrderPageLocators.CONFIRM_NO_BUTTON)

    @allure.step('Полный процесс оформления заказа')
    def complete_order_process(self, user_data: UserData):
        self.fill_customer_info(user_data)
        self.fill_rental_info(user_data)
        self.confirm_order()

    @allure.step('Проверить успешное оформление заказа')
    def is_order_success_displayed(self) -> bool:
        return self.is_element_displayed(OrderPageLocators.ORDER_SUCCESS_TITLE)