"""
Задание: переход на новую вкладку

В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и
решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа на это задание.

https://stepik.org/lesson/184253/step/6?unit=158843
"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

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
