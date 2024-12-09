Employeeadmin2 = {}
Employeeadmin = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"} 
print(type(Employeeadmin)) 
print("printing Employee data .... ") 
print("Name : %s" %Employeeadmin["Name"]) 
print("Age : %d" %Employeeadmin["Age"]) 
print("Salary : %d" %Employeeadmin["salary"]) 
print("Company : %s" %Employeeadmin["Company"]) 
print("Enter the details of the new employee...."); 
Employeeadmin2["Name"] = input("Name: "); 
Employeeadmin2["Age"] = int(input("Age: ")); 
Employeeadmin2["salary"] = int(input("Salary: ")); 
Employeeadmin2["Company"] = input("Company:"); 
print("printing the new data....."); 
print("Name : %s" %Employeeadmin2["Name"]) 
print("Age : %d" %Employeeadmin2["Age"]) 
print("Salary : %d" %Employeeadmin2["salary"]) 
print("Company : %s" %Employeeadmin2["Company"]) 
print(Employeeadmin2)
print(Employeeadmin)