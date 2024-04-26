class railwayform:
    formtype = "RailwayForm"
    salary = 1000
    bonus = 2000
    # total_income = 32000

    @property
    def total_income(self):  # this is function
        return self.salary+self.bonus
# *****************************************


abhiform = railwayform()
print(abhiform.total_income)
