s, a, b = input(), input(), input()
count = 0

while count < 999:
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        print(count)
        break
else:
    print('Impossible')