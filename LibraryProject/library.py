class Library:

    def __init__(self,bookList):
        # bookList = ['python','java','c','c++','database']
        self.bookList = bookList

    def issueBook(self,bookName):
        print("Available books in the library are:")
        for index, books in enumerate(self.bookList):
            print(index,books)
        if bookName in self.bookList:
            print(f"{bookName} has been issued to you.")
            self.bookList.remove(bookName)
            print(f"total no of books available now is {len(self.bookList)} and updated list is: {[(index,item) for index, item in enumerate(self.bookList)]}")

    def returnBook(self,bookName):
        self.bookList.append(bookName)
        print(f" total no of books available now is {len(self.bookList)} and Updated book list after adding returned book to the library: {[(index,item) for index, item in enumerate(self.bookList)]}")
        
class Student:
    def issueBook(self):
        self.book = input("Enter the name of the book , you want to issue: ")
        return self.book

    def returnBook(self):
        self.book = input("enter the name of the book you want to return: ")
        return self.book

if __name__=='__main__':
    lib = Library(['python','java','c','c++','database'])
    s = Student()
    # lib.issueBook('java')
    # lib.returnBook('java')

    while(True):
        choice  = int(input("Enter a choice (1,2,3): "))
        if choice == 1:
            lib.issueBook(s.issueBook())

        elif choice == 2: 
            lib.returnBook(s.returnBook())
        elif choice == 3:
            exit()
        else:
            print("Invalid Choice!.")