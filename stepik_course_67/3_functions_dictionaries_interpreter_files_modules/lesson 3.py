"""
3.1 Функции
"""
import os.path

"""

def min2(a, b):  # def, имя функции, аргумент(параметры)
    if a <= b:  # тело функции, return
        return a
    else:
        return b
"""

"""
Вызов функции

# минимум из чисел 42, 30

m = min2(42, 30)

# минимум из чисел 42, 30, 25

m = min2(min2(42, 30), 25)

- Функция должна быть объявлена ранее первого вызова; 

Различные функции

- Без возвращаемого значения;
- Без параметов;
- Произвольное число параметров; $
- Параметры со значениями по умолчанию;
"""

"""
def min(*a):  # произвольное количество аргументов
    m = a[0]
    for x in a:
        if m > x:
            m = x
        return m

"""
"""
Значение параметров по умолчанию 

"""
"""

def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
        return res

"""
"""
Локальные переменные
- переменные объявленные внутри функции недоступны;

"""
"""ђ
def f():
    a = 1
    print(a)


a = 0
f()
print(a)

"""

"""
Глобальные переменные
- переменные объявленные внутри функции недоступны;

def f():
    print(a)


a = 1
f()

# начало куска кода, который можно копировать из программы в программу
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# конец куска кода

n = int(input())
f = factorial(n)
# дальше всякие действия с переменной f



"""
"""
Напишите функцию f(x), которая возвращает значение следующей функции, 
определённой на всей числовой прямой:

x = float(input())


def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    elif 2 < x:
        return (x - 2) ** 2 + 1
print(f(x))


def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            l.pop(i)


lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
"""

"""
Факториал числа

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(3))
"""

"""
def max(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max(max(a, b), c)


print(max3(3, 5, 4))


def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res
    

print(max(3, 5, 4))
"""

"""



# Рекурсия

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
"""

"""
Множество

s = set() # создание пустокого множества


basket = {'apple', 'orange', 'apple', 'pear'}

'orange' in basket = # true
'python' in basket = # false

# Операциис с множеством

s.add(element) - если такое есть, то ничего не изменится
s.remove(element) - удаляет, если нет такого - ошибка
s.discard(element) - удаляет без ошибки
s.clear() - все удаляет множиства
s.lean(s) - число елементов во множестве

List - Элементы в списке хранятся последовательно, каждому из них присвоены индексы, начиная с нуля.
Turple - Кортеж, неизменяемый и более быстрый аналог списка.
Set - Множество, набор уникальных элементов в случайном порядке (неупорядоченный список).
"""

"""
# Словари

Capitals = dict()   # создаем пустой словарь

Capitals['Russian'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Russian', 'France', 'USA', 'Russian']

for country in Countries:
    if country in Capitals:
        print('Столица страны' + country + ': ' + Capitals[country])
    else:
        print('В базе нет такой страны с названием' + country)

# Создание словаря

Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)

"""

"""
### Creating an empty dictionary ###

data = {}
# OR
data = dict()

### Creating a dictionary with initial values ###

data = {'a':1,'b':2,'c':3}
# OR
data = dict(a=1, b=2, c=3)

### Inserting/Updating a single value ###

data['a']=1  # Updates if 'a' exists, else adds 'a'
# OR
data.update({'a':1})
# OR
data.update(dict(a=1))
# OR
data.update(a=1)

### Inserting/Updating multiple values ###

data.update({'c':3,'d':4})  # Updates 'c' and adds 'd'

### Creating a merged dictionary without modifying originals

data3 = {}
data3.update(data)  # Modifies data3, not data
data3.update(data2)  # Modifies data3, not data2

### Deleting items in dictionary ###

del data[key]  # Removes specific element in a dictionary
data.pop(key)  # Removes the key & returns the value
data.clear()  # Clears entire dictionary


"""

"""
# 3.2 Словари 5 out of 7 steps passed


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key * 2 in d:
        d[key * 2] += [value]
    elif key not in d:
        d[key * 2] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)



Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, 
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке 
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное сло должно выводиться только один раз.

Sample Input 1:

a aa abC aa ac abc bcd a

"""

my_list = ["a", "aa", "abC", "aa", 'ac', 'abc', 'bcd', 'a']
"""
3.1 Функции
"""
"""

def min2(a, b):  # def, имя функции, аргумент(параметры)
    if a <= b:  # тело функции, return
        return a
    else:
        return b
"""

"""
Вызов функции

# минимум из чисел 42, 30

m = min2(42, 30)

# минимум из чисел 42, 30, 25

m = min2(min2(42, 30), 25)

- Функция должна быть объявлена ранее первого вызова; 

Различные функции

- Без возвращаемого значения;
- Без параметов;
- Произвольное число параметров; $
- Параметры со значениями по умолчанию;
"""

