n=[]
def dis():
    return n
choice=1
while choice!=0:
    print("0.Exit")
    print("1.Add")
    print("2.Delete")
    print("3.Insert")
    print("4.Display")
    print("5.POP")
    choice=int(input("Enter choice: "))
    if choice==1:
        a =int(input("Enter Element to append: ")) 
        n.append(a)
        print("List: ",dis())
    elif choice==2:
        if n == []:
            print("No elements in the List")
        else:
            b=eval(input("Enter number to remove:"))
            n.remove(b)
            print("List: ",dis())
    elif choice==3:
        pos = eval(input("Enter a position to insert: "))
        value = eval(input("Enter a Number to insert: "))
        n.insert(pos, value)
        print("List: ",dis())
    elif choice==4:
        print("List: ",dis())
    elif choice==5:
        n.pop()
        print("List:",dis())
    elif choice==0:
        print("Exiting!")
else:
    print("Invalid choice!!")
print()