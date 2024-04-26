def facto(a, b):

    return (a+facto(b))


a = int(input("Enter no. u  want ffactorial :  "))
b = int(input("Enter no. u  want ffactorial :  "))
print(facto(a, b))
