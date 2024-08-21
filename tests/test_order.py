import allure

from locators.locators_main_page import LocatorsOrder
from locators.locators_order_page import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка оформления заказа с адресом, без выбора цвета и комментария')
    def test_order_with_address_header_button(self, open_main_page, main_page, driver):
        main_page.wait_and_find_element(LocatorsOrder.BUTTON_ORDER_HEADER).click()

        order_page = OrderPage(driver)

        order_page.wait_and_find_element(OrderPageLocators.NAME).send_keys('Имя')
        order_page.wait_and_find_element(OrderPageLocators.SURNAME).send_keys('Фамилия')
        order_page.wait_and_find_element(OrderPageLocators.ADDRESS).send_keys('Тестовая ул., д.22')
        order_page.wait_and_find_element(OrderPageLocators.SELECT_METRO).click()
        order_page.wait_and_find_element(OrderPageLocators.LUBIANKA).click()
        order_page.wait_and_find_element(OrderPageLocators.PHONE).send_keys('12345678987')

        order_page.click_button_next()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.TITLE))

        order_page.wait_and_find_element(OrderPageLocators.SELECT_DATE).send_keys('01.09.2024')
        order_page.wait_and_find_element(OrderPageLocators.TITLE).click()
        order_page.wait_and_find_element(OrderPageLocators.SELECT_TIME).click()
        order_page.wait_and_find_element(OrderPageLocators.TIME).click()
        order_page.wait_and_find_element(OrderPageLocators.BUTTON_ORDER).click()
        order_page.wait_and_find_element(OrderPageLocators.BUTTON_YES).click()

        assert order_page.wait_and_find_element(OrderPageLocators.ORDER_READY).text.find("Заказ оформлен") >= 0

    @allure.title('Проверка оформления заказа без адреса, с выбором цвета и комментарием')
    def test_order_without_address_body_button(self, open_and_scroll_page, main_page, driver):
        main_page.wait_and_find_element(LocatorsOrder.BUTTON_ORDER_BODY).click()

        order_page = OrderPage(driver)

        order_page.wait_and_find_element(OrderPageLocators.NAME).send_keys('Имя')
        order_page.wait_and_find_element(OrderPageLocators.SURNAME).send_keys('Фамилия')
        order_page.wait_and_find_element(OrderPageLocators.SELECT_METRO).click()
        order_page.wait_and_find_element(OrderPageLocators.LUBIANKA).click()
        order_page.wait_and_find_element(OrderPageLocators.PHONE).send_keys('12345678987')

        order_page.click_button_next()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.TITLE))

        order_page.wait_and_find_element(OrderPageLocators.SELECT_DATE).send_keys('01.09.2024')
        order_page.wait_and_find_element(OrderPageLocators.TITLE).click()
        order_page.wait_and_find_element(OrderPageLocators.SELECT_TIME).click()
        order_page.wait_and_find_element(OrderPageLocators.TIME).click()
        order_page.wait_and_find_element(OrderPageLocators.COLOR_BLACK).click()
        order_page.wait_and_find_element(OrderPageLocators.COMMENT).send_keys('Okay!')
        order_page.wait_and_find_element(OrderPageLocators.BUTTON_ORDER).click()
        order_page.wait_and_find_element(OrderPageLocators.BUTTON_YES).click()

        assert order_page.wait_and_find_element(OrderPageLocators.ORDER_READY).text.find("Заказ оформлен") >= 0
