"""
Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк
исходного списка.

https://stepik.org/lesson/326725/step/4?unit=310010
"""
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(i) for i in keywords]

print(lengths)