"""
def min(*a):  # произвольное количество аргументов
    m = a[0]
    for x in a:
        if m > x:
            m = x
        return m

"""
"""
Значение параметров по умолчанию 

"""
"""

def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
        return res

"""
"""
Локальные переменные
- переменные объявленные внутри функции недоступны;

"""
"""ђ
def f():
    a = 1
    print(a)


a = 0
f()
print(a)

"""

"""
Глобальные переменные
- переменные объявленные внутри функции недоступны;

def f():
    print(a)


a = 1
f()

# начало куска кода, который можно копировать из программы в программу
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# конец куска кода

n = int(input())
f = factorial(n)
# дальше всякие действия с переменной f



"""
"""
Напишите функцию f(x), которая возвращает значение следующей функции, 
определённой на всей числовой прямой:

x = float(input())


def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    elif 2 < x:
        return (x - 2) ** 2 + 1
print(f(x))


def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            l.pop(i)


lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
"""

"""
Факториал числа

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(3))
"""

"""
def max(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max(max(a, b), c)


print(max3(3, 5, 4))


def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res


print(max(3, 5, 4))
"""

"""



# Рекурсия

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
"""

"""
Множество

s = set() # создание пустокого множества


basket = {'apple', 'orange', 'apple', 'pear'}

'orange' in basket = # true
'python' in basket = # false

# Операциис с множеством

s.add(element) - если такое есть, то ничего не изменится
s.remove(element) - удаляет, если нет такого - ошибка
s.discard(element) - удаляет без ошибки
s.clear() - все удаляет множиства
s.lean(s) - число елементов во множестве

List - Элементы в списке хранятся последовательно, каждому из них присвоены индексы, начиная с нуля.
Turple - Кортеж, неизменяемый и более быстрый аналог списка.
Set - Множество, набор уникальных элементов в случайном порядке (неупорядоченный список).
"""

"""
# Словари

Capitals = dict()   # создаем пустой словарь

Capitals['Russian'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Russian', 'France', 'USA', 'Russian']

for country in Countries:
    if country in Capitals:
        print('Столица страны' + country + ': ' + Capitals[country])
    else:
        print('В базе нет такой страны с названием' + country)

# Создание словаря

Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)

"""

"""
### Creating an empty dictionary ###

data = {}
# OR
data = dict()

### Creating a dictionary with initial values ###

data = {'a':1,'b':2,'c':3}
# OR
data = dict(a=1, b=2, c=3)

### Inserting/Updating a single value ###

data['a']=1  # Updates if 'a' exists, else adds 'a'
# OR
data.update({'a':1})
# OR
data.update(dict(a=1))
# OR
data.update(a=1)

### Inserting/Updating multiple values ###

data.update({'c':3,'d':4})  # Updates 'c' and adds 'd'

### Creating a merged dictionary without modifying originals

data3 = {}
data3.update(data)  # Modifies data3, not data
data3.update(data2)  # Modifies data3, not data2

### Deleting items in dictionary ###

del data[key]  # Removes specific element in a dictionary
data.pop(key)  # Removes the key & returns the value
data.clear()  # Clears entire dictionary


"""

"""
# 3.2 Словари 5 out of 7 steps passed


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key * 2 in d:
        d[key * 2] += [value]
    elif key not in d:
        d[key * 2] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)



Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, 
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке 
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное сло должно выводиться только один раз.

Sample Input 1:

a aa abC aa ac abc bcd a

my_list = input().lower().split()
my_dict = {}

for element in my_list:
    if element in my_dict:
        my_dict[element] = my_list.count(element)
    else:
        my_dict[element] = my_list.count(element)

for key, value in my_dict.items():
    print(key, value)



cache = {}                              # кэш памяти браузера

def get_page(url):                      # поступает гет запрос от пользователя
    if cache.get(url):                  # если этот запрос поступал ранее
        return cache[url]               # то из кеша достаем инфо и выдаем пользователю
    else:                               # иначе
       data = get_data_from_server(url) # делаем запрос к базе данным и получаем инфо
       cache[url] = data                # полученное инфо также кладем в кеш в виде словаря
       return data                      # выдаем клиенту инфо, следующий раз при таком запросе
                                        # мы по ключу словаря запросу выдадим со словаря всю информацию




Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать. 
Далее считывает N строк с числами xi, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа xi программа должна на отдельной строке вывести значение f(x_i). 
Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x. 
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

5
5
12
9
20
12
Sample Output:

11
41
47
61


dict = {}                   # создаем пустой словарь
n = int(input())            # ввод

for i in range(n):          # в цикле вводим х столько раз, чему равно n, проверяя:
    x = int(input())        # если такой Х(ключ) уже есть в словаре, то просто выводим его из словаря;
    if x in dict:
        print(dict[x])
    else:                   # добавляем в наш словарь ключ Х со значением f(х) и выводим его
        dict[x] = f(x)
        print(dict[x])
"""

