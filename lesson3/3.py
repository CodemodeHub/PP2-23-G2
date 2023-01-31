def gen(a):
    n = 0
    while n <= a:
        yield n ** 2
        n += 1

print(*gen(int(input())))