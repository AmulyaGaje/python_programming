def palindrome(j):
    for n in range(1,j):
        rev=0
        temp=n
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        if(temp==rev):
            print(temp)
n=int(input())
palindrome(n)