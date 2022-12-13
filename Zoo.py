from Animals.BaseAnimal import BaseAnimal
from Valier import Valier


class Zoo:
    def __init__(self):
        self.valiers = []

    def addValier(self, valier):
        self.valiers.append(valier)

    def removeValier(self, valier):
        if valier not in self.valiers:
            return False
        self.valiers.remove(valier)
        return True

    def addFood(self, typeFood, num):
        for valier in self.valiers:
            if typeFood not in valier.getFoodNeed().keys():
                continue
            foodNeed = valier.getFoodNeed()[typeFood]
            num -= foodNeed
            if num < 0:
                valier.addFood(typeFood, foodNeed - num)
            else:
                valier.addFood(typeFood, foodNeed)

    def feedAllAnimals(self):
        for valier in self.valiers:
            valier.feedAnimals()

    def pereselitAnimal(self, fromV: Valier, toV: Valier, animal: BaseAnimal):
        if toV.addAnimal(animal):
            fromV.removeAnimal(animal)

    def addAnimalToValier(self, valier: Valier, animal: BaseAnimal):
        return valier.addAnimal(animal)

    def getFoodInValiers(self):
        food = {}
        for valier in self.valiers:
            for foodInVal in valier.foodRemaining:
                if foodInVal not in food.keys():
                    food[foodInVal] = valier.foodRemaining[foodInVal]
                else:
                    food[foodInVal] += valier.foodRemaining[foodInVal]
        return food
