def sum_resursive(n):
    if n == 0: 
        return 0
    return n + sum_resursive(n-1)


print(sum_resursive(4))