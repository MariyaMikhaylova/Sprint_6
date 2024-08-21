import pytest
from selenium import webdriver
from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()

    yield firefox

    firefox.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture(scope='function')
def open_and_scroll_page(main_page):
    main_page.open_page(Urls.SCOOTER)
    main_page.scroll_page()


@pytest.fixture(scope='function')
def open_main_page(main_page):
    main_page.open_page(Urls.SCOOTER)


@pytest.fixture(scope='function')
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page


@pytest.fixture(scope='function')
def open_order_page(order_page):
    order_page.open_page(Urls.ORDER)
