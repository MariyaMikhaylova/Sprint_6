from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators


class OrderPage(BasePage):

    def order_client_data_with_address(self):
        self.wait_and_find_element(OrderPageLocators.NAME).send_keys('Имя')
        self.wait_and_find_element(OrderPageLocators.SURNAME).send_keys('Фамилия')
        self.wait_and_find_element(OrderPageLocators.ADDRESS).send_keys('Тестовая ул., д.22')
        self.wait_and_find_element(OrderPageLocators.SELECT_METRO).click()
        self.wait_and_find_element(OrderPageLocators.LUBIANKA).click()
        self.wait_and_find_element(OrderPageLocators.PHONE).send_keys('12345678987')
        self.click_button_next()

    def order_client_data_without_address(self):
        self.wait_and_find_element(OrderPageLocators.NAME).send_keys('Имя')
        self.wait_and_find_element(OrderPageLocators.SURNAME).send_keys('Фамилия')
        self.wait_and_find_element(OrderPageLocators.SELECT_METRO).click()
        self.wait_and_find_element(OrderPageLocators.LUBIANKA).click()
        self.wait_and_find_element(OrderPageLocators.PHONE).send_keys('12345678987')
        self.click_button_next()

    def order_scooter_data_without_color_comment(self):
        self.wait_and_find_element(OrderPageLocators.SELECT_DATE).send_keys('01.09.2024')
        self.wait_and_find_element(OrderPageLocators.TITLE).click()
        self.wait_and_find_element(OrderPageLocators.SELECT_TIME).click()
        self.wait_and_find_element(OrderPageLocators.TIME).click()
        self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER).click()
        self.wait_and_find_element(OrderPageLocators.BUTTON_YES).click()

    def order_scooter_data_with_color_comment(self):
        self.wait_and_find_element(OrderPageLocators.SELECT_DATE).send_keys('01.09.2024')
        self.wait_and_find_element(OrderPageLocators.TITLE).click()
        self.wait_and_find_element(OrderPageLocators.SELECT_TIME).click()
        self.wait_and_find_element(OrderPageLocators.TIME).click()
        self.wait_and_find_element(OrderPageLocators.COLOR_BLACK).click()
        self.wait_and_find_element(OrderPageLocators.COMMENT).send_keys('Okay!')
        self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER).click()
        self.wait_and_find_element(OrderPageLocators.BUTTON_YES).click()