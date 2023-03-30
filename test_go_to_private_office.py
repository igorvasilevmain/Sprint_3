from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestStellarBurgersGoToPrivateOffice:

    def test_go_to_private_office_from_private_office_button(self, login):
        login.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        user_profile = WebDriverWait(login, 5).until(EC.visibility_of_element_located(Locators.USER_PROFILE)).text
        assert user_profile == 'Профиль'
