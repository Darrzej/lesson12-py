from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass 

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is saying woof woof")

    def move(self):
        print(f"{self.name} is running fast") 

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} is saying ciu ciu")

    def move(self):
        print(f"{self.name} is flying high")

animals = [
    Dog("Kuci"),
    Bird("Diddy")
]         

def describe_animal(Animal):
    Animal.make_sound()
    Animal.move()
    Animal.sleep()



for kafshet in animals:
    print("Animals information:")
    describe_animal(kafshet)
    
    



