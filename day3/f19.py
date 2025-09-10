# you are building a Library Management System in Python. The system should store books in a dictionary where:
# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup)
d=dict()
def addBook(d,k,v):
    if k not in d.keys():
        d[k]=v
        print("Added")
def removeBook(d,k):
    if k in d.keys():
        del d[k]
    else:
        print("Book not present")
def searchBook(d,k):
    if k in d.keys():
        print("Book present-Name is")
        print(d[k])
    else:
        print("Book not present")
def UpdateTitle(d,k,v):
    if k in d.keys():
       d[k]=v
       print("Updated")
def display(d):
   print(d)
def count(d):
    print("The total number of books are",len(d.keys()))

while(True):
    x=int(input("Enter your choice"))
#     print("Add a book to the library (Book ID, Title)".
# Remove a book using Book ID.
#  Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# print ("Count the total number of books in the library.")
    if(x==1):
        bid=int(input("Enter the bid"))
        bname=input("Enter the title of the book")
        addBook(d,bid,bname)
    elif(x==2):
        bid=int(input("Enter the bid of the book to remove"))
        removeBook(d,bid)
    elif(x==3):
        bid=int(input("Enter the bid"))
        searchBook(d,bid)
    elif(x==4):
        bid=int(input("Enter the bid"))
        bname=input("Enter the correct title")
        UpdateTitle(d,bid,bname)
    elif(x==5):
        display(d)
    elif(x==6):
        count(d)
    else:
        print("Exiting")
        break