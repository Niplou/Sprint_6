from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы страницы заказа"""
    
    # Page 1: Customer information
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, ".//div[text()='Парк культуры']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Page 2: Rental information
    DELIVERY_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_THREE_DAYS = (By.XPATH, ".//div[text()='трое суток']")
    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GRAY_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, ".//button[text()='Назад']")
    ORDER_BUTTON = (By.XPATH, "(.//button[text()='Заказать'])[2]")

    # Order confirmation modal
    CONFIRM_NO_BUTTON = (By.XPATH, ".//button[text()='Нет']")
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")

    # Order success modal
    ORDER_SUCCESS_TITLE = (By.XPATH, ".//div[text()='Заказ оформлен']")
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")