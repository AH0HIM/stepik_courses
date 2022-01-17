"""
Задание: принимаем alert

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа на это задание.

https://stepik.org/lesson/184253/step/4?unit=158843
"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from sendToStepik import sendToStepik

link = "http://suninjuly.github.io/alert_accept.html"
task_link = "https://stepik.org/lesson/184253/step/4?unit=158843"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()

    get_value = browser.find_element(By.ID, "input_value").text

    browser.find_element(By.NAME, "text").send_keys(calc(get_value))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(5)
    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # alert.accept()
    # answer = alert_text.split(': ')[-1]
    # print(answer)
    # time.sleep(2)
    # sendToStepik(task_link, answer)
