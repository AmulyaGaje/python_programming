def Occurence(a):
    s=""
    visited = [] 
    for i in a:
        if i not in visited:
            count=0
            for c in a:
                if c==i:
                    count+=1
            s+=i+str(count)
            visited.append(i)
    print(s)
x=input("Enter")
Occurence(x)