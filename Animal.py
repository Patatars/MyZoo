class Animal:
    def __init__(self, species: str, biome: str, needArea: int, food: list, predator: bool, sound: str):
        self.species = species
        self.biome = biome
        self.needArea = needArea
        self.food = food
        self.predator = predator
        self.sound = sound

    def doSound(self):
        print(self.sound)

    def eat(self):
        print("Я ем")

    def play(self):
        print("Я играю")
