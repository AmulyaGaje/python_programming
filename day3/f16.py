def highestFreq(str):
    max=0
    ch=""
    for i in str:
        count=str.count(i)
        if count>max:
            max=count
            ch=i
    print (f"{max}-{ch}")
x=input("Enter")
highestFreq(x)
