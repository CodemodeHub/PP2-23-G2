import os

os.chdir("/Users/ЯСЛАН/Документы/pp2")

print(os.getcwd())

for i in os.listdir(os.getcwd()):
    print(i)
    if os.path.isdir(i):
        print(f'<DIR> : {i}')
    if os.path.isfile(i):
        print(f'<FILE> : {i}')