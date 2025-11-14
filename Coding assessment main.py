from library_books import library_books
from datetime import datetime, timedelta

#I used the codehs python docs file https://codehs.com/editor/documentation/python to understand the function of the language

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def inventory():
    #this part prints the id, title, and author of the book 
    #by using for loop for as many book there are in the list
    
    #key and value, i had to recall from SDE classes
    #list function line 17 learned from codehs doc file
    #but for the books.list i had to find it from google
    for books in library_books:
        print("-")
        for key, value in list(books.items())[:3]:#slicing learned by python doc file(codehs) 
            if books['available']==True:
                print(f'{key}: {value}')

inventory()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search():
    search_book=str(input("Enter the author OR genre of the book: ")).lower()
    book_list=[]
    for books in library_books:
        if search_book==books["author"].lower() or search_book==books["genre"].lower():
            book_list.append(books)
    if book_list:
        print(book_list)
#    else:
 #       print(f"No results for {search_book}")
search()


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
