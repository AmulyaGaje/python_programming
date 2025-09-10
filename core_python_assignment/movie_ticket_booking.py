<<<<<<< HEAD
x=int(input("total_seats"))
li1=[]
seats=[]
for i in range(1,x+1):
    li1.append(i)
booked_seats=[2,5,7]
def book_seat():
    sno=int(input("book_seat ="))
    if(sno>x or sno<1):
        print("Seat is invalid")
    elif sno in booked_seats:
            print("Seat is already booked")
    else:
        booked_seats.append(sno)
def cancel_seat():
    sno=int(input("cancel_seat ="))
    if sno in booked_seats:
        booked_seats.remove(sno)
    else:
        print("The seat is not yet booked")
def available():
    for seat in li1:
        if seat not in booked_seats:
            seats.append(seat)
    print("Available seats: ",seats)
book_seat()
cancel_seat()
=======
x=int(input("total_seats"))
li1=[]
seats=[]
for i in range(1,x+1):
    li1.append(i)
booked_seats=[2,5,7]
def book_seat():
    sno=int(input("book_seat ="))
    if(sno>x or sno<1):
        print("Seat is invalid")
    elif sno in booked_seats:
            print("Seat is already booked")
    else:
        booked_seats.append(sno)
def cancel_seat():
    sno=int(input("cancel_seat ="))
    if sno in booked_seats:
        booked_seats.remove(sno)
    else:
        print("The seat is not yet booked")
def available():
    for seat in li1:
        if seat not in booked_seats:
            seats.append(seat)
    print("Available seats: ",seats)
book_seat()
cancel_seat()
>>>>>>> 0fa6456496e9d71ee8c18890d9747d5bd6d029d0
available()