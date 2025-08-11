from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import faker

faker = faker.Faker()

def test_steam(browser: WebDriver):
   browser.get('https://store.steampowered.com/')
   browser.maximize_window()
   assert browser.title == 'Welcome to Steam', 'Миша сайт на Русском'
   wait = WebDriverWait(browser, 10)
   sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'login')]")))
   sign_in.click()
   input_mail = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type, 'text')])[1]")))
   input_mail.clear()
   input_mail.send_keys(faker.email())
   input_pass = browser.find_element(By.XPATH, "//input[contains(@type, 'password')]")
   input_pass.clear()
   input_pass.send_keys(faker.password())
   btn_sign = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
   btn_sign.click()
   assert\
      wait.until(EC.visibility_of_element_located((By.XPATH,
                                                       "//*[contains(text(), 'Please check your password')]")))