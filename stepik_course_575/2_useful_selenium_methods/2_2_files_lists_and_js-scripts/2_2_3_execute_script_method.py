import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing'; alert('Robot at work')")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("window.scrollBy(0, 100);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

    time.sleep(5)
