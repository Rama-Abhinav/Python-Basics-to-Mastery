# Q) Write code to take input from the user their name, the name should be alteast 3 charecters and max of 50 charecters
# Solution:-
name = input("Enter your name: ")
if len(name) < 3 :
    print("Name should be alteast 3 charecters")
elif len(name) > 50 :
    print("Name should be max of 50 charecters")
else:
    print(f"Hey! {name}, You have a nice name....")