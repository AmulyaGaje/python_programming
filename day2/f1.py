def weekname(num):
    if(num==1):
        return"Sunday"
    elif(num==2):
        return "Monday"
    elif(num==3):
        return "Tuesday"
    elif(num==4):
        return "Wednesday"
    elif(num==5):
        return "Thursday"
    elif(num==6):
        return "Friday"
    else:
        return "saturday"
n=int(input("Enter week number from 1 to 7"))
res=weekname(n)
print(res)