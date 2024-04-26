def sum(n):
    if (n == 0):
        return 0
    return (n+sum(n-1))


a = int(input("Enter no. u  want Sum :  "))
print(sum(a))
