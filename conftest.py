import pytest
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://store.steampowered.com/')
    yield driver
    driver.quit()

