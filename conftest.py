import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Data
from locators import Locators

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT_FIELD_ON_AUTH_FORM).send_keys(Data.email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Data.password)
    driver.find_element(*Locators.SIGN_IN_BUTTON_ON_AUTH_FORM).click()
    return driver
