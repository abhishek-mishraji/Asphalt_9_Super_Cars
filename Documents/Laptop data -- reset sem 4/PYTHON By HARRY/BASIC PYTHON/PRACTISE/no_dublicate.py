a = [1, 2, 3, 4, 5]
b = [1, 2, 6, 8]

for item in a:
    if item not in b:
        c = b.append(item)

print(b)
