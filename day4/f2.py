class Student:
    def __init__(self,name,marks): 
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.marks)
s1=Student("abc",67)
s2=Student("mnj",99)
s1.display()
s2.display()
