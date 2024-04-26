import random
j = 0
while True:
    if(j == (0+j)):
        # it will give random no. between 1 to 100
        rand = random.randint(1, 100)
    # print(rand)
    r = 0
    i = 0
    print(""" \n ******************************* 
    Guess no. b/w 1 to 100 : 
    \n  ***********************************\n""")
    while(True):
        print("\n For EXIT ------- Press ------ 'e'\n")
        r = input(" Guess no. :  ")

        if(r == 'e'):
            print("Thanks for playing the game 😊👍👌👌👌👌👌👌👌😘😘😘👾👾👾👊")
            break

    # *********************************
        else:
            # while(rand != r):

            try:
                i = i+1
                r = int(r)

                if(r > rand):
                    print("   Guess lessser no. ------👻👻\n")

                elif(r < rand):
                    print("   Guess greater no. --------😶‍🌫️😶‍🌫️😶‍🌫️\n ")

                # **********************************
                elif(r == rand):
                    print("\n hurray ! 👍👍👌 ,\n you are write ! -----")
                    print(f"\n  U took__ {i} __attemps")
                    # ********************
                    j = (i+1)
                    # *******************
                    with open("POints_table.txt", "r") as f:
                        high_score = int(f.read())

                    if(i < high_score):
                        print("  U just broke the highest record -- 🤹‍♀️🤹‍♀️🤹‍♀️🤹‍♂️\n \n")
                        with open("POints_table.txt", "w") as f:
                            f.write(str(i))
            
            except Exception as e:
                print(
                    f"u enter other than no. OR no. grreater than 100 , please try again : {e}")
