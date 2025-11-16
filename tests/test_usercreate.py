from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators.locatorstest import LocatorsForTest
from testuser.existtestuser import ExistUser
from faker import Faker

driver = webdriver.Chrome()
driver.get("https://qa-desk.stand.praktikum-services.ru/")

class TestUserCreate:
       def test_user_create(self, driver):
             faker_email = Faker("en_US")
             password_test = "1234"
             
             driver.find_element(*LocatorsForTest.log_and_reg_button).click()
             driver.find_element(*LocatorsForTest.create_acc_button).click()
             driver.find_element(*LocatorsForTest.email_input).send_keys(faker_email.email())
             driver.find_element(*LocatorsForTest.password_input).send_keys(password_test)
             driver.find_element(*LocatorsForTest.password_repit_input).send_keys(password_test)
             driver.find_element(*LocatorsForTest.create_acc_button).click()
             assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.user_avatar)).is_displayed()
             assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.user_name)).text == "User."
             driver.quit()

       def test_user_create_err(self, driver):
              err_email = "ivanovemail"
              password_test = "1234"

              driver.find_element(*LocatorsForTest.log_and_reg_button).click()
              driver.find_element(*LocatorsForTest.create_acc_button).click()
              driver.find_element(*LocatorsForTest.email_input).send_keys(err_email)
              driver.find_element(*LocatorsForTest.password_input).send_keys(password_test)
              driver.find_element(*LocatorsForTest.password_repit_input).send_keys(password_test)
              driver.find_element(*LocatorsForTest.create_acc_button).click()

              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.email_input_err))
              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.password_input_err))
              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.password_repit_input_err))
              driver.quit()

       def test_exist_user_create(self, driver):
              driver.find_element(*LocatorsForTest.log_and_reg_button).click()
              driver.find_element(*LocatorsForTest.create_acc_button).click()
              driver.find_element(*LocatorsForTest.email_input).send_keys(ExistUser.email)
              driver.find_element(*LocatorsForTest.password_input).send_keys(ExistUser.password)
              driver.find_element(*LocatorsForTest.password_repit_input).send_keys(ExistUser.password)
              driver.find_element(*LocatorsForTest.create_acc_button).click()

              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.email_input_err))
              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.password_input_err))
              WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.password_repit_input_err))
              driver.quit()


