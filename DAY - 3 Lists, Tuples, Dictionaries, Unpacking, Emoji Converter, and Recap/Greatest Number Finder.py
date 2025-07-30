# Take an input of 10 random numbers for a user and find the largest and the smallest number from the entered numbers without using in-build functions of python.

user_nums=input('''ENTER 10 RANDOM NUMBERS SEPERATED BY SPACES: ''')# .split()

Num_list=[int(x) for x in user_nums.split()]  # List Comprehension

if len(Num_list)>10:
    Num_list = Num_list[0:10]
    print('''You have entered more than 10 numbers, therefore only the 1st ten numbers entered are considered.
           ''')
else:
    pass

Max_Num=Num_list[0]
Min_Num=Num_list[0]

for Num in Num_list:            #For loop to check the max and min numbers in the list
    if Num > Max_Num:
        Max_Num = Num
    elif Num < Min_Num:
        Min_Num = Num

print(f"The Greatest Number is {Max_Num} and The Smallest Number is {Min_Num}")
    