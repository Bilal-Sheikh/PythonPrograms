def getNonBlankInput(message, error_message):

        x = input(message)
        while len(x.strip()) == 0:
            x = input(error_message)

        return x

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def ViewBooks(self):
        print("Books present in this library are: ")
        for index, book in enumerate(self.books): 
            print(index+1 ,book)
    
    def IssueBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        if (bookName in self.books):
            print("This Books already exits")
        elif (bookName.strip()==''):
            print("Enter a proper name")
        elif(len(bookName)<5):
            print("Characters entered is less than the required value")
        else:
            self.books.append(bookName)
            print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

centraLibrary = Library(["Algorithms", "Django", "Python Notes", "Java Advance Edition"])
student = Student()

while(True):
            welcomeMsg = '''\n ====== Welcome to Central Library ======
            Please choose an option:
            1. View all the books
            2. Issue a book
            3. Return/Donate a book
            4. Exit console
            '''
            try:
                print(welcomeMsg)
                a = int(input("Enter a choice: "))
                if a == 1:
                    centraLibrary.ViewBooks()
                elif a == 2:
                    centraLibrary.IssueBook(student.requestBook())
                elif a == 3:
                    centraLibrary.returnBook(student.returnBook())
                elif a == 4:
                    print("Thanks for choosing Central Library. Have a great day ahead!")
                    break
                elif a>=5:
                    print("Option Unavailable")
            except ValueError as e:
                print("Enter numbers only")