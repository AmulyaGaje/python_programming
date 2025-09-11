def division(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("Error:Divivsion by zero in not allowed")
    else:
        print("Result of division is",c)
    finally:
        print("Done")
a,b=map(int,input("Enter two numbers").split())
division(a,b)