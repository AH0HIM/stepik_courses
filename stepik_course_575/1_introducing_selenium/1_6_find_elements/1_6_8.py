"""
Задание: поиск элемента по XPath
На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в
нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать в
коде именно на неё.

Ваши шаги:

В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать
как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
Запустите ваш код.
Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве ответа
на это задание.

https://stepik.org/lesson/138920/step/8?unit=196194
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import choice
import time
import string

url = "http://suninjuly.github.io/find_xpath_form"
values = [1, 2, 3, 4]

with webdriver.Chrome() as browser:
    browser.get(url)

    elements = browser.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys('test')

    button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    time.sleep(3)
