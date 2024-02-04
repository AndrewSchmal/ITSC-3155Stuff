from Animal import Animal

class Dog(Animal):
    def get_greeting(self):
        return f"{self.name} says woof"

    def get_food_preference(self):
        return f"{self.name} wants steak"

    def get_appearance(self):
        return f"{self.name} has {self.color} fur"
