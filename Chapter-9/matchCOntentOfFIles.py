with open('this.txt', 'r') as f1, open('this_copy.txt' ,'r') as f2:
    line1 = f1.read()
    line2 = f2.read()

if line1 == line2:
    print("Yes, files are identical")
else:
    print("files are not identical")