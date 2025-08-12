class Animal:
    def Speak(self):
        pass

class Dog(Animal):
    def Speak(self):
        print("BOW BOW BOOWWWWWW")
    
class Cat(Animal):
    def Speak(self):
        print("Meowwwwwwww")

class Parrot(Animal):
    def Speak(self):
        print("I AM A GREEN PARROT !!")


def Animal_Sounds(Animal_List):
    for animal in Animal_List:
        if animal == "DOG":
                Animal_Sound=Dog()
                Animal_Sound.Speak()
                continue
        elif animal == "CAT":
                Animal_Sound=Cat()
                Animal_Sound.Speak()
                continue
        elif animal == "PARROT":
                Animal_Sound=Parrot()
                Animal_Sound.Speak()
                continue
        else:
             print("inavlid input")
            

User_Animal = (str(input("Enter all or any of the following [Dog, Cat, Parrot] seperated by commas: ").upper().strip())).split()
print(User_Animal)
Animal_Sounds(User_Animal)

"""
XXX Animal_Sounds function is using a bunch of if/elif checks to figure out which animal to create.
    That means I AM  deciding the type in the function, instead of letting polymorphism do it for Me.
"""