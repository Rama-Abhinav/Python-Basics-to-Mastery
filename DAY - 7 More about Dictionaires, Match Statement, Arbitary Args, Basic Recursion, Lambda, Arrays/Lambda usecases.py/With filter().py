#🧠 Problem: Keep Names Longer Than 4 Characters: Given a list of names, use filter() and lambda to keep only names with more than 4 letters.


user_input = input("enter names (like; Amy, Bob, Clara, David, Eli): ").split(",")

Name_FourLetters = list(filter(lambda x : len(x)> 4, user_input))
print(f"From the given list {user_input} the names with more than 4 letters are {Name_FourLetters}")

