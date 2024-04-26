# Multi_Level inheritence
# when derived class become base class (means Parent)
class base:
    comapny = "microsoft"

    def call(self):
        print("this is base class fun : ")


class derive_1(base):
    comapny = "makhat"
    # pass

    def call(self):
        print("this is derive_1 class fun : ")


class derived_2(derive_1):  # jisko pahele derive karoge usko 1st priority milegi

    # comapny = "Google"
    pass

    # def call(self):
    #     print("this is chiled Derivved_2 fun : ")


# *******************
# a = base()
# b = derive_1()
c = derived_2()
c.call()  # first priority to own function # then nearest parent (base class )
print(c.comapny)
