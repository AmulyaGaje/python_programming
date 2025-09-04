def display(m,n):
    for i in range(m):
        for j in range(n):
            if(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
x=int(input())
y=int(input())
display(x,y)