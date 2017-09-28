import sys
import re

for i in range(40):
    if i % 3 == 0:
        print(i, bin(i))

for input_line in sys.stdin:
    line = input_line.rstrip()
    new_line = re.sub(r'(\w)(\1)+', r'\1', line)
    print(new_line)
