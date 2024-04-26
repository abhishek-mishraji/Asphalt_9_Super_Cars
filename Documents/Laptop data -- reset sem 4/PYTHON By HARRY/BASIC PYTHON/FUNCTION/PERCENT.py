def percent(m1):
    # return (((m[0] + m[1] + m[2] + m[3] + m[4])*100)/500)
    return ((sum(m1)/5))


m1 = [1, 2, 3, 4, 5]
# per1 = percent(m1)
# print(per1)
print(percent(m1))
# *******************

m2 = [1, 2, 3, 4, 50]
# per1 = percent(m1)
# print(per1)
print(percent(m2))
