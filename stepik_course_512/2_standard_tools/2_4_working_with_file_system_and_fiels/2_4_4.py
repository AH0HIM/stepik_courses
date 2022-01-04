lines = open('dataset_24465_4.txt').readlines()
with open('output.txt', 'w') as out:
    out.writelines(reversed(lines))
