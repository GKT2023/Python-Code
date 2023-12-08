s = set()
s.add(20)
s.add(20.0)
s.add("20")

for i in s:
    print(type(i))

print(len(s))