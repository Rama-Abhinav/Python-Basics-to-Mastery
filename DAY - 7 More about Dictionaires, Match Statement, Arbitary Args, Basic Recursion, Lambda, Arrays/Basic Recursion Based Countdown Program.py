def Countdown(n):
    if n>0:
        print(n)
        Countdown(n-1)
    else:
        print("Times's Up !!!")

Countdown(10)