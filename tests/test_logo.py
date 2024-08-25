import allure
from data import Urls
from locators.locators_main_page import LocatorsOrder
from locators.locators_order_page import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogo:

    @allure.title('Проверка перехода на главную страницу при клике на Самокат в лого')
    def test_logo_scooter(self, open_order_page, order_page, driver):
        order_page.wait_and_find_element(OrderPageLocators.LOGO_SCOOTER).click()
        order_page.wait_and_find_element(LocatorsOrder.TITLE_SCOOTER).text.find("Самокат ")
        assert driver.current_url == Urls.SCOOTER

    @allure.title('Проверка открытия страницы Яндекс.Дзен при клике на Яндекс в лого')
    def test_logo_dzen(self, open_main_page, main_page, driver):
        main_page.wait_and_find_element(LocatorsOrder.LOGO_YANDEX).click()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.DZEN))
        assert driver.current_url == Urls.DZEN
