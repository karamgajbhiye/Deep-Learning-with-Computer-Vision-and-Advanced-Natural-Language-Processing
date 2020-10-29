'''1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.'''

class triangle:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

class area(triangle):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_triangle_area(self):
        s = (self.a + self.b + self.c) / 2
        result = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return result

a = input("a = ")
b = input("b = ")
c = input("c = ")

T = area(a,b,c)
print('Area of the triangle : ', T.get_triangle_area())


