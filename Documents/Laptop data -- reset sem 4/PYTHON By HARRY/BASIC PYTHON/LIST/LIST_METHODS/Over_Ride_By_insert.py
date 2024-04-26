

# a = [1, "abhi", 7, 8, 5, 2, 9, 6] NOT SUPPORT IN B/W INT AND STR
a = [1, 4, 7, 8, 5, 2, 9, 6]
i = int(input("enter inndex no. : "))
v = int(input("enter value  :  "))
a.insert(i, v)
a.pop((i+1))

print(a)
