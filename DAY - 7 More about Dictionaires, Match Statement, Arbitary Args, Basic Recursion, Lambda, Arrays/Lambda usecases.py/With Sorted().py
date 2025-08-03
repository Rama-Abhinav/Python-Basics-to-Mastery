#🧠 Problem: Sort People by Age: Given a list of tuples with names and ages, use sorted() and lambda to sort the list by age.

people = [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('Rama',18)]


BY_AGE = sorted(people, key=lambda x : x[1], reverse=False)
print(BY_AGE)