#4 2 6 36
# проверка на логарифм, если какое то является норм логарифмом: print"Гуд бай всем я домой"
# в противном случае, вывод sin(a), cos(b), tg(c), ctg(d)

import math
def check_for_log(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if math.log(l[i], l[j]) == int(math.log(l[i], l[j])) and i != j:
                return True
    return False

l = list(map(int, input().split()))
if check_for_log(l) == True:
    print("Poka")
else:
    print(f'{math.sin(l[0])}, {math.cos(l[1])}, {math.tan(l[2])}, {1/math.tan(l[3])}')
