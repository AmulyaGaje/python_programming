def numberName(n):
    words={
        0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
    }
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    while(rev>0):
        r=rev%10
        print(words[r],end=" ")
        rev=rev//10
x=int(input())
numberName(x)