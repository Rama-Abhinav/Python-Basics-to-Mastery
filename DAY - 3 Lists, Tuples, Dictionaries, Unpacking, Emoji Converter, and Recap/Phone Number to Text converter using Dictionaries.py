# Taking a 10 digit phone number from a user and converting into text form.

Number_Dictionary = {
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
}

User_Num = input("Enter Phone Number: ")

Digit_List = [int(Digit) for Digit in str(User_Num)]

Text_Num=[]
while True:
    if len(User_Num)==10:
        for Digits in Digit_List:
            for Numbers in Number_Dictionary:
                if Digits == Numbers:
                    Text_Num.append(Number_Dictionary[Numbers])
        print('-'.join(Text_Num))         
        break   
    else:
        print(f"Entered Number Has only {len(User_Num)} while it should have 10!!")
        break