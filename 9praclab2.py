class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        print(self.book_id, "|", self.title, "|", self.author, "| Issued:", self.is_issued)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(book_id, title, author))
        print("Book added successfully!")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))
        for book in self.books:
            if book.book_id == book_id and not book.is_issued:
                book.is_issued = True
                print("Book issued!")
                return
        print("Book not available!")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for book in self.books:
            if book.book_id == book_id and book.is_issued:
                book.is_issued = False
                print("Book returned!")
                return
        print("Invalid return!")

    def display_books(self):
        print("\n--- Book List ---")
        for book in self.books:
            book.display()


# Menu-driven program
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.issue_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
