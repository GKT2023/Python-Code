li = ['donkey','monkey','cat', 'lion']

with open ('donkey.txt', 'r') as f:
    data = f.read()
for i in li:
    data = data.replace(i,"*%$^")

with open('donkey.txt','w') as f:
    f.write(data)
