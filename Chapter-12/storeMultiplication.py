n = int(input("Enter a number: "))

print([(n*i) for i in range(1,11)])

with open ('Tables.txt', 'a') as f1:
    f1.write(str([(n*i) for i in range(1,11)]))