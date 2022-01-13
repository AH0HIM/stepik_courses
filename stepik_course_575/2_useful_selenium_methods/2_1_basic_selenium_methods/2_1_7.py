from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    get_treasure = browser.find_element(By.ID, "treasure").get_attribute('valuex')
    input_answer = browser.find_element(By.ID, 'answer').send_keys(calc(get_treasure))

    for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
        browser.find_element(By.CSS_SELECTOR, selector).click()

    time.sleep(5)
