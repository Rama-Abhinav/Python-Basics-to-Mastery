#LISTS - Denoted by '[]'

Names=['Rama', 'Abhinav', 'Krishna', 'Jen', 'Ravi']     # Defining a list and assigning it to a variable.

print(Names)                                    # Print the list as it is.

#Indexing lists; list_name[x:y], this produces a list with the elments including x element till the element before y i.e. y is not printed as range ends at y.

print(Names[0:4])                               # Indexing the list using positive values
print(Names[0:5])                               # To Print all elements index end should be 1 more than no.of elements in list.
print(Names[-5:])                               # Indexing using negative values

Names[1] = 'George'                             # Replacing elements in the list
print(Names)

