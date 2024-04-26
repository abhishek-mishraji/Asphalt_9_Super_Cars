# X is use to creatte file and X+ for create and read and write

r = open('Xx.txt', 'x+')

r.write("abhishek")
data = r.read(3)
# data = r.read(3)  # how many char u want to read

print(data)
r.close()
# *******************************
