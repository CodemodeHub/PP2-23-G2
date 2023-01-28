l = list(map(int, input().split(';')))
for i in l:
    print(i, end = '.')
print()
for i in range(len(l)):
    print(l[i], end = '.')