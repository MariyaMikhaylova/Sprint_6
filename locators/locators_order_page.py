from selenium.webdriver.common.by import By


class OrderPageLocators:

    LOGO_SCOOTER = (By.XPATH, ".//a[@href = '/']")  # ссылка на главную страницу
    NAME = (By.XPATH, '//input[@placeholder = "* Имя"]')  # поле ввода Имя
    SURNAME = (By.XPATH, '//input[@placeholder = "* Фамилия"]')  # поле ввода Фамилия
    ADDRESS = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')  # поле ввода Адрес
    SELECT_METRO = (By.XPATH, '//div[@class = "select-search__value"]')  # выпадающий список со станциями метро
    LUBIANKA = (By.XPATH, '//button[starts-with(@class, "Order_SelectOption")]/div[text()="Лубянка"]')  # метро Лубянка
    PHONE = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')  # поле ввода Телефон
    BUTTON_NEXT = (By.XPATH, '//button[text() = "Далее"]')  # кнопка Далее в форме заказа

    TITLE = (By.XPATH, '//div[text() = "Про аренду"]')  # Заголовок "Про аренду"
    SELECT_DATE = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')  # поле ввода даты
    SELECT_TIME = (By.XPATH, '//div[@class="Dropdown-control"]')  # выпадающий список вариантов срока аренда
    TIME = (By.XPATH, '//*[text()="сутки"]')  # срок аренды сутки
    COLOR_BLACK = (By.XPATH, '//input[@id ="black"]')  # выбор цвета Черный
    COMMENT = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')  # поле ввода Комментарий
    BUTTON_ORDER = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/child::button[text() = "Заказать"]')  # Кнопка Заказать в форме заказа
    BUTTON_YES = (By.XPATH, '//button[text() = "Да"]')  # кнопка Да во всплывающем окне "Хотите оформить заказ?"
    ORDER_READY = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')  # заголовок "Заказ оформлен" во всплывающем окне
