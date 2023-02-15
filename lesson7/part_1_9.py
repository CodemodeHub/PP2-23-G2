import re

with open('1.txt', 'r') as f:
    x = f.read()

pattern = r'^a.*z$'
if re.search(pattern,x):
    print("Yes")
else: 
    print("No")
