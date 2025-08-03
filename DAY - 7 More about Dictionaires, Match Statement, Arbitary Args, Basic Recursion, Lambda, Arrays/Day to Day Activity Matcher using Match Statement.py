"""
🧪 Exercise: Day to Activity Matcher

    📝 Task:

        Write a Python program that asks the user to enter a day of the week (e.g., "Monday", "Tuesday", etc.) 
        and then uses a match statement to print an activity for that day.
            
    ✅ Example Output:

        Enter a day: Wednesday  
        Activity: Gym and coding practice
"""

#---------------------- SOLUTION-------------------------#


user_input=str(input("Enter a Day of the Week(Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday): ")).capitalize().strip()

match user_input:
    case "Monday":
        print("Study Python")
    case "Tuesday":
        print("Go for a walk")
    case "Wednesday":
        print("Gym and coding practice")
    case "Thursday":
        print("Watch a tech documentary")
    case "Friday":
        print("Work on a mini project")
    case "Saturday":
        print("Play games or chill")
    case "Sunday":
        print("Weekly review and plan next week")
    case _ :
        print("Please Enter A Day From the Given Options !!")