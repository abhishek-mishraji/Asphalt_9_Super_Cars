while True:

    try:
        age = int(input("enter age  "))
        print(age)

    except Exception as e:
        # print(e)
        print("please enter your age in nummber format")
