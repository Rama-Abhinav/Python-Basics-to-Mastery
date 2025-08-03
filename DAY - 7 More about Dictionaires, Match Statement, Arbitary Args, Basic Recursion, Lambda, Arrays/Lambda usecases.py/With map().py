# 🧠 Problem: Square All Numbers: You have a list of numbers. Use map() and lambda to create a new list where each number is squared.

user_input = input("enter numbers seperated by commas (like 1,2,3,4...etc): ").split(",")
user_input = [int(x) for x in user_input]

Squared_List = list(map(lambda x : x**2, user_input))
print(f"Squared List of Numbers for {user_input} are {Squared_List}")