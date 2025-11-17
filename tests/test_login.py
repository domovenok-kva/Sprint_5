from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators.locatorstest import LocatorsForTest
from testuser.existtestuser import ExistUser

class TestLoginWorking:

    def test_exist_user_login(self, driver):
       driver.find_element(*LocatorsForTest.log_and_reg_button).click()
       driver.find_element(*LocatorsForTest.email_input).send_keys(ExistUser.email)
       driver.find_element(*LocatorsForTest.password_input).send_keys(ExistUser.password)
       driver.find_element(*LocatorsForTest.login_button).click()
       assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.user_avatar)).is_displayed()
       assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.user_name)).text == 'User.'

        
