import re

with open('1.txt','r', encoding = 'utf8') as f:
    x = f.read()
# print(x)
pattern = r'\bf\w*\d\w*'
pattern2 = r'\w*[%]\w*x\Z'
pattern3 = r'\b[a-z]\w*'
pattern3 = r'\b[az]\w*'

print(re.findall(pattern3, x))
