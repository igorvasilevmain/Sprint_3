from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

faker = Faker()

class TestStellarBurgersRegistration:

    def test_successful_registration(self, driver):
        name = 'Игорь'
        email = faker.email()
        password = 'Qwe123'
        driver.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        sign_in_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGN_IN_BUTTON_ON_AUTH_FORM)).text
        assert sign_in_button == 'Войти'

    def test_try_to_registration_with_incorrectly_filled_fields(self, driver):
        name = ''
        email = '123'
        password = '12345'
        driver.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_ERROR)).text
        assert error == 'Некорректный пароль'