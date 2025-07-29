#Defineing a string by assigning it to a variable
String = "Python Is Awesome!!"
print(String)

#Indexing String
print(String[0:6]) #Positive Index
print(String[-9:-2]) # Negative Index
print(String[::2]) #Step Index

#Formated String
String_1="Python"
String_2="Awesome!!"
print(f'{String_1} is {String_2}, Its the Best..')

#String Methods
##len()
print(len(String))

##.upper and .lower
print(String.upper())
print(String.lower())

##.find
print(String.find('I'))

##.Replace
print(String.replace('Awesome', 'Fantastic'))

## in
print("Python" in String)
print('Fantastic'in String)

#Multi-Line String
Paragraph='''

My Name is Rama Abhinav 

I like Python !!

'''
print(Paragraph)
