def gen(a, b):
    for i in range(a,b + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a,b = map(int, input().split())
print(*gen(a, b))
