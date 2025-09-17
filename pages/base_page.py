from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple
import allure

class BasePage:
    DEFAULT_TIMEOUT = 10
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_for_element_visible(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание присутствия элемента: {locator}')
    def wait_for_element_present(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Получение текущего URL')
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step('Поиск элемента: {locator}')
    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait_for_element_visible(locator)

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator: Tuple[str, str]) -> None:
        self.find_element(locator).click()

    @allure.step('Ввод текста "{text}" в элемент: {locator}')
    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста элемента: {locator}')
    def get_element_text(self, locator: Tuple[str, str]) -> str:
        return self.find_element(locator).text

    @allure.step('Прокрутка к элементу: {locator}')
    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка отображения элемента: {locator}')
    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        return self.find_element(locator).is_displayed()

    @allure.step('Принятие cookies: {locator}')
    def accept_cookies(self, locator: Tuple[str, str]) -> None:
        self.click_element(locator)