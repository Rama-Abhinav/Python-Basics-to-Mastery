import re

names = ['Finn   Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

# Finding Words with only 1st and last name 
regex = r'^\w+\s+\w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(name,":", result,'\n')

# Searching for word Char squence starting with C
regex_1 = r'C\w*'
for name in names:
    result = re.search(regex_1, name)
    if result:
        print(name)
        print(f"Start Char = {result.start()} and Stop Char = {result.end()}")
        print(f"Span of check for {name} is {result.span()} for the sub string {result.group()}\n")

names = ['Brian Daugette',
         'Veronica Supersonica',
         'Tony Gasparovic',
         'Patrick Germann',
         'm!sha']

#Printing 1st and last name seperately by grouping 
regex_2 = r'^(?P<First_name>\w+)\s+(?P<Lastname>\w+)$'

for name in names:
    match = re.search(regex_2, name)
    if match:
        print(name)
        print(f"1st name is : {match.group("First_name")}")
        print(f"Last name is : {match.group("Lastname")}\n")

#Detect last name 
regex = r'^[a-zA-Z!]+$'   ## [] --> Anything specified inside this is allowed set of chrecters in Match test
for name in names:
    match = re.search(regex, name)
    if match:
        print(name,'\n')

#Scanning for blocks of lower case letters
regex = r"[a-z]+"
for name in names:
    scan = re.findall(regex, name)
    print(scan,"\n")

#Checking all occurance of https or http
values = ['https://www.socratica.com',
          'http://www.socratica.org',
          'file://test.this.path',
          'com.socratica.www_https://']

regex = "https?"    #"https?" in regex means:"http" part is fixed. The s? means: Match zero occurrences of "s" (so just "http") OR match one occurrence of "s" (so "https").
for val in values:
    Match = re.match(regex, val)
    if Match:
        print(val)
    
