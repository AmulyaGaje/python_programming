from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,l,b):
        print("Area of rectangle=",l*b)
class Circle(Shape):
    def area(self,r):
        print("Area of circle",3.14*r*r)
c1=Circle()
r1=Rectangle()
c1.area(5)
r1.area(3,4)
