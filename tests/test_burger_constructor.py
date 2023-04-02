from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from burger_constructor_data import BurgerConstructorData
from locators import Locators


class TestStellarBurgersGoToConstructorSections:

    def test_go_to_buns_section(self, driver):
        driver.find_element(*Locators.STUFFING_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        driver.find_element(*Locators.BUN).click()
        modal = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.MODAL)).text
        assert BurgerConstructorData.roll_r2d3 in modal, \
            f'{BurgerConstructorData.roll_r2d3} отсутствует в модальном окне'

    def test_go_to_sauce_section(self, driver):
        driver.find_element(*Locators.SAUSE_SECTION).click()
        driver.find_element(*Locators.SAUCE).click()
        modal = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.MODAL)).text
        assert BurgerConstructorData.sauce_with_ships in modal, \
            f'{BurgerConstructorData.sauce_with_ships} отсутствует в модальном окне'

    def test_go_to_stuffing_section(self, driver):
        driver.find_element(*Locators.STUFFING_SECTION).click()
        cheese = driver.find_element(*Locators.CHEESE)
        driver.execute_script("arguments[0].scrollIntoView();", cheese)
        cheese.click()
        modal = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.MODAL)).text
        assert BurgerConstructorData.cheese_with_mold in modal, \
            f'{BurgerConstructorData.cheese_with_mold} отсутствует в модальном окне'
