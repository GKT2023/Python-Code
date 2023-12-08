
## normal factorial 

def fact_inter(n):
    product = 1
    for i in range(0,n):
        product *= (i+1)
    return product

print(fact_inter(5))


## recursive factorial

def fact_recursive(n):
    if n ==1 or n ==0:
        return 1
    return n * fact_recursive(n-1)

print(fact_recursive(5))
