from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer').send_keys(calc(x_element))

    checkbox_robot = browser.find_element(By.ID, 'robotCheckbox').click()

    radio_robot = browser.find_element(By.ID, 'robotsRule').click()

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(5)
