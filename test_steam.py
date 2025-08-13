from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import faker

faker = faker.Faker()
CURRENT_URL = 'https://store.steampowered.com/'
MAIN_TITLE = By.XPATH,"//*[@id='home_featured_and_recommended']"
WAIT = 10

SIGN_IN = By.XPATH, "(//*[contains(text(), 'login')])[1]"
INPUT_MAIL = By.XPATH, "(//input[contains(@type, 'text')])[1]"
INPUT_PASS = By.XPATH, "//input[contains(@type, 'password')]"
BTN_SIGN_IN = By.XPATH, "//button[contains(text(), 'Sign in')]"
ERR_MSG = By.XPATH, "//*[contains(text(), 'password and account')]"


def test_steam(browser: WebDriver):
    assert browser.current_url == CURRENT_URL
    assert browser.execute_script('return document.readyState;') == 'complete'
    wait = WebDriverWait(browser, WAIT)
    wait.until(EC.presence_of_element_located(MAIN_TITLE))
    sign_in = wait.until(EC.element_to_be_clickable(SIGN_IN))
    sign_in.click()
    assert browser.execute_script('return document.readyState;') == 'complete'
    input_mail = wait.until(EC.element_to_be_clickable(INPUT_MAIL))
    input_mail.clear()
    wait.until(EC.element_to_be_clickable(INPUT_MAIL))
    input_mail.send_keys(faker.email())
    input_pass = wait.until(EC.element_to_be_clickable(INPUT_PASS))
    input_pass.clear()
    wait.until(EC.element_to_be_clickable(INPUT_PASS))
    input_pass.send_keys(faker.password())
    btn_sign = wait.until(EC.element_to_be_clickable(BTN_SIGN_IN))
    btn_sign.click()
    assert wait.until(EC.text_to_be_present_in_element(ERR_MSG, 'password and account'))
