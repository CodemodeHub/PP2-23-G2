# print(list(map(lambda x : x ** 2, list(map(int, input().split())))))
l = list(map(int, input().split()))
func = lambda x : x ** 2
l2 = list(map(func, l))
print(l2)