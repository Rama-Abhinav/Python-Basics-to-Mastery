#Importing and using the utilities file 

import Utils
from Utils import find_sum

User_input = str(input("Enter 5 Numbers Seperated by commas(,): ")).split(",")
User_input = [int(num) for num in User_input]

Utils.find_max(User_input)
Utils.find_min(User_input)
find_sum(User_input)


