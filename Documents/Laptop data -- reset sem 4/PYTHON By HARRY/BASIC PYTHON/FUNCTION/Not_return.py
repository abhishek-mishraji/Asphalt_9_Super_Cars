def even(list):
    for num in list:
        if num % 2 == 0:
            return True
        else:
            pass

    return False


list = [1, 212, 30]
print(even(list))
