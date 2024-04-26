a = [222, 77, 10, 1, 2, 3, 4, 5, 6]


def call(dataa):
    return dataa > 10


print(list(filter(call, a)))  # it will call the function untill list exist
# it will return true  condition
