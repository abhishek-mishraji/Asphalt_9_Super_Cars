r = open('FILE.txt', 'r')
# r = open('FILE.txt') # if u will not specifi mode then by default takr READ (r) MODE
data = r.read()
# data = r.read(3)  # how many char u want to read

print(data)
r.close()
# *******************************
