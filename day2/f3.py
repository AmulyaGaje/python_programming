sno=int(input("Enter the student number"))
sname=input("Enter the name of the Student")
m1=int(input("Enter the marks of three subjects"))
m2=int(input("Enter the marks of three subjects"))
m3=int(input("Enter the marks of three subjects"))
total=m1+m2+m3
avg=(m1+m2+m3)/3
print("Student Details")
print(f"student no{sno}\n student name{sname}\n marks in three subjects{m1}{m2}{m3}\n total marks{total}\n average marks\n{avg}")
def grade(x,y,z):
    if(x>=40 and y>=40 and z>=40):
        print("Pass")
        avg=(x+y+z)/3
        if(avg>80):
            print("Distinction")
        elif(avg>70 and avg<=80):
            print("A")
        elif(avg>50 and avg<=70):
            print("B")
        elif(avg<50):
            print("C")
    else:
        print("Fail")
print("Grade is ",grade(m1,m2,m3))