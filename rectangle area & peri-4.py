class Rectangle:
 def __init__(self,l,b):
    self.l = l
    self.b = b
 def area(self):
    return self.l * self.b
 def peri(self):
    return 2 *(self.l + self.b)
 def display(self):
    print("Area of Rectangle = %.2f" %(self.area()))
    print("Perimeter of Rectangle = %.2f" %(self.peri()))

length = eval(input("Enter Length ="))
breadth = eval(input("Enter Breadth ="))
c2 = Rectangle(length, breadth)
print("Given Object Data")
print("Length = ",c2.l)
print("Breadth = ",c2.b)
print("--------------------------")
c2.display()
print("--------------------------")