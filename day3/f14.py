x=input("Enter a String")
ch=input("Enter a character to search")
def Search(x,ch):
    count=0
    for i in x:
        if ch==i:
            print(i)
            count+=1
    print(f"The no of occurences of{ch} is {count}")
Search(x,ch)