sno=int(input("Enter the student number"))
sname=input("Enter the name of the Student")
m1=int(input("Enter the marks of three subjects"))
m2=int(input("Enter the marks of three subjects"))
m3=int(input("Enter the marks of three subjects"))
total=m1+m2+m3
avg=(m1+m2+m3)/3
print("Student Details")
print(f"student no{sno}\n student name{sname}\n marks in three subjects{m1}{m2}{m3}\n total marks{total}\n average marks\n{avg}")