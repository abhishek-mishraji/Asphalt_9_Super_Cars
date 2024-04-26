def facto(n):
    if (n == 1) or (n == 0):
        return 1
    return (n*facto(n-1))


a = int(input("Enter no. u  want ffactorial :  "))
print(facto(a))
