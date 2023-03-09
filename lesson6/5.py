import json
# json.dump() is used to write the JSON data directly to a file-like object.
# It takes two arguments: the Python object you want to convert to JSON, and the file-like object you want to write the JSON data to.

# json.dumps() on the other hand, is used to convert a 
# Python object to a JSON formatted string. 

# json.load() is used to load JSON data from a file-like object. 

# json.loads() on the other hand, is used to load a JSON formatted string into a Python object. 
# It takes one argument: the JSON formatted string you want to load.
d = {
    'name' : 'Magzhan',
    'surname': 'Akhmadi',
    'age': 18,
    'subjects': ['pp2','stata','calc2','global','physics']
}
x = json.dumps(d)
print(x)
print(type(x))