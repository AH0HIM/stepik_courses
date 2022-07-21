with open('data.txt', 'r', encoding='utf-8') as f:
    value = f.readlines()
    print(*value, sep='\n')
