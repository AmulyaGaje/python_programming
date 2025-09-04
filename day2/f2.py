def check(x):
    if(x>='a' and x<='z') or (x>='A' and x<='Z'):
        return "Alphabet"
    elif(x>='0' and x<='9'):
        return "digit"
    else:
        return "special character"
n=input("Enter a single charcter")
print(check(n))