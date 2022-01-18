"""
Задание: составные сообщения об ошибках и поиск подстроки

Иногда при работе с текстами не нужны жёсткие проверки на полное совпадение, и требуется проверить, что некий текст является подстрокой другого текста. Это можно сделать либо с помощью ключевого слова in, либо с помощью функции find:

 s = 'My Name is Julia'

 if 'Name' in s:
    print('Substring found')

 index = s.find('Name')
 if index != -1:
     print(f'Substring found at index {index}')
Попробуйте запустить этот код в интерпретаторе, чтобы понять разницу в подходах.

Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена. Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.

Например, для проверки того, что в текущем url содержится строка login:

assert "login" in browser.current_url, # сообщение об ошибке
Реализуйте подобную проверку самостоятельно.

Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.

Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, в случае
несовпадения, предоставить исчерпывающее сообщение об ошибке.

Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!

Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных введенных
значениях, проверьте вывод вашей функции на разных парах. Обрабатывать ситуацию с пустым или невалидным вводом не нужно.

https://stepik.org/lesson/36285/step/9?unit=162401
"""


def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"

