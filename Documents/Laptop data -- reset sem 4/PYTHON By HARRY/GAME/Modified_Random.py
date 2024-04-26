import random
j = 0
r = 0
while True:
    if(r == 'e'):
        break
    if(j == (0+j)):
        # it will give random no. between 1 to 100
        rand = random.randint(1, 100)
        print("""
    Guess no. b/w 1 to 100 : 
    \n  ***********************************""")
    # print(rand)
    r = 0
    i = 0

    while(True):
      
        print("\n For EXIT ------- Press ------ 'e'\n")
        print(" For RESTART ------- Press ------ 'r'\n")
        print("****************************************\n")
        r = input(" Guess no. :  ")
# ******************************************************************

        if(r == 'e'):
            print("\n\nThanks for playing the game 😊👍👌👌👌👌👌👌👌😘😘😘👾👾👾👊\n")
            break
        if(r == 'r'):
            print("\n\nREstarted..........--- \n")
            break

# **********************************************************************

    # *********************************
        else:
            # while(rand != r):

            try:
                i = i+1
                r = int(r)
                # ****************
                if (r > 100):
                    r = str(r)
                # ***************    #
                if(r > rand):
                    print("   Guess lessser no. ------👻👻\n")

                elif(r < rand):
                    print("   Guess greater no. --------😶‍🌫️😶‍🌫️😶‍🌫️\n ")

                # **********************************
                elif(r == rand):
                    print(
                        "\n***************************\n hurray ! 👍👍👌 ,\n you are write ! -----\n******************")
                    print(f" U took__ {i} __attemps")
                    # ********************
                    j = (i+1)
                    # *******************
                    with open("POints_table.txt", "r") as f:
                        high_score = int(f.read())

                    if(i < high_score):
                        print(
                            "-----------------  U just broke the REcord : 🤹‍♀️🤹‍♀️🤹‍♀️🤹‍♂️------------\n \n")
                        with open("POints_table.txt", "w") as f:
                            f.write(str(i))

                    break
            #
            except Exception as e:
                print(
                    f"\nu enter other than no. OR no. grreater than 100 , please try again : {e}")
