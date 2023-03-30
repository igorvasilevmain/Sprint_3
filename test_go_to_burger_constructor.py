from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestStellarBurgersGoToConstructor:

    def test_go_to_burger_constructor_by_constructor_button_from_private_office(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.USER_PROFILE)).text
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        burger_constructor = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR)).text
        assert 'Соберите бургер' in burger_constructor

    def test_go_to_burger_constructor_by_stellar_burgers_logo_from_private_office(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.USER_PROFILE)).text
        login.find_element(*Locators.STELLAR_BURGERG_LOGO).click()
        burger_constructor = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR)).text
        assert 'Соберите бургер' in burger_constructor
