class Employee:
    company = "Google"  # this is attribute # by default company

    # Constractor call it self when object is created # u have to pass argument for print data of object but in function not
    def __init__(self, name, company, id):
        print("Constractor call it self when object is created")
        self.name = name
        self.company = company
        self.id = id
        print(f"Name is : {self.name}")
        print(f"Id is : {self.id}")
        print(f"Commpany is : {self.company}")
        # *******************

    # @staticmethod # not worth in contractor


# *****************************
# Detail of 1
# ************************
Employee_1 = Employee
# Employee_1 = Employee("abhi", input("Enter company : "), Employee.company)
Employee_1("abhi",  Employee.company, input("Enter company : "))
