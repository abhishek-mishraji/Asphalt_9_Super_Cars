# # u don't have to return
#
# square=lambda num: num**2
# # print(square(5))
# print(lambda num: num**2)

# *****************************************
# str1 = 'ENOUGH'
# # lambda returns a function object
# rev_upper = lambda string: string.upper()[0:1]
# print(rev_upper(str1))
# ********************************************

# str1 = 'ENOUGH'
# # lambda returns a function object
# rev_first = lambda str: str[0]
# print(rev_first(str1))
# ************************************


str1 = 'ENOUGH'
# lambda returns a function object
def rev_first(str): return str[0]


print(rev_first(str1))
