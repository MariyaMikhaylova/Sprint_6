from selenium.webdriver.common.by import By


class LocatorsOrder:

    TITLE_SCOOTER = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')  # заголовок "Самокат "
    LOGO_YANDEX = (By.XPATH, ".//a[@href = '//yandex.ru']")  # ссылка на страницу Яндекс.Дзен
    BUTTON_ORDER_HEADER = (By.XPATH, '//button[text() = "Заказать"]')  # кнопка Заказать в шапке страницы
    BUTTON_ORDER_BODY = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/child::button')  # кнопка Заказать в теле страницы`


class LocatorsQuestionsAndAnswer:

    PRICE = (By.XPATH, '//*[@id="accordion__heading-0"]')  # Сколько это стоит? И как оплатить?
    ANSWER_PRICE = (By.XPATH, '//*[@id="accordion__panel-0"]')
    SOME_SCOOTERS = (By.XPATH, '//*[@id="accordion__heading-1"]')  # Хочу сразу несколько самокатов! Так можно?
    ANSWER_SOME_SCOOTERS = (By.XPATH, '//*[@id="accordion__panel-1"]')
    RENTAL_TIME = (By.XPATH, '//*[@id="accordion__heading-2"]')  # Как рассчитывается время аренды?
    ANSWER_RENTAL_TIME = (By.XPATH, '//*[@id="accordion__panel-2"]')
    RENTAL_TODAY = (By.XPATH, '//*[@id="accordion__heading-3"]')  # Можно ли заказать самокат прямо на сегодня?
    ANSWER_RENTAL_TODAY = (By.XPATH, '//*[@id="accordion__panel-3"]')
    CHANGE_RENTAL_TIME = (By.XPATH, '//*[@id="accordion__heading-4"]')  # Можно ли продлить заказ или вернуть самокат раньше?
    ANSWER_CHANGE_RENTAL_TIME = (By.XPATH, '//*[@id="accordion__panel-4"]')
    CHARGE = (By.XPATH, '//*[@id="accordion__heading-5"]')  # Вы привозите зарядку вместе с самокатом?
    ANSWER_CHARGE = (By.XPATH, '//*[@id="accordion__panel-5"]')
    CANCEL_ORDER = (By.XPATH, '//*[@id="accordion__heading-6"]')  # Можно ли отменить заказ?
    ANSWER_CANCEL_ORDER = (By.XPATH, '//*[@id="accordion__panel-6"]')
    MKAD = (By.XPATH, '//*[@id="accordion__heading-7"]')  # Я жизу за МКАДом, привезёте?
    ANSWER_MKAD = (By.XPATH, '//*[@id="accordion__panel-7"]')
