l = [1,2,3,4,56]
l2 = (1,2,3)
func = lambda x : x % 2 == 0
print(tuple(map(lambda x: x ** 2, l2)))
print(list(map(func, l2)))
print(list(filter(lambda x : x % 2 == 1, l)))
