from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.driver import *
def test_login(chrome_browser):
    url = "https://elmir.ua"

    chrome_browser.get(url)

    text_element = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Войти"]'))
    )
    text_element.click()

    modal_window = WebDriverWait(chrome_browser, 10).until(
        EC.visibility_of_element_located((By.ID, "mw-lf"))
    )

    login_field = modal_window.find_element(By.ID, "lf-login")
    login_field.send_keys("deremin06@gmail.com")

    password_field = modal_window.find_element(By.ID, "lf-password")
    password_field.send_keys("2e68GBkQwqcaTde")

    submit_button = modal_window.find_element(By.CLASS_NAME, "mw-submit")
    submit_button.click()
