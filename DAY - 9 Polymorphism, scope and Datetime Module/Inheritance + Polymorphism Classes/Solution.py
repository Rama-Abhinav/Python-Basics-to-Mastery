class Shape:
    def area(self):
        pass

class rectangle(Shape):
    def __init__(self,Length,Breadth):
        self.Length = Length
        self.Breadth = Breadth
    def area(self):
        return f"Area of Rectangle = {self.Length * self.Breadth}"

class circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return f"Area of circle = {3.14 * (self.radius**2)}"

class triangle(Shape):
    def __init__(self,Height, base):
        self.Height = Height
        self.base = base

    def area(self):
        return f"Area of Triangle = {0.5 * (self.base * self.Height)}"
    
class sqaure(Shape):
    def __init__(self,Length):
        self.Length = Length

    def area(self):
        return f"Area of Square = {self.Length**2}"

def shape_area(shape_list):
    for shape_name in shape_list:
        print(shape_name.area())  

User = (input("Enter the list of shapes whose area you would like to compute seperated by spaces: ").lower().strip()).split()

shapelist = []

for shape in User:
    if shape == "rectangle":
        print ("Enter the dimensions of the rectangel whose area is to be calculated ?")
        length = input("Enter Length of Rectangle: ")
        breadth = input("Enter Breadth of Rectangle: ")
        shapelist.append(rectangle(float(length) , float(breadth)))

    elif shape == "circle":
        print ("Enter the radius of the circle whose area is to be calculated ?")
        Radius = input("Enter Radius of Circle: ")
        shapelist.append(circle(float(Radius)))

    elif shape == "triangle":
        print ("Enter the dimension of the triangle whose area is to be calculated ?")
        height = input("Enter Height of Triangle: ")
        Base_Len = input("Enter Base Length of Triangle: ")
        shapelist.append(triangle(float(height),float(Base_Len)))

    elif shape == "square":
        print ("Enter the side of the square whose area is to be calculated ?")
        Side_Len = input("Enter Length of Side of Sqaure: ")
        shapelist.append(sqaure(float(Side_Len)))

    else:
        print(f"invalid shape : {shape}")


    
shape_area(shapelist)