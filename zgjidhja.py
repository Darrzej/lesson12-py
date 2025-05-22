from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value<0:
            raise ValueError("Smun negativ")
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value<0:
            raise ValueError("Smun negativ")

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(
            f"Name:{self.name}, Age:{self.age}, Weight:{self.weight}, Height:{self.height}"
            f"{self.calculate_bmi(), {self.get_bmi_category()}}"
        )        
        
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi<18.5:
            return "underweight"
        elif 18.5<= bmi < 24.5:
            return "Normal weight"
        elif 24.5<= bmi < 29.0:
            return "overweight"
        else:
            return "obese"
            


class Adult(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) *1.3
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi<15.5:
            return "underweight"
        elif 15.5<= bmi < 20.5:
            return "Normal weight"
        elif 20.5<= bmi < 24.0:
            return "overweight"
        else:
            return "obese"

class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self,person):
        self.people.append(person)    

    def collect_user_data(self):
        name = input("Enter name")
        age = int(input("Enter age:"))
        weight = float(input("Enter weight:"))
        height = float(input("Enter height:"))

        if age>=18:
            person = Adult(name,age,weight,height)
                