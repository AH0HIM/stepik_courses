"""
Дополните приведенный код, используя списочный метод extend(), чтобы список list1 имел вид:

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
Подсписок для расширения  sub_list = ['h', 'i', 'j'].

https://stepik.org/lesson/416752/step/13?unit=406260
"""
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']


list1[2][1][2].extend(sub_list)

print(list1)
