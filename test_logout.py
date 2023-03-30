from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestStellarBurgers:

    def test_logout_by_logout_button_from_private_office(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.USER_PROFILE)).text
        login.find_element(*Locators.LOGOUT_BUTTON).click()
        auth_form = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.AUTH_FORM)).text
        assert auth_form == 'Вход'
