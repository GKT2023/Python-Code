row = 3
for i in range(row,0,-1):
    print("*" * i)


for i in reversed(range(row+1)):
    print("*" * i)

def lowerLeftTriangle(row):
    for i in range(1,row+1):
        print("*" * ((row+1)-i))

lowerLeftTriangle(int(input('enter no of rows: ')))


