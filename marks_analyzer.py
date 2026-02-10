# Student Marks Analyzer with Grade

name = input("Enter student name: ")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
