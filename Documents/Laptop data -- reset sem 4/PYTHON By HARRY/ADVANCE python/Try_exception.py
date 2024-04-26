

while(True):
    try:
        a = int(input("enter no. : "))
        c = 1/a

        print(c)
# ******************

    except ValueError as e:
        print("please enter valid value :")

    except ZeroDivisionError as f:
        print("please don't devide by 0")

    # except Exception as g:  # it can accept any type of zzero
    #     print(f"kya kar rahe of bhai ........ {g}")
