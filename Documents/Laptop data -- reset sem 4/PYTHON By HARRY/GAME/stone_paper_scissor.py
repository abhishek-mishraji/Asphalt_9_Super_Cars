import random
i = 1
while (i > 0):
    def gamewin(comp, you):
        if (comp == you):
            return None
        elif (comp == 's'):
            if (you == 'k'):
                return False
            elif (you == 'p'):
                return True
                # ***********************
        elif (comp == 'k'):
            if (you == 'p'):
                return False
            elif (you == 's'):
                return True
                # ***********************
        elif (comp == 'p'):
            if (you == 's'):
                return False
            elif (you == 'k'):
                return True
                # ***********************
    print("Comp turn :")
    rand = random.randint(1, 3)
    if (rand == 1):
        comp = 's'
    elif (rand == 2):
        comp = 'k'
    elif (rand == 3):
        comp = 'p'
# ************************
    you = input("Your turn : ")
    a = gamewin(comp, you)

    if (a == None):
        print(f"\n Computer choose - :  {comp}")
        print("\n Tieeeeee 🤦‍♀️🤦‍♀️🤦‍♀️\n")
    elif a:
        print(f"\n Computer choose - :  {comp}")
        print("\n WINNNNNNNNNNER 👍👍👍👍👍👊\n")
    else:
        print(f"\n Computer choose - :  {comp}")
        print("\n LOSSS 😒😒😒😒😒😒\n")
