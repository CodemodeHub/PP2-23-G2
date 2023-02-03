l = list(map(int, input().split()))
print(sorted(l, key = lambda x: x % 3, reverse = True))
l.sort(key = lambda x: x % 3, reverse = True)
print(l)