# string = 'a3b4c2e10b1'
# recode_digit = ''
# record_alpha = ''
#
# for element in string:
#     if element.isdigit():
#         recode_digit += element
#         if recode_digit < '10':
#             continue
#         else:
#             record_alpha += record_alpha[-1] * (int(recode_digit) - 1)
#             recode_digit = ''
#     else:
#         record_alpha += element
# print(record_alpha)

# os.path.join('.', 'dirname', 'filename.txt')
#
"""
------------------------------------------------------------------------------------------------------------------------
3.4 Файловый ввод/вывод 2 out of 4 steps 

На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной 
строки обратно. Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью 
кодирования повторов, и производит обратную операцию, получая исходный текст. Запишите полученный текст в файл и 
прикрепите его, как ответ на это задание.В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
------------------------------------------------------------------------------------------------------------------------

with open('/Users/ilyaikonnykov/Downloads/dataset_3363_2.txt') as file_in:
    for line in file_in:
        line = line.strip()

recode_digit = ''
record_alpha = ''
i = 0
for element in line:
    if element.isdigit():
        recode_digit += element
        if int(recode_digit) < 10:
            i += 1
            continue
        else:
            record_alpha += record_alpha[-1] * (int(recode_digit) - 1)
            recode_digit = ''
            i -= 1
    elif element.isalpha() and i == 1:
            i -= 1
            record_alpha += record_alpha[-1] * (int(recode_digit) - 1)
            record_alpha += element
            recode_digit = ''
    elif element.isalpha():
        record_alpha += element
        recode_digit = ''
if line[-1].isalpha():
    record_alpha += line[-1]
elif line[-1].isdigit():
    record_alpha += record_alpha[-1] * (int(recode_digit) - 1)

with open('/Users/ilyaikonnykov/Downloads/dataset_3363_2.txt', 'w') as file_ouf:
    file_ouf.write(record_alpha)
"""

"""
------------------------------------------------------------------------------------------------------------------------
3.4 Файловый ввод/вывод 3 out of 4 steps 

Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно 
смотреть, как, например, на наиболее часто используемые. Напишите программу, которая считывает текст из файла 
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, 
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое 
(можно использовать оператор < для строк).В качестве ответа укажите вывод программы, а не саму программу. Слова, 
написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3


dictionary = {}

with open('/Users/ilyaikonnykov/Downloads/dataset_3363_3.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.lower()
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 1
            elif word in dictionary:
                dictionary[word] += 1

max_quantity = 1
word_with_max_quantity = ""
for key, value in dictionary.items():
    current_quantity = dictionary[key]
    if current_quantity > max_quantity:
        max_quantity = current_quantity
        word_with_max_quantity = key

with open('/Users/ilyaikonnykov/Downloads/dataset_3363_3.txt', 'w') as out_f_obj:
    most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
    out_f_obj.write(most_popular)
    
    
# with open('/Users/ilyaikonnykov/Downloads/dataset_3363_3.txt', 'r') as file_in:
#     for line in file_in:
#         line = line.lower()
#         for word in line.split():
#             if word not in dict:
#                 dict[word] = 1
#             elif word in dict:
#                 dict[word] += 1
#
# dict = {}
# max_quantity = 1
#
# for key, value in dict.items():
#     current_quantity = dict[key]
#     if current_quantity > max_quantity:
#         max_quantity = current_quantity
#         word_with_max_quantity = key
#
# with open('/Users/ilyaikonnykov/Downloads/dataset_3363_3.txt', 'w') as file_ouf:
#     most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
#     file_ouf.write(most_popular)
"""
"""
# import  math
# print(2*math.pi*float(input()))
"""
"""
# import sys
# print(' '.*(sys.argv[1:]))
"""
"""
import requests

r = requests.get('http://example.com')  # простой GET запрос
print(r.text)  # вывод ответа от сервера

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)  # Передача параметров в запрос
print(r.url)  # Сформированный url-адрес с учётом параметров GET запроса



url='https://3.python-requests.org/user/quickstart/'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # отправка сформированых cookies на сервер
r.cookies
for cookie in r.cookies:    # использование cookies, полученных от сервера
    print('cookie domain = ' + cookie.domain)
    print('cookie name = ' + cookie.name)
    print('cookie value = ' + cookie.value)

"""

""" Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать 
число строк в нём. Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому 
параметру, чтобы убрать пробельные символы по краям). После получения файла вы можете проверить результат, обратившись 
к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества 
строк разбейте текст с помощью метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests

count = 0

with open('/Users/ilyaikonnykov/Downloads/dataset_3378_2.txt', 'r') as in_file:
    for line in in_file:
        line = line.strip()
        url = line

r = requests.get(url)
text = r.text.splitlines()

for i in range(len(text)):
    count += 1
print(count) """
