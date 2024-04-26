r = open('FILE.txt', 'rb')  # this is a binary mode
# r = open('FILE.txt', 'rt')
data = r.readline()  # use to read one linne and also print (\n)
print(data)
data = r.readline()
print(data)
r.close()
# **************************
