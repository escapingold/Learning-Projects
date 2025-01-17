class Library:
    def __init__(self):
        self.name = input("Enter your name: ").strip()  
        self.books = {}  
        self.budget = 1000
        self.library_name = input("Enter a custom title for your library: ").strip()  

    def display(self):
        print(f"Welcome {self.name} to your {self.library_name}".center(50))

        if self.books:
            print("Here are all your available books in the library:".center(50))
            for i, (book, status) in enumerate(self.books.items()):
                print(f"{i + 1})--->{book} (Status: {status})")
        else:
            print("No books available yet...")

    def search(self):
        search_book = input("Enter the name of the book you want to search:\n").strip()

        if search_book in self.books:
            print(f"{search_book} is available in the library with status: {self.books[search_book]}")
        else:
            print(f"{search_book} is not available in the library...")

    def addbook(self):
        print("Enter the name of the book you want to store:\n")
        book_name = input("Enter: ").strip()

        if book_name in self.books:
            print("This book is already available...")
        else:
            self.books[book_name] = "available" 
            print(f"Book: {book_name}\nadded for {self.name}")
            print(f"Total number of books: {len(self.books)}")

    def lent(self):
        print("Books available for lending: ")
        available_books = [book for book, status in self.books.items() if status == "available"]
        
        if available_books:
            for i, book in enumerate(available_books):
                print(f"{i + 1}) ==> {book}")

            lent_ask = input("Enter the name of the book you want to lend: ").strip()

            if lent_ask not in available_books:
                print("Book not available.")
            else:
                print(f"Your available balance: ₹{self.budget}")
                book_cost = 100
                if self.budget < book_cost:
                    print("Insufficient balance to lend the book.")
                else:
                    print(f"Book cost: ₹{book_cost}")
                    ch = input("Enter 'yes' to lend: ").strip().lower()

                    if ch == "yes":
                        self.budget -= book_cost
                        self.books[lent_ask] = "lent"  # Update status to 'lent'
                        print(f"Book lent successfully! Your remaining balance: ₹{self.budget}")
                    else:
                        print("Lending cancelled.")
        else:
            print("No books available for lending.")

    def return_book(self):
        returnbook = input("Enter the name of the book you want to return:\n").strip()

        if returnbook not in self.books:
            print("This book does not belong to the library.")
        elif self.books[returnbook] == "available":
            print("This book is already available in the library.")
        else:
            self.books[returnbook] = "available" 
            print(f"Book '{returnbook}' has been successfully returned and added to the library.")


print("Welcome To Custom Library".center(100))
show = Library()

while True:
    print("""\nEnter the option you want to explore:
D- To display all books
A- To add books
L- To lend/buy a book
R- To return a book
S- To search a book
Q- To quit
""")

    choose = input("Enter: ").strip().lower()  

    if choose == "d":
        show.display()
    elif choose == "a":
         show.addbook()
    elif choose == "l":
        show.lent()
    elif choose == "r":
        show.return_book()
    elif choose == "s":
        show.search()
    elif choose == "q":
        print("Thanks for visiting...")
        break
    else:
        print("Invalid input. Please try again.")
