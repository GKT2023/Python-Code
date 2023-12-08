maths_marks = int(input("ENter your marks in maths: "))
english_marks = int(input("ENter your marks in english: "))
science_marks = int(input("ENter your marks in science: "))

print("maths marks: " , maths_marks)
print("science marks: ", science_marks)
print("english marks: ",english_marks)

if maths_marks > 33 and english_marks > 33 and science_marks > 33:
    print("your marks in each subject is greated than 33.")
    total_marks = ((maths_marks + science_marks + english_marks)/300) *100
    print("total marks: ", total_marks)
    if total_marks > 40:
        print("YOu are pass!!")
    else: 
        print("you are fail")
else:
    print("you are fail")