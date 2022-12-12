from BaseAnimal import BaseAnimal


class Valier:
    def __init__(self, biome, area=10):
        self.animals = []
        self.biome = biome
        self.area = area
        self.employedArea = 0
        self.__numOfFood = 0

    def addAnimal(self, animal: BaseAnimal):
        if self.biome != animal.biome:
            return False
        if self.employedArea + animal.needArea > self.area:
            return False
        if animal.isPredator:
            for i in self.animals:
                if not i.isPredator:
                    return False
                if i is not animal:
                    return False
        if not animal.isPredator:
            for i in self.animals:
                if i.isPredator:
                    return False
        self.animals.append(animal)
        self.employedArea += animal.needArea
        return True

    def removeAnimal(self, animal):
        if animal not in self.animals:
            return False
        self.animals.remove(animal)
        return True

    def feedAnimals(self, food, numOfFood):
        numOfFood += self.__numOfFood
        for i in self.animals:
            if numOfFood <= 0:
                return
            numOfFood -= i.eat(food, numOfFood)
        self.__numOfFood = numOfFood

    @property
    def foodRemaining(self):
        return self.__numOfFood

    def getHungryAnimals(self):
        animals = []
        for animal in self.animals:
            if not animal.Feeded:
                animals.append(animal)
        return animals

    def doSound(self):
        for animal in self.animals:
            animal.doSound()



