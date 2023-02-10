import json

d = {
    "Aidana" : 7832433,
    "Magzhan" : 4387324798,
    "Yaslan" : 329347234
}
x = json.dumps(d)
f = open('c.json','w')
f.write(x)
f.close()