def func(name = "Yaslan"):
    return ("my name is " + name)

print(func("Alua"))
print(func())

def printing(**full_name):
    print( full_name["name"] + "'s surname is " + full_name["sur"])

printing(name = "Magzhan", sur = "Akhmadi")