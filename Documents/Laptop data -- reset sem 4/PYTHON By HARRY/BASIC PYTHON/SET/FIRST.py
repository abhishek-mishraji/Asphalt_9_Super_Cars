# SET IS A COLLECTION OF NON-REPETATIVE ELEMENTS
# SET'S ARE UN-ORDERED AND NON-INDEX
s = {1, 3, 3, 3, 2, 14}
s.add(3333)
print(s)

# *************************
# METHOD

a = set()  # empty Set
print(type(s))
a.add(9)
a.add(889)
a.add(997)
a.add(997)  # it will not add multiple time
print(a)

# ***************************
#
# we can't add list,dic and Set bcz it is changeable (un_hashable)
# a.add([1, 2, 2])
# a.add({3, 2, 1})
# a.add({3:1})

# ************************

# we can add TUPLE
a.add((3, 2, 1))
print(a)
