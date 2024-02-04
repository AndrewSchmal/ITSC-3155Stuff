from Animal import Animal

class Penguin(Animal):
    def get_greeting(self):
        return f"{self.name} says squawk"

    def get_food_preference(self):
        return f"{self.name} wants fishes"

    def get_appearance(self):
        return f"{self.name} has {self.color} feathers"
