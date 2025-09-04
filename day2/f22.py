def strong(w):
    for n in range(1, w + 1):
        temp = n
        total = 0
        while temp > 0:
            r = temp % 10
            fact = 1
            for i in range(1, r + 1):
                fact *= i
            total += fact
            temp //= 10
        if total == n:
            print(n)

x = int(input("Enter a number: "))
strong(x)
