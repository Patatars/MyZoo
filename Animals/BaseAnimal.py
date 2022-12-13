class BaseAnimal:
    def __init__(self, name, age, biome, needArea, foodTypes, predator, sound,
                 foodVolume):
        if foodTypes is None:
            foodTypes = []
        self.__biome = biome
        self.__needArea = needArea
        self.__foodTypes = foodTypes
        self.__predator = predator
        self.__isFeeded = False
        self.__foodEated = 0
        self.__sound = sound
        self.__foodVolume = foodVolume
        self.__name = name
        self.__age = age

    @property
    def biome(self):
        return self.__biome

    @property
    def needArea(self):
        return self.__needArea

    @property
    def foodTypes(self):
        return self.__foodTypes

    @property
    def isPredator(self):
        return self.__predator

    @property
    def Feeded(self):
        return self.__isFeeded

    @property
    def needFood(self):
        if self.Feeded:
            return 0
        return self.__foodVolume - self.__foodEated

    def doSound(self):
        print(self.__sound)

    def eat(self, foods):
        for food in foods:
            if food not in self.__foodTypes:
                continue
            if self.__isFeeded:
                return False
            if self.__foodEated >= self.__foodVolume:
                self.__isFeeded = True
                return False
            if food in self.__foodTypes:
                if self.__foodEated + foods[food] > self.__foodVolume:
                    foods[food] -= self.__foodVolume - self.__foodEated
                    self.__isFeeded = True
                    self.__foodEated = 0
                    return True
                self.__foodEated += foods[food]
                foods[food] = 0
                if self.__foodEated >= self.__foodVolume:
                    self.__isFeeded = True
                    self.__foodEated = 0
                return True

    def play(self):
        print("Я играю")
