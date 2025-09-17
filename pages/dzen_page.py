from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class DzenPageLocators:
    MAIN_BUTTON = (By.XPATH, ".//span[text()='Главная']")

class DzenPage(BasePage):

    @allure.step('Проверить отображение кнопки "Главная" на DZEN')
    def is_main_button_displayed(self) -> bool:
        return self.is_element_displayed(DzenPageLocators.MAIN_BUTTON)