import os
import os.path

with open('answer.txt', 'w') as answer:
    for currentDir, dirs, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                answer.write(currentDir)
                answer.write('\n')
                break