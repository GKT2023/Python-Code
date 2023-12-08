for i in range (2,21):
    with open (f"tableOf{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(str(i*j))
            f.write("\n")