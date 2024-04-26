a = input("Enter a String : ")
if len(a) < 3:
    print("output is : ", a)
    # print(f"Given number {a}  is  divisible by 3")
else:
    # print(a[0], end="")
    # print(a[1], end="")
    # print(a[-2], end="")
    # print(a[-1], end="")
    print("output is : ", a[:2] + a[-2:])
