import re

s = "kjdscnsdadcnipavpnr Magzhan iudeipnMagzhanprieuvnrpnr"

pattern = r'Magzhan'

match = re.search(pattern, s)
if match:
    print("Found", match.group())
else:
    print("Not found")