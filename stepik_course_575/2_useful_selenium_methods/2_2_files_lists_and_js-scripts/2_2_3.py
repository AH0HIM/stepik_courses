"""
Задание: работа с выпадающим списком

Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он
справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа для этого задания.



Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для
нее тоже должен пройти успешно.

Подсказка: если вы получаете ошибку в духе "argument of type 'int' is not iterable", перепроверьте тип переменной,
которую вы передаете в функцию поиска. Нужно передать строку!

https://stepik.org/lesson/228249/step/3?unit=200781
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(num1) + int(num2)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(5)
