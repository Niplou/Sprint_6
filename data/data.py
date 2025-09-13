from dataclasses import dataclass
from typing import List

@dataclass
class UserData:
    first_name: str
    last_name: str
    address: str
    metro_station: str
    phone_number: str
    delivery_date: str
    comment: str

class TestUsers:
    VITALY = UserData(
        first_name='Иван',
        last_name='Иванов',
        address='Москва, ул. Ленина, д. 1',
        metro_station='Парк культуры',
        phone_number='89997009080',
        delivery_date='01.09.2025',
        comment='Тестовый комментарий'
    )
    
    ALEXEY = UserData(
        first_name='Петр',
        last_name='Первый',
        address='Москва, ул. Пресненская набережная, д. 1',
        metro_station='Парк культуры',
        phone_number='89991809070',
        delivery_date='01.09.2025',
        comment='Тестовый комментарий 2'
    )

class URL:
    DZEN = "https://dzen.ru/?yredirect=true"
    QA_SCOOTER_MAIN = "https://qa-scooter.praktikum-services.ru/"
    QA_SCOOTER_ORDER = "https://qa-scooter.praktikum-services.ru/order"
    QA_SCOOTER_TRACK = "https://qa-scooter.praktikum-services.ru/track"

class ExpectedAnswers:
    FAQ_ANSWERS = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
    ]