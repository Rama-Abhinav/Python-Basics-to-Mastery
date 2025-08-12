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


def Animal_Sounds(Animals_List):
    for animal in Animals_List:
        animal.Speak()

Animal_Sounds([Dog(),Cat(),Parrot()])

