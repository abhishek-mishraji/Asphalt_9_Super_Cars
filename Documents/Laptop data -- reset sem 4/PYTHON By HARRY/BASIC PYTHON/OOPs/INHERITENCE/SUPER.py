# Multi_Level inheritence
# when derived class become base class (means Parent)
class base:
    def __init__(self):
        print("called base class")
# ***********************

    def call(self):
        print("this is base class fun : ")


class derive_1(base):
    def __init__(self):
        super().__init__()
        print("called Derived_1")

        # ***************

    def call(self):
        super().call()
        print("this is derive_1 class fun : ")


class derived_2(derive_1):  # jisko pahele derive karoge usko 1st priority milegi
    def __init__(self):
        super().__init__()
        print("called Derived_222")
        # ******************

    def call(self):
        super().call()  # if u  want call own as well as nearest base function of constractor
        # derive_1.call(self)
        print("this is chiled Derivved_2 fun : ")


# *******************

c = derived_2()
c.call()  # first priority to own function # then nearest parent (base class )
