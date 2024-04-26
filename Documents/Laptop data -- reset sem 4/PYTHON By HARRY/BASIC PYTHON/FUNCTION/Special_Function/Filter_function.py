# same as map.. call all element in list or other but it returns filtered or True value

def square(listt): return listt % 2 == 0


listt = [1, 2, 3, 4, 5]
print(filter(square, listt))
print(list(filter(square, listt)))
