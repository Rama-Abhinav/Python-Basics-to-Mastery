class Person:
    def __init__(self,name):
        self.name = str(name)
    
    def talk(self):
        print(f"Hello World !! My Name is {self.name} ")

P1 = Person('Rama')
P1.talk()


