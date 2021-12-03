"""
Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово
строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом
остаются строчными, а прописные – прописными.

Формат входных данных
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.

https://stepik.org/lesson/352860/step/4?unit=336821
"""
txt = input()


def encryption():
    lang = [chr(i) for i in range(97, 123)]
    result = ''.strip()
    for i in txt.split():
        count = 0
        for j in i:
            if j.isalpha():
                count += 1
        for k in i:
            if k in lang:
                result += lang[(lang.index(k) + count) % len(lang)]
            elif k.lower() in lang:
                result += lang[(lang.index(k.lower()) + count) % len(lang)].upper()
            else:
                result += k
        result += ' '

    return result


print(encryption())
