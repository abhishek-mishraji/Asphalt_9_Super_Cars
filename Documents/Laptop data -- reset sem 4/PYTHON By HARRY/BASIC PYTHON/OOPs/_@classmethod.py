class railwayform:
    train = "Railway"
    #  **********************

    def printdata(self, traine):  # it will only change for particular object not for global
        self.train = traine
    # ***********************
    # @classmethod
    # def printdata(cls, traine):  # this is function
    #     cls.train = traine
        #     # *****************************************


abhiform = railwayform()
_2nd = railwayform()
print(abhiform.train)
abhiform.printdata("Udhampur")
print(abhiform.train)
print(_2nd.train)
# ***************
print(railwayform.train)
