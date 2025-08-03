# Exploring new methods with dictionaires

Dictionary = {
    "L1":"A",
    "L2":"B",
    "L3":"C",
    "L4":"D",
    "L5":"E"
}

#Accessing Keys, Value and Items from a dictionary
print(Dictionary.keys())        
print(Dictionary.values())
print(Dictionary.items())

#Adding Keys, Values and Items to a dictinary
Dictionary.update({"KEY":"Value"}) ## Adding the item {KEY : Value} to the Dictionary
print(Dictionary)

Dictionary["Key_Index"] = "Value_Index"
print(Dictionary)

#Methods to remove items from dictionary 
Dictionary.pop("L4")
print(Dictionary)

Dictionary.popitem() #Remove the last item from the dictionary i.e. 'Key_Index': 'Value_Index'
print(Dictionary)

del Dictionary["L5"]
print(Dictionary)

DictionarytoDelete = {
    "L1":"A",
    "L2":"B",
    "L3":"C",
    "L4":"D",
    "L5":"E"
}

del DictionarytoDelete
try:
    print(DictionarytoDelete)
except NameError:
    print("\nThe Whole Dictionary has been Deleted !!\n")

DictionarytoClear = {
    "L1":"A",
    "L2":"B",
    "L3":"C",
    "L4":"D",
    "L5":"E"
}

DictionarytoClear.clear()
print(DictionarytoClear)

New_Dictionary = Dictionary.copy()
print(f"\n{Dictionary} has been copied into {New_Dictionary}")

