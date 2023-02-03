def histogram(l):
    ll = []
    for i in l:
        ll.append('*' * i)
    return ll
# l = list(map(int, input().split()))
# ll = histogram(l)
# print(*ll, sep = '\n')
print(*histogram(list(map(int, input().split()))), sep = '\n')