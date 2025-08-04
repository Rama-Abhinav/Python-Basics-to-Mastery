"""
Objective:
    Create a custom iterator class called ReverseString,
    that takes a string and returns its characters in reverse order, one character at a time.

Input:
    rev_iter = ReverseString("Python")

    Using:
    for ch in rev_iter:
        print(ch)

Output:
    n
    o
    h
    t
    y
    P

"""

class ReverseString:

    def __init__(self,Word):
        self.Word = Word
        self.index = len(Word)-1    # Takes the index from the last charecter as no.of letters - 1 gives the last index value 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0 :
            raise StopIteration
        else:
            Letter = self.Word[self.index] # Get charecter at current index 
            self.index-=1                  # Move to previous charecter
            return Letter
        
String = ReverseString("RAMA")

for letter in String:
    print(letter)
        

