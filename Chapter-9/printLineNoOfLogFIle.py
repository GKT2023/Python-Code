content = True
i = 1

with open ('log.txt') as f:
    while content:
        content = f.readline()
        if 'Python' in content:
            print(f"yes python is present on line no {i}")

        i += 1