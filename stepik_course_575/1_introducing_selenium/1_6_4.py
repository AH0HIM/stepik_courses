"""
Задание: поиск элементов с помощью Selenium

Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения для поиска вместо слов value1, value2 и т.д. Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.

Создайте файл lesson6_step4.py (обратите внимание на расширение .py) и вставьте туда шаблон кода. Подберите селекторы и запустите из командной строки, так же, как в уроке 2:

python lesson6_step4.py

https://stepik.org/lesson/138920/step/4?unit=196194
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
values = {
    "first_name": "Ilya",
    "last_name": "Ikonnikov",
    "city": "Kyiv",
    "country": "Ukraine"
}

with webdriver.Chrome() as browser:
    browser.get(link)

    input_first_name = browser.find_element(By.TAG_NAME, "input[name='first_name']")
    input_first_name.send_keys(f"{values['first_name']}")

    input_last_name = browser.find_element(By.NAME, "last_name")
    input_last_name.send_keys(f"{values['last_name']}")

    input_city = browser.find_element(By.CLASS_NAME, "city")
    input_city.send_keys(f"{values['city']}")

    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys(f"{values['country']}")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)

    browser.quit()
