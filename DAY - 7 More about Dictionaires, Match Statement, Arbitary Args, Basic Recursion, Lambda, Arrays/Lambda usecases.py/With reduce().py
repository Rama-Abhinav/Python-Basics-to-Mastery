#🧠 Problem: Multiply All Numbers : Use reduce() and lambda to multiply all numbers in a list together.

user_input = input("enter numbers seperated by commas (like 1,2,3,4...etc): ").split(",")
user_input = [int(x) for x in user_input]

from functools import reduce

Product = reduce(lambda x,y : x*y, user_input)
print(Product)