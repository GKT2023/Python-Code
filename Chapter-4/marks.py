marks = []

for i in range(0,6):
    score = int(input("please enter the marks: "))
    marks.append(score)
print("marks of 6 students are: ", marks)
marks.sort()
print("marks in the sorted form: ", marks)