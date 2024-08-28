from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Urls
from locators.locators_order_page import OrderPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def check_the_transition_to_dzen(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.DZEN))
        assert driver.current_url == Urls.DZEN

    def click_button_next(self):
        button = self.wait_and_find_element(OrderPageLocators.BUTTON_NEXT)
        button.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.TITLE))
