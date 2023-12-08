try:
    with open('1.txt') as f1, open('2.txt') as f2, open('3.txt') as f3:
        print("inside try statement")
        print('{f1} exists')
        print('{f2} exists')
        print('{f3} exists')
except Exception as e:
    print(e)
finally:
    print("Program executed")