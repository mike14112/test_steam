import faker
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

faker = faker.Faker()
MAIN_ELEM = (By.ID, "home_featured_and_recommended")
LOGIN_ELEM = (By.XPATH, "//*[contains(@class, 'headline')]")
WAIT = 10
SIGN_IN = (By.XPATH, "(//*[contains(text(), 'login')])[1]")
INPUT_MAIL = (By.XPATH, "(//input[contains(@type, 'text')])[1]")
INPUT_PASS = (By.XPATH, "//input[contains(@type, 'password')]")
BTN_SIGN_IN = (By.XPATH, "//button[contains(text(), 'Sign in')]")
FORM_ERR = (By.XPATH, "(//form//div)[13]")
EXPECTED = 'password and account'
actual = ''


def test_steam(browser: WebDriver):
    wait = WebDriverWait(browser, WAIT)
    wait.until(EC.visibility_of_element_located(MAIN_ELEM)).is_displayed()
    sign_in = wait.until(EC.element_to_be_clickable(SIGN_IN))
    sign_in.click()
    wait.until(EC.visibility_of_element_located(LOGIN_ELEM)).is_displayed()
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
    try:
        err_text = WebDriverWait(browser, 10).until(
            lambda b: b.find_element(*FORM_ERR).text.replace("\xa0", " ").strip()
        )
        print("Ошибка появилась:", err_text)
        assert EXPECTED in err_text.lower()
    except TimeoutException:
        print("Ошибка так и не появилась")
