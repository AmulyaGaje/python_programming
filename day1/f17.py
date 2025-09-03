def leapYear(n):
    if((n%4==0 and n%100!=0) or (n%400==0)):
        return True
    else:
        return False
a=int(input("Enter a year"))
x=leapYear(a)
if(x==True):
    print("Leap Year")
else:
    print("Not leap Year")