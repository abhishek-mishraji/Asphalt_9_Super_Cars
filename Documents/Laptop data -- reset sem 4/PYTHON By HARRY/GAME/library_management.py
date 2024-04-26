class Library:

    store_ret_borr = []

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        i=1
        print("Books present in this library are: ")
        for book in self.books:
            print(f"{i}.{book}")
            i=i+1

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            self.store_ret_borr.append(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        if bookName in self.store_ret_borr:
            self.books.append(bookName)
            self.store_ret_borr.remove(bookName)
            print(
                "Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        else:
            print("u did't take this book, so so we can not take this book :")


class Student:
    store_ret_borr = []

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):

        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
    Pres :-      1. List all the books
    Pres :-      2. Request a book
    Pres :-      3. Return a book
    Pres :-      4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
