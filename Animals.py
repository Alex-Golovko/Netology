class MilkAnimal:
    def __init__(self, name, type_of_animal, sounds, weight, milk=20, energy=100, paws=2):
        self.name = name
        self.type_of_animal = type_of_animal
        self.sounds = sounds
        self.weight = weight
        self.energy = energy
        self.paws = paws
        self.milk = milk

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def milk_animal(self, hours):
        if self.milk <= 20:
            self.milk -= hours * 4
            self.energy -= hours * 2
        elif self.milk < 5:
            print('Not milk')
