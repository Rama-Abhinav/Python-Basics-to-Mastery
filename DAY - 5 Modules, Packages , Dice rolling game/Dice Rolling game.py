# The user is going to say roll and everytime they do so a random pair of numbers are printed in the format (num_1, num_2). num_1 being the value on the 1st dice and num_2 being the value on the 2nd dice respectively.
# Using random() functions here

# Basic Method

import random

user_start = str(input("TO START TYPE 'ROLL': ")).upper().strip()

if user_start == "ROLL":
    Dices = [(num_1,num_2) for num_1 in range(1,7) for num_2 in range(1,7) ]
    print(random.choice(Dices))
else:
    print("Thank YOU for playing!!")

#------------------------------------------------------------------------------#

# Using classes to roll dice

import random


class Dice:
    
    def roll(self):
        return(random.choice([(num_1,num_2) for num_1 in range(1,7) for num_2 in range(1,7)]))   # Using Return to avoid "NONE"


print(Dice.roll())


