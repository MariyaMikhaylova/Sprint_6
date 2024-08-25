import allure
from locators.locators_main_page import LocatorsOrder
from locators.locators_order_page import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка оформления заказа с адресом, без выбора цвета и комментария')
    def test_order_with_address_header_button(self, open_main_page, main_page, driver):
        main_page.wait_and_find_element(LocatorsOrder.BUTTON_ORDER_HEADER).click()
        order_page = OrderPage(driver)
        order_page.order_client_data_with_address()
        order_page.order_scooter_data_without_color_comment()
        assert order_page.wait_and_find_element(OrderPageLocators.ORDER_READY).text.find("Заказ оформлен") >= 0

    @allure.title('Проверка оформления заказа без адреса, с выбором цвета и комментарием')
    def test_order_without_address_body_button(self, open_and_scroll_page, main_page, driver):
        main_page.wait_and_find_element(LocatorsOrder.BUTTON_ORDER_BODY).click()
        order_page = OrderPage(driver)
        order_page.order_client_data_without_address()
        order_page.order_scooter_data_with_color_comment()
        assert order_page.wait_and_find_element(OrderPageLocators.ORDER_READY).text.find("Заказ оформлен") >= 0
