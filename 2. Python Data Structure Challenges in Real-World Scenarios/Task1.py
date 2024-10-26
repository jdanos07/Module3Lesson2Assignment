# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def library_addition():
    
    for addition in library:
        new_addition = input("Is there a new book to add? Yes/No ").lower()
        if new_addition == 'yes':
            title = input('Title: ')
            author = input("Author: ")

            new_book = ((
                title,
                author
            ))

            if new_book in library:
                print('This book is already in the system. No duplicates are permitted at this time.')
            else:
                library.append(new_book)
                print(library)
        else:
            print('Goodbye')
            break

library_addition()