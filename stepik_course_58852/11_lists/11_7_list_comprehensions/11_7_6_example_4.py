"""
Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов
от 100 до 1000.

https://stepik.org/lesson/326725/step/6?unit=310010
"""
palindromes = [i for i in range(100, 1001) if i // 100 == i % 10]

print(palindromes)
