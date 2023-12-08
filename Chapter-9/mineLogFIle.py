with open('log.txt') as f:
    data = f.read()

if 'Python' in data:
    print("python is present")
else:
    print("python is not present")