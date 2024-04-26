a = 888


def glo():
    global a  # if u use 'Global' keyword yhen it will change everywhere
    print(a)
    a = 00
    print(a)


glo()
print(a)
