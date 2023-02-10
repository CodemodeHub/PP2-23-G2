import re

s = "Magzhan Amina Masdsan;s,a"

pattern = r'M.....n'
pattern2 = r'^M'
pattern3 = r'M.+n'

print(re.findall(pattern3, s))
