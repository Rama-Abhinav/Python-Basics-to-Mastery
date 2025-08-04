"""
Objective: Create a custom iterator class called "EvenNumbers" that returns all even numbers between a given start and end (inclusive).

    ➕ Input:

        even_iter = EvenNumbers(4, 15)

    ✅ Output:
        Using:

        for num in even_iter:
            print(num)

        You should get:

        4
        6
        8
        10
        12
        14
"""


class EvenNumbers:

    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):         # Initializes the iterator class
        return self
    
    def __next__(self):                         
        while self.current <= self.end:         
            val = self.current
            self.current += 1
            if val % 2 == 0:
                return val
        raise StopIteration                 


for i in EvenNumbers(4,15):
    print(i) 
    

# Mistake I Learnt from :-
"""
def __next__(self):
    if self.start >= self.end:
        raise StopIteration
    else:
        val = self.start
        if val%2==0:
            self.start += 1
            return val
        else:
            self.start += 1

If the number is even, it correctly returns the value.

But if the number is odd, you increase self.start, but you don’t return anything, which means Python implicitly returns None.

So the loop prints None for those iterations where val was odd.

✅ How to Fix It:
You need to keep skipping numbers until you find the next even one before returning. 
You can do this by using a while loop inside __next__().


"""

                

