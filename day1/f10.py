def conversion(x):
    years=round(x/365,2)
    months=int(x/30)
    print(f"{x} days={years} years and {months} months")
conversion(234)