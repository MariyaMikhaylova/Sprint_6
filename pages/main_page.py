from pages.base_page import BasePage


class MainPage(BasePage):

    def expand_answer(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()
