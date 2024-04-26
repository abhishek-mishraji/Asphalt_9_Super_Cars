with open('FILE.txt', 'r') as r:
    data = r.read()

a = input("which word u want find in file : ")
dataa = data.lower()
l = a.lower()
if l in dataa:
    print(f"{a} is present in file")
else:
    print("not present in file")
