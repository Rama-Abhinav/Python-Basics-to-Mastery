# Defining a module called utils in which I will define basic functions like find_max(), find_min(), find_Sum() Of a given list.

def find_max(x):
    Max = x[0]
    for element in x:
        if element > Max:
            Max = element
    print(Max)
        
def find_min(x):
    Min = x[0]
    for element in x:
        if element < Min:
            Min = element
    print(Min)

def find_sum(x):
    Sum = 0
    for num in x:
        Sum += num
    print(Sum)

