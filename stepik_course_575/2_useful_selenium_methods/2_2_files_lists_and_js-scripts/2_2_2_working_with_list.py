import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe') as browser:
    browser.get(link)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1")
    # select.select_by_visible_text("text")
    # select.select_by_index(index)

    time.sleep(10)
