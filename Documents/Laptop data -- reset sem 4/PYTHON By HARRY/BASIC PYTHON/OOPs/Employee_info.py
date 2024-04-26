class Employee:
    company = "Google"  # this is attribute # by default company

    def print_info(self):
        print(f"Name is : {self.name}")
        print(f"Id is : {self.id}")
        print(f"Commpany is : {self.company}")


# *****************************
# Detail of 1
# ************************
Employee_1 = Employee()
Employee_1.name = input("enter employee_1 name : ")  # this is instances
Employee_1.id = int(input("enter employee_1 Id : "))
Employee.company = input("enter employee_1 company : ")
print("\n")
# *****************************
# Detail of 2
# ************************
Employee_2 = Employee()
Employee_2.name = input("enter employee_2 name : ")  # this is instances
Employee_2.id = int(input("enter employee_2 Id : "))
Employee.company = input("enter employee_2 company : ")
print("\n")
# *****************************
# Detail of 3
# ************************
Employee_3 = Employee()
Employee_3.name = input("enter employee_3 name : ")  # this is instances
Employee_3.id = int(input("enter employee_3 Id : "))
Employee.company = input("enter employee_2 company : ")
print("\n")

# ******************************
#  detail of all employees will print here
# ****************************
print("Detail of all Employees : ")
Employee_1.print_info()
print("\n")
Employee_2.print_info()
print("\n")
Employee_3.print_info()
