import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    LINK = 'https://store.steampowered.com/'
    SCREEN_SIZE = 'window-size=1920x1080'
    MAXIMIZED_SCREEN_SIZE = '--start-maximized'
    options = Options()
    options.add_argument(SCREEN_SIZE)
    options.add_argument(MAXIMIZED_SCREEN_SIZE)
    driver = webdriver.Chrome(options=options)
    driver.get(LINK)
    yield driver
    driver.quit()
