from functools import reduce 

li = [3,4,56,9,8,76]

val = reduce(lambda x,y : max(x,y),li)
print(val)