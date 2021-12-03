"""
Гипотеза Эйлера о сумме степеней
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая, что по крайней мере n
энных степеней необходимо для получения суммы, которая сама является энной степенью для n>2. Напишите программу для
опровержения гипотезы Эйлера (продержавшейся до 1967 года), и найдите четыре положительных целых числа, сумма 5-х
степеней которых равна 5-й степени другого положительного целого числа.

Таким образом, найдите пять натуральных чисел a,b,c,d,e удовлетворяющих условию:

В ответе укажите сумму a+b+c+d+e.

Примечание 1. Используйте вложенный цикл for.

Примечание 2. Считайте, что числа a,b,c,d,e не превосходят 150.

Примечание 3. Программа может работать дольше чем обычно. В зависимости от способа решения задачи на выполнение
программы может уходить до нескольких минут. Попробуйте сократить количество вложенных циклов.

https://stepik.org/lesson/298795/step/13?auth=login&unit=280622
"""
from datetime import datetime
start_time = datetime.now()

for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))