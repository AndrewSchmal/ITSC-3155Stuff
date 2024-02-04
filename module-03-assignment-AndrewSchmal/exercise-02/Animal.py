from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_greeting(self):
        pass

    @abstractmethod
    def get_food_preference(self):
        pass

    @abstractmethod
    def get_appearance(self):
        pass


# https://www.geeksforgeeks.org/abstract-classes-in-python/ and BroCode youtube vids