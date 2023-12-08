from functools import reduce

li = [1,2,3,4]

def total(x,y):
    return x+y
print(reduce(total,li))