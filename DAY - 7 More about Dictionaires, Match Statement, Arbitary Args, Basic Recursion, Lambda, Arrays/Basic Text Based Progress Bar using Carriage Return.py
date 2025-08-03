import time

for i in range(101):
    bar = "█"*(i//2) + "-"*((100-i)//2)
    print(f"\r[{bar}] {i}%",end="")         # Always add end="" with \r to avoid line breaks
    time.sleep(0.3)