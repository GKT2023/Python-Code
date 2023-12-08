with open ('this_copy.txt', 'r+') as f:
    data = f.read()
    print("Before content", data)
    f.seek(0)
    f.truncate()
    data = f.read()
    print("after content",data)