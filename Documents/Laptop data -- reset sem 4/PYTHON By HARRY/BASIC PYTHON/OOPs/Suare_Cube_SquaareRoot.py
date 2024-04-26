import math  # for squareRoot


class calculator:
    def __init__(self, a):
        print(
            f"Square : {a**2} \n Cube : {a**3} \n squareRoot :{math.sqrt(a)}")
# squree num**2
# cube num**3 as so on
# square_Root : num*0.5


calculator_1 = calculator(
    int(input("Enter no. which u want  squarre,cube ,and squareRoott : ")))
