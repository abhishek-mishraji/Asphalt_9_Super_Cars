from functools import reduce

l = [1, 2, 3, 4, 5]


def sum(a, b):
    return a+b


# use do steps to do some work like add # returns step  of all elements in 1 terms
new_l = reduce(sum, l)
print(new_l)
