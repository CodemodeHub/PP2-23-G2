import re

s = "Today Magzhan is online"

pattern = r'[a-zA-C]' #найдет все символы от a-z и A-C
pattern2 = r"[a-zA-Z]+"
s2 = re.sub("Magzhan", "Amina", s)
print(s2)

print(re.findall(pattern, s))
print(re.findall(pattern2, s))
print(re.match(pattern2,s))