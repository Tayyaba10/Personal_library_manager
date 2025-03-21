import json
import os

data_file = 'requirement.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

#add books in library
def add_book(library):
    print("--- Add a new book to the library. ---")
    title = input("Enter book title:")
    author = input("Enter author name:")
    year = input("Enter the publication year:")
    genre = input("Enter the genre:")
    read = input("Have you read this book? (yes/no):").lower() == 'yes'
            
    new_book = {
        "title": title, 
        "author": author, 
        "genre": genre, 
        "year": year,
        "status": read
    }

    library.append(new_book)
    save_library(library)
    print(f"\n Book {title} added sucessfully.")

#remove books in library   
def remove_book(library):
     print("--- Remove a book from the library. ---")
     title = input("Enter the title of the book to remove:")
     initial_length = len(library)
     new_library = [book for book in library if book["title"].lower() != title]
     if len(new_library) < initial_length:
       save_library(library)
       print(f"Book {title} removed successfully!  ")
     else:
        print(f"Book '{title}' not found.")
        

#search books in libraray
def search_library(library):
     print("--- Search for a book by title or author. ---")
     print("\nSearch by:")
     print("1. Title")
     print("2. Author")

     serach_type = input("Enter your choice (1 or 2):")

     results = []
     #serach book in library by title or author
     if serach_type == '1':
        search_term = input("Enter Title: ").lower()
        results = [book for book in library if search_term in book['title'].lower()]
     elif serach_type == '2':
        search_term = input("Enter Author: ").lower()
        results = [book for book in library if search_term in book['author'].lower()]
     else:
        print("Invalid Search Type!")
        return

    #search result show
     if results:
        print("\n📚 Serach Results:")
        print("Matching Books:")
        for book in results:
            status = "Read" if book ['status'] else 'Unread'
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
     else:
        print("\nNo book found matching your search criteria.")

#display all books in library
def display_book(library):
     print("--- Display all books. ---")
     if library:
         for book in library:
            status = "Read" if book['status'] else 'Unread'
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
     else:
        print("No books in your library.")


#updates status of book in library 
def display_statistics(library):
      print("--- Display statistics about the library. ---")
      total_books = len(library)
      read_books = len([book for book in library if book ['status']])
      unread_books = total_books - read_books
      percentage_book = (total_books / read_books)* 100 if total_books > 0 else 0

      print("\n📊 Library Statistics 📊")
      print(f"📚 Total Books: {total_books}")
      print(f"📖 Read Books: {read_books}") 
      print(f"📘 Unread Books: {unread_books}")
      print(f"Percentage Books: {percentage_book}")

#library menu
def main():
    library = load_library()
    while True:
        print("========= WELCOME to your Personal Library Manager! ========= ")
        print("\n==== Personal Library Manager ====")
        print("--- Menu ---")
        print("1. Add a book")
        print("2. Remova a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input('Enter your choice (1-6):')
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_book(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Thank you for using Personal Library Manager!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()