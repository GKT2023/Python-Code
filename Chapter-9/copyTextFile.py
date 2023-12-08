with open ('this.txt' ,'r') as f1, open('this_copy.txt','a') as f2:
    line = f1.read()
    f2.write(line)
    f2.write("\n")
    f2.write("this is a copy of this.txt")
