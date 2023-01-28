l = [1,"dsoinjc", True,23213.2312]
# for i in range(len(l)):
#     print(l[i])
# for i in range(1, len(l), 2):
#     print(l[i])
for i in range(len(l) - 1, -1, -1):
    print(l[i])
l.reverse()
print(l)