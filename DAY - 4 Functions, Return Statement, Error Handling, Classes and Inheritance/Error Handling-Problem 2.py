# Problem 2: List Index Lookup
    # Description:
        # Create a list of 5 elements and ask the user to enter an index to access. Use try and except to handle:
        # Index out of range (IndexError)
        # Invalid index input (e.g., letters instead of numbers) (ValueError)
            # Expected Behavior:
                # Enter index (0-4): 10
                # Error: Index out of range.

##----------------SOLUTION----------------##

#Trying to make a list of 5 elements and asking the user to inter an index value to get the element at that index
def Solution_1():
    try:
        Elements_Collection = ["","MARK 1", "MARK 2", "MARK 32", "MARK 55","IRON MAN"]
        User_input = str(input(f'''
    {Elements_Collection[1:6]}                       
    Enter an index value of the element you would like to access(1-5) from the above list: '''))
        User_input = int(User_input)
        print(Elements_Collection[User_input])

    #Dealing with and index error
    except IndexError:
        print(f"Entered value '{User_input}' is not the index range specified !! ")

    #Dealing with value error
    except ValueError:
        print("Invalid Input Type !!")

    if User_input==0:
        print("Index 0 is not available")


## Better Method ---> Generated on discussion of this problem with chaptgpt
def Solution_2():
    try:
        Elements_Collection = ["MARK 1", "MARK 2", "MARK 32", "MARK 55", "IRON MAN"]

        # Printing all index-item pairs in one line
        print("Available elements in the list:")
        print(" | ".join([f"{idx} ➤ {element}" for idx, element in enumerate(Elements_Collection)]))

        # Asking for user input
        User_input = int(input("Enter an index (0 to 4) to access the element: "))
        
        # Accessing the element
        print(f"Element at index {User_input} ➤ {Elements_Collection[User_input]}")

    except IndexError:
        print("❌ Error: That index is out of range! Please enter a number between 0 and 4.")

    except ValueError:
        print("❌ Error: Invalid input. Please enter a number (e.g., 0, 1, 2, ...).")

Solution_1()