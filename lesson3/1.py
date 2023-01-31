def sum(a,b):
    return a + b

def sum2(a,b):
    print(a + b)

def sum_of_list(*l):
    sum = 0
    # for i in range(len(l)):
    #     sum += l[i]

    for x in l:
        sum += x
    return sum

def sum3(l):
    sum = 0
    # for i in range(len(l)):
    #     sum += l[i]

    for x in l:
        sum += x
    return sum

print(sum(5,3))
sum2(5,6)
print(sum_of_list(1,2,3,4,52))
print(sum3([1,2,3]))