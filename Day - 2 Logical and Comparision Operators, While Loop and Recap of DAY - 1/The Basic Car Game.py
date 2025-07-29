# A basic car game in which the user can start, stop, change the speeds of the car and Quit the game.

initial_Speed = 10                                                                                                              #Intital Speed of the car and Changed Speed of the car when increased or decreased.
Variating_Speed=10                                                                                                              #The Variable speed of the car that keeps changing and then updates the initial speed.

User_Initiation=input('''Welcome to The Text Car Game !
Type "Controls" to find out the controls in the game:  ''').upper().strip()                                                     #The Controls command that opens/intializes the game after which all commands in the game can be accessed and used to play the game.

if User_Initiation == "CONTROLS":                                                                                               #Starting the game only if the initialization command "Controls" is given.

    print('''                                                                                                                   
The Controls of the game are:-
1. START -> To Begin the game.
2. STOP -> To End the game.
3. SPEED  -> To Change speed of vehicle
4. EXIT -> To Quit the game.
          ''')                                                                                                                  #These are the commands that can used to play the game. Here we are showing them to the player.
    
    while True:                                                                                                                 #Iterating all the commands do that the user can play the game till they want

        Control_Input=input("Enter Command >>  ").upper().strip()

        if Control_Input == "START":                                                                                            #Code Block for the START Command
            print(f'''!! THE GAME HAS BEGUN !!
The Car has started and is moving at {initial_Speed}Km/h ''')
            while True:                                                                                                         #This loop iterates the commands of speed and stop that can be used by the user to play the game. Once the game is stopped, the player needs to start again in order to play the game as the stop code block breaks this loop.
                Control_Input=input("Enter Command >>  ").upper().strip()

                if Control_Input == "SPEED":                                                                                    #Code Block for the SPEED Command

                    UP_DOWN=input("Do You Want to Increase [UP] or Decrease [DOWN] the speed of the car: ").upper().strip()     #Asking user whether they want to increase or decrease the speed

                    if UP_DOWN == "UP":                                                                                         #Code Block to increase speed
                        Speed_UP=int(input("How much would you like the speed to be increased by (Only Numbers) >> "))
                        Variating_Speed += Speed_UP
                        print(f"The Speed of the car has increased from {initial_Speed}Km/h to {Variating_Speed}Km/h")
                        initial_Speed = Variating_Speed

                    elif UP_DOWN=="DOWN":                                                                                       #Code Block to Decrease speed
                        Speed_DOWN=int(input("How much would you like the speed to be Decreased by (Only Numbers) >> "))
                        Variating_Speed -= Speed_DOWN
                        print(f"The Speed of the car has Decreased from {initial_Speed}Km/h to {Variating_Speed}Km/h")
                        initial_Speed = Variating_Speed  

                    else:                                                                                                       #Code Block to execute if the player wants to neither increase nor decrease the speed
                        print(f"Car Speed at {initial_Speed}Km/h")

                elif Control_Input == "STOP":                                                                                   #Code Block for the STOP Command.
                    print("Breaks Applied!!!! --- Car At Rest...")
                    break

        elif Control_Input == "EXIT":                                                                                           #Code Block for the EXIT Command, This command breaks the whole while loop and ends the game and thanks the user for playing our game.
                print("Game has Ended.....Thank You For Playing")
                break

        else:                                                                                                                   #This Block of Code asks the user to start the game, in case, they have stopped the game or are restarting after quitting the game the previous time.
            print("!! START THE GAME !!")

else:                                                                                                                           #This block of code tells the user to enter controls in the user initiation phase of the game above
    print("Command Not Found..!!  ENTER 'CONTROLS' ")



    
