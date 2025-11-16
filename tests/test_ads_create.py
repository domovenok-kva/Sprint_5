from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators.locatorstest import LocatorsForTest
from testuser.existtestuser import ExistUser


driver = webdriver.Chrome()
driver.get("https://qa-desk.stand.praktikum-services.ru/")

class TestAdaCreation:

    def test_create_ads_login(self, driver):
       
       name_product = "Сипулька"
       description = "Только что с конвеера. Возможна скидка"
       price = 5000


       driver.find_element(*LocatorsForTest.log_and_reg_button).click()
       driver.find_element(*LocatorsForTest.email_input).send_keys(ExistUser.email)
       driver.find_element(*LocatorsForTest.password_input).send_keys(ExistUser.password)
       driver.find_element(*LocatorsForTest.login_button).click()
       WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsForTest.place_an_ad_button)).click()

       driver.find_element(*LocatorsForTest.product_name_input).send_keys(name_product)
       driver.find_element(*LocatorsForTest.product_description_input).send_keys(description)
       driver.find_element(*LocatorsForTest.price_input).send_keys(price)

       driver.find_element(*LocatorsForTest.product_category_dropdown).click()
       driver.find_element(*LocatorsForTest.product_category_dropdown_choose).click()
       driver.find_element(*LocatorsForTest.city_select_dropdown).click()
       driver.find_element(*LocatorsForTest.city_select_dropdown_choose).click()

       driver.find_element(*LocatorsForTest.product_condition_used_radiobutton).click()
       driver.find_element(*LocatorsForTest.publish_button).click()
       assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.user_ad_exist)).get_attribute(name_product)

       driver.quit()
          

    def test_create_ads_not_login(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LocatorsForTest.place_an_ad_button)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.message_window)).text == "Чтобы разместить объявление, авторизуйтесь"
        driver.quit()



       