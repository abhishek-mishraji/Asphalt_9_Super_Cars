"""  ( Derived  class  can 
 acces data of base class ) but (Base class can't access data of derived class)"""
# Example of ---- Single inheritence
# 1 base has 1 derived and 1 derived has 1 base


class base:
    comapny = "microsoft"

    def call(self):
        print("this is base class fun : ")


class derived(base):
    comapny = "Google"

    def call(self):
        print("this is base Derivved fun : ")


b = base()
# b.call()
# print(b.comapny)
# *******************

d = derived()
d.call()  # first priority to own function
print(d.comapny)
