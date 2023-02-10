import json

f = open('c.json')
d = json.load(f)
sum = 0
for i in d.values():
    sum += i
d["total salary"] = sum
with open('c.json', 'w') as f:
    json.dump(d,f)