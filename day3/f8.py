# You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
# 1.Add a product to the cart.
# 2.Remove a product from the cart 
# 3.Search for a product in the cart 
# 4.Display all products in the cart
# 5.Show the total number of products in the cart
 
# Cart Operations:
# 1. Add Product
# 2. Remove Product
# 3. Search Product
# 4. Display Cart
# 5. Count Products
# 6. Exit
 
# Enter choice: 1
# Enter product to add: Laptop
# Product 'Laptop' added to cart.
 
# Enter choice: 1
# Enter product to add: Phone
# Product 'Phone' added to cart.
 
# Enter choice: 4
# Cart: ['Laptop', 'Phone']
 
# Enter choice: 3
# Enter product to search: Phone
# Yes, 'Phone' is in the cart.
 
# Enter choice: 5
# Total products in cart: 2
def addProduct(li, x):
    li.append(x)  
def removeProduct(li, x):
    if x in li:
        li.remove(x)
        print(f"{x} removed from cart")
    else:
        print(f"{x} not found in cart")
def searchProduct(li, x):
    if x in li:
        print(f"{x} is found in the cart")
    else:
        print(f"{x} not found in the cart")
def display(li):
    print(li)
def countProducts(li):
    count = 0
    for i in li:
        count += 1
    print("Total products in cart =", count)
def sortCart(li):
    li.sort()
    print(li)
def clearCart(li):
    print(li.clear())
li = []
while True:
    print("Cart Operations")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Display Cart")
    print("5. Count Products")
    print("6. Sort")
    print("7 clear cart")
    print("8.exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = input("Enter product name: ")
        addProduct(li, x)
    elif choice == 2:
        x = input("Enter product name: ")
        removeProduct(li, x)
    elif choice == 3:
        x = input("Enter product name: ")
        searchProduct(li, x)
    elif choice == 4:
        display(li)
    elif choice == 5:
        countProducts(li)
    elif choice==6:
        sortCart(li)
    elif choice==7:
        clearCart(li)
    else:
        print("Exiting")
        break

