import pytest
from  selenium import webdriver
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://store.steampowered.com/')
    yield driver
    driver.quit()

