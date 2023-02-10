import json

f = open('a.json')
d = json.load(f)
print(type(d))
d["age"] = 18
print(d)