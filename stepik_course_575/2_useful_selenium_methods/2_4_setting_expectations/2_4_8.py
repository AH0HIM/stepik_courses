from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/wait2.html"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)

    browser.get(link)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    ).click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
