import re

text = "Real Madrid is the champion"
pattern = r'[a-zA-Z]+e\b'
print(re.match(pattern,text))