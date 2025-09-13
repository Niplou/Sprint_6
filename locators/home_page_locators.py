from selenium.webdriver.common.by import By

class HomePageLocators:
    """Локаторы главной страницы"""
    
    # Header elements
    YANDEX_LOGO = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    HEADER_ORDER_BUTTON = (By.XPATH, "(.//button[text()='Заказать'])[1]")
    ORDER_STATUS_BUTTON = (By.XPATH, ".//button[text()='Статус заказа']")
    ORDER_NUMBER_INPUT = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Header_Input__xIoUq']")
    GO_BUTTON = (By.XPATH, ".//button[text()='Go!']")
    HEADER_TITLE = (By.XPATH, ".//div[text()='Учебный тренажер']")

    # Main page elements
    PAGE_TITLE = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    MAIN_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    FAQ_SECTION_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']")

    @staticmethod
    def get_question_locator(question_index: int):
        return (By.ID, f"accordion__heading-{question_index}")

    @staticmethod
    def get_answer_locator(question_index: int):
        return (By.ID, f"accordion__panel-{question_index}")