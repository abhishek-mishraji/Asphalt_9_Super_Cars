

n = int(input("Enter number of rows:"))
spaces = n
for i in range(1, n + 1):

    # Use inner for loop 1  for spaces before stars

    for j in range(1, spaces + 1):
        # print spaces
        print(" ", end="")
    # Use inner for loop 2  for columns / stars

    for k in range(1, i + 1):
        # print stars in each row
        print("* ", end="")

    # End of line after each row
    print()
    # decrease spaces
    spaces = spaces - 1
