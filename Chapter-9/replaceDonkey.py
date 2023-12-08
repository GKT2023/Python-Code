with open('donkey.txt','r') as f:
    data = f.read()
    if 'donkey' in data:
        data = data.replace('donkey', "#####")
print(data)

with open('donkey.txt','w') as f:
    f.write(data)