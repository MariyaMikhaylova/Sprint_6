import allure
from locators.locators_main_page import LocatorsQuestionsAndAnswer
import pytest


class TestQuestions:

    @allure.title('Проверка открытия ответов при клике на вопрос и их соответствия')
    @pytest.mark.parametrize('question,answer,result',
                             [
                                 [LocatorsQuestionsAndAnswer.PRICE, LocatorsQuestionsAndAnswer.ANSWER_PRICE, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
                                 [LocatorsQuestionsAndAnswer.SOME_SCOOTERS, LocatorsQuestionsAndAnswer.ANSWER_SOME_SCOOTERS, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
                                 [LocatorsQuestionsAndAnswer.RENTAL_TIME, LocatorsQuestionsAndAnswer.ANSWER_RENTAL_TIME, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
                                 [LocatorsQuestionsAndAnswer.RENTAL_TODAY, LocatorsQuestionsAndAnswer.ANSWER_RENTAL_TODAY, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
                                 [LocatorsQuestionsAndAnswer.CHANGE_RENTAL_TIME, LocatorsQuestionsAndAnswer.ANSWER_CHANGE_RENTAL_TIME, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
                                 [LocatorsQuestionsAndAnswer.CHARGE, LocatorsQuestionsAndAnswer.ANSWER_CHARGE, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
                                 [LocatorsQuestionsAndAnswer.CANCEL_ORDER, LocatorsQuestionsAndAnswer.ANSWER_CANCEL_ORDER, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
                                 [LocatorsQuestionsAndAnswer.MKAD, LocatorsQuestionsAndAnswer.ANSWER_MKAD, "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
                             ]
                             )
    def test_what_is_the_price(self, main_page, open_and_scroll_page, driver, question, answer, result):
        main_page.expand_answer(question)
        assert main_page.wait_and_find_element(answer).text == result
