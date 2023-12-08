row = 4

for index in range(1,row+1):
    if index == 1 or index == row:
        print("*" * row)
    else:
        space = row - 2
        # print("*" , "x" * 2 , "*")
        print("*"," " * space, "*", sep="")