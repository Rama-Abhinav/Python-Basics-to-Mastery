# Problem 1: Divide and Conquer
    #Description:
    #Ask the user to input two numbers and divide the first number by the second. Use try and except to handle the following errors:
    #Division by zero (ZeroDivisionError)
    #Invalid input (e.g., the user enters letters instead of numbers)
        #Expected Behavior:
            #Enter numerator: 10
            #Enter denominator: 0
            #Error: You cannot divide by zero.

##  ------------------- SOLUTION ------------------------ ##

try:
# Taking user input for numerator and denominator as both int and float
    print("Enter Valid Numbers like 1 ,2.5, 0.2, etc.")
    numerator = str(input("Enter Numerator: "))
    denominator = str(input("Enter Denominator: "))

#Converting Recieved Strings to Floats so that i can take both integers and decimals as values
    numerator = float(numerator)
    denominator = float(denominator)

#Trying to Divide Numerator by Denominator and Handling Recieved Errors
    Result = (numerator/denominator)
    print(Result)

#Dealing with ZeroDivisionError
except ZeroDivisionError:
    print(" !!! YOU CANNOT DIVIDE AN NUMBER BY ZERO ( 0 ) !!! ")

#Dealing with ValueError
except ValueError:
        print(" Invalid Type Of Values Entered !! ")


