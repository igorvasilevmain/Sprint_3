from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestStellarBurgersGoToConstructorSections:

    def test_go_to_buns_section(self, driver):
        driver.find_element(*Locators.STUFFING_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        driver.find_element(*Locators.BUN).click()
        modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MODAL)).text
        assert 'Флюоресцентная булка R2-D3' in modal, 'Такого нет! Убедись, что выбран правильный раздел!'

    def test_go_to_sauce_section(self, driver):
        driver.find_element(*Locators.SAUSE_SECTION).click()
        driver.find_element(*Locators.SAUCE).click()
        modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MODAL)).text
        assert 'Соус с шипами Антарианского плоскоходца' in modal, 'Такого нет! Убедись, что выбран правильный раздел!'

    def test_go_to_stuffing_section(self, driver):
        driver.find_element(*Locators.STUFFING_SECTION).click()
        cheese = driver.find_element(*Locators.CHEESE)
        driver.execute_script("arguments[0].scrollIntoView();", cheese)
        cheese.click()
        modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MODAL)).text
        assert 'Сыр с астероидной плесенью' in modal, 'Такого нет! Убедись, что выбран правильный раздел!'
