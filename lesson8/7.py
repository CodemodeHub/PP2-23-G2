# создать папки, имена которых все прайм числа [x,y].
# x,y - input from console
import os

def prime_in_range(x,y):
    l = []
    for i in range(x,y + 1):
        if i != 0 and i != 1:
            check = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    check = False
            if check == True:
                l.append(i)
    return l

x,y = map(int, input().split())
for i in prime_in_range(x,y):
    os.mkdir(f'./{i}')



            


