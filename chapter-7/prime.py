n = int(input("enter a number: "))

prime = False
if n == 1:
    print("not a prime no.")
elif n > 1:
    for i in range(2,n):
        if n % i == 0:
            prime = True
            break


if prime == True:
    print("not a prime number")
else:
    print("no is prime")