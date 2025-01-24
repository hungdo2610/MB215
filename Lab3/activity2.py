#ask users for grade output 
nGrade = float(int(input("Enter your grade: ")))
#convert grade into letter grade
if nGrade >= 90:
    nGrade = "A+"
    print('Your grade is: ', nGrade)
elif nGrade >= 80 and nGrade <= 89:
    nGrade = "A"
    print('Your grade is: ', nGrade)
elif nGrade >= 70 and nGrade <= 79:
    nGrade = "B"
    print('Your grade is: ', nGrade)
elif nGrade >= 60 and nGrade <= 69:
    nGrade = "C"
    print('Your grade is: ', nGrade)
elif nGrade >= 50 and nGrade <= 59:
    nGrade = "D"
    print('Your grade is: ', nGrade)
else: 
    nGrade = "F"
    print('Your grade is: ', nGrade)
