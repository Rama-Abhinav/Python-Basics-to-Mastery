#Conditional Statements are: if..elif..else

#Problem Statements
#1. Based on whether the wheather is cold or hot suggest person to wear warm clothes or drink plenty of water respectively and if none then wish them a lovely day

print('''How is the weather in your area?
         Is it HOT or COLD?''')
User_Input=input('It Is --> ')
User_Response=(User_Input.upper())
print(User_Response)
if User_Response == 'HOT' :
    print('''Hey!! Since the weather is hot,
Drink ample amount of water and 
stay away from the sun in shade. ''')
elif User_Response == 'COLD':
    print('''Hey!! Since the weather is cold,
Keep yourself warm by wearing a sweater 
and Drinking some hot ginger tea.''')
else:
    print('''
No Update about the weather
Have a nice day ahead
          ''')
    
#2.Price of a house is $1M.If buyer has good credit,they need to put down 10%Otherwisethey need to put down 20%.Print the down payment

print('''Welcome Buyer, The house you are seeing is on sale for $1million.
Please let u know your credit score based on the below scale:-
Option(1): 500 - 700
Option(2): 350 - 500
Option(3): Below 350''')

user_input=input("Please Enter Option Number(1/2/3): ")

if user_input == '1':
    print(f'You will have to pay 10% i.e. ${(10/100)*1000000} as Downpayment')
elif user_input == '2':
     print(f'You will have to pay 20% i.e. ${(20/100)*1000000} as Downpayment')
elif user_input == '3':
     print(f'You will have to pay 40% i.e. ${(40/100)*1000000} as Downpayment')
else:
     print("No Option Entered, Please Try Again. Thank You")