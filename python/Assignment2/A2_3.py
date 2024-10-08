from collections import defaultdict

class Library:
    def __init__(self):
        self.books = {}
        self.checked_out_books = defaultdict(int)
        self.total_checkouts = defaultdict(int)

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title]["copies"] += copies
        else:
            self.books[title] = {"author": author, "copies": copies}
        print(f"Added {copies} copies of '{title}' by {author}.")

    def checkout_book(self, title):
        if title in self.books and self.books[title]["copies"] > 0:
            self.books[title]["copies"] -= 1
            self.checked_out_books[title] += 1
            self.total_checkouts[title] += 1
            print(f"'{title}' has been checked out.")
        else:
            print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        if title in self.checked_out_books and self.checked_out_books[title] > 0:
            self.checked_out_books[title] -= 1
            self.books[title]["copies"] += 1
            print(f"'{title}' has been returned.")
        else:
            print(f"'{title}' was not checked out or is not recognized.")

    def library_status(self):
        print("\nLibrary Status:")
        for title, info in self.books.items():
            print(f"'{title}' by {info['author']} - {info['copies']} copies available")

    def most_checked_out_books(self):
        if not self.total_checkouts:
            print("No books have been checked out yet.")
            return
        
        most_checked_out = max(self.total_checkouts.values())
        most_checked_out_books = [title for title, count in self.total_checkouts.items() if count == most_checked_out]

        print("\nMost Frequently Checked-Out Books:")
        for title in most_checked_out_books:
            print(f"'{title}' - {self.total_checkouts[title]} checkouts")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Checkout a Book")
        print("3. Return a Book")
        print("4. View Library Status")
        print("5. View Most Checked-Out Books")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)
        elif choice == "2":
            title = input("Enter book title to checkout: ")
            library.checkout_book(title)
        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.library_status()
        elif choice == "5":
            library.most_checked_out_books()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
