def isGreaterThan(x):
    return x >10

l = [2,5,7,8,12,15,50,80,9,7,4,100]

print(list(filter(isGreaterThan, l)))


print(list(filter(lambda x : x>20, l)))