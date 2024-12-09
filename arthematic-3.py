class cal():
 def __init__(self,a,b):
    self.a=a
    self.b=b
 def add(self):
    return self.a+self.b
 def mul(self):
    return self.a*self.b
 def div(self):
    return self.a/self.b
 def sub(self):
    return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=None
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Add Result: ",obj.add())
    elif choice==2:
        print("Sub Result: ",obj.sub())
    elif choice==3:
        print("Mul Result: ",obj.mul())
    elif choice==4:
        print("Div Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")