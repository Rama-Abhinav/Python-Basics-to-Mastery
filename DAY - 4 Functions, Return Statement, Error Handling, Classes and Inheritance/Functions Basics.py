# Function : Blocks of personalized reusable code.

# Defining a function
def My_1st_Function():
    print("This is my 1st function !!")

# Calling Function :-
My_1st_Function()

# Adding Parameters to a function
def func_with_parameters(name, Year_of_birth, Present_Year):
    print(f'''
HEY ! {name}, 
Since you were born in the year {Year_of_birth} 
and now the year is {Present_Year}.
You are {(Present_Year - Year_of_birth)} Years old . 🤩
''')
    
func_with_parameters("Rama Abhinav", 2007, 2025)

#Using Keyword arguments
func_with_parameters(name="Kishore",Year_of_birth=1980,Present_Year=2025)

# Return Statement : Used only within a function. When in action, it exits the functions and returns a value using the given expression back to the caller of the funtion. By default all functions return "NONE".
## Useful in functions related to calculations and math 
def calc_return_func(num):
    return num*num

print(calc_return_func(2)) #Without return the output would have been : 4 None



    


