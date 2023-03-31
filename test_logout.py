from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgersLogout:

    def test_logout_by_logout_button_from_private_office(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        WebDriverWait(login, 5).until(
            EC.visibility_of_element_located(Locators.USER_PROFILE)).text
        login.find_element(*Locators.LOGOUT_BUTTON).click()
        sign_in_button = WebDriverWait(login, 5).until(
            EC.visibility_of_element_located(Locators.SIGN_IN_BUTTON_ON_AUTH_FORM)).text
        assert sign_in_button == 'Войти'
