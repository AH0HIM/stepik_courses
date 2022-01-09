import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    line = re.sub(pattern, r'\1', line)
    print(line)