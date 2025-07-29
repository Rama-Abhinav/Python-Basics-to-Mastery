Num1=100
Num2=10
Num3=5
Num4=3

#Addition(+)
print(Num1+Num2+Num3+Num4)

#Subtraction(-)
print(Num1-Num2)

#Multiplication 
print(Num2*Num4)

#Division
print(Num3/Num4) #Floating Division
print(Num3//Num4) #Integer Division

#Modulous(%); Gives Remainder
print(Num3%Num4)

#Exponents(**)
print(Num2**Num3) 

#Augmented Assignment Operator
Num1=Num1+100 #Ans : 200
print(Num1)
Num1 += 200   #Ans : 400  ------>> AUGMENTED ASSIGNMENT OPERATOR
print(Num1)
Num2 -= 10    #Ans : 0
print(Num2)

Num1=100 # Reset Value for further Operations 

#Operator Precedence (Order in which operations take place when applied in code)
## Paranthesis -----> Exponentiation ------> Multiplication or Division ------> Addition or Subtraction
OP_Num1=10+3*2**4  #Ans: 58
OP_Num2=((10+3)*2)**4 #Ans: 4,56,976
print(f'{OP_Num1} & {OP_Num2} are examples of operator precedence')

#Basic Math Functions and Math Module
print(round(int(10/3)))
print(abs(float(-3.54)))

import math #{Link to Documentation : #https://docs.python.org/3/library/math.html#math.isnan}
print(math.ceil(float(5/2)))  #Max Round OFF
print(math.floor(float(5/2))) #Min Round OFF

