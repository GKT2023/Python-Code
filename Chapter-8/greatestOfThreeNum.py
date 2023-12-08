def gretestNum(n1,n2,n3):
    largestNum = 0
    if n1 > n2:
        largestNum = n1
    else:
        largestNum = n2

    if largestNum < n3:
        largestNum = n3

    return largestNum


print(gretestNum(51,400,8))
