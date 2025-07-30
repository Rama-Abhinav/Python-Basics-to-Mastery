# A emoji generator the user can use based on the given emotional options available at the start of the program


## Telling User the Available Emotions
print('''
!! Welcome to Emotional Emoji !!

Available Emotions to Convert are :-
    1.Happy
    2.Excited
    3.Sad
    4.Annoyed
    5.Scared

''')

##Making a Dictionary of all the emotions we have told, can be converted from.
Emotional_Dictionary = {
    'Happy': "😃",
    'Excited': "🤩",
    'Sad': "☹️",
    'Annoyed': "😑",
    'Scared': "😨"
}

while True:
    ##Asking user to select the emotion they are feeling
    User_Emotion = input("HOW ARE YOU FEELING TODAY? (enter as shown above):  ").capitalize().strip()
    #Matching user emotion with emotional dictionary to generate respective emoji
    if User_Emotion in Emotional_Dictionary:
        print(Emotional_Dictionary[User_Emotion])
    else:
        print("Emotion not yet updated !!")
    #Asking the user if they want to try again.
    Repeat = input('''
Do You Want to try again? (YES / NO): ''').upper().strip()
    if Repeat == "YES":
        continue
    else:
        print("THANK YOU FOR USING !!")
        break
    

    

        

       


