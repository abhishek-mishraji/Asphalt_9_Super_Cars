import random
rand1 = random.randint(1, 99)
print(rand1)

a = rand1 % 10
rand1 = rand1//10
b = rand1 % 10
if a == b:
    print("you won Rs 10,000")
elif b > a:
    print("you won Rs 5000")
