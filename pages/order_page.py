from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators


class OrderPage(BasePage):

    def click_button_next(self):
        button = self.wait_and_find_element(OrderPageLocators.BUTTON_NEXT)
        button.click()
