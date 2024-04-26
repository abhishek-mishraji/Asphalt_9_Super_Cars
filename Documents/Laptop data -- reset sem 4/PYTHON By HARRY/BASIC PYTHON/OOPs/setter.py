class railwayform:
    formtype = "RailwayForm"
    salary = 10
    bonus = 20
    # total_income = 32000

    @property  # also known as getter decorator
    def total_income(self):  # this is function
        return self.salary+self.bonus
        # ****************

    @total_income.setter
    def total_income(self, val):  # this is function
        self.bonus = val-self.salary
# *****************************************


abhiform = railwayform()
print(abhiform.total_income)
abhiform.total_income = 100  # this automatically call setter
print(abhiform.bonus)
