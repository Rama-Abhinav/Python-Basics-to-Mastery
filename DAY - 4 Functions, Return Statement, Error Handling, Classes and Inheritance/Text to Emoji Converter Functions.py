#This is the main function
def emoji(User_Words):
    words = User_Words.split(" ")
    emojis = {
        ":)" :'😃' ,
        ":(" :'☹️'
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return(output)

# I have Put the whole emoji function in this function for ease of access
def Run():
    user_input = input(">")
    print(emoji(user_input))

for x in range(5):
    Run()
