# Multiple inheritence
# DERIVERD HAS MORE THAN 1 BASE CLASS
class base:
    comapny = "microsoft"

    def call(self):
        print("this is base class fun : ")


class base1:
    comapny = "makhat"

    def call(self):
        print("this is base_1 class fun : ")


class derived(base, base1):  # jisko pahele derive karoge usko 1st priority milegi
    # class derived(base1, base):
    # comapny = "Google"
    pass
    # def call(self):
    #     print("this is base Derivved fun : ")


# *******************
d = derived()
d.call()  # first priority to own function
print(d.comapny)
