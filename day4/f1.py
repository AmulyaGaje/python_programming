class Student:
    name=""
    roll_no=""
    marks=0
    def display(self,name,rno,m):
        print("Name of the Student is",name)
        print("Roll no of the student is",rno)
        print("MarksScored",m)
s1=Student()
s2=Student()
s1.display("abc",35,77)
s2.display("amulya","y7",99)