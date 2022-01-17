from selenium import webdriver
from selenium.webdriver.common.by import By
from random import choice
import time
import string

link = "http://suninjuly.github.io/registration1.html"


def get_random_line(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])


with webdriver.Chrome() as browser:
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]")
    input_first_name.send_keys(get_random_line())

    input_last_name = browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]")
    input_last_name.send_keys(get_random_line())

    input_email = browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]")
    input_email.send_keys(get_random_line())

    # input_phone = browser.find_element(By.TAG_NAME, "input[placeholder='Input your phone:']")
    # input_phone.send_keys(get_random_line())
    # input_address = browser.find_element(By.TAG_NAME, "input[placeholder='Input your address:']")
    # input_address.send_keys(get_random_line())

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    time.sleep(2)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(2)