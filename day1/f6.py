cno=int(input("Enter the consumer number"))
cname=input("Enter the consumer name")
pmr,lmr=map(int,input("Enter the present month reading adn last month reading").split())
tu=pmr=lmr
cbill=tu*3.80
print(f"Consumer number {cno}\nConsumer Name{cname}\nPresent month reading{pmr}\nLast Month Reading{lmr}\ntotal units {tu}\nCurrent bill{cbill}")