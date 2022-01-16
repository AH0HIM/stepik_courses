import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
with webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe") as browser:
    browser.get(link)

    for inp in browser.find_elements(By.CLASS_NAME, "form-control"):
        inp.send_keys("data")

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file_example.txt")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)