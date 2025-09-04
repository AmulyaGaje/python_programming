def count(amount):
    m=0
    deno=[2000,500,200,100,50,10,20,5,2,1]
    for note in deno:
        if amount > note:
            sum = amount // note   
            amount = amount % note   
            sum+=1
    return sum


x=int(input("Enter the amount"))
print(count(x))

