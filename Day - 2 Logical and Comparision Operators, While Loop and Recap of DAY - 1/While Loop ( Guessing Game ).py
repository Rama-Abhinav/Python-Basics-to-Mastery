# A gussing game in which a word with max of 10 letters is kept as the secret word and the player is given enough chances to guess the word and after each failed try they get to try again x times and before each try they can see a letter of the word appear.

Secret_Word = "Guessing"                                                                        # Manual Input of Word

Trail_Count = 1                                                                                 # While Loop Control Counter Variable

if len(Secret_Word) <= 10:                                                                      # If length of the word given to guess has less than 10 letters then do as follows

    while Trail_Count<= len(Secret_Word):                                                       # Intiating While Loop with limit of interations equal to no.of letter in the word.

        x = (input("Guess the word: ").upper().strip())                                         # Taking Guess Input from User everytime the while loop runs

        if x == Secret_Word:                                                                    # If the gussed word is correct, tell the user the guessed word is correct and break while loop
            print("That's Awesome you have gussed the right word..!!")
            break

        elif Trail_Count <= (len(Secret_Word)-1):                                               # Otherwise if, the gussed word is wrong then generate a hint in the form of Letter(s) and dashes [Ex. R_ _ _] and tell to try again and re-run while loop 
            print(f''' Hint: {Secret_Word[:Trail_Count]}{"_"*(len(Secret_Word) - Trail_Count)}
Try Again You Are Almost there...! ''') 
        
        elif Trail_Count == len(Secret_Word):                                                   # Finally if the player has not gussed the correct word and reached the last guess and got that also wrong then, Tell that the gusses have maxed out and show the secret word
            print(f'''Gusses Maxed Out!! Try Again..
The Secret Word is "{Secret_Word}" ''')
        
        Trail_Count += 1                                                                        # Incrementing While Loop Control Counter Variable To Make sure the while loop runs only for required no.of times and not run infinitely

else:                                                                                           # If length of the word given to guess has more than 10 letters then do as follows
    print('Word Given is too long!!!')
    
        