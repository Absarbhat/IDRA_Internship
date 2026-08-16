class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")

        self.books[book_id] = title
        print("Book added successfully!")

    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nBooks in Library:")
            for book_id, title in self.books.items():
                print(book_id, "-", title)

    def issue_book(self):
        book_id = input("Enter book ID to issue: ")

        if book_id in self.books:
            print("Book issued:", self.books[book_id])
            del self.books[book_id]
        else:
            print("Book not found.")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book_id, title in self.books.items():
                file.write(book_id + "," + title + "\n")

        print("Books saved to file.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Save Books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            library.issue_book()

        elif choice == 4:
            library.save_books()

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a number.")