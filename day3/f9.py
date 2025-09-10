
# A school stores student records as tuples in the format (roll_no, name, marks).
# Write a Python program to:
# Store the data of 5 students in a list of tuples.
# Print the name of the student who scored the highest marks.
# Print all students who scored more than 75 marks
li=[]
n=int(input("Enter the number of students"))
for i in range(n):
    name=input("ENTER NAME ")
    rno=int(input("Enter th roll no"))
    marks=int(input("Enter the marks"))
    li.append((name,rno,marks))
def Highest(li):
    for i in li:
        if(i[2]>75):
            print(i[0])
Highest(li)
def Largest(li):
    big=-1
    stu=None
    for i in li:
        if i[2]>big:
            big=i[2]
            stu=i[0]
    print(stu,"Highest score")
Largest(li)