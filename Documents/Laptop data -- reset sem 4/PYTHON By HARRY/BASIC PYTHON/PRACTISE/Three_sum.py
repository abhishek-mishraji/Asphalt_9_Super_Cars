array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(array)):
    for j in range(len(array)):
        for k in range(len(array)):
            if (k != i & k != j):
                if ((array[i] + array[j] + array[k]) == 13):
                    print(array[i], array[j], array[k])
