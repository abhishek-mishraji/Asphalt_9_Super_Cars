# Use to call every element of list again and again

def square(listt): return listt**2


listt = [1, 2, 3, 4, 5]
print(map(square, listt))
print(list(map(square, listt)))
