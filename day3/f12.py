def Check(x):
    vc=0
    cc=0
    for i in x:
        if i in['a','e','i','o','u']:
            vc+=1
        else:
            cc+=1
    print(f"Vowel count={vc} and consonant count ={cc}")
str=input("ENTER ")
Check(str)