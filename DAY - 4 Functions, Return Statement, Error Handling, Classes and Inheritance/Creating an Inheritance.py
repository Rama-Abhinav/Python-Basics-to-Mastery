# Learning the concept of inheritance

class Parent:

    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def I_AM_PARENT(self):
        print(f"{self.father} and {self.mother} are my parents.")

class Child(Parent):

    def __init__(self, father, mother, child_name):
        Parent.__init__(self,father, mother) #or# super()._init_(father, mother)
        self.child_name = child_name

    def My_Name(self):
        print(f"My name is {self.child_name}")

Child1 = Child("HARRY", "MARY", "BEN")
Child1.I_AM_PARENT()
Child1.My_Name()
        