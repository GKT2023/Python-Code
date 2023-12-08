
row = 5
for i in range(1,row+1):
    leftspace = row - i
    if i ==1:
        # print(" " * leftspace , "*" )
        print(" " * ((row-i)+1) + "*" * (2*i - 1))
        # print(" " * (row-i) + "*" * (2*i - 1))

    elif i ==row:
        # print(" " * (row-i) + "*" * (2*i - 1))
        print("*" * (2*i - 1))
    else:
        midspace = abs((4 - (2 * i))-1) + 1
        print(" " * leftspace + "*"+ " " * midspace + "*")
