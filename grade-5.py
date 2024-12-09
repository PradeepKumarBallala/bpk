class student:
 def __init__(self,rno,name,s1,s2,s3):
    self.rno=rno
    self.name = name
    self.s1=s1
    self.s2=s2
    self.s3=s3
 def tot(self):
    self.t= self.s1 + self.s2 + self.s3
    return self.t
 def percentage(self):
    self.p= self.t/3
    return self.p
 def result(self):
    if self.s1 >=40 and self.s2 >=40 and self.s3 >=40:
        self.r = "Pass"
    else:
        self.r = "Fail"
    return self.r
 def Grade(self):
    if self.r == 'Pass':
        if self.p > 95:
            return 'O'
        elif self.p > 80:
            return 'A'
        elif self.p > 70:
            return 'B'
        elif self.p >60:
            return 'C'
        elif self.p > 50:
            return 'D'
        else:
            return 'P' 
    else:
        return 'Nil'
 def output(self):
    print("Register Number:",self.rno)
    print("Name:",self.name)
    print("Subject 1 Marks:",self.s1)
    print("Subject 2 Marks:",self.s2)
    print("Subject 3 Marks:",self.s3)
    print("Total Marks:",self.tot())
    print("Percentage of Marks:",round(self.percentage(),2))
    print("Result:",self.result())
    print("Grade:",self.Grade())
rno = int(input("enter student register no : "))
name = str(input("enter student name : "))
s1 = int(input("enter Subject 1 marks : "))
s2 = int(input("enter Subject 2 marks : "))
s3 = int(input("enter Subject 3 marks : "))
m=student(rno,name,s1,s2,s3)
m.output()
