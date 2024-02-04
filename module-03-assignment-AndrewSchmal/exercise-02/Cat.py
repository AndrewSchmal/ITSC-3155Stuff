from Animal import Animal

class Cat(Animal):
    def get_greeting(self):
        return f"{self.name} says meow"

    def get_food_preference(self):
        return f"{self.name} wants chicken"

    def get_appearance(self):
        return f"{self.name} has {self.color} fur"
