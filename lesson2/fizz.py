num = int(input())
for i in range(1,num + 1):
    if i % 3 == 0 and i % 5 == 0:
        if i == num:
            print(" fizzbuzz", end = '.')
        else:    
            print(" fizzbuzz", end = ',')
    elif i % 3 == 0:
        if i == num: 
            print(' ' * 4, end = '')
            print(" fizz",end = '.')
        else:
            print(' ' * 4, end = '')
            print(" fizz",end = ',')
    elif i % 5 == 0:
        if i == num:
            print(' ' * 4, end = '')
            print(" buzz",end = '.')
        else:
            print(' ' * 4, end = '')
            print(" buzz",end = ',')
    else:
        if i == num:
            print(' ' * (9 - len(str(i))), end = '')
            print(i,end = '.')    
        else:
            print(' ' * (9 - len(str(i))), end = '')
            print(i,end = ',')
    if i % 10 == 0:
        print()
    