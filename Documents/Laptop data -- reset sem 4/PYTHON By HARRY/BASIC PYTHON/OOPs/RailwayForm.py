class railwayform:

    formtype = "RailwayForm"

    def printdata(self):  # this is function
        print(f"name is {self.name}")
        print(f"train name is {self.train}")
        print(f"form type is {self.formtype}")

# *****************************************


abhiform = railwayform()
abhiform.name = "Abhishek"
abhiform.train = "Udhampur"
abhiform.printdata()
