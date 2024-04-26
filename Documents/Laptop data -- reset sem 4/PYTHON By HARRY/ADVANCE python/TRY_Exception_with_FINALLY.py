while(True):
    try:
        a = int(input("enter no. : "))
        c = 1/a

        print(c)
# ******************
    except Exception as g:  # it can accept any type of zzero
        print(f"kya kar rahe of bhai ........ {g}")
        exit()
    finally:
        # use to clear last file of which should done in last
        # if u  wil exit the programme then also it will execute
        print("it will always execute :")
