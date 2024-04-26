

while(True):
    try:
        a = int(input("enter no. : "))
        c = 1/a

        print(c)
# ******************
    except Exception as g:  # it can accept any type of zzero
        print(f"kya kar rahe of bhai ........ {g}")

    else:
        # when exception not execute then this (Else) will execute
        print("Code run successful")
