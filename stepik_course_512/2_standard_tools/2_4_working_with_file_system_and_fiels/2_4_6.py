import os

os.chdir('C:\\main')

with open('2_4_6.txt', 'w') as out:
    for currentDir, dirs, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                out.write(currentDir)
                out.write('\n')
                break