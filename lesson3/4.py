def prime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def gen(a):
    for i in range(a + 1):
        if prime(i):
            yield i

print(*gen(int(input())))
