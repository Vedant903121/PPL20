class Animal:
    def __init__(self, legs = 4, eyes = 2):
        self.legs = legs
        self.eyes = eyes
class wild_ani(Animal):
    def place(self):
        print('Jungle')
    
class carnivore(wild_ani):
    def food(self):
        print("Meat")
class tiger(carnivore):
    def speak(self):
        print("Roar")
    def skin(self):
        print("Black stripes on yellow")
class lion(carnivore):
    def speak(self):
        print('Roar')
    def skin(self):
        print('Yellow')
class bear(carnivore):
    def speak(self):
        print('growl')
    def skin(self):
        print('black or brown')
class wolf(carnivore):
    def speak(self):
        print('howl')
    def skin(self):
        print('No specific color')
class herbivore(wild_ani):
    def food(self):
        print('Grass and tree')
class deer(herbivore):
    def speak(self):
        print("Bellow")
    def skin(self):
        print('White dots on orange')
class donkey(herbivore):
    def speak(self):
        print('bray')
    def skin(self):
        print("gray")
class elephant(herbivore):
    def speak(self):
        print('trumpet')
    def skin(self):
        print('gray')
class domestic_animals(Animal):
    def place(self):
        print("Human societies or household areas")
class cow(domestic_animals):
    def speak(self):
        print("moo")
    def skin(self):
        print("No specific color")
class dog(domestic_animals):
    def speak(self):
        print('bark')
    def skin(self):
        print("No specific color")
class horse(domestic_animals):
    def speak(self):
        print('neigh')
    def skin(self):
        print('No specific color')
