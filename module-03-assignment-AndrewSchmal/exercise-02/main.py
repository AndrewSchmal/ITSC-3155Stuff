# Updated import to include the new Dolphin class
from Cat import Cat
from Dog import Dog
from Penguin import Penguin
from Dolphin import Dolphin  # Added import for the new Dolphin class

# Updated list of animals with a new instance of Dolphin
animals = [
    Cat('Piero', 'orange'),
    Dog('Robin', 'blonde'),
    Penguin('Pete', 'black and white'),
    Cat('Shadowspawn', 'black'),
    Dolphin('Nifalap', 'blue'),  # Adding a new instance of Dolphin
]


for animal in animals:
    print('Greeting:')
    print(animal.get_greeting())

    print('\nFood Preference: ')
    print(animal.get_food_preference())

    print('\nAppearance:')
    print(animal.get_appearance())

    print()

# removed og dictionaries & declarations