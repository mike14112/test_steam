from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import faker

faker = faker.Faker()
CURRENT_URL = 'https://store.steampowered.com/'
MAIN_TITLE = By.XPATH,"//*[contains(@id, 'logo_holder')]//img[contains(@alt, 'Steam')]"
LOGIN_URL = 'https://store.steampowered.com/login/?redir=&redir_ssl=1'
SIGN_IN = By.XPATH, "(//*[contains(text(), 'login')])[1]"
INPUT_MAIL = By.XPATH, "(//input[contains(@type, 'text')])[1]"
INPUT_PASS = By.XPATH, "//input[contains(@type, 'password')]"
BTN_SIGN_IN = By.XPATH, "//button[contains(text(), 'Sign in')]"
ERR_MSG = By.XPATH, "//*[@data-featuretarget='login']//div[5]"


def test_steam(browser: WebDriver):
    browser.set_window_size(1920, 1080)
    assert browser.current_url == CURRENT_URL
    assert browser.execute_script('return document.readyState;') == 'complete'
    wait = WebDriverWait(browser, 10)
    assert wait.until(EC.presence_of_element_located(MAIN_TITLE))
    sign_in = wait.until(EC.element_to_be_clickable(SIGN_IN))
    sign_in.click()
    assert wait.until(EC.url_to_be(LOGIN_URL))
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
    wait.until(EC.visibility_of_element_located(ERR_MSG))
