import os
import os.path

with open('sample_ans.txt', 'w') as ans:
    for currentDir, dirs, files in os.walk('sample'):
        for file in files:
            file.replace('\\', '/')
            if file.endswith('.py'):
                ans.write(currentDir)
                ans.repa
                ans.write('\n')
                break