# Personal Library Manager

A simple Python-based library management system that helps you keep track of your books and manage borrowing records.

## Features

- Add and remove books
- Search books by title or author
- Track book borrowing and returns
- View borrowing history
- SQLite database for persistent storage

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
# Create a library manager instance
library = LibraryManager()

# Add a book
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

# Search for books
results = library.search_books("Gatsby")

# Borrow a book
library.borrow_book(book_id=1, borrower_name="John Doe")

# Return a book
library.return_book(book_id=1)

# List all books
books = library.list_all_books()

# View borrowing history
history = library.get_borrowing_history()
```

## Database Structure

The system uses SQLite with two main tables:

1. `books` - Stores book information:
   - id (PRIMARY KEY)
   - title
   - author
   - isbn (UNIQUE)
   - status
   - added_date

2. `borrowing_records` - Tracks borrowing history:
   - id (PRIMARY KEY)
   - book_id (FOREIGN KEY)
   - borrower_name
   - borrow_date
   - return_date

## Features Explanation

1. **Book Management**
   - Add new books with title, author, and optional ISBN
   - Remove books from the library
   - Search books by title or author
   - List all books in the library

2. **Borrowing System**
   - Track who borrowed which books
   - Record borrowing and return dates
   - Prevent borrowing of already borrowed books
   - View complete borrowing history

3. **Data Persistence**
   - All data is stored in a SQLite database
   - Data persists between program runs
   - Automatic database creation and table setup 