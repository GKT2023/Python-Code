with open ('poems.txt','r') as f:
    data = f.read()
    if 'twinkle'  in data:
        print("poem contains twikle word")
    else:
        print("twinkle word is not present")
