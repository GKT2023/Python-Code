a = 30
b = int(input("enter a number: "))

try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("Infinite loop, ", e)

finally:
    print("done")