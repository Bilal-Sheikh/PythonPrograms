class Animals:
    animal= "Mammal"

class Pets(Animals):
    color="Black"
    

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow!! Bow!! Imma Dawg Bow!! Bow!!")

d= Dog()
d.bark()