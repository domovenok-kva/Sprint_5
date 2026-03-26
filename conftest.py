import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()
