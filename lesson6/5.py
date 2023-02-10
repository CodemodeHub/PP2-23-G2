import json

d = {
    'name' : 'Magzhan',
    'surname': 'Akhmadi',
    'age': 18,
    'subjects': ['pp2','stata','calc2','global','physics']
}
x = json.dumps(d)
print(x)
print(type(x))