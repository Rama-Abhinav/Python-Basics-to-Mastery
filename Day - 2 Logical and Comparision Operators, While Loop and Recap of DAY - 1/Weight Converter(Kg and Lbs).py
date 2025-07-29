# Write the code to take input of the user weight and units and then convert to the other units (Kg <---> Lbs)

Weight_User = int(input("Enter Your Weight : "))       # Used int() to make sure we do not get a error during calculations in the 7th and the 9th step as it would have taken the input as a string data type
Units_Weight=str(input('Kg(K) or Pounds(L):').upper())

if Units_Weight == 'K':
    print(f"Your Weight is {Weight_User*2.2}lbs ")
elif Units_Weight == 'L':
    print(f"Your weight is {Weight_User/2.2}Kg ")
else:
    print("Invaild Input!!!")

