import re

with open('1.txt', 'r', encoding = 'utf8') as f:
    x = f.read()

pattern = r'world$'
if re.search(pattern, x):
    print("Yes")
else: 
    print("No")