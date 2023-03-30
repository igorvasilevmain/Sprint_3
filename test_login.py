from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

# аккаунт предварительно создан, в нижеприведенных тестах использую уже имеющегося юзера
email = 'igor_vasilev_08_123@example.com'
password = 'Qwe123'

class TestStellarBurgersLogin:

    def test_successful_account_login_from_sign_in_button(self, driver):
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ON_AUTH_FORM).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ON_AUTH_FORM).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON_ON_AUTH_FORM).click()
        checkout_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text
        assert checkout_button == 'Оформить заказ'

    def test_successful_account_login_from_private_office_button(self, driver):
        driver.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ON_AUTH_FORM).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ON_AUTH_FORM).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON_ON_AUTH_FORM).click()
        checkout_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text
        assert checkout_button == 'Оформить заказ'

    def test_successful_account_login_from_sign_in_link_on_registration_form(self, driver):
        driver.find_element(*Locators.PRIVATE_OFFICE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.SIGN_IN_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ON_AUTH_FORM).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ON_AUTH_FORM).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON_ON_AUTH_FORM).click()
        checkout_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text
        assert checkout_button == 'Оформить заказ'

    def test_successful_account_login_from_sign_in_link_on_password_restore_form(self, driver):
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.PASSWORD_RESTORE_LINK).click()
        driver.find_element(*Locators.SIGN_IN_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ON_AUTH_FORM).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ON_AUTH_FORM).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON_ON_AUTH_FORM).click()
        checkout_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text
        assert checkout_button == 'Оформить заказ'
