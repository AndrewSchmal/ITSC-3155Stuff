from Animal import Animal

class Dolphin(Animal):
    def get_greeting(self):
        return f"{self.name} says eek eek"

    def get_food_preference(self):
        return f"{self.name} loves jellyfish and squid"

    def get_appearance(self):
        return f"{self.name} has shiny, blue skin"
