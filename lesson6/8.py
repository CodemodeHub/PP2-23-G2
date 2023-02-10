import json

with open('a.json','r') as f:
    x = f.read()
# print(x)

d = json.loads(x)
print(type(d))
print(*d.keys())
print(*d.values(), sep = '\n')
