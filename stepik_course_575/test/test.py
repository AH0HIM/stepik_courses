import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_answer(answer, link):
    browser = webdriver.Chrome()

    email = ''
    password = ''

    browser.get(link)
    time.sleep(5)

    current_url = str(browser.current_url)
    if 'promo' in current_url:
        browser.get(current_url + '?auth=login')
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[name = "login"]').send_keys(email)
        browser.find_element(By.CSS_SELECTOR, '[name = "password"]').send_keys(password)
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
        time.sleep(1)

    browser.get(link)
    time.sleep(5)
    right = browser.find_element(By.CSS_SELECTOR, 'div[data-type="string-quiz"]').get_attribute('data-state')
    if right == 'no_submission':
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    else:
        browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'footer[class="modal-popup__footer ember-view"] :first-child').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'button[class ="submit-submission"]').click()


link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    get_value = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(get_value))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(30)
