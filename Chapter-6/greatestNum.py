n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))

greatestNum_1 = 0
greatestNum_2 = 0
if n1 > n2: 
    greatestNum_1 = n1
else:
    greatestNum_1 = n2

if n3 > n4:
    greatestNum_2 = n3
else:
    greatestNum_2 = n4

if greatestNum_1 > greatestNum_2:
    print("largest no: ", greatestNum_1)
else:
    print("largest no: ", greatestNum_2)

