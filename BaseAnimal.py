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
    def isPredator(self):
        return self.__predator

    @property
    def Feeded(self):
        return self.__isFeeded

    def doSound(self):
        print(self.__sound)

    def eat(self, foodType, foodVolume):
        if foodType not in self.__foodTypes:
            return 0
        if self.__isFeeded:
            return 0
        if self.__foodEated >= self.__foodVolume:
            self.__isFeeded = True
            return 0
        if foodType in self.__foodTypes:
            if self.__foodEated + foodVolume > self.__foodVolume:
                self.__isFeeded = True
                self.__foodEated = 0
                return self.__foodVolume - self.__foodEated
            self.__foodEated += foodVolume
            if self.__foodEated >= self.__foodVolume:
                self.__isFeeded = True
                self.__foodEated = 0
                return foodVolume

    def play(self):
        print("Я играю")
