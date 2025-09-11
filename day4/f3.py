class Employee:
    def __init__(self,name):
        self.name=name
    def display(self,salary):
        print("Name=",self.name)
        print("sALARY",salary)
class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
    def display(self,salary,dept):
       super().display(salary)
       print("Department",dept)

e1=Employee("amulya")
m1=Manager("abc")
e1.display(50000)
m1.display(70000,"Finance")