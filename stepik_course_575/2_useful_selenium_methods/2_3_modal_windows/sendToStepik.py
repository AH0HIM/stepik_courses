import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def sendToStepik(task_link, answer):
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(task_link)
    browser.implicitly_wait(4)

    element = browser.find_element(By.CSS_SELECTOR, 'attempt-main.ember-view')
    element.location_once_scrolled_into_view
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(answer)
    print('answer = ', answer)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    time.sleep(20)
