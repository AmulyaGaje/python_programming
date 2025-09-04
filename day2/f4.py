pmr,lmr=map(int,input("Enter the present month reading adn last month reading").split())
tu=pmr-lmr
def cbill(tu):
    if(tu<=50):
        cbill=3.80*tu
        return cbill
    elif(tu>50 and tu<=100):
        cbill=(3.80*50)+(tu-50)*4.20
        return cbill
    elif(tu>100 and tu<=200):
        cbill=(3.80*50)+(4.20*50)+(tu-100)*5.10
        return cbill
    elif(tu>200 and tu<=300):
        cbill=((3.80*50)+(4.20*50)+(100*5.10)+(tu-200)*6.30)
        return cbill
    else:
        cbill=((3.80*50)+(4.20*50)+(100*5.10)+(6.30*100)+(tu-300)*7.5)
        return cbill
print("The CURRENT BILL IS",cbill(tu))