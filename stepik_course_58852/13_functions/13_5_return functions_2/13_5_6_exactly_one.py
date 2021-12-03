"""
Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

Примечание. Следующий программный код:
print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))

должен выводить:
True
True
False
False
https://stepik.org/lesson/334150/step/6?unit=317559
"""


def is_one_away(word1, word2):
    return len(word1) == len(word2) and len([i for i in range(len(word1)) if word1[i] != word2[i]]) == 1


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))