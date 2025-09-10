str=input("Enter any string")
def check(str):
    ac=0
    dc=0
    sc=0
    for i in str:
        if((i>='a' and i<='z') or (i>='A' and i<='Z')):
            ac+=1
        elif(i>='0' and i<='9'):
            dc+=1
        else:
            sc+=1
    print("Alphabet count=",ac)
    print("Digit count=",dc)
    print("Symbol count=",sc)
check(str)
