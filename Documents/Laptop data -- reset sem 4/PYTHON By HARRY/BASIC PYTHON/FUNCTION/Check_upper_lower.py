
str = "Live life to the Fullest"
lower = []
Upper = []

for char in str:
    k = char.islower()  # Returning only True or False
    u = char.isupper()
    if k == True:
        # print(f"Upper : {char}")
        lower.append(char)
    elif u == True:
        # print(f"Lower : {char}")
        Upper.append(char)
print(lower, "\n", Upper)
