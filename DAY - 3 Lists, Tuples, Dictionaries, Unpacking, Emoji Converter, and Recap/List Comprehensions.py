# What is List Comprehension? : List comprehension is a compact syntax for generating a new list by applying an expression to each item in an iterable (like a list, string, or range).

# 1. Create a list of the squares of numbers from 1 to 10.

Squaring_Comprehension = [int(x**2) for x in range(1,11)]           # Syntax : EXPRESSION for ITEM in ITERABLE
print(Squaring_Comprehension)

print('''
      --------------------------------------------------
      ''')

# 2. Use list comprehension to get only even numbers from 1 to 200.

Even_Nums_Find = [int(x) for x in range(1,201) if x%2==0]           # Syntax : EXPRESSION for ITEM in ITERABLE CONDITIONAL
print(Even_Nums_Find)

print('''
      --------------------------------------------------
      ''')

# 3. Given this list of words: words = ["AI", "robot", "future", "is", "now", "big"] . Use list comprehension to extract words with more than 3 letters.

Words_Lessthan3 = [word for word in ["AI", "robot", "future", "is", "now", "big"] if len(word) > 3 ]
print(Words_Lessthan3)

print('''
      --------------------------------------------------
      ''')

# 4. From the same list:["AI", "robot", "future", "is", "now", "big"]. Get only the words with 3 or fewer characters, and return them in UPPERCASE.

uppercase_versions_of_short_words = [word.upper() for word in ["AI", "robot", "future", "is", "now", "big"] if len(word)<=3 ]
print(uppercase_versions_of_short_words)

print('''
      --------------------------------------------------
      ''')

# 5. Nested List Comprehensions : Create a 3x3 multiplication table (like a grid), using nested list comprehension.

Table_3x3=[[i*j for j in range(1,6)] for i in range(1,11)]   # loop 1 {for j in range(1,4)} : Specifies no.of Mutiples to generate in each table AND Loop 2 {for i in range(1,10)} : Specifies the numbers of which multiples need to be printed.
print(Table_3x3)

print('''
      --------------------------------------------------
      ''')

# 6.  From numbers 1 to 30; Keep even numbers as they are. Replace odd numbers with the string "ODD"

Replace_Odd = ["ODD" if x%2 != 0 else x for x in range (1,31)]  # Ternary Function or Inline if - else function
print(Replace_Odd)

print('''
      --------------------------------------------------
      ''')

# 7. From numbers 1 to 50:🔹 Replace odd numbers divisible by 5 with the string "ODD-FIVE"🔹 Replace other odd numbers with "ODD"🔹 Keep even numbers as they are ❌ Exclude (filter out) the number 25 completely — don't include it at all.

Mixed_Filtering_Replacement = [ "ODD-FIVE" if x%2!=0 and x%5==0 else  "ODD " if x%2!=0 else x for x in range(1,51) if x != 25 ]
print(Mixed_Filtering_Replacement)

##------------OR-------------##

Nums = list(range(1,51))

for Num in Nums:
    if Num%2!=0:
        if Num == 25:
            Nums.remove(Num)
        elif Num%5==0:
            Nums[Nums.index(Num)]="ODD-FIVE"
        else:
            Nums[Nums.index(Num)]="ODD"
        
    else:
        pass

print(Nums)

# But this method has drawbacks:-
#  You are removing and replacing elements while looping over the same list (Nums). This causes:
#   Items to be skipped
#   Wrong replacements
#   ValueError or inconsistent behavior

# Best version of above code is:-

Nums = list(range(1,51))
New_Nums=[]

for Num in Nums:
    if Num == 25:                         #Skips 25 entirely 
        continue 
    elif Num%2!=0 and Num%5==0:                           
        New_Nums.append("ODD-FIVE")
    elif Num%2!=0:
        New_Nums.append("ODD")
    else:
        New_Nums.append(Num)
        
print(New_Nums)