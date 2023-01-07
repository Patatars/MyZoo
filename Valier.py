from Animals.BaseAnimal import BaseAnimal


class Valier:
    def __init__(self, biome, area=10):
        self.animals = []
        self.biome = biome
        self.area = area
        self.employedArea = 0
        self.__food = {}

    def addAnimal(self, animal: BaseAnimal):
        if animal in self.animals:
            return False
        if self.biome != animal.biome:
            return False
        if self.employedArea + animal.needArea > self.area:
            return False
        if animal.isPredator:
            for i in self.animals:
                if not i.isPredator:
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
        self.employedArea -= animal.needArea
        return True

    def addFood(self, food, numOfFood):
        if food not in self.__food.keys():
            self.__food[food] = numOfFood
        else:
            self.__food[food] += numOfFood

    def feedAnimals(self):
        for i in self.animals:
            i.eat(self.__food)

    @property
    def foodRemaining(self):
        return self.__food

    def getHungryAnimals(self):
        animals = []
        for animal in self.animals:
            if not animal.Feeded:
                animals.append(animal)
        return animals

    def getFoodNeed(self):
        foodNeed = {}
        for animal in self.getHungryAnimals():
            if animal.foodTypes[0] not in self.__food.keys():
                foodNeed[animal.foodTypes[0]] = animal.needFood
            else:
                foodNeed[animal.foodTypes[0]] += animal.needFood
        return foodNeed

    def doSound(self):
        for animal in self.animals:
            animal.doSound()
