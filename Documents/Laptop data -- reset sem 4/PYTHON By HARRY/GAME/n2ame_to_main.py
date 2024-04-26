def my_function():
    print("I am outside the (file) function")
    if __name__ == "__main__":
        print("Executed when invoked directly")
    else:
        print("Executed when imported")
