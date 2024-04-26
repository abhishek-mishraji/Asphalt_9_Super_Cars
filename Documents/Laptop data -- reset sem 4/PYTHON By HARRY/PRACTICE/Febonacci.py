l = [0, 1, 1, 2, 3, 4, 5]
# l = 1, 1, 2, 3, 5, 8
feb = [0]
i = 0
while(i <= (len(l)-2)):

    feb.append(l[i] + l[i+1])

    i = i+1
print(feb)
